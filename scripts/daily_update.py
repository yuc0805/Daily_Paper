#!/usr/bin/env python3
"""
Daily Paper Update (GitHub Actions version)
===========================================
Runs every morning at 6:00 AM ET via .github/workflows/daily.yml.

1. Ingest like/dislike feedback from feedback/inbox/*.json
   (written automatically by the like-worker when Leo rates papers on the site)
2. For each liked paper, add it to the knowledge graph with the correct
   category BEFORE generating today's list:
   papers/YYYY/MM/DD/<id>.md, areas/<area>.md timeline, lineage/<area>.json,
   docs/papers/<id>.html
   Then refresh the static website for the new papers:
   docs/data/graph.json (Research Areas tab counts) and the affected
   docs/areas/<area>.html pages (count, paper list, activity).
3. Discover new papers with an exploitation/exploration split:
   - ~80% exploitation: relevant to Leo's research, weighted by like history
   - ~20% exploration: popular papers from unrelated fields
4. Write docs/data/today.json
5. Delete processed inbox files.

Git add/commit/push is handled by the workflow (uses GITHUB_TOKEN).

State that persists between runs (committed in the repo):
  _meta/user_profile.json    area affinity weights learned from likes
  _meta/paper_history.json   metadata of previously recommended papers
  _meta/likes_processed.json keys already added to the knowledge graph
"""

import glob
import json
import math
import os
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date, datetime
from pathlib import Path

# --- Config ---
EXPLORE_RATIO = 0.20  # 20% of daily picks are exploration
N_DAILY_PAPERS = 8    # total papers per day

REPO = Path(__file__).resolve().parent.parent
META = REPO / "_meta"
INBOX = REPO / "feedback" / "inbox"

AREA_WEIGHTS = {
    "time-series.md": 3.0,
    "llm-health.md": 3.0,
    "llm.md": 2.0,
    "reasoning.md": 2.0,
    "multi-modal.md": 2.0,
    "self-supervised.md": 2.0,
}

AREA_ARXIV_CATS = {
    "time-series.md": ["stat.ML", "cs.LG", "cs.AI"],
    "llm-health.md": ["cs.AI", "cs.LG", "q-bio.QM"],
    "llm.md": ["cs.CL", "cs.AI", "cs.LG"],
    "reasoning.md": ["cs.AI", "cs.CL", "cs.LG"],
    "multi-modal.md": ["cs.CV", "cs.CL", "cs.AI"],
    "self-supervised.md": ["cs.LG", "cs.CV", "cs.AI"],
    "agent.md": ["cs.AI", "cs.MA", "cs.LG"],
    "computer-vision.md": ["cs.CV", "cs.AI"],
    "mamba.md": ["cs.LG", "cs.AI"],
}

EXPLORE_CATS = ["cs.CR", "cs.DB", "cs.HC", "cs.RO", "econ.EM", "physics.soc-ph"]


def log(msg):
    print(f"[{datetime.now().isoformat()}] {msg}", flush=True)


def load_json(path, default=None):
    p = Path(path)
    if p.exists():
        try:
            return json.loads(p.read_text())
        except Exception as e:
            log(f"WARN: could not parse {path}: {e}")
    return default if default is not None else {}


def save_json(path, data):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, indent=2, ensure_ascii=False))


def arxiv_search(query, max_results=20, retries=3):
    base = "http://export.arxiv.org/api/query"
    params = {
        "search_query": query, "start": 0, "max_results": max_results,
        "sortBy": "submittedDate", "sortOrder": "descending",
    }
    url = base + "?" + urllib.parse.urlencode(params)
    log(f"arXiv search: {query[:80]}...")
    xml_data = None
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(url, timeout=30) as resp:
                xml_data = resp.read()
            break
        except Exception as e:
            log(f"arXiv attempt {attempt+1}/{retries} failed: {e}")
            if attempt < retries - 1:
                import time as _t
                _t.sleep(2 * (attempt + 1))
    if xml_data is None:
        return []
    try:
        root = ET.fromstring(xml_data)
    except Exception as e:
        log(f"arXiv XML parse failed: {e}")
        return []
    ns = {"a": "http://www.w3.org/2005/Atom"}
    papers = []
    for entry in root.findall("a:entry", ns):
        raw_id = entry.find("a:id", ns).text.strip().split("/")[-1]
        pid = raw_id.split("v")[0]
        title = " ".join(entry.find("a:title", ns).text.strip().split())
        summary = " ".join(entry.find("a:summary", ns).text.strip().split())
        authors = [a.find("a:name", ns).text for a in entry.findall("a:author", ns)]
        published = entry.find("a:published", ns).text[:10]
        papers.append({"arxiv_id": pid, "title": title, "summary": summary,
                       "authors": authors, "published": published})
    return papers


