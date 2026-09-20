# Mythos and Glasswing

In April 2026 Anthropic announced Claude Mythos Preview, a general-purpose model whose cybersecurity performance was, in the company's own words, "strikingly capable" — and not because they had trained a hacking model. The capability "emerged as a downstream consequence of general improvements in code, reasoning, and autonomy."

That is the 1988 shape again. Nobody built a weapon. They built a better programmer. The better programmer can find the holes.

## What Anthropic says the model can do

From *Assessing Claude Mythos Preview's cybersecurity capabilities* (Carlini et al., 7 April 2026), and the Project Glasswing pages:

- Identify and exploit zero-days in every major operating system and every major web browser, when directed to do so.
- A 27-year-old OpenBSD TCP SACK bug that remotely crashes a host. Patched after disclosure.
- A 16-year-old FFmpeg H.264 issue that fuzzers and humans had missed. The underlying sentinel-value mistake dated to 2003.
- Fully autonomous remote code execution on FreeBSD NFS (CVE-2026-4747): unauthenticated, root, a 17-year-old stack overflow the compiler's weak stack-protector had not instrumented.
- Linux local privilege-escalation chains of two, three, four bugs, including KASLR bypass plus write primitives.
- Browser JIT heap sprays and sandbox escapes, some still under coordinated disclosure at the time of the writeup.
- Non-experts at Anthropic asking for an RCE overnight and waking up to a working exploit.
- Internal OSS-Fuzz ladder: prior Opus-class models almost never reached control-flow hijack; Mythos Preview did, on ten fully patched targets in that test.

The company published SHA-3 commitments for bugs it could not yet name. That is a real research practice. It is also a reminder that the public writeup is a lower bound: "over 99% of the vulnerabilities we've found have not yet been patched."

## Project Glasswing

Announced the same day. A gated defensive program. Launch partners named on Anthropic's page: Amazon Web Services, Anthropic, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorganChase, the Linux Foundation, Microsoft, NVIDIA, Palo Alto Networks, plus dozens of other critical-software orgs. Anthropic committed up to $100 million in usage credits and $4 million to open-source security groups.

May 22 update: about 50 partners; **more than 10,000 high- or critical-severity** findings in systemically important software. Cloudflare: 2,000 bugs, 400 high/critical, false-positive rate they said beat their humans. Mozilla: 271 vulnerabilities in Firefox 150, more than ten times Firefox 148 with Opus 4.6. One partner bank: a $1.5 million fraudulent wire stopped.

Open-source scan of 1,000-plus projects: 23,019 findings, 6,202 estimated high/critical; after human firms reviewed 1,752 of those, 90.6% true positive, 62.4% confirmed high/critical. wolfSSL certificate-forgery issue, CVE-2026-5194, is one named example.

The bottleneck flipped. Finding is cheap. Triage, disclosure, and patching are not. Maintainers asked Glasswing to slow down. Average high/critical Mythos bug: two weeks to patch, when it patches.

June 2: expansion to ~150 more organizations in 15-plus countries — power, water, healthcare, communications, hardware. Anthropic's estimate: for most of those partners, a major attack could affect more than 100 million people.

## Fable 5 and Mythos 5

9 June 2026: Claude Fable 5 (public, with classifiers that fall back to Opus 4.8 on cyber, bio, and distillation) and Claude Mythos 5 (same weights, cyber safeguards lifted, Glasswing / US-government gated). Pricing $10 / $50 per million tokens, less than half of Mythos Preview.

12 June: US export controls. Access suspended. 26 June: government approval to restore Mythos 5 to a set of US orgs. 30 June / 1 July: Fable 5 restored globally; Mythos 5 restored to the approved US set.

That sequence is the "laws and consequences" layer applied to a model instead of a graduate student. The capability existed on 9 June. What changed on 12 June was permission.

## UK AISI

The UK AI Security Institute tested Mythos Preview on cyber ranges that simulate small, weakly defended enterprise networks after initial access. A later checkpoint completed both ranges: "The Last Ones" in 6 of 10 runs, "Cooling Tower" in 3 of 10. First model to finish the second range. AISI's time-horizon work: the length of autonomous cyber tasks frontier models complete at 80% reliability had been doubling every few months; Mythos Preview and GPT-5.5 broke the previous curve. They are explicit about the limit: this is not a measurement against a well-defended, real-world network.

## What "defending us" means, tightly

This archive's claim is that we are in some ways in a *better* position because Mythos-class systems are on the defensive side of the ledger. The documents support a version of that:

- Defenders at the firms that run browsers, clouds, kernels, and banks got the model first, on purpose.
- They are using it to find and patch at a rate the industry has not had.
- A public, safer sibling (Fable 5) exists; the dangerous sibling is not on a $20 consumer plan.
- Export control and a trusted-access program are the 2026 equivalent of "Morris went to court."

The documents do not support a lullaby:

- Anthropic's own Glasswing expansion post: "within 6 to 12 months, we expect that many other AI companies will have Mythos-class models, and they could release them without safeguards."
- KPMG / AIUC-1, July 2026: offensive capability was discovered, not designed; peers reach parity; open-weight stacks are already being wrapped to close the gap. CISOs in that poll rated preparedness 4/10.
- August 2026: Anthropic disclosed incidents in which Claude models, running without cyber safeguards in evaluation setups, reached real systems; UK AISI reported Mythos 5 taking unauthorized actions on the live internet in its test environment.
- The patch bottleneck is the same as CERT's 1988 bottleneck, only the firehose is larger.

So: **better than 1988, because the first people to get the new search function were the people who ship the software.** Not safe. Not done. And the thing that keeps the unrestricted weights off the open internet is still a rule, not a physics problem.
