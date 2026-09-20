# Primary documents and provenance

The original three source files are preserved unchanged. They were present at baseline commit `dd7c15396f5d1043f2a4d6336bf6567f29af4378`.

| Existing file | Git blob SHA-1 at baseline | Status of this research pass |
| --- | --- | --- |
| `rfc1135.txt` | `e57d0976eba138b5c555a466d4440c2eaa65e4cc` | Official RFC text read online; local bytes not compared |
| `cornell-worm-report.pdf` | `011b2408659213ee4307fe41f67f45065e98914e` | Inventoried and retained; not fully inspected; original acquisition URL and page-count claim remain unauthenticated |
| `eisenberg-cacm-cornell.pdf` | `8474cd208738f47ae46750a9e6c6189d89dbc004` | Separate Cornell-hosted four-page CACM excerpt inspected; byte identity with this file not established |

These are **Git blob identifiers**, not file SHA-256 digests and not proofs of authenticity. They allow future researchers to identify exactly which repository objects were preserved.

Verified public locators, page/section references, reporting dates, and source limitations live in [the source register](../research/09-bibliography.md). The newly consulted MIT technical report is linked there; no exploit source or dictionary has been added.

The earlier description of the long report as 145 pages should not be confused with the CACM introduction's description of a 45-page commission report and accompanying materials. Without examining the full stored object, this pass does not resolve whether the difference is appendices, a different compilation, or an erroneous count.

## What an archive capture should record

For any newly downloaded source: canonical URL, retrieval timestamp, publication/update date, exact filename, SHA-256 of the captured bytes, relevant page/section locators, and any missing content. Never assign a digest to a source that was only read through a web rendering.

The two existing JPEGs have no demonstrated photographer, creation date, license, or archival provenance in the original notes. They are retained in `assets/` but not displayed as documentary photographs in the revised public essay.