def classify_area(paper):
    text = (paper.get("title", "") + " " + paper.get("summary", "")).lower()
    keywords = {
        "time-series.md": ["time series", "forecasting", "temporal", "wearable", "sensor", "ecg", "ppg", "imu"],
        "llm-health.md": ["health", "clinical", "medical", "biosignal", "patient", "disease"],
        "llm.md": ["large language model", "llm", "gpt", "prompt"],
        "reasoning.md": ["reasoning", "chain-of-thought", "planning"],
        "multi-modal.md": ["multimodal", "multi-modal", "vision-language", "audio-visual"],
        "self-supervised.md": ["self-supervised", "contrastive", "masked", "pretraining"],
        "agent.md": ["agent", "tool use", "autonomous"],
        "computer-vision.md": ["image", "vision", "detection", "segmentation"],
        "mamba.md": ["mamba", "state space", "ssm"],
        "world-model-rl.md": ["reinforcement", "world model", "policy"],
        "hallucination.md": ["hallucination", "factuality"],
        "interpretable-ml.md": ["interpretab", "explainab", "fairness"],
        "causal-inference.md": ["causal", "counterfactual"],
        "nlp.md": ["nlp", "language", "translation"],
        "audio.md": ["audio", "speech", "sound"],
        "generative-cv.md": ["diffusion", "generative", "text-to-image"],
        "optimizer.md": ["optimizer", "adam", "gradient"],
        "automl.md": ["automl", "hyperparameter"],
        "mathematics-ml.md": ["theorem", "proof"],
        "moe.md": ["mixture of experts", "sparse"],
        "test-time-training.md": ["test-time", "adaptation"],
    }
    scores = {area: sum(1 for kw in kws if kw in text) for area, kws in keywords.items()}
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "llm.md"


def read_inbox():
    """Read all feedback files; latest action wins per paper key."""
    latest = {}
    files = sorted(glob.glob(str(INBOX / "*.json")))
    for f in files:
        try:
            item = json.loads(Path(f).read_text())
        except Exception as e:
            log(f"WARN: skipping unreadable inbox file {f}: {e}")
            continue
        key = item.get("key")
        if not key:
            continue
        ts = item.get("ts", "")
        prev = latest.get(key)
        if prev is None or ts >= prev.get("ts", ""):
            latest[key] = item
    log(f"Inbox: {len(files)} files, {len(latest)} unique papers")
    return latest, files


def _esc(s):
    return (s or "").replace("&", "&amp;").replace("<", "&lt;") \
        .replace(">", "&gt;").replace('"', "&quot;")


def _insert_before(html, marker, entry):
    idx = html.find(marker)
    if idx == -1:
        return html
    return html[:idx] + entry + "\n" + html[idx:]


def _insert_after(html, marker, entry):
    idx = html.find(marker)
    if idx == -1:
        return html
    end = idx + len(marker)
    return html[:end] + "\n" + entry + html[end:]


def update_area_page(slug, items, new_count):
    """Insert newly KG-added papers into a static docs/areas/<slug>.html page.

    Prepends paper-list entries at the top (the list runs newest-first) and
    adds a Recent Activity line. Callers pass only papers not already on the
    page, so re-runs are safe. The Timeline section was removed from area
    pages; the paper list is the chronological record.
    """
    page = REPO / "docs" / "areas" / f"{slug}.html"
    if not page.exists():
        log(f"WARN: refresh_site: no area page for '{slug}'; page not updated")
        return
    html = page.read_text()
    fresh = items
    if not fresh:
        return
    if new_count is not None:
        html = re.sub(r'<span class="meta">\d+ papers</span>',
                      f'<span class="meta">{new_count} papers</span>',
                      html, count=1)
    year = date.today().year
    block = []
    for e in fresh:
        title = _esc(e.get("title") or e["key"])
        authors = _esc(e.get("authors") or "")
        block.append(f'<a class="paper-entry" href="../papers/{e["key"]}.html">'
                     f'[{year}] {authors} — {title}.</a>')
    html = _insert_after(html, "<h3>Paper List</h3>", "\n".join(block))
    keys = ", ".join(e["key"] for e in fresh[:5]) + ("..." if len(fresh) > 5 else "")
    activity = (f'<p>{date.today().isoformat()} | {len(fresh)} paper'
                f'{"s" if len(fresh) != 1 else ""} added from likes | {keys}</p>')
    html = _insert_after(html, "<h3>Recent Activity</h3>", activity)
    page.write_text(html)
    log(f"  site: {slug}.html +{len(fresh)} papers")


