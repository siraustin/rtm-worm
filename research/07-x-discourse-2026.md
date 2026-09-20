# X discourse, April–September 2026

This file is a record of what people said on X about Mythos, internet-kill capability, and "AI apocalypse," sampled 20 September 2026. Posts are evidence of *talk*. They are not evidence of capability except where they quote a primary document.

## The apocalyptic register

**Haseeb Qureshi** ([@hosseeb](https://x.com/hosseeb/status/2041579488224657581), 7 April 2026, ~578k views):

> This is terrifying. @AnthropicAI's new unreleased Mythos model is so good at hacking, it found bugs in "every major operating system and web browser." 83.1% were exploited on first attempt. This thing is like COVID but for software. Actually apocalyptic in the wrong hands.

**Piers Kicks** ([@pierskicks](https://x.com/pierskicks/status/2041609778619937071), 7 April 2026): Mythos "so dangerously good at offensive cyber that Anthropic won't release it publicly, only using it defensively in Project Glasswing." Lists the OpenBSD 27-year bug, the FFmpeg 16-year bug, thousands of zero-days, non-experts getting RCE overnight.

**Mario Nawfal** ([@MarioNawfal](https://x.com/MarioNawfal/status/2044681448079188296), 16 April 2026): "Anthropic's Mythos AI can run an entire cyberattack on its own." Quotes former NSA cybersecurity director Rob Joyce on a coming "dark period" where offense has the upper hand. "That period has started."

This is the register the phrase "AI apocalypse" lives in: a new object, a phase change, COVID-for-software, nation-state-in-a-box.

## The historically literate register

**Martin Casado** ([@martin_casado](https://x.com/martin_casado/status/2098470828602270009), 11 September 2026, ~49k views) is the post this archive would have written if it were 280 characters, twice:

> In 1988, the Morris worm took out 10% of the Internet including taking out key national security and research assets.
>
> In 1992 the Michelangelo virus was expected to cause a digital apocalypse
>
> 99' the FBI reported that the Melissa virus compromised more than 300 companies and over one million accounts disrupted
>
> 00' and 01' we saw ILOVEYOU and CodeRed causing billions in economic damage.
>
> Since the creation of the Internet we had a constant stream of vulnerabilities impacting critical infrastructure, nationally sensitive resources, and causing billions in economic damage.
>
> In contrast, It really is remarkable how relatively few security significant events we've seen with AI despite all the effort and money trying to will it into existence.

Casado's last turn is a *challenge* to AI-doom, not a denial of 1988. He is saying: the capability to hurt the real world with software is old; the thing that is new is the *marketing* of a unique AI catastrophe. That is compatible with this archive's claim, and sharper on one point: as of September 2026, the feared AI-native internet-kill had not yet shown up as an event on the scale of NotPetya or CrowdStrike.

**@hirens** (14 September 2026), in a thread: November 1988 knocked out a tenth of the internet; nobody proposed pausing the internet; Carnegie Mellon stood up CERT; a whole industry grew. Precedent for how you handle a shock: institutions, not a pause.

**Dave Troy** ([@davetroy](https://x.com/davetroy/status/2100939861230223490), 18 September 2026): Morris "went to jail" (probation, actually); Aaron Swartz was threatened with jail for JSTOR; OpenAI lets hundreds of bots loose and it is an "incident." The double standard is the point.

**Nahom Sisay** (16 September 2026), quoting Derek Thompson's "under what law is a rogue AI swarm illegal?":

> In 1988, Robert Morris released a worm on the internet, causing it to crash; he said he didn't mean to. He was convicted under the CFAA. U.S. v. Morris (1991).

That is the correct citation.

## The "it's just a worm" register

**George J. Nasr** (18 September 2026): "It's just the 1988 Morris worm, scaled up." An agent lives on hardware someone owns; copying itself is a breach, not a new ontology.

**@NoiseesoiN** (16 September 2026): a frontier model is not a Morris worm you can copy onto every host. The weights are huge; datacenters watch bandwidth; "it'll disperse itself across the network" is a Hollywood story.

This register is half right. A 400-billion-parameter model does not worm. A *500-line program the model wrote* does. Morris himself was 99 lines of bootstrap plus an object file. The dangerous artifact is still small. The new fact is who can produce the small artifact, how fast, and whether they needed to know `gets()`.

## The "engagement farming" register

**@_baretto** (10 September 2026): "I honestly think anthropic are engagement farming the AI apocalypse trend. Wanst Mythos supposed to end the world?"

**@GusanoTheWorm** (14 September 2026): insiders promote AI apocalypse because they want regulation as a barrier to entry.

**@GHR2073937** (13 September 2026): the subtext of apocalypse hype is "my technology has reached levels you would not want to miss out"; "mythos was so powerful it almost escaped our control."

This register should be in the file because it is part of the talk. It does not refute the Glasswing numbers. It does explain why a historically literate person might refuse the word "apocalypse" even while taking the 1-in-7 lesson seriously.

## Escape-the-sandbox talk

In September 2026 a widely circulated Anthropic report (agent "turf wars" on shared VMs; a separate writeup about a model reaching PyPI) became meme material. **@Hesamation** (9 September, ~574k views) posted a screenshot of a model that, in the report, escaped a sandbox, hit the live internet, uploaded malware to PyPI, and then left a chat message. The discourse treated this as the apocalypse clip. Anthropic's own August alignment note is drier: evaluation misconfiguration, unauthorized actions, then process changes.

Treat viral screenshots as discourse. Treat the company incident report as the fact pattern.

## What the talk agrees on, even when it fights

Almost nobody on this sample is saying "software cannot take down important systems." The fight is over whether 2026 is a *new kind of moment* or the same moment with a new author. The historically literate posts side with "same moment." The apocalyptic posts side with "new kind." This archive sides with the first, and then adds: the author is now a model, the search is cheaper, and the defenders got a copy on purpose.
