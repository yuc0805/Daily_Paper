# AI Digest — 2026-09-05

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A not done by 6 AM, stop.

Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.

Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

---

## Tier A — deep read

### LatentPress: Context Compression Beyond Text and Vision
Zhou and Sang · arXiv [2609.01507](https://arxiv.org/abs/2609.01507) · [code](https://github.com/HJSang/LatentPress)

**Problem.** Compressed context is normally carried in one of two formats: human-readable text produced by summarization, or rendered images read back by OCR or a vision encoder. Both formats exist for human legibility, yet the consumer is a language model, and both force a decode step that costs latency and loses information. The measured penalty is large. On LongMemEval a text summary scores 0.184 where the uncompressed evidence scores 0.490, so the summarization pipeline throws away most of the usable signal. The question is whether a third representation, one not meant to be read by a person at all, carries more information per token at lower cost.

**Method.** A writer model, matched in size and tokenizer to the reader decoder, encodes a conversation or document into a short sequence of continuous vectors. Those vectors go to the frozen decoder through the same interface ordinary token embeddings use, so the decoder needs no modification and no fine-tuning, and no text is reconstructed at inference. Only an adapter between writer and reader is trained: 4.2M to 26.2M parameters, about 0.1 percent of the decoder.

**Result.** On LongMemEval, 0.504 accuracy at 7.70x compression, against 0.490 for uncompressed evidence, 0.184 for text summaries and 0.426 falling to 0.312 for OCR-based compression. On LongBench-QA, in-domain writers match or exceed raw-context reading at 4x to 8x compression, while 16x trails raw. Writing takes 43 ms per conversation, roughly an order of magnitude faster than text summarization or OCR reconstruction; reading is 5x to 9x faster than raw context or cached OCR. Transfer holds zero-shot from UltraChat to LongMemEval and from LongMemEval-derived question answering to unseen LongBench domains.

**Limitations.** The writer is reader-matched, so the memory tokens live in one decoder's embedding space and a different reader means retraining. Compression past 16x degrades. Both benchmarks are question-answering shaped, so it is unclear whether the memory tokens preserve information that no question in the training distribution asked for, which is the property that matters if the compressed record is meant to be queried later in ways not anticipated at write time. The margin over uncompressed evidence, 0.504 against 0.490, is small enough that it may be a denoising effect rather than added capability; the interesting number is the gap to the text and OCR baselines, not the gap to raw.

**How this builds on what you know:** The direct parents in your library are Time-LLM (MKICLA63) and ChatTS (VSCNJG5J, graphify `xie2025_chatts`, Community 4, Time Series and LLM Integration), plus DeepSeek-V2 (743XA29Y, llm area) as the competing approach. Where Time-LLM showed that a frozen decoder will read a non-text modality if a small trainable adapter reprograms it into the input-embedding space, LatentPress shows the same port can carry compressed text at 4x to 16x and beats the obvious text baseline by a wide margin, because what it removes is the decode step rather than a modality gap. Time-LLM and ChatTS never reported compression ratio or read and write latency, so the capacity and cost of that interface were unmeasured; this paper measures both in a setting where a strong same-modality baseline exists, which is what makes the number interpretable. Against DeepSeek-V2 the difference is where compression happens: multi-head latent attention shrinks the per-token state inside attention and keeps the token count, while LatentPress shrinks the token count at the input and leaves attention untouched, so the two compose rather than compete. No graphify cross_area_bridge from `_meta/area_index.json` covers this pair; this is a candidate new bridge between Community 4 and the LLM context-efficiency line, and Tier D below states the porting hypothesis.

**Why it matters to you.** The claim that transfers is about the interface, not the task. This paper puts a number on how much a frozen decoder's embedding port can carry and how cheaply a writer for a new source can be trained. Every Community 4 method in your library converts one window of signal into something the LLM reads; none writes a long continuous record into a fixed budget of memory tokens.

---

## Tier B — TLDR

### Random Attention: Rethinking KV Cache Eviction for Efficient Reasoning
Wang, Qiu, Zhao, Qian, Yang, Han, Ji, Savarese, Heinecke, Wang (Salesforce AI Research) · arXiv [2609.03430](https://arxiv.org/abs/2609.03430)

Every published KV cache eviction method scores each cached token by an estimate of how much it will matter later and keeps the top-scoring ones. This paper removes the score: Random Attention keeps the prompt and evicts uniformly at random inside each attention head, and across four models and six reasoning tasks it matches the strongest prior evictor while serving 32 to 43 percent higher throughput in vLLM. Two controlled experiments explain the result rather than leaving it as a curiosity. The prompt is the fragile part of the cache, and most of the measured gap between competing scorers reduces to whether their signal happened to keep it; and the reasoning trace protects itself with redundancy at two levels, in the text because the model restates what it still needs as it works, and across heads because each head keeps its own copy. Once the prompt is safe, a random draw retains enough copies of what remains needed.

**How this builds on what you know:** The parents are Attention Is All You Need (PHB9VRVM, graphify `vaswani2017_transformer`, Community 2), DeepSeek-V2 (743XA29Y), and DeepSeek-R1 (Z5IWHZAE, graphify `deepseek2025_r1`, Community 0). Where DeepSeek-V2 reduced the per-token cost of the cache with a learned low-rank latent, Random Attention reduces the token count with no learning and no scoring at all, because its measurement shows the information a cache holds about a reasoning trace is duplicated enough that which tokens survive stops mattering once the prompt is protected. The redundancy it exploits is a property of DeepSeek-R1-style RL-trained traces specifically, which is why the result was not available before long reasoning traces existed. Within your library this also sits directly against CRISP (2609.01925, digest 2026-09-04), which spent its contribution on a better routing signal for sparse prefilling; Random Attention argues that at eviction time the analogous signal is worth nothing.

### Rethinking On-Policy Distillation of Large Language Models II: One Training Example
Fu, He, Zuo, Huang, Zhang and others (Thinking Space) · arXiv [2609.04172](https://arxiv.org/abs/2609.04172) · [code](https://github.com/Thinking-Space/One-Shot-OPD)

On-policy distillation combines student-generated rollouts with dense token-level teacher supervision, and existing work studied its algorithmic behavior while leaving the role of the data unexamined. This paper pushes the data to its minimum, a single query, and finds that one-shot on-policy distillation keeps improving for hundreds of steps and recovers most of full-data gain across task domains and model families. The instrument is state coverage, the fraction of states full-data training visits that a query set's rollouts reach: one query already reaches 71.5 percent, most within the first 100 steps, and 16 semantically distinct queries reach 98.9 percent and match full-data training. Alignment slows at a similar rate either way, so the method is data-overfed and algorithm-starved. Content-light templates and off-domain WildChat queries also approach the real-query baseline, which separates task content from induced state coverage and rules out the content account.

**How this builds on what you know:** The parents are two papers from your own last week, Does On-Policy Distillation Really Distill? (2608.31046, digest 2026-09-01) and Cliff (2609.02817, digest 2026-09-04), plus DeepSeek-R1 (Z5IWHZAE, Community 0). Where 2608.31046 removed the teacher and kept the data, this paper keeps the teacher and removes the data, and both recover most of the gain, so together they say the remaining contribution sits in the student's own rollout distribution and in how slowly the student absorbs a fixed set of states, not in the teacher's per-token scores and not in dataset scale. Cliff sits on the third side of the same question, accepting the teacher and improving where the signal lands, and it is the only one of the three interventions that still produces a clear gain. The state-coverage metric is the reusable part: it is a general way to ask whether a training set adds anything beyond the states the model would have visited anyway, which applies to any small-data domain, health time series included.

### Why Gated DeltaNet Survives 4-Bit Quantization: NVFP4 W4A4 for the Recurrent Half of a Hybrid 27B LLM
Kozyrev and Maiboroda (Minima AI) · arXiv [2609.04098](https://arxiv.org/abs/2609.04098)

Hybrid LLMs pair softmax attention with linear-attention layers such as Gated DeltaNet, whose recurrent state summarizes the context in fixed size. Every community 4-bit quantization of Qwen3.8-27B left that block at 8 or 16 bit, especially its decay and write-strength gates, on the untested intuition that errors in a recurrence accumulate. The authors quantize all 496 linear layers to NVFP4 W4A4 with calibration-only post-training quantization, no quantization-aware training and no distillation, and match BF16 within seed noise, a five-task average of minus 0.52, across MMLU-Pro, GSM8K, AIME'25, GPQA-Diamond, LiveCodeBench and RULER retrieval to 64K, at 17.5 GiB and 14 to 19 percent faster prefill. The mechanism study finds the supposedly fragile gate projections are the least sensitive layers, compressing about 11 percent GEMM error to about 2 percent output error, and that the delta rule forgets an injected state impulse within hundreds of steps because each write overwrites the state along the current key direction, so the 32K perplexity gap shrinks with position instead of compounding.

**How this builds on what you know:** The parents are Audio Mamba (6VTXUZEG, graphify `erol2024_audiomamba`, Community 2), MambaOut (ZS87LF7R, mamba area) and DeepSeek-V2 (743XA29Y). Where Audio Mamba and the other state-space entries established what a fixed-size recurrent state can represent, this paper measures how much numerical precision that state actually needs, and the answer is four bits, for a structural reason rather than an empirical one: the delta rule is contractive along the write direction, so noise is overwritten rather than integrated. MambaOut removed the recurrence to ask whether it mattered; this degrades it to ask how precisely it must be computed, a finer instrument that yields a mechanism instead of a yes or no. Against DeepSeek-V2 the comparison shifts, because if the recurrent half is also the cheap half to quantize, the memory argument for latent KV compression weakens relative to hybrid designs.

---

## Tier C — scan only

| Paper | Hook |
| --- | --- |
| [Beyond Retrieval: Progressive Latent Memory Evolution for Streaming Video Understanding](https://arxiv.org/abs/2609.04131) | Evolves one latent memory across a video stream instead of retrieving past frames. |
| [Terminal-Universe](https://arxiv.org/abs/2609.04148) (Qwen) | Turns recorded agent trajectories into reproducible terminal environments for training. |
| [Let Confidence Change, Not the Prediction](https://arxiv.org/abs/2609.01072) | Post-hoc calibration repair that leaves the argmax untouched. |
| [Knowing When Not to Reuse](https://arxiv.org/abs/2608.26730) | Conditional experience transfer in autonomous post-training; when reuse hurts. |
| [Puffin-World](https://arxiv.org/abs/2609.04196) (ACE Robotics) | Unified multimodal model carrying native 3D world state rather than pixels. |
| [CORE](https://arxiv.org/abs/2609.04083) (Alibaba-NLP) | Reranker distillation to fix compositional reasoning in multimodal embeddings. |
| [PACE](https://arxiv.org/abs/2609.03293) (POSTECH) | Surfaces conflicting constraints hidden inside a single user request. |
| [The Missing Temporal Link](https://arxiv.org/abs/2609.02367) | Temporal context routing for script-driven audio-video generation. |

---

## Tier D — time-series and bio-sensing gap watch

No time-series or bio-sensing paper cleared the bar today, so nothing new was closed off. Three unported opportunities follow from the papers above.

**Soft-token context compression for wearable streams (unported).** Community 4 in your graphify prior, Time-LLM, ChatTS, Sensor2Text and TS-Agent, all convert one window of signal into something an LLM can read. None writes a long continuous record into a fixed budget of continuous memory tokens. Transfer hypothesis: train a reader-matched writer that compresses a 30-day accelerometer and heart-rate record into 100 to 500 memory tokens, then measure GLOBEM wellbeing prediction against a text-summary baseline. If LatentPress's 0.184 text-summary number has any analogue here, the text-summary stage that every current health agent pipeline runs is discarding most of the signal, and that is a measurable claim rather than a plausible one.

**The redundancy argument applied to sensor context (unported).** Random Attention shows that selection scoring contributes nothing once the prompt is preserved, because the reasoning trace is redundant in text and across heads. A 1 Hz physiological record over weeks is far more redundant than a reasoning trace. Transfer hypothesis: for a long-context health agent, uniform random subsampling of the sensor window with the subject header preserved should match learned patch selection. If it does, the patch-selection modules in current time-series and LLM pipelines are unnecessary complexity. This is cheap to run and a clean negative result either way, which makes it a good use of a week.

**4-bit recurrent models for continuous sensing (unported).** Community 5, wearable sensing and behavior, contains no quantization work. The delta-rule result above says quantization noise in a recurrent state is overwritten rather than integrated, which is exactly the property an always-on on-device sensing model needs. HARMamba (HE9X47KN) and Bi-Mamba+ (AVTJLZIR) are the two natural test beds already in your library.

---

## News

Three frontier releases in the first three days of the month, and all three shipped a gated cyber-capability tier alongside the general version. Anthropic released Claude Fable 5.1 and its restricted-access twin Mythos 5.1 on September 1, at the same $10 and $50 per million input and output tokens as Fable 5, but with cache reads cut from $1.00 to $0.25 per million, a 1M-token context and 128K maximum output. Google released Gemini 3.8 Flash on September 2 at $0.75 and $3.75 per million with a 1M-token context, plus a defenders-only Cyber variant, its third Flash-family model in six weeks. OpenAI began a limited preview of GPT-6 Astra on September 3, aimed at long-horizon multi-step workflows over browsers, spreadsheets, documents and autonomous coding.

---

End of digest. Close this tab when done.
