# AI Digest — 2026-09-01

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A not done by 6 AM, stop.

Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.

Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

---

## Tier A — deep read (~20 min)

### Does On-Policy Distillation Really Distill? From Noisy Teacher to Self-Improvement
Ding and Zhang (Purdue) · arXiv:2608.31046 · https://arxiv.org/abs/2608.31046

**Problem.** Reinforcement learning with verifiable rewards gives one scalar per trajectory, which is a thin signal for a long chain of tokens. On-policy distillation was proposed as the dense alternative: a stronger teacher scores every token the student produced, so credit assignment happens per position rather than per episode. The step nobody checked is that the teacher is scoring text the student wrote, which is off-policy for the teacher. A model asked to assign probability to text it would not have produced is being queried outside the distribution it was trained on, so the reliability of those per-token scores is an empirical question, not something the method's motivation settles.

**Method.** The analysis proceeds by subtraction. First, measure teacher noise across training and across teacher scales, which yields the counterintuitive result that larger teachers produce noisier supervision rather than cleaner supervision. Second, delete the noisy supervision and retrain: the student converges to comparable performance either way, so it is insensitive to the very thing the method exists to provide. Third, ask what is left, and find that learning concentrates on low log-probability tokens, and that a single fixed negative advantage reproduces the teacher-provided ones. The constructive step follows directly. If the operative mechanism is suppression of tail tokens, the student's own entropy locates them, so On-Policy Self-Adaptation assigns stronger negative signal at high-entropy positions, suppressing tail tokens and redistributing probability mass evenly among head tokens, with no teacher forward pass anywhere in the loop.

**Result with numbers.** Against base Qwen3-1.7B, On-Policy Self-Adaptation improves Avg@32 on AIME24 by 35.41 points, a 263 percent relative gain, and more than doubles Pass@32 on all three benchmarks tested. Against on-policy distillation itself, it gains 16.77 points in Avg@32 on AIME24. So the teacher-free method does not merely match the teacher-based one, it beats it, which is the evidence that the teacher's contribution was net negative rather than merely redundant. The authors report the effect across model families and tasks.

**Limitations.** The headline numbers come from mathematics benchmarks, where the space of correct continuations is narrow and a low-probability token is usually a wrong token. Entropy is a plausible proxy for token quality in that setting and much less obviously so in open-ended generation, where the tail may hold legitimate alternatives rather than errors. The paper also demonstrates that a constant negative advantage matches a teacher's advantages, which is a strong claim about the teacher but a weak claim about the ceiling: it shows the teacher was not helping, not that no form of external supervision could. And the base model is 1.7B, so whether a larger student would extract more from a teacher is untested.

**Why it matters to Leo.** This is a negative control that most distillation papers do not run, and the experimental design is portable regardless of what one thinks of the specific method. The test is: replace the teacher's signal with a constant, or with a statistic the student computes itself, and see whether the result survives. That applies directly to knowledge distillation in bio-sensing, where large physiological foundation models are routinely distilled into small on-device students and the assumed value of the teacher is almost never isolated. The entropy-adaptive advantage is itself a candidate transfer, since a wearable model's predictive entropy over signal patches is available without any teacher forward pass, which is what matters when the deployment constraint is compute on the device.

**How this builds on what you know:** The strongest parents in your library are DeepSeek-R1 (Z5IWHZAE, graphify community 0, LLM Agents and Reasoning) and Chain-of-Thought Prompting (HBLPTRMY, the anchor node for reasoning with 7 edges), with DeepSeek-V3 (2JCKA7GI) as the large-teacher regime the noise measurement spans. Where DeepSeek-R1 accepted a sparse outcome reward as the price of not needing a teacher, and where on-policy distillation accepted a teacher as the price of a dense signal, this paper shows the second trade was never necessary, because the informative content of the dense signal is a policy-internal quantity the student already has. This paper also extends DeepSeek-R1, which the graphify prior lists as a cross-area bridge to Chain-of-Thought — reasoning-via-reinforcement-learning against reasoning-via-prompting. The new work pushes that bridge further in the reinforcement-learning direction by removing the last external component from the loop, so the two communities now meet at the question of where the supervision lives rather than how it is elicited.

---

## Tier B — TLDR (~10 min total)

### P2E-VQ: ECG-linked representation augmentation for PPG via discrete patch retrieval
Wu, Gao, Zhao, Zhou, Lip, Zheng and colleagues (Liverpool) · arXiv:2608.14656 · https://arxiv.org/abs/2608.14656

