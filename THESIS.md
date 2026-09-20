# The claim

The ability to take down a meaningful fraction of the internet has existed since the late 1980s. It has not been waiting on artificial general intelligence, on "AI apocalypse," or on some future capability threshold. It showed up on the evening of 2 November 1988, when a Cornell graduate student released a self-replicating program that exploited already-known Unix holes and then reinfected hosts at a rate that was wrong by a dangerous margin.

What stopped a repeat from becoming the ordinary weather of the network was not missing technical ability. It was law, professional consequence, patch culture, and — later — a defender industry. Those restraints are still what stop it. The ability itself has only become cheaper, faster, and more widely distributed.

In 2026 the picture is not simply worse. Defenders now have Mythos-class models, gated through Project Glasswing, scanning the software the world actually runs. That is a real change. It does not cancel the 1988 lesson. It is the 1988 lesson, applied at machine speed: the bugs were always there; the question is who finds them first, and under what rules.

## What this archive argues

1. **The 1988 event was internet-scale.** It did not "destroy ARPANET" as a single object, and it did not take down classified defense networks. It did grind thousands of Unix hosts — including NASA, national labs, and military research sites — to a halt, and it forced a defensive partition of the research internet. That is enough. Folklore that says "the entire internet died" is too large; folklore that says "it was just a campus prank" is too small.

2. **The damage mechanism was a magnitude error, not a payload.** The worm did not delete files. It copied itself. Morris designed a 1-in-7 override so that a host claiming to be already infected would still be reinfected about 14 percent of the time. On a network of tens of thousands of machines, that rate made unbounded replication the expected outcome. Cornell's own commission said he knew or clearly should have known this was certain.

3. **The legal response is the template.** *United States v. Morris* (1991) was the first jury conviction under the Computer Fraud and Abuse Act. The Second Circuit held that the government did not have to prove Morris intended the damage — only that he intended the unauthorized access. That is still the doctrine people reach for when an AI lab, a worm author, or an agent swarm "didn't mean to."

4. **The lineage is continuous.** Code Red, SQL Slammer, Conficker, Mirai, WannaCry, NotPetya, log4j, and the CrowdStrike outage of 19 July 2024 are the same story at larger scale. CrowdStrike is the cleanest modern rhyme: a logic error in a content update, not an attack, took down 8.5 million Windows machines and grounded flights. Capability plus concentration plus a small numeric mistake.

5. **Current X talk about an "AI apocalypse" mostly rediscovers 1988.** Some posts treat Mythos as a new species of doom. Some treat AI-safety rhetoric as regulatory capture. The historically literate posts — Martin Casado's 11 September 2026 thread is the type specimen — point at Morris, Melissa, ILOVEYOU, and Code Red and ask why this decade is being sold as the first time software could hurt the real world.

6. **We are in one specific way in a better position.** CERT exists because of Morris. Patch Tuesday exists because of the 2000s worms. Mythos and Glasswing exist because a frontier model started finding thousand-count vulnerability sets in the software that runs browsers, kernels, and clouds. Ability is not the scarce resource. Custody of the ability is.

## What this archive does not claim

- That Morris "took down ARPANET" in the sense of destroying the backbone. Cornell: the networks themselves functioned. Hosts did not.
- That classified military networks fell. MILNET had been split from ARPANET in 1983; the Defense Communications Agency closed mailbridges during the incident. Unclassified military *research* machines were hit.
- That 6,000 infected hosts is a measured census. Paul Graham later said the 10-percent-of-60,000 figure was cooked from a guess. Cornell said thousands, order of magnitude likely correct. Clifford Stoll said a couple thousand. The FBI still prints 6,000 of 60,000.
- That Mythos has "saved the internet." It has given a gated set of defenders a head start against a capability that Anthropic itself says other labs will match. That is better than 1988. It is not a shield.
- That this file is legal advice, a how-to, or exploit documentation. It is a historical argument.
