# AI Knowledge Graph

A progressively-built knowledge graph of AI/ML research, anchored on Leo's Zotero library (475 papers across 25 collections as of 2026-05-13).

## Purpose

Two jobs. First, maintain one Luna Dong-style area page per research topic, kept current as new papers land. Second, for every new paper that arrives in the daily digest, write a short lineage note explaining how the new paper builds on papers Leo already knows.

## Layout

```
AI-Knowledge-Graph/
├── README.md                    (this file)
├── areas/                       (one .md per research area)
│   ├── reasoning.md
│   ├── llm.md
│   ├── time-series.md
│   └── ...
├── papers/                      (one .md per new paper added by digest)
│   └── 2026/05/13/
│       └── <arxiv-id>.md
├── lineage/                     (one .json per area: paper→ancestors map)
│   └── reasoning.json
├── scripts/
│   ├── AREA_TEMPLATE.md         (Luna Dong-style schema)
│   └── (future helpers)
└── _meta/
    ├── zotero_index.json        (cached list of Zotero items keyed by arXiv ID / DOI)
    ├── area_index.json          (which Zotero collection maps to which area page)
    ├── style_rules.md           (banned word list, tone rules)
    └── timeline_archive_*.md    (old timeline entries that overflowed)
```

## Daily update flow

The scheduled task `daily-ai-digest-5am` runs at 5:00 AM ET. For each new paper that qualifies for the digest, it:

1. Identifies the area page the paper belongs to (creates one if none exists).
2. Looks up direct intellectual parents in `zotero_index.json` (1-hop only).
3. Writes a short note to `papers/<YYYY>/<MM>/<DD>/<arxiv-id>.md` explaining what the paper does and how it extends those parents.
4. Edits the relevant `areas/<area>.md` in place — updates the Timeline, Key Methods, Benchmark Results, and Recent Activity sections.
5. Appends a lineage edge to `lineage/<area>.json`.
6. Stages, commits, and pushes to GitHub (if remote is configured).

## Seeding flow

A one-time seeding task `seed-knowledge-graph` (created separately) walks all 25 Zotero collections and produces an initial Luna Dong-style page per collection. This is heavy and runs once.