def refresh_site(added):
    """Keep the static website in sync with papers newly added to the KG.

    Updates docs/data/graph.json (the Research Areas tab counts) and the
    affected docs/areas/<slug>.html pages (count, paper list,
    recent activity). Paper detail pages are already written by
    add_paper_to_kg; this only links to them.
    """
    if not added:
        return
    by_area = {}
    for e in added:
        by_area.setdefault(e["area_slug"], []).append(e)

    # Drop papers already linked on their area page so re-runs are safe.
    fresh_by_area = {}
    for slug, items in by_area.items():
        page = REPO / "docs" / "areas" / f"{slug}.html"
        if page.exists():
            html = page.read_text()
            fresh = [e for e in items if f'../papers/{e["key"]}.html' not in html]
        else:
            fresh = items
        if fresh:
            fresh_by_area[slug] = fresh
    if not fresh_by_area:
        return

    graph_path = REPO / "docs" / "data" / "graph.json"
    graph = load_json(graph_path, default={"nodes": []})
    node_ids = {n.get("id") for n in graph.get("nodes", [])}
    new_counts = {}
    for slug in fresh_by_area:
        if slug not in node_ids:
            log(f"WARN: refresh_site: no graph node for area '{slug}'; count not updated")
    for n in graph.get("nodes", []):
        if n.get("id") in fresh_by_area:
            n["papers"] = n.get("papers", 0) + len(fresh_by_area[n["id"]])
            new_counts[n["id"]] = n["papers"]
    graph["total_papers"] = sum(n.get("papers", 0) for n in graph.get("nodes", []))
    save_json(graph_path, graph)
    log(f"  site: graph.json counts updated ({len(fresh_by_area)} areas, "
        f"total {graph['total_papers']} papers)")

    for slug, items in fresh_by_area.items():
        try:
            update_area_page(slug, items, new_counts.get(slug))
        except Exception as e:
            log(f"WARN: refresh_site failed for area '{slug}': {e}")


def add_paper_to_kg(key, meta, area_index):
    """Add a liked paper to the knowledge graph. Returns area file."""
    area_file = classify_area(meta)
    area_slug = area_file.replace(".md", "")
    area_label = area_index.get("collections", {}).get(area_slug, {}).get("name", area_slug)
    today = date.today()

    paper_dir = REPO / "papers" / str(today.year) / f"{today.month:02d}" / f"{today.day:02d}"
    paper_dir.mkdir(parents=True, exist_ok=True)
    paper_md = paper_dir / f"{key}.md"
    if not paper_md.exists():
        paper_md.write_text(
            f"# {meta.get('title', '')}\n\n"
            f"**Authors:** {meta.get('authors', '')}\n\n"
            f"**Area:** {area_label}\n\n"
            f"**Liked:** {today.isoformat()} (Leo liked from Today's Papers)\n\n"
            f"## What\n{(meta.get('summary', '') or '')[:800]}\n"
        )

    area_path = REPO / "areas" / area_file
    if area_path.exists():
        content = area_path.read_text()
        if key not in content:
            entry = f"\n{today.strftime('%Y-%m')} | {(meta.get('title','') or '')[:60]} ({key}) | liked by Leo — added to KG\n"
            if "### Timeline" in content:
                content = content.replace("### Timeline", "### Timeline" + entry, 1)
            else:
                content += "\n### Timeline\n" + entry
            area_path.write_text(content)

    lineage_path = REPO / "lineage" / f"{area_slug}.json"
    lineage = load_json(lineage_path, default={"edges": []})
    if not isinstance(lineage, dict) or "edges" not in lineage:
        lineage = {"edges": []}
    if not any(e.get("paper") == key for e in lineage["edges"]):
        lineage["edges"].append({
            "paper": key, "title": meta.get("title", ""),
            "source": "user-like", "date": today.isoformat(), "area": area_file,
        })
        save_json(lineage_path, lineage)

    docs_paper = _paper_page_path(key)
    if not docs_paper.exists():
        docs_paper.parent.mkdir(parents=True, exist_ok=True)
        docs_paper.write_text(
            "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n<meta charset=\"UTF-8\">\n"
            "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
            f"<title>{_esc(meta.get('title', ''))} — AI Knowledge Graph</title>\n"
            "<link rel=\"stylesheet\" href=\"../style.css\">\n</head>\n<body>\n"
            "<div class=\"paper-page\">\n"
            f"<a href=\"../areas/{area_slug}.html\" class=\"back-link\">&larr; Back to {_esc(area_label)}</a>\n"
            f"<h2>{_esc(meta.get('title', ''))}</h2>\n"
            f"<p class=\"paper-meta\">{_esc(meta.get('authors', ''))} &middot; "
            f"Liked {today.isoformat()} &middot; "
            f"<a href=\"https://arxiv.org/abs/{_esc(key)}\" target=\"_blank\" "
            f"rel=\"noopener\">arXiv:{_esc(key)}</a></p>\n"
            f"<h3>What</h3>\n<p>{_esc((meta.get('summary', '') or '')[:1500])}</p>\n"
            "</div>\n</body>\n</html>\n")
    return area_file