PPG is what consumer wearables actually collect, but it measures peripheral pulse rather than cardiac electrical activity, so the morphological cues cardiac prediction depends on are simply absent. The standard fix is to reconstruct an ECG waveform from the PPG, which is ill-posed, and the paper makes the sharper point that waveform fidelity does not track downstream accuracy anyway. P2E-VQ drops reconstruction entirely: PPG patches are quantised into discrete tokens, and each token indexes a memory bank of ECG-linked representations built only from training data, so inference consumes PPG alone. Across five public datasets and six downstream tasks covering clinical endpoints and affective state, it beats pretrained baselines under a single frozen-feature linear-probing protocol.

**How this builds on what you know:** Sensor2Text (ELYUE3NF, graphify community 4, Time Series plus LLM Integration, 7 edges) and Foundation Models for Biosignals (2XWEG7AF, the anchor node for llm-health, 6 edges) are the direct parents, with SSL for HAR on 700K person-days (RTMH75VW, community 1) as the single-modality pretraining baseline. Where Sensor2Text maps a sensor stream into a richer modality and treats the generated output as the deliverable, this paper keeps the cross-modal supervision but discards the generated target, because the mapping is ill-posed and generation quality is not what the downstream task reads. Where Yuan 2024 improves the encoder by pretraining on more unlabelled signal, this paper leaves the input distribution alone and spends a paired ECG corpus as a retrieval index instead, which is a different use of the same data. This paper extends Sensor2Text, which the graphify prior already lists as a cross-area bridge to LLMs are Few-Shot Health Learners (JX3X3KH5), crossing Time Series plus LLM Integration and Health AI. The new work pushes that bridge further toward representation-level cross-modal transfer and away from language as the intermediate.

### On the Design of Qwen3.8-Next Architecture: Evaluation, Efficiency, and Training Stability
Qiu, Wang, Li, Men, Mao and colleagues (Qwen) · arXiv:2608.30320 · https://arxiv.org/abs/2608.30320

An architecture report for a 125B sparse mixture-of-experts model with 6B activated per token, plus 51B parameters of n-gram embedding tables kept in host memory rather than on the accelerator. Token mixing alternates Gated DeltaNet with global attention at one full-attention layer in four, and those attention layers are swapped at continued-pretraining time for a block-sparse variant scored through a compressed indexer. It leads the 397B-A17B predecessor on eight of fourteen pre-training benchmarks and trails on the rest by at most 2.6 points, at one third the activated parameters and roughly one ninth the training FLOPs. The finding worth carrying away is separate from the model: enlarging the n-gram vocabulary lowers loss monotonically while downstream accuracy saturates, which is direct evidence against selecting architecture variants on validation loss.

**How this builds on what you know:** Attention Is All You Need (PHB9VRVM, the anchor node for llm with 12 edges, graphify community 2) is the full-attention layer kept at one in four, and Mamba (XNI34DQX) with Mamba-2 (JPKDWV2Q) are the state-space line whose linear recurrence Gated DeltaNet extends. Where Mamba argued a selective recurrence could replace attention outright, this report answers the follow-up question the parents left open by fixing the hybrid ratio empirically and reporting what it costs separately in training, prefill and decode, because an aggregate FLOP count hides where the cost lands. It also reports something the parents did not evaluate: the architecture moves the optimal learning rate and batch size, so comparisons that hold hyperparameters fixed across architectures are not measuring the architecture.

### CAST: Critique-Aware Supervision for Training Reliable Long-Horizon Tool-Calling Agents
Saeidi, Zhang, Singh, Gupta, Baral and colleagues · arXiv:2608.30147 · https://arxiv.org/abs/2608.30147

In a stateful environment some actions cannot be undone, so the quantity that matters is reliability across repeated trials rather than average success on one run. CAST works backwards from completed trajectories to synthesise structured rationales explaining why each action was valid or invalid under partial observability, trains a critique model on those rationales, and uses the critique to generate training data for the policy. Fine-tuning Qwen3-family models, it exceeds GPT-OSS-120B by more than 10 percent pass^4 on Retail tasks and gains a further 9 percent on Telehealth held out of domain. The evaluation choice is worth separating from the method: pass^k credits a system only when it succeeds on all k independent trials, which is the right measure whenever one bad action is unrecoverable.

**How this builds on what you know:** ToolkenGPT (6RDHVVA2), LATS (77ERE7HA) and the Memory Mechanisms survey (BDY3HUCV) are all in graphify community 0. Where LATS catches a bad action by expanding alternatives and scoring them at inference, paying search compute on every run and leaving the base policy untouched, CAST moves that judgement into training so the deployed agent needs no search and the gain survives a domain change. Where ToolkenGPT made the tool call a token the model emits, this work supplies the per-action credit signal that setup lacked, given that the only ground truth is whether the whole episode succeeded. This paper extends ToolkenGPT, which the graphify prior lists as a cross-area bridge to PyVision, already crossing tool-using agents and agentic vision in your library. The new work pushes that bridge toward training-time reliability rather than inference-time scaffolding.

