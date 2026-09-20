# Laws and consequences

If the technical story of 1988 is a magnitude error, the political story is the invention of a federal crime that did not require the author to mean the damage.

## The statute

Congress passed the Computer Fraud and Abuse Act in 1986, 18 U.S.C. § 1030, two years before the worm. It had not yet produced a jury conviction. The FBI's own history page still frames the legal question as it was asked in 1988: "But had Morris broken federal law? Turns out, he had."

He was indicted in 1989, tried in the Northern District of New York, and convicted in January 1990 of violating § 1030(a)(5)(A) as it then read: intentionally accessing a federal-interest computer without authorization, and thereby causing loss of $1,000 or more. On 4 May 1990 Judge Howard G. Munson sentenced him to three years' probation, 400 hours of community service, a $10,050 fine, and the cost of supervision. That was a departure below the federal sentencing guidelines, which called for prison time. Munson said prison did not fit. The *Times*: the Justice Department had spent eight months deciding to prosecute at all, and at sentencing the government declined to recommend a number.

## What the Second Circuit decided

*United States v. Morris*, 928 F.2d 504 (2d Cir. 7 March 1991), Judge Jon O. Newman. Three issues, all of which still matter for anyone who wants to say "the model didn't mean to."

**Intent.** Morris argued that "intentionally" applied to the damage, and that he had not intended to prevent use of the machines. The government argued the adverb attached only to *access*. The court agreed with the government. Congress had tightened "knowingly" to "intentionally" in 1986 to spare people who wandered into a system by mistake — not to spare people who wandered in on purpose and then caused more harm than they budgeted for.

**Authorization.** Morris had accounts at Cornell, Harvard, Berkeley. He said he had exceeded authorized access, not gained unauthorized access, and that the Act was aimed at outsiders. The court: he used sendmail and fingerd in ways unrelated to their intended function; he guessed passwords; the worm crossed departmental and military systems. That is unauthorized access.

**The jury.** "Authorization" is a common word. The district court did not have to define it.

The 1991 opinion is also, as later writers noted, the first U.S. appellate decision to use the word "Internet," which it defined as "a national computer network."

In 1996 Congress amended the CFAA again to put mental-state words in more places, in part because of the fight in this case.

## What the conviction was for

Not for being clever. Not for measuring the network. For accessing machines without authorization and causing loss. Reckless design counted. "I meant it as an experiment" did not.

That is the load-bearing legal fact of the next forty years of worms, ransomware, and now agent incidents. When people on X in September 2026 ask what law would cover a rogue AI swarm, the answer that keeps coming back is this case. Derek Thompson asked; Nahom Sisay answered with *U.S. v. Morris*. David Thaw pointed at the same opinion. Dave Troy compared Morris (who "went to jail" — he did not, he got probation — but the direction is right) with OpenAI "incidents."

## CERT

DARPA funded the Computer Emergency Response Team at Carnegie Mellon's Software Engineering Institute in the days after the worm. FBI: "Just days after the attack." A 29 November MILNET FTP break-in is often listed as the last shove. CERT/CC became the template for CSIRTs worldwide. Spafford's Phage list was the ad-hoc version the same week.

This is the other half of "what stopped it." Not only a felony statute. An institution whose job is to tell everyone else, at 3 a.m., which patch to install.

## Ethics documents the incident produced

RFC 1135 reprints, and RFC 1087 is, the Internet Activities Board's ethics statement of January 1989 (local copy: `sources/rfc1087.txt`). It calls "unethical and unacceptable" any activity which purposely "(a) seeks to gain unauthorized access to the resources of the Internet, (b) disrupts the intended use of the Internet, (c) wastes resources (people, capacity, computer) through such actions, (d) destroys the integrity of computer-based information, and/or (e) compromises the privacy of users." Access to the Internet, it says, "is a privilege and should be treated as such." NSF's DAP said the same in November 1988. MIT already had a student statement. CPSR warned against closing the network in a panic.

Cornell's own comment is the one this archive keeps:

> This was not a simple act of trespass analogous to wandering through someone's unlocked house without permission but with no intent to cause damage. A more apt analogy would be the driving of a golf cart on a rainy day through most houses in a neighborhood. The driver may have navigated carefully and broken no china, but it should have been obvious to the driver that the mud on the tires would soil the carpets.

Experiments of this kind, the commission said, belong in an isolated environment. The Cornell CS faculty would have helped set one up. Nobody asked.

## Afterward

Morris finished his Ph.D. at Harvard, cofounded Y Combinator with Paul Graham, and has taught distributed systems at MIT. The first lecture of that course, as people on X still clip, includes a dry warning about building distributed systems. He is the existence proof that the 1990 sentence did not "destroy a career," which is what the professional community told Cornell it wanted: serious discipline, not exile.

The CFAA, meanwhile, became the statute used against Aaron Swartz, against Lori Drew, against countless CFAA-as-blunt-instrument cases. That later history is real and ugly. It does not unmake the 1988 holding: if you put a self-replicating program on other people's computers and they fall over, "I didn't mean that part" is not a defense.
