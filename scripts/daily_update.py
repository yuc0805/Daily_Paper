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
import os
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

    docs_paper = REPO / "docs" / "papers" / f"{key}.html"
    if not docs_paper.exists():
        docs_paper.parent.mkdir(parents=True, exist_ok=True)
        docs_paper.write_text(
            "<!DOCTYPE html><html><head><meta charset='utf-8'>"
            f"<title>{meta.get('title', '')}</title></head><body>"
            f"<h1>{meta.get('title', '')}</h1>"
            f"<p>{meta.get('authors', '')}</p>"
            f"<p>{(meta.get('summary', '') or '')[:1500]}</p>"
            f"<p><em>Liked by Leo on {today.isoformat()}, added to {area_label}</em></p>"
            "</body></html>"
        )
    return area_file


def ingest_feedback(area_index, profile, history):
    """Process inbox: likes -> KG first, dislikes -> downweight. Returns counts."""
    latest, files = read_inbox()
    processed = load_json(META / "likes_processed.json", default={"processed": []})
    processed_keys = set(processed.get("processed", []))

    n_liked = n_disliked = 0
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
            n_liked += 1
            log(f"  + like {key} -> {area_file}")
        elif action == "dislike":
            area_file = classify_area(meta) if meta["title"] else None
            if area_file:
                profile["area_affinity"][area_file] = profile.get("area_affinity", {}).get(area_file, 0) - 0.3
            n_disliked += 1
            log(f"  - dislike {key}" + (f" ({area_file})" if area_file else ""))
        # "clear" (toggle-off): intentionally no-op; KG entries already added stay.

    processed["processed"] = sorted(processed_keys)
    save_json(META / "likes_processed.json", processed)

    for f in files:
        try:
            Path(f).unlink()
        except Exception as e:
            log(f"WARN: could not delete inbox file {f}: {e}")
    return n_liked, n_disliked


def discover_papers(profile):
    n_explore = max(1, round(N_DAILY_PAPERS * EXPLORE_RATIO))
    n_exploit = N_DAILY_PAPERS - n_explore
    log(f"Discovering {n_exploit} for-you + {n_explore} explore papers")

    affinity = profile.get("area_affinity", {})
    papers, seen = [], set()

    weighted = sorted(
        ((AREA_WEIGHTS.get(a, 1.0) + affinity.get(a, 0) * 0.5, a)
         for a in set(list(AREA_WEIGHTS) + list(affinity))),
        reverse=True)
    for _, area_file in weighted:
        if sum(1 for p in papers if p["rec_type"] == "for-you") >= n_exploit:
            break
        cats = AREA_ARXIV_CATS.get(area_file, ["cs.AI", "cs.LG"])
        query = " OR ".join(f"cat:{c}" for c in cats)
        for r in arxiv_search(query, max_results=10):
            if r["arxiv_id"] in seen:
                continue
            seen.add(r["arxiv_id"])
            area = classify_area(r)
            papers.append({
                "zotero_key": r["arxiv_id"], "title": r["title"],
                "authors": ", ".join(r["authors"][:4]) + (" et al." if len(r["authors"]) > 4 else ""),
                "year": int(r["published"][:4]), "what": r["summary"][:300],
                "summary": r["summary"],
                "area_label": area.replace(".md", "").replace("-", " ").title(),
                "area_slug": area.replace(".md", ""), "builds_on": "",
                "rec_type": "for-you",
            })
            if sum(1 for p in papers if p["rec_type"] == "for-you") >= n_exploit:
                break

    for cat in EXPLORE_CATS:
        if sum(1 for p in papers if p["rec_type"] == "explore") >= n_explore:
            break
        for r in arxiv_search(f"cat:{cat}", max_results=5):
            if r["arxiv_id"] in seen:
                continue
            seen.add(r["arxiv_id"])
            papers.append({
                "zotero_key": r["arxiv_id"], "title": r["title"],
                "authors": ", ".join(r["authors"][:4]) + (" et al." if len(r["authors"]) > 4 else ""),
                "year": int(r["published"][:4]),
                "what": "[Explore] " + r["summary"][:280], "summary": r["summary"],
                "area_label": cat, "area_slug": "explore", "builds_on": "",
                "rec_type": "explore",
            })
            break
    return papers[:N_DAILY_PAPERS]


def main():
    log("=== Daily Paper Update starting ===")
    area_index = load_json(META / "area_index.json", default={"collections": {}})
    profile = load_json(META / "user_profile.json",
                        default={"area_affinity": dict.fromkeys(AREA_WEIGHTS, 0.0)})
    if "area_affinity" not in profile:
        profile = {"area_affinity": dict.fromkeys(AREA_WEIGHTS, 0.0)}
    history = load_json(META / "paper_history.json", default={})

    n_liked, n_disliked = ingest_feedback(area_index, profile, history)
    log(f"Feedback ingested: {n_liked} new likes -> KG, {n_disliked} dislikes")
    save_json(META / "user_profile.json", profile)

    papers = discover_papers(profile)
    for p in papers:
        history[p["zotero_key"]] = {"title": p["title"], "authors": p["authors"],
                                   "summary": p.get("summary", ""), "what": p["what"]}
    save_json(META / "paper_history.json", history)

    save_json(REPO / "docs" / "data" / "today.json",
              {"date": date.today().isoformat(), "papers": papers})
    log(f"Wrote today.json with {len(papers)} papers")
    log("=== Daily Paper Update done ===")


if __name__ == "__main__":
    sys.exit(main())