def ingest_feedback(area_index, profile, history):
    """Process inbox: likes -> KG first, dislikes -> downweight.

    Returns (n_liked, n_disliked, added) where added is a list of
    {key, title, authors, area_slug} dicts for the site refresh.
    """
    latest, files = read_inbox()
    processed = load_json(META / "likes_processed.json", default={"processed": []})
    processed_keys = set(processed.get("processed", []))
    dislike_store = load_json(META / "dislikes.json", default={})

    n_liked = n_disliked = 0
    added = []
    for key, item in latest.items():
        action = item.get("action")
        paper = item.get("paper") or {}
        meta = {
            "title": paper.get("title") or history.get(key, {}).get("title", ""),
            "authors": paper.get("authors") or history.get(key, {}).get("authors", ""),
            "summary": paper.get("summary") or history.get(key, {}).get("summary", ""),
        }
        if action == "like":
            if key in processed_keys:
                continue
            if not meta["title"]:
                log(f"  skip {key}: no metadata")
                continue
            area_file = add_paper_to_kg(key, meta, area_index)
            processed_keys.add(key)
            profile["area_affinity"][area_file] = profile.get("area_affinity", {}).get(area_file, 0) + 1.0
            added.append({"key": key, "title": meta["title"],
                          "authors": meta["authors"],
                          "area_slug": area_file.replace(".md", "")})
            n_liked += 1
            log(f"  + like {key} -> {area_file}")
        elif action == "dislike":
            area_file = classify_area(meta) if meta["title"] else None
            if area_file:
                profile["area_affinity"][area_file] = profile.get("area_affinity", {}).get(area_file, 0) - 0.3
            if meta["title"]:
                # keep the text: dislikes are negative examples for ranking
                dislike_store[key] = {"title": meta["title"], "summary": meta["summary"]}
            n_disliked += 1
            log(f"  - dislike {key}" + (f" ({area_file})" if area_file else ""))
        # "clear" (toggle-off): intentionally no-op; KG entries already added stay.

    processed["processed"] = sorted(processed_keys)
    save_json(META / "likes_processed.json", processed)
    # keep the most recent 200 dislikes as negative ranking examples
    save_json(META / "dislikes.json", dict(list(dislike_store.items())[-200:]))

    for f in files:
        try:
            Path(f).unlink()
        except Exception as e:
            log(f"WARN: could not delete inbox file {f}: {e}")
    return n_liked, n_disliked, added


# --- Content-based ranking (TF-IDF cosine, stdlib only) ---
_STOPWORDS = frozenset("""
a an and are as at be been by can do does for from had has have having he her
his how i if in into is it its of on or our she so such than that the their
them then there these they this to was we were will with would you your
not no nor only own same too very can will just should now paper papers
propose proposed method methods based using use used novel approach
results result show shown study arxiv preprint
""".split())


