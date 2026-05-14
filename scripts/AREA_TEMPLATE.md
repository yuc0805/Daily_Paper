# Area Page Template — Luna Dong Style

This is the schema every area page in `areas/` must follow. When the scheduled task adds a new paper to an existing area page, it edits in-place to keep this structure.

Required sections, in this order. Do not skip any. If a section has no content yet, write `_To be added as papers accumulate._`

---

## `<Area Name>`

### What

A two to four sentence definition of the area. Plain language, no jargon a competent ML researcher would not know. Avoid the banned word list.

### Why

Two to four sentences on why this area matters: what problem it solves, which downstream applications benefit, why the baseline approach is insufficient.

### Baseline

The dumb-default approach you would try first if you had never read a paper in this area. Describe the baseline as a concrete procedure (one paragraph), and state explicitly what its main failure mode is. This anchors every method below as "improving on this baseline along axis X."

### Running Example

Pick one small, concrete task instance and use it consistently throughout the page. For reasoning, the running example might be a single GSM8K problem. For time-series, a single forecasting window from a public benchmark. Describe the example, the desired output, and the baseline's output on it. Every "Key Method" entry below should refer back to this example when explaining what the method does differently.

### Baseline vs Method Comparison on the Running Example

| Approach | Output on running example | Why it differs from baseline |
|---|---|---|
| Baseline | <baseline output> | (anchor) |
| <Method 1> | <output> | <one clause> |
| <Method 2> | <output> | <one clause> |

Keep this table to at most six rows. Drop the oldest methods as new ones land.

### Timeline

Chronological list of method-introducing papers, oldest to newest. Format: `YYYY-MM | <paper short title> | <one-line idea>`. Cap at 25 entries. When the table fills, archive the bottom entries to `_meta/timeline_archive_<area>.md` and keep the most recent 25 here.

### Key Methods

| Method | Year | Core idea (one clause) | Best benchmark result | Cost / limitation |
|---|---|---|---|---|
| <Method> | YYYY | <clause> | <number on benchmark> | <main weakness> |

### Benchmark Results

| Method | Benchmark | Metric | Score | Source paper |
|---|---|---|---|---|
| <Method> | <benchmark name> | <metric> | <number> | <citation key or arXiv ID> |

If methods are not directly comparable on a shared benchmark, say so explicitly above the table.

### Limitations

Bulleted list of three to seven open problems in the area. Each bullet is one sentence. These should be the limitations a researcher would cite in the related work section of their next paper.

### Paper List

Grouped by sub-area. Each paper line: `[YYYY] <Authors short> — <Title>. <link>. <zotero_key if in library, else "external">.`

Mark papers Leo has already read (those in his Zotero library) with `[KNOWN]` at the start of the line.

### Recent Activity

Last five updates to this area page. Format: `YYYY-MM-DD | <new paper added> | <one-line delta>`.

---

## Style Rules

Plain prose, no marketing language. Banned word list applies (see `_meta/style_rules.md`). Use full forms (it is, he would), not contractions. Tables are allowed; long bullet lists are not. Each section should be readable in under thirty seconds.
