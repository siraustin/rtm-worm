# The magnitude error

The worm's payload was replication. The disaster was the rate.

## The check, and the override

Morris did not want a fork bomb. He wanted a census. A host that was already infected should not get another copy. He also did not want a system administrator to fake the "already infected" handshake and immunize a machine. So he coded an override.

The canonical description, used by Wikipedia, by the Second Circuit's fact summary, and by most later writing:

> The worm was designed so that it would not spread to computers that it had already infected. To prevent computers from defending against this by pretending to have the worm, however, it would still infect an already infected computer one out of seven times.

One in seven is about 14 percent. Each time the worm landed on a host that reported "I'm already here," it rolled a die and, on a 1, copied anyway.

That is not a mysterious compiler bug. It is a parameter. The parameter was too large.

## Why 14 percent is a catastrophe

On a network of tens of thousands of reachable Unix hosts, a worm that *never* reinfects will still spread to every vulnerable machine that the graph can reach. That is epidemiology: an R0 above 1 with no recovery. A worm that reinfects 14 percent of the time, on every pass, on a graph that also keeps scanning, does something worse. Each host accumulates copies. Each copy keeps scanning. Load average goes to the moon. Swap thrashes. The machine is up, in the sense that the kernel is running, and down, in the sense that no person can use it.

Cornell, February 1989:

> There is no direct evidence to suggest that Morris intended for the worm to replicate uncontrollably. However, given Morris' evident knowledge of systems and networks, he knew or clearly should have known that such a consequence was certain, given the design of the worm.

A 1993 law-review writeup of the case called it "a mathematical error" that "caused the worm to spread far more quickly and widely than he had anticipated." Later popular accounts say "order of magnitude." That is the right *kind* of sentence. A 1-in-70 or 1-in-700 override might have been a hedge. A 1-in-7 override, on the actual internet of 1988, is a fork bomb with extra steps.

Michael O. Rabin's randomization mantra is sometimes cited as the inspiration for the probabilistic check. Rabin, told about the result, said Morris should have tried it on a simulator first.

## What it was not

It was not a logic bomb. It was not ransomware. Seeley: it did not modify existing files, did not install Trojan horses, did not record or transmit decrypted passwords, did not try to capture superuser privileges as an objective.

The "grappling hook" — a small portable C stub — ran on machines the main body could not fully infect, and pulled the VAX or Sun object over. Those peripheral hosts got loaded down anyway. Monoculture did the rest. Stoll: if every ARPANET host had been Berkeley Unix, the worm would have disabled all of them.

## The pattern that does not go away

A small integer, chosen by a person who is thinking about a different problem (evading a fake handshake; matching 21 inputs; shipping a channel file), applied to a system whose fan-out is enormous.

- 1988: 1 in 7.
- 2003: SQL Slammer, 376 bytes, doubling time ~8.5 seconds, because UDP and a single packet were enough.
- 19 July 2024: CrowdStrike Channel File 291, a sensor expecting 21 values and receiving 20, an out-of-bounds read, 8.5 million Windows machines in a boot loop.

The 2024 event was not a worm. It was a magnitude error in a *defender's* update, pushed to a concentrated installed base. That is the 1988 lesson with the sign flipped: the same class of mistake, now sitting inside the software that is supposed to prevent the 1988 class of attack.

## What this file will not do

It will not print the worm, the 432-word dictionary, or a reconstruction of the fingerd overflow. Those exist in museums, in RFC 1135's bibliography, at the Computer History Museum on a floppy, and in thirty years of operating-systems courses. They are not the point. The point is the rate.