def _tokens(text):
    return [t for t in re.findall(r"[a-z]{3,}", (text or "").lower())
            if t not in _STOPWORDS]


def _norm_title(t):
    return re.sub(r"[^a-z0-9]", "", (t or "").lower())


def _build_tfidf(doc_texts):
    """L2-normalized TF-IDF vectors (dicts) for each doc, stdlib only."""
    docs = [_tokens(t) for t in doc_texts]
    n = len(docs)
    df = {}
    for toks in docs:
        for t in set(toks):
            df[t] = df.get(t, 0) + 1
    idf = {t: math.log((1 + n) / (1 + c)) + 1.0 for t, c in df.items()}
    vecs = []
    for toks in docs:
        if not toks:
            vecs.append({})
            continue
        tf = {}
        for t in toks:
            tf[t] = tf.get(t, 0) + 1
        v = {t: (c / len(toks)) * idf[t] for t, c in tf.items()}
        norm = math.sqrt(sum(x * x for x in v.values())) or 1.0
        vecs.append({t: x / norm for t, x in v.items()})
    return vecs


def _cos(a, b):
    if len(a) > len(b):
        a, b = b, a
    return sum(x * b.get(t, 0.0) for t, x in a.items())


def _paper_page_path(key):
    safe = re.sub(r"[^a-zA-Z0-9._-]", "_", key or "untitled")
    return REPO / "docs" / "papers" / f"{safe}.html"


def write_digest_paper_pages(today_papers, pool):
    """Detail pages for digest papers so feed cards don't 404.

    Writes docs/papers/<key>.html for every paper in the current digest
    (with a "Why recommended" note) and prunes pages whose papers have
    rotated out of the digest. Liked papers keep their page: add_paper_to_kg
    overwrites it with the library version.
    """
    pages_dir = REPO / "docs" / "papers"
    pages_dir.mkdir(parents=True, exist_ok=True)
    liked_keys = set(load_json(META / "likes_processed.json",
                               default={"processed": []}).get("processed", []))

    def why(p):
        if p.get("rec_type") == "explore":
            cat = _esc(p.get("explore_cat") or "another field")
            return (f"Picked for exploration — from {cat}, outside your usual "
                    f"research areas.")
        contribs = [("Close to papers already in your library.", 0.40 * p.get("_lib", 0)),
                    ("Similar to a paper you liked.", 0.30 * p.get("_like", 0)),
                    ("Very recent in your research areas.", 0.20 * p.get("_rec", 0))]
        text = max(contribs, key=lambda x: x[1])[0]
        if p.get("_dis", 0) > 0.15:
            text += " (Somewhat similar to something you passed on before.)"
        return text

    new_keys = set()
    for p in today_papers + pool:
        key = p.get("zotero_key", "")
        if not key:
            continue
        new_keys.add(key)
        pub = p.get("published") or p.get("year") or ""
        pub = str(pub)
        badge = ("<span class=\"rec-badge\">For you</span>"
                 if p.get("rec_type") == "for-you"
                 else "<span class=\"rec-badge explore\">Explore</span>")
        html = (
            "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n<meta charset=\"UTF-8\">\n"
            "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
            f"<title>{_esc(p.get('title', key))} — Daily Paper</title>\n"
            "<link rel=\"stylesheet\" href=\"../style.css\">\n</head>\n<body>\n"
            "<div class=\"paper-page\">\n"
            "<a href=\"../index.html\" class=\"back-link\">&larr; Back to Today's Papers</a>\n"
            f"<h2>{_esc(p.get('title', key))}</h2>\n"
            f"<p class=\"paper-meta\">{_esc(p.get('authors', ''))} &middot; "
            f"{_esc(pub)} &middot; {badge} &middot; "
            f"<a href=\"https://arxiv.org/abs/{_esc(key)}\" target=\"_blank\" "
            f"rel=\"noopener\">arXiv:{_esc(key)}</a></p>\n"
            f"<h3>Why recommended</h3>\n<p>{why(p)}</p>\n"
            f"<h3>Abstract</h3>\n<p>{_esc(p.get('summary', ''))}</p>\n"
            "<p class=\"paper-note\">Not in your library yet — tap 👍 on its card "
            "to add it, 👎 to pass.</p>\n"
            "</div>\n</body>\n</html>\n")
        _paper_page_path(key).write_text(html)

    old_keys = set(load_json(META / "digest_pages.json", default=[]))
    pruned = 0
    for key in old_keys - new_keys - liked_keys:
        try:
            _paper_page_path(key).unlink()
            pruned += 1
        except FileNotFoundError:
            pass
    save_json(META / "digest_pages.json", sorted(new_keys))
    log(f"  site: {len(new_keys)} digest paper pages written, {pruned} pruned")


