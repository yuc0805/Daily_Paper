# Area Page Template — Luna Dong Style

This is the schema every area page in `areas/` must follow. When the scheduled task adds a new paper to an existing area page, it edits in-place to keep this structure.

Required sections, in this order. Do not skip any. If a section has no content yet, write `_To be added as papers accumulate._`

---

## `<Area Name>`

### Timeline

Chronological list of method-introducing papers, oldest to newest. Format: `YYYY-MM | <paper short title> | <one-line idea>`. Cap at 25 entries. When the table fills, archive the bottom entries to `_meta/timeline_archive_<area>.md` and keep the most recent 25 here.

### Paper List

Grouped by sub-area. Each paper line: `[YYYY] <Authors short> — <Title>. <link>. <zotero_key if in library, else "external">.`

Mark papers Leo has already read (those in his Zotero library) with `[KNOWN]` at the start of the line. When the paper has a detail page at `docs/papers/<zotero_key>.html`, the renderer turns the line into a hyperlink to that page automatically. Per-paper What / Why / How / lineage content lives on the paper page, not here.

### Recent Activity

Last five updates to this area page. Format: `YYYY-MM-DD | <new paper added> | <one-line delta>`.

---

## Style Rules

Plain prose, no marketing language. Banned word list applies (see `_meta/style_rules.md`). Use full forms (it is, he would), not contractions. Tables are allowed; long bullet lists are not. Each section should be readable in under thirty seconds.
