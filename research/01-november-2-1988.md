# 2 November 1988

At about 8:30 p.m. Eastern on Wednesday, 2 November 1988, a self-replicating program left a machine at MIT and began looking for other Unix hosts. By Thursday morning, system administrators at universities, national laboratories, and military research sites were watching load averages climb until machines became unusable. A Berkeley student mailed: "We are currently under attack."

The author was Robert Tappan Morris, 23, a first-year Cornell computer-science graduate student, Harvard '88, son of Robert Morris Sr. — then chief scientist at the NSA's National Computer Security Center, and one of the people who had helped invent Unix password hashing at Bell Labs. The son released the program from MIT so it would not point straight back to Ithaca.

## What it was

RFC 1135, Joyce Reynolds, December 1989, still the Internet's own after-action report, calls the event "the helminthiasis of the Internet": infestation by parasitic worms. The program infected VAX computers and Sun-3 workstations running 4.2 and 4.3 Berkeley Unix. It was a worm, not a virus. It ran on its own. It did not need a host program.

It got in four ways, all already known in spirit to people who ran Unix:

1. **sendmail debug.** A non-standard `DEBUG` command, left on in many distributions, let a remote client pass commands. The worm used it as a delivery path.
2. **fingerd.** On 4.3BSD VAX machines, the daemon used `gets()` with no bounds check. The worm overflowed the buffer and ran a small stub. This is the incident that taught a generation of programmers that `gets` is a loaded gun.
3. **rsh / rexec and trusted hosts.** `.rhosts`, `/etc/hosts.equiv`, and the culture of "this machine trusts that machine" let the worm walk across local clusters without guessing anything.
4. **Password guessing.** It tried empty passwords, the username, the username twice, the nickname, the last name, the last name backwards, a 432-word private dictionary, and `/usr/dict/words`.

The worm did not delete files. It did not install a backdoor for later use. It did not try to become root as a goal. It hid itself, guessed where to go next, and copied. Seeley, *A Tour of the Worm*: it did not propagate over UUCP, X.25, DECnet, or BITNET. It was a TCP/IP animal.

## Who got hit

FBI case summary, still on fbi.gov: Harvard, Princeton, Stanford, Johns Hopkins, NASA, Lawrence Livermore. The Second Circuit, when it later affirmed the conviction, said "leading universities, military sites, and medical research facilities." Cornell found copies of the worm in Morris's own account in stages of development through the afternoon of 2 November, structurally identical to the specimen Berkeley decompiled off the network.

The famous number is **6,000 of about 60,000** internet-connected computers — 10 percent — within 24 hours. The FBI still uses it. Paul Graham, who was at Harvard, later wrote that he was in the room when the statistic was cooked: someone guessed 60,000 hosts and guessed 10 percent. Clifford Stoll, who fought the worm at the time, wrote that he surveyed the network and found about 2,000 machines "dead in the water" within fifteen hours, and that cleanup often took two days. Cornell declined to census the network, said several thousand were infected, said many thousands more had to be checked and patched, and said a population-dynamics estimate put the number nearer 3,000. MIT AI Lab: about 90 Unix machines infected of 300 in the lab, plus 50 HP machines the worm could enter but not rebuild itself on. Cornell campus: Krafft estimated 100–150. Berkeley: around 100.

The order of magnitude is not in serious dispute. Thousands of hosts, a large fraction of the BSD Unix population, in hours.

## What people did

There was no CERT yet. Gene Spafford stood up the Phage mailing list. Berkeley and MIT teams decompiled the binary independently and compared notes on the phone in the middle of the night. Patches for sendmail and fingerd went out over the same network the worm was using. Sites disconnected from NSFNET to clean themselves without being recontaminated. Cornell isolated itself on the morning of 3 November and was back that evening. RFC 1135: most machines were cleaned in 48–72 hours; government and commercial sites were slower than the universities.

Morris asked a Harvard friend, Andrew Sudduth, to post an anonymous apology and a hint at a kill. The message arrived late, because the mail system was the thing that was sick. He did not call his advisor, his chair, or anyone who could have acted nationally. Cornell: "minimal efforts," and a greater desire to remain anonymous.

John Markoff at the *New York Times* got the story. Sudduth, talking to the paper, slipped and used the initials RTM. The *Times* named him.

## What it was for

Morris has said, then and later, that he wanted to measure the internet — to see how far a quiet program could walk. Cornell found no evidence he meant to destroy data or to knock machines over. Cornell also found that he designed the worm to hide, to persist even if discovered, and that given the design, uncontrollable replication was certain. "Reckless disregard of those probable consequences."

The Cornell commission, which did not interview him (his lawyer invoked the Fifth while a grand jury was sitting), called the launch "a juvenile act that ignored the clear potential consequences." It rejected the press frame that he had done the community a favor by exposing Unix. Dennis Ritchie's own note in the Unix manual already said Unix was not developed with security in mind, "and this fact alone guarantees a vast number of holes."

That is the opening fact of this archive. The holes were known. The network was trusted. One student, one night, one numeric choice.