---

## Tier C — scan (~5 min)

| Paper | Hook | Link |
| --- | --- | --- |
| GenFirst (2608.29335, ByteDance Seed) | End-to-end latent generative training without collapse; gFID 0.97 on ImageNet-256 | https://arxiv.org/abs/2608.29335 |
| DreamX-Creator (2608.31106) | Native joint audio-video generation at 2K resolution | https://arxiv.org/abs/2608.31106 |
| Scaling Large Reasoning Models beyond Human Supervision (2608.31075) | Five-level ladder for where human control leaves the reward and experience loop | https://arxiv.org/abs/2608.31075 |
| Normalized Low-Rank Adaptation (2608.31036) | Normalisation applied inside the LoRA update rather than around it | https://arxiv.org/abs/2608.31036 |
| SHAPE of Chain-of-Thought in Math Reasoning (2608.28600, SNU) | Asks what structural shape a reasoning chain needs, not just its length | https://arxiv.org/abs/2608.28600 |
| Matrix-Game 3.5 (2608.29910) | Real-time streaming interactive world model with patch-level memory | https://arxiv.org/abs/2608.29910 |
| Verification-Aware Training for Speculative Decoding (2608.30135, NAVER) | Trains the draft model for the verifier rather than for its own likelihood | https://arxiv.org/abs/2608.30135 |
| PaperGym (2608.31119) | Rubric-centred evolution for research-plan generation | https://arxiv.org/abs/2608.31119 |

---

## Tier D — Time-series / bio-sensing gap watch

**Already ported (closed off).** P2E-VQ closes discrete tokenisation plus retrieval augmentation for physiological signal. That pairing has been standard in language modelling for several years and it is now demonstrated on PPG with an ECG-keyed memory bank, matching the hyperedges of graphify community 4 (Time Series plus LLM Integration) and community 5 (Wearable Sensing and Behavior). If retrieval-augmented bio-signal representation was on your list of open transfers, it is no longer open in the PPG-to-ECG direction. What remains reusable is the argument rather than the architecture: when a cross-modal mapping is ill-posed, retrieve the paired representation instead of generating the paired signal, which applies equally to IMU-to-video and PPG-to-blood-pressure.

**Unported opportunity 1 — generation-before-reconstruction curricula for biosignal autoencoders.** GenFirst (2608.29335) shows that in end-to-end latent generative training, reconstruction is fast and strongly supervised while generation is slow and weakly supervised, and that letting the generative objective shape the latent space first under weak reconstruction pressure avoids latent collapse. Nothing in community 1 or community 5 does this: biosignal masked autoencoders and VQ tokenizers are trained reconstruction-first by default, which is exactly the ordering GenFirst argues produces generation-hostile latents. Transfer hypothesis: for a PPG or ECG tokenizer, schedule the reconstruction weight to ramp up rather than holding it fixed, and the resulting codebook should be more useful for downstream probing than a reconstruction-optimised one, which is testable directly against the P2E-VQ protocol.

**Unported opportunity 2 — entropy-adaptive negative advantages for on-device biosignal distillation.** The Tier A paper shows that in on-policy distillation the teacher's contribution is replaceable by the student's own entropy. Physiological foundation models are routinely distilled to small wearable-deployable students, and none of the work in community 1 tests whether the teacher is carrying information or whether a self-computed uncertainty signal would do as well. Transfer hypothesis: distil a biosignal foundation model into an on-device student twice, once with teacher logits and once with a fixed negative advantage weighted by the student's own predictive entropy over signal patches, and if the second matches the first, the teacher forward pass can be dropped from the training pipeline entirely.

---

## News

The US Department of Defense opened GenAI.mil, a secure portal bundling OpenAI's ChatGPT Mil, xAI and Starshield's Grok for Government, and Google Gemini for roughly 3 million Department of Defense personnel, with 1.7 million unique users reported onboarded. The notable part is the multi-vendor structure rather than any single model, since it makes the three providers directly comparable inside one procurement.

Otherwise quiet on releases. The Qwen3.8-Next architecture report covered in Tier B is the substantive model disclosure of the day, and it is a technical report rather than a launch.

---

## Note on today's selection

Time-series and bio-sensing were thin on the daily feeds. The Tier B entry in your primary area, P2E-VQ, was posted on 31 July and surfaced now rather than appearing today; it is included because it is the strongest recent result in the primary area and because it closes a transfer that was worth tracking. Everything else is from the 31 August to 1 September batch.

End of digest. Close this tab when done.
