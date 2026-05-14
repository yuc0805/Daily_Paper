# Style Rules

All output in this repo must follow these rules.

## Banned words

Do not use any of these: burgeoning, pivotal, in the realm of, keen, adept, endeavor, uphold, imperative, profound, ponder, cultivate, hone, delve, embrace, pave, embark, encompass, monumental, scrutinize, vast, versatile, paramount, foster, necessitates.

## Form

Use full forms only. "It is" not "it's". "He would" not "he'd". "Cannot" not "can't".

## Tone

Plain, scientifically accessible language. No marketing copy. No "this groundbreaking paper..." or "this important contribution...". State what the paper does and what number it produces; the reader judges importance.

## Format

Paragraphs are the default. Tables are allowed for structured comparison. Long bullet lists are not — if a list runs past four bullets, rewrite it as a paragraph or a table. Headers should follow the AREA_TEMPLATE.md schema exactly.

## Citations

Inside an area page, refer to papers by Zotero citation key when available, otherwise by arXiv ID. Link to the arXiv abs page (https://arxiv.org/abs/...) — never to the PDF.

## Lineage notes (papers/<YYYY>/<MM>/<DD>/<arxiv-id>.md)

Each paper note follows this structure:

```
# <Paper title>

**Arxiv:** <id> | **Date:** YYYY-MM-DD | **Area:** <area>

## What it does
Two to four sentence summary.

## Direct parents (in Leo's library)
- [<zotero_key>] <Parent title> — <one sentence on what this parent established>
- [<zotero_key>] <Parent title> — ...

## Delta from parents
One paragraph (3-5 sentences) explaining what the new paper changes relative to the parents named above. This is the "how does it build on what I know" answer Leo asked for. Frame it as: "Where <parent> did X, this paper does Y, because Z."

## Why Leo should care
One paragraph. If the paper is in time-series or bio-sensing, also note: which CV/NLP method it imported, and whether that method is now closed off as low-hanging fruit.

## Verdict
One of: Tier A deep read | Tier B TLDR | Tier C scan | Skip (with reason).
```
