# AI Digest — 2026-09-07

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A not done by 6 AM, stop.

Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.

Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

---

## Tier A — deep read

### When Quantization Breaks Memory: Recurrent-State Write-Back in Low-Precision Temporal Inference
Erbas, Intes, Pandey · [arXiv:2609.04490](https://arxiv.org/abs/2609.04490)

**Problem.** In a recurrent network the hidden state is written to memory at each step and read back at the next one, so the rule used to store that state is not an implementation detail but part of the computation. Quantization accounting is well developed for weights and activations, where each rounding error perturbs one computation independently. A recurrence breaks that independence, and no prior work isolates the storage rule from the arithmetic.

**Method.** The authors name the rule the recurrent-state write-back and study it in a compact GRU encoder-decoder that estimates two fluorescence lifetime parameters from high-noise time-resolved optical signals, a molecular imaging task with real deployment pressure. The trained model is held completely fixed and only the state-storage rule is varied, which isolates the interface. Three post-training interventions carry information from suppressed updates forward: error feedback accumulates the leftover rounding residual into the next write, residual memory keeps a small continuous correction alongside the quantized state, and direction memory tracks the sign of repeated sub-threshold updates.

**Result with numbers.** Replacing continuous state propagation with deterministic 4-bit state storage raises estimation error on the short-lived component by roughly 70x and on the long-lived component by roughly 300x, with no other change to the model. The mechanism is that repeated small updates each fall below the write threshold, so the stored state stays nearly frozen while the network continues to propose change and computes on stale memory. All three interventions recover most of the lost accuracy with zero retraining. A precision sweep shows that increasing state precision can worsen a fixed recurrent solution, because a model trained against a coarse interface adapted to it, so bit-width alone is the wrong variable and compatibility between the learned dynamics and the storage rule is the right one. The same failure and rescue reproduce in an independently trained LSTM, where the cell state is more sensitive than the hidden state.

**Limitations.** The primary evidence is one task in one modality with a compact model, so the magnitude of the effect is not transferable as a number, only the mechanism is. The LSTM replication is a second architecture but still a small one, and there is no result on a large state-space model where the state is high-dimensional and the update is selective rather than uniformly gated. The three interventions are compared against each other and against the broken baseline, not against quantization-aware training, which would be the obvious strong alternative if retraining is affordable.

**Why it matters to Leo.** Every wearable and bio-sensing pipeline in the library that reaches for a recurrent or state-space encoder does so on an efficiency argument, and this paper shows that argument has an unpriced term. The check is cheap to run: freeze a trained HARMamba or Bi-Mamba+ checkpoint, quantize only the state write, and see whether activity or physiological accuracy collapses the same way. If it does, all three fixes transfer directly, because none requires retraining.

**How this builds on what you know:** The direct parents are HARMamba (Li 2024), which sits in graphify Community 2 and established the fixed-size recurrent state as the deployment-friendly encoder for wearable streams, and Mamba (Gu and Dao 2023) in the mamba area, whose efficiency claim rests entirely on the state being small. Where HARMamba and Mamba argued that a compact recurrent state is what makes long sensor sequences affordable at the edge, this paper measures what happens when that state is actually stored at edge precision, and finds a coupling across time that per-computation quantization analysis cannot see. A third parent, Foundation Models for Biosignals (Gu 2025, Community 1), names constrained-hardware deployment as the open problem for biosignal models but supplies no mechanism; this work supplies one. Read it against the Gated DeltaNet 4-bit result already in the library from 2026-09-05, which found a recurrence that tolerates coarse state storage because its delta rule overwrites the state along each new key direction. The pair suggests the governing property is whether the update rule forgets injected state noise or accumulates it, which is a sharper question than bit-width.

---

## Tier B — TLDR

### Iris: Climbing to the Search Frontier
AllSpark Research · [arXiv:2609.04304](https://arxiv.org/abs/2609.04304)

Two search agents at 35B-A3B and 397B-A17B, released with the full data and training recipe. Training questions are reverse-constructed from the hyperlink structure of a web corpus, with every non-answer entity rewritten as a descriptive reference so no clue resolves by string matching, and only questions a reference model fails closed-book yet solves with the evidence supplied are kept. Supervised fine-tuning and RL against live search alternate, with the hardest solved and most efficient rollouts of each RL round returned to the next supervised pass. With inference-time context management the two models reach 82.2/84.8/86.9/52.3 and 88.6/85.1/92.9/56.4 on BrowseComp, BrowseComp-ZH, DeepSearchQA and HLE, from a single ReAct agent with no sub-agents and no test-time verification. The part worth keeping is the ablation: every benchmark is reported with and without context management, and the gap it produces is larger than most reported differences between competing systems, which is a reason to distrust single-number agent comparisons.

**How this builds on what you know:** The parents are DeepEyesV2 (Hong 2026) and LATS (Zhou 2024), both graphify Community 0, plus DeepSeek-R1 (2025) in the same community. Where LATS bought search-agent capability at inference time by expanding a tree over candidate trajectories, Iris moves that expenditure into the weights and then runs a single flat ReAct pass, because expensive exploration can be paid for once during training but not once per user query. Against DeepSeek-R1 the difference is the environment: R1 optimises against a verifier on a fixed answer set, while Iris optimises against live search, which is nonstationary and forces the systems work the paper spends most of its length on. This also touches the recorded cross-area bridge between ADaPT and LATS, the planning-decomposition agent pair in the library, and it pushes against both: Iris reaches these numbers with no decomposition and no sub-agents at all.

### RISE: Recursive Improvement via Self-Extrapolating Policy Distillation
Li, Yavuz, Joty (Salesforce AI Research) · [arXiv:2609.05295](https://arxiv.org/abs/2609.05295)

On-policy distillation gives dense per-token supervision, which outcome-reward RL lacks, but its ceiling is the teacher: an external teacher brings a distribution mismatch, and self-distillation with privileged conditioning is capped by in-context capacity. RISE builds the teacher from the model's own RL trajectory, taking the displacement between the current checkpoint and a trailing anchor, in parameter space or logit space, and extrapolating along it. That converts a sparse outcome-induced parameter update into dense token-level targets with no external model. The teacher is refreshed every iteration as the student improves, so distillation becomes a recursive loop rather than one-shot compression, and the method beats RLVR-only training and on-policy self-distillation across math, multi-domain STEM, code and multi-turn agentic tasks.

**How this builds on what you know:** This paper extends the DeepSeek-R1 to Chain-of-Thought bridge already recorded in your area index, which pairs reasoning-via-RL against reasoning-via-prompting. Where DeepSeek-R1 turned a sparse outcome reward into a parameter update and stopped, RISE reads that update as a direction and steps further along it, because the displacement between two checkpoints already encodes what the reward was pushing toward at every token. The new work pushes the bridge toward treating optimizer trajectories, rather than models, as the source of supervision. It also lands directly on the on-policy distillation analysis you read on 2026-09-05, which concluded that method is algorithm-starved rather than data-starved; the two agree on the diagnosis and RISE supplies the intervention that diagnosis implies.

### Motion-Omni: End-to-End Joint Speech and Full-Body Motion for Spoken Dialogue
Ma, Tao, Zhang, Guo (Peking University) · [arXiv:2609.04250](https://arxiv.org/abs/2609.04250)

A conversational avatar has to decide what to say and how to move while saying it, but the standard system is a cascade that generates speech and then runs a motion model over the finished audio, costing a second inference pass and preventing joint optimisation. Motion-Omni emits facial expression, hand, upper-body and lower-body motion from the same hidden states that produce the speech. Supervision comes from a model-agnostic pipeline that pseudo-labels consistent-voice speech responses with a replaceable motion teacher, giving 422,856 quality-ranked pairs across 1,402 hours. On a Qwen2.5-7B-Instruct backbone the model stays within 2 percent of the same-audio teacher cascade on reference-free motion metrics while responding 5.4x faster at RTF 0.78, and reaches 2.62 percent word error rate. The result to take is the ablation, not the system: with the speech pathway frozen, motion stays misaligned with the audio, and only co-adapting all three components recovers alignment.

**How this builds on what you know:** This paper extends Sensor2Text (Chen 2024), which already crossed Community 4 and Community 5 in your library by joining wearable sensing to language, and the new work pushes that bridge into the generative direction: Sensor2Text reads body motion and writes language, while Motion-Omni writes body motion and language together from one hidden state. Motion Mamba, in your mamba area, models motion as an independent generative sequence and is therefore a strong motion model and an awkward dialogue component, because it has no access to the linguistic plan; Motion-Omni gives up the specialised architecture for a shared latent and reports that this costs under 2 percent on motion metrics. The frozen-backbone negative result is the transferable part, since most multimodal work on physiological signals attaches a head to a frozen language model and reports success, and this is a clean case where that recipe fails specifically on temporal alignment.

---

## Tier C — scan

| Paper | Hook |
|---|---|
| [MaxKernel: Agentic Kernel Generation for TPUs](https://arxiv.org/abs/2609.04523) (Google) | Agent writes and tunes TPU kernels directly; compiler work moving into the policy. |
| [Don't Drop Dropout: Optimizing Layer Sparsity](https://arxiv.org/abs/2609.05275) (Cerebras) | Layer dropout saves up to 25 percent training FLOPs and enables 1.5x inference speedup. |
| [tau^tau-Bench: End-To-End Realistic Agent Construction](https://arxiv.org/abs/2609.04611) (Sierra) | Environment for building agents, not only scoring them; benchmark design shifting upstream. |
| [Enoki: Efficient Multi-Level Hallucination Detection](https://arxiv.org/abs/2609.00581) | Detects hallucination at several granularities in one pass rather than per claim. |
| [WorldSculpt: Compositional Worlds from Grounded Videos](https://arxiv.org/abs/2609.05416) | Builds editable 3D worlds from video, with parts addressable separately. |
| [Ask Before You Optimize](https://arxiv.org/abs/2609.05258) | Model asks clarifying questions before formulating the optimisation problem. |
| [Group Adaptive Clipping Policy Optimization](https://arxiv.org/abs/2609.00444) (Amazon) | Per-group adaptive clipping in policy optimisation; small change to the RL recipe. |
| [ShallowStream: Index Shallow then Answer Deep](https://arxiv.org/abs/2609.02780) | Cheap shallow index over a video stream, deep computation only where the query lands. |

---

## Tier D — Time-series / bio-sensing gap watch

Only one paper today lands squarely in the temporal-signal space, and it is the Tier A result, so this section is mostly forward-looking.

**Already ported (closed off).** Error-feedback quantization, imported from the gradient-compression and optimizer literature into recurrent state storage, by arXiv:2609.04490. This is now done for GRU and LSTM on a bio-imaging inverse problem. What remains open is the same test on a selective state-space model, since Community 2 in your graph contains HARMamba, Audio Mamba and Swin-UMamba and none of them has been measured at the state-storage interface. That is a narrow, cheap, publishable gap rather than a closed one.

**Unported opportunity 1 — layer dropout and self-speculative decoding for wearable encoders.** The Cerebras result (arXiv:2609.05275) shows layer dropout during pretraining buys lower loss at equal FLOPs and then unlocks early exit and self-speculative decoding for up to 1.5x inference speedup. Nothing in Community 4 or Community 5 of your library uses stochastic depth, and continuous physiological monitoring is the setting where early exit should pay most, because the great majority of windows are unremarkable and only a small fraction need the full depth. Transfer hypothesis: a wearable encoder trained with layer dropout can exit early on low-information windows and spend full depth only on candidate events, cutting on-device energy without a separate gating model.

**Unported opportunity 2 — checkpoint extrapolation as dense supervision for sparse-outcome physiological tasks.** RISE (arXiv:2609.05295) manufactures per-token targets from the displacement between two checkpoints of an RL run. Most clinical and behavioural labels are episode-level, not per-timestep, which is the same density gap RISE closes for reasoning traces. Transfer hypothesis: for a task where only an episode outcome is known, such as sleep-stage quality or an exacerbation event, extrapolating the training trajectory could supply per-timestep targets without any additional annotation. The failure to watch for is that extrapolation amplifies whatever systematic bias the trajectory carries, and physiological training sets are more biased than math benchmarks.

---

## News

The first week of September was unusually dense on frontier releases. Anthropic shipped Claude Fable 5.1 and Mythos 5.1 on 1 September at unchanged list pricing, with three breaking API changes worth checking if you have jobs pinned to the old interface. Google released Gemini 3.8 Flash on 2 September at the same introductory price as 3.7 Flash but with an end date now printed for that price, alongside a gated Cyber variant, and Meta released Muse Spark 1.3 the same evening. OpenAI released GPT-6 Astra on 3 September as `gpt-6-astra`, with a 1.05M context window, 128K output, and standard pricing of 10 dollars input and 50 dollars output per million tokens. The structural signal across all four is that pricing has become a quarterly moving target with scheduled changes rather than a stable number, which matters for any budgeting on a grant timeline.

---

End of digest. Close this tab when done.
