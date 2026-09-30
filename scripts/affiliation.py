"""Affiliation filter: keep papers whose first AND last authors are at top institutions.

Leo's rule (2026-09-30): don't recommend a paper if its first author or its
last author is not from a top-50 university. The top-50 set is QS World
University Rankings 2026 (ranks 1-46 verbatim; 47-50 approximated with the
ML-relevant boundary schools — CMU, Duke, UT Austin, KAIST).

Affiliation data comes from OpenAlex (title search; arXiv-ID lookup is not
reliable there). Results are cached 30 days in _meta/affiliation_cache.json.

Fail-open by design: if OpenAlex has no record for a paper (common for
papers < ~2 weeks old), the paper is KEPT and the miss is logged. Dropping
unknowns would nuke most fresh arXiv candidates.

Set ALLOW_TOP_LABS = False for a strict universities-only filter.
"""

import json
import re
import time
import urllib.parse
import urllib.request
from datetime import date, datetime, timedelta
from pathlib import Path

META = Path(__file__).resolve().parent.parent / "_meta"
CACHE_FILE = META / "affiliation_cache.json"
CACHE_TTL_DAYS = 30
CACHE_VERSION = 3  # bump when verdict logic changes to invalidate old entries

# Leo's call (2026-09-30): top industry labs count as top-tier alongside
# universities. Flip to False for strict universities-only.
ALLOW_TOP_LABS = False

# (canonical display, [match aliases]) — matching is lowercase substring on
# word boundaries against the OpenAlex institution display_name.
_TOP50 = [
    ("Massachusetts Institute of Technology", ["massachusetts institute of technology", "mit"]),
    ("Imperial College London", ["imperial college london", "imperial college"]),
    ("Stanford University", ["stanford university", "stanford"]),
    ("University of Oxford", ["university of oxford", "oxford"]),
    ("Harvard University", ["harvard university", "harvard"]),
    ("University of Cambridge", ["university of cambridge", "cambridge"]),
    ("ETH Zurich", ["eth zurich", "eth zürich", "swiss federal institute of technology zurich"]),
    ("National University of Singapore", ["national university of singapore"]),
    ("University College London", ["university college london"]),
    ("California Institute of Technology", ["california institute of technology", "caltech"]),
    ("University of Hong Kong", ["university of hong kong"]),
    ("Nanyang Technological University", ["nanyang technological university"]),
    ("University of Chicago", ["university of chicago"]),
    ("Peking University", ["peking university"]),
    ("University of Pennsylvania", ["university of pennsylvania"]),
    ("Cornell University", ["cornell university", "cornell"]),
    ("Tsinghua University", ["tsinghua university"]),
    ("University of California, Berkeley", ["university of california berkeley", "uc berkeley", "berkeley"]),
    ("University of Melbourne", ["university of melbourne"]),
    ("University of New South Wales", ["university of new south wales", "unsw"]),
    ("Yale University", ["yale university", "yale"]),
    ("EPFL", ["epfl", "ecole polytechnique federale de lausanne"]),
    ("Technical University of Munich", ["technical university of munich", "tum"]),
    ("Johns Hopkins University", ["johns hopkins university", "johns hopkins"]),
    ("Princeton University", ["princeton university", "princeton"]),
    ("University of Sydney", ["university of sydney"]),
    ("McGill University", ["mcgill university", "mcgill"]),
    ("PSL Research University", ["psl university", "psl research university", "universite psl"]),
    ("University of Toronto", ["university of toronto"]),
    ("Fudan University", ["fudan university", "fudan"]),
    ("King's College London", ["king's college london", "kings college london", "kcl"]),
    ("Australian National University", ["australian national university"]),
    ("Chinese University of Hong Kong", ["chinese university of hong kong", "cuhk"]),
    ("University of Edinburgh", ["university of edinburgh", "edinburgh"]),
    ("University of Manchester", ["university of manchester", "manchester"]),
    ("Monash University", ["monash university", "monash"]),
    ("University of Tokyo", ["university of tokyo"]),
    ("Columbia University", ["columbia university", "columbia"]),
    ("Seoul National University", ["seoul national university"]),
    ("University of British Columbia", ["university of british columbia"]),
    ("Institut Polytechnique de Paris", ["institut polytechnique de paris"]),
    ("Northwestern University", ["northwestern university", "northwestern"]),
    ("University of Queensland", ["university of queensland"]),
    ("HKUST", ["hong kong university of science and technology", "hkust"]),
    ("University of Michigan", ["university of michigan"]),
    ("UCLA", ["university of california los angeles", "ucla"]),
    # QS-2026 boundary (~47-50), ML-relevant schools included deliberately:
    ("Carnegie Mellon University", ["carnegie mellon university", "carnegie mellon", "cmu"]),
    ("Duke University", ["duke university", "duke"]),
    ("University of Texas at Austin", ["university of texas at austin", "ut austin"]),
    ("KAIST", ["kaist", "korea advanced institute of science"]),
]