def discover_papers(profile, history):
    """Discover candidates from arXiv and rank them.

    Returns (today_papers, pool):
      today_papers: N_DAILY_PAPERS picks for today.json (exploit + explore).
      pool: remaining ranked candidates for the frontend Refresh button.

    Ranking: for-you papers score
      0.40 * similarity-to-library-taste + 0.30 * similarity-to-likes
      + 0.20 * recency - 0.30 * similarity-to-dislikes.
    The library taste is a year-weighted centroid of every paper in the
    knowledge graph (newer library papers count more); likes/dislikes are
    max-similarity to any individual rated paper, so multiple interests and
    strong aversions both survive. Explore papers come from unrelated
    categories (OOD by construction) and rank by recency minus similarity to
    the library taste, so the most out-of-distribution surface first.
    Papers recommended on earlier days, already in the library, or rated in
    the feed are never served again.
    """
    n_explore = max(1, round(N_DAILY_PAPERS * EXPLORE_RATIO))
    n_exploit = N_DAILY_PAPERS - n_explore
    today = date.today()
    seen = set(history.keys())  # never recommend the same paper twice
    # never recommend something already in Leo's library (match on normalized title)
    known_titles = {_norm_title(e.get("title")) for e in
                    load_json(META / "zotero_index.json", default=[])
                    if e.get("title")}
    known_titles |= {_norm_title(v.get("title")) for v in history.values()
                     if isinstance(v, dict) and v.get("title")}
    known_titles.discard("")

    def mk_paper(r, rec_type, explore_cat=None):
        authors = ", ".join(r["authors"][:4]) + (" et al." if len(r["authors"]) > 4 else "")
        if rec_type == "for-you":
            area = classify_area(r)
            label = area.replace(".md", "").replace("-", " ").title()
            slug = area.replace(".md", "")
            what = r["summary"][:300]
        else:
            label, slug = explore_cat, "explore"
            what = "[Explore] " + r["summary"][:280]
        try:
            days_old = max(0, (today - date.fromisoformat(r["published"])).days)
        except ValueError:
            days_old = 30
        return {
            "zotero_key": r["arxiv_id"], "title": r["title"],
            "authors": authors, "year": int(r["published"][:4]),
            "what": what, "summary": r["summary"],
            "area_label": label, "area_slug": slug, "builds_on": "",
            "rec_type": rec_type, "_days_old": days_old,
            "_text": f"{r['title']} {r['summary']}",
        }

    affinity = profile.get("area_affinity", {})
    foryou, explore = [], []
    weighted = sorted(
        ((AREA_WEIGHTS.get(a, 1.0) + affinity.get(a, 0) * 0.5, a)
         for a in set(list(AREA_WEIGHTS) + list(affinity))),
        reverse=True)
    for _, area_file in weighted:
        cats = AREA_ARXIV_CATS.get(area_file, ["cs.AI", "cs.LG"])
        query = " OR ".join(f"cat:{c}" for c in cats)
        for r in arxiv_search(query, max_results=10):
            if r["arxiv_id"] in seen or _norm_title(r["title"]) in known_titles:
                continue
            seen.add(r["arxiv_id"])
            foryou.append(mk_paper(r, "for-you"))

    for cat in EXPLORE_CATS:
        for r in arxiv_search(f"cat:{cat}", max_results=5):
            if r["arxiv_id"] in seen or _norm_title(r["title"]) in known_titles:
                continue
            seen.add(r["arxiv_id"])
            explore.append(mk_paper(r, "explore", explore_cat=cat))

    # --- taste profile: library background + likes + dislikes ---
    lib_entries = load_json(META / "zotero_index.json", default=[])
    lib_texts, lib_weights = [], []
    for e in lib_entries:
        if not e.get("title"):
            continue
        lib_texts.append(f"{e.get('title', '')} {e.get('abstract', '')}")
        try:
            age = max(0, today.year - int(e.get("year") or today.year))
        except (ValueError, TypeError):
            age = 0
        lib_weights.append(1.0 / (1.0 + 0.5 * age))  # newer library papers count more

    liked = load_json(META / "likes_processed.json", default={"processed": []}).get("processed", [])
    liked_texts = [f"{history[k]['title']} {history[k].get('summary', '')}"
                   for k in liked if k in history and history[k].get("title")]
    disliked = load_json(META / "dislikes.json", default={})
    disliked_texts = [f"{v.get('title', '')} {v.get('summary', '')}"
                      for v in disliked.values() if v.get("title")]

    cand_vecs = _build_tfidf(
        lib_texts + liked_texts + disliked_texts + [c["_text"] for c in foryou + explore])
    n_lib, n_liked, n_dis = len(lib_texts), len(liked_texts), len(disliked_texts)
    lib_vecs = cand_vecs[:n_lib]
    liked_vecs = cand_vecs[n_lib:n_lib + n_liked]
    dis_vecs = cand_vecs[n_lib + n_liked:n_lib + n_liked + n_dis]
    cand_vecs = cand_vecs[n_lib + n_liked + n_dis:]

    # year-weighted library centroid = background taste
    centroid = {}
    for v, w in zip(lib_vecs, lib_weights):
        for t, x in v.items():
            centroid[t] = centroid.get(t, 0.0) + x * w
    cn = math.sqrt(sum(x * x for x in centroid.values())) or 1.0
    centroid = {t: x / cn for t, x in centroid.items()}

    for c, cv in zip(foryou + explore, cand_vecs):
        c["_lib"] = _cos(cv, centroid)
        c["_like"] = max([_cos(cv, lv) for lv in liked_vecs], default=0.0)
        c["_dis"] = max([_cos(cv, dv) for dv in dis_vecs], default=0.0)
        c["_rec"] = 1.0 / (1.0 + c["_days_old"] / 7.0)

    for c in foryou:
        c["_score"] = (0.40 * c["_lib"] + 0.30 * c["_like"]
                       + 0.20 * c["_rec"] - 0.30 * c["_dis"])
    foryou.sort(key=lambda c: c["_score"], reverse=True)
    for c in explore:
        c["_score"] = c["_rec"] - 0.5 * c["_lib"]
    explore.sort(key=lambda c: c["_score"], reverse=True)

    today_papers = foryou[:n_exploit] + explore[:n_explore]
    pool = (foryou[n_exploit:] + explore[n_explore:])[:60]
    write_digest_paper_pages(today_papers, pool)  # before internal keys are popped
    for p in today_papers + pool:
        for k in ("_days_old", "_text", "_score", "_lib", "_like", "_dis", "_rec"):
            p.pop(k, None)
    log(f"discovery: {len(foryou)} for-you + {len(explore)} explore candidates, "
        f"pool={len(pool)}, library={n_lib}, liked={n_liked}, disliked={n_dis}")
    return today_papers, pool


