# 2 November 1988: the warning was on the same network

The rescue instructions had to travel through the system that needed rescuing.

After Robert Tappan Morris released his program from MIT on 2 November 1988, it multiplied faster than he expected. He contacted a Harvard friend; an anonymous message describing countermeasures followed. The appellate record says it arrived too late because its network route was clogged. That is a documented sequence, not a reconstructed scene. [S04, p. 506](09-bibliography.md)

There was a second, less familiar obstruction. Once administrators recognized email software as one infection route, some shut down mail service. MIT's investigators report delays of up to twenty hours for critical messages at major forwarding nodes. Other infection routes remained available. A machine could lose the warning without losing the worm. [S02, §2.1.5](09-bibliography.md)

## What crossed the boundary

Morris was a first-year Cornell graduate student with considerable systems experience. The worm used flaws in sendmail and fingerd, trusted-host relationships, and password guessing. Its main executable bodies targeted VAX and Sun systems running BSD-derived Unix. These were not interchangeable paths: rsh used host trust; rexec used credentials. Calling both simply passwordless trust erases a meaningful distinction. [S04, pp. 505–506; S01, §2; S02, §§2.1.3–2.1.4](09-bibliography.md)

A worm can run and propagate as a program in its own right. It need not insert itself into a separate host program. Here, the resource-consuming replication was enough: no file-destruction payload was required. The absence of deleted files was not the absence of damage. [S01, §§1–2; S03, pp. 706–707](09-bibliography.md)

The dangerous familiarity was that useful network relationships became routes for unwanted execution. The stranger who arrived did not need a new network. It used the one built for colleagues.

## What the participants did not know yet

Finding the process did not settle how it entered. Closing one route did not settle whether another remained. Stopping the current copies did not make a still-vulnerable machine immune to its neighbors. The MIT analysis records ineffective quick remedies as well as successful ones; its account is far less tidy than a story in which everyone promptly found the same bug. [S02, §§2.3–2.4](09-bibliography.md)

RFC 1135 describes the collaboration among responders and reports elimination from most computers within 48–72 hours. That is a recovery interval, not an exact duration for every site. It is also evidence that working technical intervention mattered. The worm did not wait for a court judgment to stop spreading. [S01, §3](09-bibliography.md)

## How many?

The Cornell commission's published findings say **several thousand infected computers**, expressly without a systematic census; many additional machines needed checking or preventive work. That distinction between infected and affected should survive every retelling. [S03, p. 707](09-bibliography.md)

The FBI's retrospective uses the familiar approximately 6,000 of 60,000, or ten percent. Keep it as a conventional estimate, not a measured count accurate to the nearest host. This revision removes the uncited campus-by-campus totals rather than pretending they reconcile into a national census. [S05](09-bibliography.md)

## What was he trying to do?

The appellate court describes a goal of demonstrating inadequate security while spreading quietly. Cornell's findings distinguish likely non-destructive intent from reckless disregard of foreseeable consequences. Neither supports narration that confidently enters his mind and announces a cleanly designed internet census. [S04, pp. 505–506; S03, p. 707](09-bibliography.md)

The distinction matters. Calling it an experiment does not make it authorized. Calling it a national disruption does not prove he wanted a national disruption.

The next question is not why a program copied itself. It is why the copies failed to make room for one another. [Continue: the magnitude error](02-the-magnitude-error.md).