_TOP_LABS = [
    ("Google DeepMind", ["deepmind", "google deepmind"]),
    ("Google", ["google"]),
    ("OpenAI", ["openai"]),
    ("Meta FAIR", ["meta", "facebook ai research", "fair"]),
    ("Microsoft Research", ["microsoft research", "microsoft"]),
    ("NVIDIA", ["nvidia"]),
    ("Anthropic", ["anthropic"]),
]

_ALIASES = [a for _, als in _TOP50 for a in als]
if ALLOW_TOP_LABS:
    _ALIASES += [a for _, als in _TOP_LABS for a in als]


def _norm(s):
    s = (s or "").lower()
    s = re.sub(r"[^a-z0-9 ]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def _norm_title(t):
    t = (t or "").lower()
    t = re.sub(r"[^a-z0-9]", "", t)
    return t


def is_top_institution(display_name):
    """True if the institution matches the top-50 (+labs) allowlist."""
    n = _norm(display_name)
    if not n:
        return False
    for alias in _ALIASES:
        # short aliases (mit, cmu, kcl...) need word boundaries; phrases match anywhere
        if " " in alias:
            if alias in n:
                return True
        else:
            if re.search(r"\b" + re.escape(alias) + r"\b", n):
                return True
    return False


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
        if hit.get("v", 1) != CACHE_VERSION:
            return False
        ts = datetime.fromisoformat(hit.get("ts", ""))
        return datetime.now() - ts < timedelta(days=CACHE_TTL_DAYS)
    except Exception:
        return False


def _openalex_search(title):
    """Search OpenAlex by title; return (first_insts, last_insts) or None."""
    q = urllib.parse.urlencode({
        "search": title, "per-page": 5,
        "select": "id,title,authorships",
    })
    req = urllib.request.Request(
        "https://api.openalex.org/works?" + q,
        headers={"User-Agent": "DailyPaper/1.0 (mailto:leochen0850@gmail.com)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.loads(r.read().decode())
    want = _norm_title(title)
    for w in data.get("results", []):
        if _norm_title(w.get("title", "")) != want:
            continue
        auths = w.get("authorships") or []
        if not auths:
            return None
        first = [i.get("display_name", "") for i in auths[0].get("institutions", [])]
        lasts = auths[-1].get("institutions", [])
        last = [i.get("display_name", "") for i in lasts]
        return first, last
    return None


def _openalex_author_insts(name):
    """Fallback for papers OpenAlex hasn't indexed: look up the author's
    last_known_institutions. Returns list of institution names, [] if the
    author can't be reliably identified (fail-open)."""
    q = urllib.parse.urlencode({
        "search": name, "per-page": 3,
        "select": "id,display_name,last_known_institutions,works_count",
    })
    req = urllib.request.Request(
        "https://api.openalex.org/authors?" + q,
        headers={"User-Agent": "DailyPaper/1.0 (mailto:leochen0850@gmail.com)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.loads(r.read().decode())
    results = data.get("results") or []
    if not results:
        return []
    # safety: only trust an established, name-matching profile.
    # Require exact token-set match ("ao wang" must NOT match "shuao wang")
    # AND a distinctive name (few total candidates -> low collision risk).
    if (data.get("meta") or {}).get("count", 9999) > 5:
        return []
    top = results[0]
    disp = _norm(top.get("display_name", ""))
    if set(_norm(name).split()) != set(disp.split()):
        return []
    if (top.get("works_count") or 0) < 3:
        return []
    return [i.get("display_name", "") for i in
            top.get("last_known_institutions", []) or []]


def _verify_side(name, paper_insts):
    """Verify one author's side.

    Returns True (verified top-50), False (verified NOT top-50),
    or None (no affiliation data available).
    """
    if paper_insts:
        return any(is_top_institution(i) for i in paper_insts)
    if name:
        try:
            prof = _openalex_author_insts(name)
            time.sleep(0.1)
        except Exception:
            prof = []
        if prof:
            return any(is_top_institution(i) for i in prof)
    return None


def _paper_verdict(fi, li, first_name=None, last_name=None):
    """True = both ends verified top-50.
    False = affirmative evidence that first or last author is NOT top-50.
    None = cannot verify (missing data) -> treated as keep (fail-open),
    because OpenAlex lacks institution data for most papers.
    """
    v_first = _verify_side(first_name, fi)
    v_last = _verify_side(last_name, li)
    if v_first is False or v_last is False:
        return False
    if v_first and v_last:
        return True
    return None


def check(title, arxiv_id=None, first_author=None, last_author=None):
    """Affiliation verdict for one paper.

    Returns (verdict, detail) where verdict is True (keep), False (drop) or
    None (unknown -> keep, fail-open). detail names the first/last institutions.
    """
    cache = _load_cache()
    key = (arxiv_id or _norm_title(title))[:120]
    hit = cache.get(key)
    if hit and _cache_fresh(hit):
        return hit["verdict"], hit.get("detail", "")

    verdict, detail = None, "unknown"
    try:
        found = _openalex_search(title)
        time.sleep(0.15)  # be polite to the API
    except Exception:
        found = None
    if found is not None:
        fi, li = found
        verdict = _paper_verdict(fi, li, first_author, last_author)
        detail = (f"first=[{', '.join(fi) or '?'}] "
                  f"last=[{', '.join(li) or '?'}] (paper record)")
    elif first_author or last_author:
        # paper too new for OpenAlex: fall back to author profiles
        try:
            fi = _openalex_author_insts(first_author) if first_author else []
            time.sleep(0.15)
            li = _openalex_author_insts(last_author) if last_author else []
            time.sleep(0.15)
        except Exception:
            fi, li = [], []
        # drop only on a RELIABLE non-top-50 hit; unknown authors stay fail-open
        fi_bad = bool(fi) and not any(is_top_institution(i) for i in fi)
        li_bad = bool(li) and not any(is_top_institution(i) for i in li)
        if fi_bad or li_bad:
            verdict = False
            detail = (f"first=[{', '.join(fi) or '?'}] "
                      f"last=[{', '.join(li) or '?'}] (author profile)")
        else:
            verdict, detail = None, "unknown (authors not reliably identified)"
    if verdict is None:
        return None, detail
    cache[key] = {"verdict": verdict, "detail": detail, "v": CACHE_VERSION,
                  "ts": datetime.now().isoformat()}
    _save_cache(cache)
    return verdict, detail


def batch_check(papers):
    """papers: iterable of dicts with 'title' (+ optional 'arxiv_id'/'zotero_key',
    'first_author', 'last_author').

    Returns (kept, dropped) lists; unknowns are kept (fail-open).
    """
    kept, dropped = [], []
    for p in papers:
        verdict, detail = check(
            p.get("title", ""),
            arxiv_id=p.get("arxiv_id") or p.get("zotero_key"),
            first_author=p.get("first_author"),
            last_author=p.get("last_author"),
        )
        p["_aff_detail"] = detail
        if verdict is False:
            dropped.append(p)
        else:
            kept.append(p)
    return kept, dropped
