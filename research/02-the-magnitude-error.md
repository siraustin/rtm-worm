# The magnitude error: the check that could fail open

**One-in-seven was real. The claim that it was the whole disaster was not.**

The Second Circuit's factual summary describes a mechanism meant to avoid duplicates, overridden one time in seven to defeat false claims that a machine was already infected. That is a useful explanation of the design's purpose. It is not a line-by-line specification of the program. [S04, p. 506](09-bibliography.md)

## Read the implementation account alongside the courtroom account

Eichin and Rochlis describe the program sometimes skipping its **local check for another running copy** altogether. They also identify race conditions between arriving copies, failed coordination on overloaded machines, and work performed before a request to terminate took effect. In particular, simultaneous arrivals could miss one another; only one became a listener. More load could cause more timeouts in the check. [S02, §A.3.1, p. 8; §2.3.1, p. 5](09-bibliography.md)

This is the feedback loop the first draft underplayed:

> Additional copies consume resources; resource pressure makes coordination less reliable; failed coordination allows additional copies to keep working.

That sentence is a synthesis of the MIT analysis, not a quotation or a calibrated growth law. Multiple processes, imperfect exclusion, delayed stopping, architecture, and contact patterns all matter. A scalar probability cannot substitute for them.

## An honest calculation

Suppose, solely for illustration, that an independent event has probability p = 1/7 on each of k trials. Then:

- Expected number of events: **k/7**.
- Probability of at least one event: **1 − (6/7)^k**.
- At 7 trials, that probability is about **66.0%**, not a guarantee of exactly one event.
- At 20 trials, it is about **95.4%**.

These results follow from the assumptions, not from measured worm traffic. They say nothing by themselves about time elapsed, number of infected hosts, CPU load, network topology, or whether a machine has failed. The historical program's random generator and interacting copies are not asserted to satisfy independent-trial assumptions.

The revised browser interactive computes this probability. It does not invent a Unix load average, make every copy add a fixed amount of load, or declare that twelve copies rendered every machine unusable. Those were unsupported features of the original interactive.

## What cannot be inferred

Changing the override to one-in-seventy or one-in-seven-hundred is not demonstrated to make the historical design safe. Other duplicate-control failures remain; even a perfectly implemented probability would need a time horizon and arrival model before supporting a resource bound.

Likewise, an R0 above one is not a proof that every susceptible machine in a real network will be infected. Reachability, randomness, heterogeneous services, disconnections, and remediation all matter. Mathematical models are useful precisely when their assumptions remain visible.

## Why this is more interesting than a typo

The dangerous choice was not simply that someone picked a large number. It was that the mechanism intended to keep the program inconspicuous was not a reliable limit on its behavior. It could keep doing useful work for itself after the conditions for safe operation had disappeared.

That is a comparison we can carry into later incidents. It does not require pretending that a worm and a faulty security update share an identical implementation.
