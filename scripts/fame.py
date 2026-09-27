"""Fame signals for the Daily Paper recommender.

Tier priority (Leo's spec): AI conference spotlight/oral -> regular paper ->
arXiv preprint, citations high-to-low within a tier.

Signals:
  1. arXiv comment field, e.g. "Accepted at NeurIPS 2025 (Spotlight)" — the
     main tier signal for fresh papers (citation APIs lag by days/weeks).
  2. Semantic Scholar batch API (free, no key): citationCount + venue per
     arXiv id, one POST for all candidates.

Results are cached in _meta/fame_cache.json (7-day TTL) so the daily run only
re-queries new or stale papers.
"""

import json
import math
import re
import urllib.error
import urllib.request
from datetime import date, datetime
from pathlib import Path

META = Path(__file__).resolve().parent.parent / "_meta"
CACHE_FILE = META / "fame_cache.json"
CACHE_TTL_DAYS = 7

# normalized venue -> aliases matched case-insensitively
TOP_VENUES = {
    "NeurIPS": ["neurips", "nips", "neural information processing systems"],
    "ICML": ["icml", "international conference on machine learning"],
    "ICLR": ["iclr", "international conference on learning representations"],
    "AAAI": ["aaai", "association for the advancement of artificial intelligence"],
    "IJCAI": ["ijcai", "international joint conference on artificial intelligence"],
    "UAI": ["uai", "uncertainty in artificial intelligence"],
    "AISTATS": ["aistats", "artificial intelligence and statistics"],
    "COLT": ["colt", "conference on learning theory"],
    "KDD": ["kdd", "knowledge discovery and data mining", "sigkdd"],
    "WWW": ["www", "the web conference", "world wide web"],
    "SIGIR": ["sigir", "information retrieval"],
    "WSDM": ["wsdm", "web search and data mining"],
    "ACL": ["acl", "association for computational linguistics"],
    "EMNLP": ["emnlp", "empirical methods in natural language processing"],
    "NAACL": ["naacl", "north american chapter of the association for computational linguistics"],
    "EACL": ["eacl"],
    "COLING": ["coling"],
    "CVPR": ["cvpr", "computer vision and pattern recognition"],
    "ICCV": ["iccv", "international conference on computer vision"],
    "ECCV": ["eccv", "european conference on computer vision"],
    "WACV": ["wacv"],
    "CoRL": ["corl", "conference on robot learning"],
    "RSS": ["rss", "robotics: science and systems"],
    "ICRA": ["icra", "international conference on robotics and automation"],
    "IROS": ["iros"],
    "AAMAS": ["aamas"],
    "MICCAI": ["miccai"],
    "JMLR": ["jmlr", "journal of machine learning research"],
    "TMLR": ["tmlr", "transactions on machine learning research"],
    "TPAMI": ["tpami", "pattern analysis and machine intelligence"],
    "IJCV": ["ijcv", "international journal of computer vision"],
}

SPOTLIGHT_RE = re.compile(r"\b(spotlight|oral)\b", re.I)
AWARD_RE = re.compile(r"\b(best paper|outstanding paper|best paper award|test of time)\b", re.I)
ARXIV_ID_RE = re.compile(r"^\d{4}\.\d{4,5}$")


def match_top_venue(text):
    """Return normalized top-venue name if text mentions one, else None."""
    if not text:
        return None
    low = text.lower()
    for name, aliases in TOP_VENUES.items():
        for a in aliases:
            if re.search(r"\b" + re.escape(a) + r"\b", low):
                return name
    return None


def parse_comment(comment):
    """(tier, venue_label) from an arXiv comment string.

    tier: 2 = spotlight/oral/award at a top venue, 1 = regular top-venue
    paper, 0 = no usable signal.
    """
    if not comment:
        return 0, ""
    venue = match_top_venue(comment)
    if SPOTLIGHT_RE.search(comment) or AWARD_RE.search(comment):
        return 2, venue or ""
    if venue:
        return 1, venue
    return 0, ""


