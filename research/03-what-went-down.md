# What actually went down

The claim in casual talk is that the Morris worm "took down ARPANET, defense networks, and basically the entire internet." That sentence is doing too much work. The documented event is still large enough that the extra work is unnecessary.

## Three networks, not one

By 1988 the thing people now call "the internet" was already a federation:

- **ARPANET**, the original DARPA packet network, in its last years. The ARPANET/MILNET split had happened in 1983. ARPANET in 1988 was a research network, not the classified military backbone.
- **MILNET**, the unclassified military operational network, connected to the research internet only at controlled mailbridges.
- **NSFNET**, the National Science Foundation backbone that actually carried most research traffic by then, plus regional networks hanging off it.

NSA's own post-mortem meeting, 8 November 1988, was titled *ARPANET/MILNET Computer Virus Attack of 3 November 1988*. That title is why later writers say "ARPANET" and "defense networks" in the same breath. It is a real document (National Security Archive, Document 01). It is not proof that classified systems fell.

## What the worm could touch

RFC 1135: VAX and Sun-3, 4.2/4.3 BSD. Cornell: Unix derived from CSRG work, including SunOS. The worm could *enter* some other Unixes (HP at MIT, for example) and fail to rebuild. It had no Windows, no IBM mainframe, no router OS, no X.25, no DECnet.

Clifford Stoll's monoculture remark is the right counterfactual: if the research internet had been all Berkeley Unix, the worm would have disabled all of it. It wasn't, so it didn't.

## Defense and military

Documented:

- The Second Circuit: "military sites."
- FBI: NASA, Lawrence Livermore. "Vital military and university functions slowed to a crawl."
- NASA Ames filed an incident report (still cited; a copy circulates as a public PDF).
- The Defense Communications Agency inhibited the mailbridges between ARPANET and MILNET during the event, which is the act of a defender who thinks the unclassified military network is in the blast radius.
- A follow-on, 29 November 1988: an FTP break-in on MILNET. That incident, on top of the worm, is part of why DARPA funded CERT.

Not documented, and should not be claimed:

- That classified networks (SIPR, what would later be SIPRNet, JWICS, etc.) were taken down. They were not on this internet.
- That the Pentagon "went dark" as an institution.
- That MILNET collapsed. The split and the mailbridge shutdown are evidence of *containment*, which is the opposite of "defense networks fell."

So: **unclassified military and national-lab Unix was in the victim set.** Classified defense networks were not. Anyone who needs a one-line version can use the Second Circuit's: universities, military sites, medical research.

## The internet itself

Cornell, on impact:

> Anecdotal evidence also suggests that slowdowns or shutdowns on infected and affected computers delayed research and other productive work, but no evidence of lasting damage has come to the Commission's attention. The main impact was on the time of hundreds of staff members around the nation.

RFC 1135's reviewers, and the MIT team (Eichin & Rochlis), are explicit on a point that later myth-making drops: **the network layer did its job.** Packets moved. Mail piled up because *hosts* were sick, not because the backbone was destroyed. Sites then *chose* to partition — regional networks dropping off NSFNET — so they could clean without being reinfected. Wikipedia's summary of that partition ("the Internet was partitioned for several days") is right as operational history and easy to misread as "the internet was dead."

Email was delayed for days. Some institutions wiped machines. Some stayed off the network for as long as a week. That is a real outage of *use*, not of *fiber*.

## Cost

GAO, via Stoll: $100,000 to $10 million. Per-site cleanup in the Second Circuit record: $200 to $53,000. An industry association floated $96 million; Cornell called that "self-serving" and "grossly exaggerated," because it priced hypothetical downtime and assumed 6,000 hosts at $16,000 each, "considering no work or data were irretrievably lost."

The honest range is: millions, not billions; days, not months; hosts, not the substrate.

## Why the inflated sentence persists

"Took down the internet" is the sentence a newspaper can print. "Rendered a large fraction of BSD Unix hosts unusable and forced a defensive partition of NSFNET, including NASA and military research, via a 1-in-7 reinfection override" is the sentence the documents support. This archive uses the second sentence, and then says: that was already enough to prove the capability.