def main():
    log("=== Daily Paper Update starting ===")
    area_index = load_json(META / "area_index.json", default={"collections": {}})
    profile = load_json(META / "user_profile.json",
                        default={"area_affinity": dict.fromkeys(AREA_WEIGHTS, 0.0)})
    if "area_affinity" not in profile:
        profile = {"area_affinity": dict.fromkeys(AREA_WEIGHTS, 0.0)}
    history = load_json(META / "paper_history.json", default={})

    n_liked, n_disliked, added = ingest_feedback(area_index, profile, history)
    log(f"Feedback ingested: {n_liked} new likes -> KG, {n_disliked} dislikes")
    refresh_site(added)
    save_json(META / "user_profile.json", profile)

    papers, pool = discover_papers(profile, history)
    for p in papers:
        history[p["zotero_key"]] = {"title": p["title"], "authors": p["authors"],
                                   "summary": p.get("summary", ""), "what": p["what"]}
    save_json(META / "paper_history.json", history)

    save_json(REPO / "docs" / "data" / "today.json",
              {"date": date.today().isoformat(), "papers": papers})
    log(f"Wrote today.json with {len(papers)} papers")
    save_json(REPO / "docs" / "data" / "pool.json",
              {"date": date.today().isoformat(), "papers": pool})
    log(f"Wrote pool.json with {len(pool)} papers for the Refresh button")
    log("=== Daily Paper Update done ===")


if __name__ == "__main__":
    sys.exit(main())