def _load_cache():
    try:
        return json.loads(CACHE_FILE.read_text())
    except Exception:
        return {}


def _save_cache(cache):
    try:
        META.mkdir(parents=True, exist_ok=True)
        CACHE_FILE.write_text(json.dumps(cache))
    except Exception:
        pass


def _cache_fresh(hit):
    try:
        age = (date.today() -
               datetime.fromisoformat(hit.get("fetched_at", "2000-01-01")).date()).days
        return age < CACHE_TTL_DAYS
    except Exception:
        return False


def s2_batch_lookup(arxiv_ids, cache):
    """Fill cache for arXiv ids via the Semantic Scholar batch endpoint.

    Returns dict arxiv_id -> (citations, venue or None). One POST for all
    ids; unknown ids get (0, None). Retries on 429 with backoff.
    """
    import time as _t
    today = date.today().isoformat()
    missing = [a for a in arxiv_ids
               if ARXIV_ID_RE.match(a or "") and not _cache_fresh(cache.get(a) or {})]
    # chunk to stay well under the batch limit
    for i in range(0, len(missing), 200):
        chunk = missing[i:i + 200]
        results = [None] * len(chunk)
        for attempt in range(4):
            try:
                body = json.dumps({"ids": [f"ARXIV:{a}" for a in chunk]}).encode()
                req = urllib.request.Request(
                    "https://api.semanticscholar.org/graph/v1/paper/batch"
                    "?fields=title,citationCount,venue,year",
                    data=body, method="POST",
                    headers={"Content-Type": "application/json",
                             "User-Agent": "daily-paper/1.0"})
                with urllib.request.urlopen(req, timeout=90) as resp:
                    results = json.loads(resp.read().decode())
                break
            except urllib.error.HTTPError as e:
                if e.code == 429 and attempt < 3:
                    _t.sleep(2 ** (attempt + 2))  # 4s, 8s, 16s
                    continue
                break
            except Exception:
                break
        for aid, r in zip(chunk, results):
            cit = int((r or {}).get("citationCount") or 0)
            venue = (r or {}).get("venue") or None
            cache[aid] = {"citations": cit, "venue": venue,
                          "fetched_at": today}
    return {a: (cache[a]["citations"], cache[a].get("venue"))
            for a in arxiv_ids if a in cache}


def fame_for(paper, cache=None, s2=None):
    """Return dict(tier, citations, venue) for a candidate paper dict.

    paper needs arxiv_id (or zotero_key as arXiv id) and optionally comment.
    Tier: 2 spotlight/oral, 1 regular top-venue, 0 arXiv/other.
    s2 is an optional pre-fetched dict arxiv_id -> (citations, venue).
    """
    if cache is None:
        cache = _load_cache()
    arxiv_id = paper.get("arxiv_id") or paper.get("zotero_key") or ""
    tier, venue = parse_comment(paper.get("comment") or "")
    citations = 0
    oa_venue = None
    if ARXIV_ID_RE.match(arxiv_id or ""):
        if s2 is not None and arxiv_id in s2:
            citations, oa_venue = s2[arxiv_id]
        elif arxiv_id in cache and _cache_fresh(cache[arxiv_id]):
            citations, oa_venue = cache[arxiv_id]["citations"], cache[arxiv_id].get("venue")
    if tier == 0 and oa_venue:
        top = match_top_venue(oa_venue)
        if top:
            tier, venue = 1, top
    if not venue and oa_venue:
        venue = oa_venue
    return {"tier": tier, "citations": citations, "venue": venue or ""}


def fame_scores(infos):
    """Map each paper info dict -> fame in [0,1].

    Tier strictly dominates (spotlight > regular > arXiv); log-scaled
    citations order papers within a tier.
    """
    max_c = max([i["citations"] for i in infos] + [0])
    denom = math.log1p(max_c) or 1.0
    out = []
    for i in infos:
        cit = math.log1p(i["citations"]) / denom
        out.append((i["tier"] + 0.99 * cit) / 3.0)
    return out
