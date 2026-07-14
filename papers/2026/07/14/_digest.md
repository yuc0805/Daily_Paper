# AI Digest — 2026-07-14

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A is not done by 6 AM, stop.
Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.
Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

Signal today is on the strong side for architecture and agents. Nothing new landed in time series or bio-sensing, so the Gap Watch runs in fallback mode: it reads two of today's method papers for transfer opportunities into your area.

---

## Tier A — deep read

### Hierarchical Sparse Attention Done Right: Toward Infinite Context Modeling (HiLS-Attention)
arXiv:2607.02980 — Tencent Hunyuan — https://arxiv.org/abs/2607.02980

**Problem.** Dense attention costs grow with the square of the sequence length, and models trained at one context length lose accuracy when the input gets longer than what they saw in training. Chunk-wise sparse attention (split the past into chunks, attend to a few) is cheaper, but every prior version selects the wrong chunks often enough that it stays below full attention in quality. The open question is how to pick the right chunks in a way the model can learn directly from the language-modeling loss, rather than through a separate heuristic.

**Method.** HiLS-Attention makes chunk selection part of the forward pass. Each query attends to each retrieved chunk on its own to pull out chunk-specific information, and the per-chunk outputs are then combined using retrieval scores that sit inside the same attention computation. Because the retrieval scores enter the forward pass, they receive gradients from the language-modeling loss, so the model learns which chunks to read end to end instead of using a fixed rule. The design also gives sparse key-value access, so both memory and compute stay low at long context.

**Result.** At in-domain context lengths, HiLS-Attention matches full attention and in some settings beats it. It extrapolates to more than 64 times the training context length while keeping 90% retrieval accuracy, well past where full attention breaks down. An existing full-attention model can be converted to HiLS-Attention with light continued pretraining (the related HiLS-Attention-7B release reports roughly 50B continued-training tokens), keeping in-domain quality while gaining the long-context reach.

**Limitations.** The reported gains are on language-modeling and general long-context tasks; the paper does not show results on non-text sequences such as physiological signals. The 90% retrieval accuracy figure means one in ten target chunks is still missed at extreme length, which matters for tasks where a single distant event carries the label. Continued-pretraining cost, while called lightweight, is still tens of billions of tokens.

**Why it matters to you.** Long biosignal recordings (multi-day PPG, ECG, actigraphy) are the exact setting where dense attention runs out of budget. A learned chunk-selection mechanism that reaches 64 times the training length with sparse key-value access is a direct candidate for models that must reason over days of wearable data without re-reading everything.

How this builds on what you know: Where Attention Is All You Need [PHB9VRVM] (Transformer, Community 2) made every token attend to every other token at quadratic cost, HiLS-Attention keeps the same attention machinery but learns to route each query to a small set of chunks, because the quadratic cost is what blocks long context. The nearest neighbor in your time-series library is iTransformer [QBX2TI2X], which re-purposed attention across variables rather than across time; HiLS instead attacks the time axis directly, which is the axis that grows without bound in wearable data. No direct time-series parent uses learned sparse long-context attention yet, so this is upstream of your area rather than inside it.

---

## Tier B — TLDRs

### TurnOPD: Making On-Policy Distillation Turn-Aware for Efficient Long-Horizon Agent Training
arXiv:2607.05804 — Tencent Hunyuan — https://arxiv.org/abs/2607.05804

On-policy distillation trains a student agent by matching a stronger teacher on the student's own trajectories. The paper identifies two wastes in the plain version for long-horizon agents: full-length rollouts spend wall-clock time on late turns that give weak, noisy supervision, and a trajectory-level objective piles most of the loss onto early, shallow tokens so deep decision turns stay under-trained. TurnOPD adds two controllers: adaptive rollout-depth budgeting, which uses probe statistics to decide how many turns to collect, and progressive turn-normalized loss budgeting, which shifts the loss weighting from token-level to turn-balanced over training. On ALFWorld, WebShop, and Multi-Hop Search it reaches higher validation accuracy for the same wall-clock training budget.

How this builds on what you know: Where DeepSeek-R1 [Z5IWHZAE] (Community 0) used reinforcement learning to shape a single reasoning trace, TurnOPD works one level up, at the multi-turn agent trajectory, and asks where in that trajectory the supervision should be spent. Where ADaPT [J8DYBKW2] decomposed a long task into sub-tasks as needed, TurnOPD keeps the task fixed but budgets training effort across its turns, because the bottleneck it targets is training efficiency rather than task decomposition.

### Vision as Unified Multimodal Generation (SenseNova-Vision)
arXiv:2607.06560 — SenseNova — https://arxiv.org/abs/2607.06560

The paper treats every computer-vision task as text-and-image generation inside one multimodal model, with no task-specific heads. Natural-language instructions plus optional visual prompts specify the task, the target region, and the output convention; the model then emits text for symbolic answers, images for dense predictions, or a mix for compositional tasks. The authors convert many vision datasets into instruction-response pairs (the SenseNova-Vision Corpus) and continue training an off-the-shelf unified model on it. One model covers detection, OCR, keypoints, segmentation, depth, surface normals, point maps, and camera pose, and matches task-specialized systems across these groups.

How this builds on what you know: Where DETR [QTFCR4G9] (Community 2) removed hand-built detection components by casting detection as set prediction, SenseNova-Vision removes task-specific heads for the whole vision stack by casting each task as generation. Where DiT [YJ9TK993] (Community 3) showed a transformer could drive high-quality image generation, this paper reuses that generation space as the output channel for dense visual predictions, because a shared generation space is what lets one model span symbolic and spatial tasks.

### Light-Omni: Reflex over Reasoning in Agentic Video Understanding with Long-Term Memory
arXiv:2607.05511 — Nanjing University — https://arxiv.org/abs/2607.05511

Agentic video models keep long-term memory and answer questions over long streams, but they usually lean on "detective-style" iterative reasoning (search, then aggregate evidence), which is slow and expensive. Light-Omni argues that heavy reasoning is mostly compensating for missing global context and poor retrieval. It keeps two states built in a single forward pass: a global state, a fixed-size multimodal script consolidated from episodic memory by hierarchical merging (recent detail kept, old events summarized), and a parametric latent state, conditioned on the global context, that drives actions and produces retrieval embeddings. This gives aligned retrieval and reflexive answers without iterative reasoning. Against M3-Agent it reports a 2.4% average accuracy gain, a 12.1x speedup, and 2.6x better GPU memory use, with near-constant ~2.3s latency regardless of video length, and it also works as a plug-in memory system for existing multimodal LLMs.

How this builds on what you know: Where the Memory Mechanisms Survey [BDY3HUCV] (Community 0) mapped how foundation agents store and recall past information, Light-Omni commits to one concrete design (a consolidated global script plus a latent action state) and shows it removes the need for iterative search. Where the Video Action Survey [RYGRHCG3] (Community 9) catalogued methods that label short clips, Light-Omni handles hour-scale streams by summarizing them into a bounded state, because fixed-size memory is what keeps latency flat as the video grows.

---

## Tier D — Time-series / Bio-sensing Gap Watch

No time-series or bio-sensing paper qualified today, so this runs in fallback mode: two unported opportunities drawn from today's method papers.

**Unported opportunity — learned sparse long-context attention for multi-day biosignals.** HiLS-Attention (Tier A) learns which chunks of the past to attend to, reaches 64 times its training length, and uses sparse key-value access. Communities 4 (Time Series + LLM Integration) and 5 (Wearable Sensing & Behavior) in your library have no method that learns sparse chunk selection over the time axis. Transfer hypothesis: replace dense temporal attention in a wearable foundation model with HiLS-style landmark chunks so it can attend over days of PPG or ECG at bounded memory, with the chunk selector trained by the downstream loss.

**Unported opportunity — dual-state memory for continuous physiological streams.** Light-Omni (Tier B) keeps a consolidated global "script" plus a latent action state and answers reflexively without re-scanning history. No wearable-sensing entry in your library maintains a bounded, continuously consolidated health state. Transfer hypothesis: a wearable agent holds a global state summarizing a patient's recent physiology, updated by hierarchical merging from episodic sensor windows, so it can answer or alert in near-constant time regardless of how long it has been recording.

---

## News

OpenAI opened its GPT-5.6 family (Sol as flagship, Terra mid-range, Luna fast and cheap) to general availability on July 9.

Google released Gemma 4 as an open-weight model on Hugging Face, with a technical report (arXiv:2607.02770) accompanying the launch.

Meta shipped Muse Spark 1.1 on July 9, its most capable coding and agentic model, and began charging developers through a new Meta Model API — the first time Meta has charged for its own model.

---

## Tier C — scan headlines

- Gemma 4 Technical Report — open-weight family with the July 2026 release. https://arxiv.org/abs/2607.02770
- Nemotron-Labs-Diffusion — one language model that switches between autoregressive, diffusion, and self-speculation decoding. https://arxiv.org/abs/2607.05722
- DSpark — confidence-scheduled speculative decoding with semi-autoregressive generation, from DeepSeek. https://arxiv.org/abs/2607.05147
- SkillOpt-Lite — agent self-evolution with a one-line change to the training loop. https://arxiv.org/abs/2607.03451
- TREK: Distill to Explore, Reinforce to Refine — two-stage recipe pairing distillation and reinforcement learning. https://arxiv.org/abs/2607.05339
- AlayaWorld — long-horizon, playable video world generation. https://arxiv.org/abs/2607.06291
- Forged Reasoning Attacks on LLM Agent Memory (FARMA) — poisons an agent's stored memories, plus defenses. https://arxiv.org/abs/2607.05029
- Layer-wise Cross-Lingual Depression Detection from Speech — contrastive alignment across languages for a health-sensing task. https://arxiv.org/abs/2607.02920

---

Quiet in your home area — no time-series or bio-sensing paper qualified for Tier A or B today. If you want a backlog read instead, the June 21 Tier A on causal semantic alignment for LLM-based time-series forecasting (CVAformer, 2606.08262) is the closest recent match to your work.

End of digest. Close this tab when done.
