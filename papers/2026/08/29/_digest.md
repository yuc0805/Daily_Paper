# AI Digest — 2026-08-29

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A not done by 6 AM, stop.

Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.

Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

---

## Tier A — deep read

### TTPO: Test-Time Policy Optimization
Wang et al., Zhejiang University. arXiv:2608.27448 — https://arxiv.org/abs/2608.27448

**Problem.** Reinforcement learning and on-policy self-distillation have driven most recent gains in mathematical reasoning, and both need a ground-truth label to define the reward or the teacher. That requirement rules out test-time training, which is the setting where a model would benefit most from adapting to the distribution actually in front of it. Substituting a majority-vote pseudo-label is the obvious fix and is fragile in a specific way: when the vote is wrong, the teacher is wrong for every token of every rollout, so the update actively degrades the model.

**Method.** The paper starts from an observed asymmetry in how a wrong vote propagates. Rollouts that disagree with the pseudo-label are usually wrong regardless of whether the vote itself is correct, so the negative signal stays reliable even when the positive one does not. TTPO splits the objective along that line: agreeing rollouts go through on-policy self-distillation, and disagreeing rollouts are pushed down by grouped reinforcement learning. Token-level selection sharpens both halves, since distillation on already-converged positions contributes nothing and penalising low-confidence tokens punishes exploration rather than error. Majority-vote routing tightens on its own as the model improves.

**Result.** Without any labels, TTPO matches label-supervised on-policy self-distillation on five competition-level benchmarks. Qwen3-1.7B goes from 38.0 to 45.2 percent under test-time training. In the no-thinking setting the gains run from 25.2 to 36.4 percent, and the paper reports cross-task transfer rather than benchmark-specific adaptation.

**Limitations.** The method needs many rollouts per test problem, so it trades label cost for inference cost, and the size of that trade is not reported against a wall-clock baseline. It also needs an answer that can be voted on, which restricts it to discrete outputs. The results are on one model family at small scale; whether the asymmetry holds when the base model is strong enough that the minority is sometimes right is the open question.

**How this builds on what you know:** The parents are TTT Layers (Sun 2024) and TTT for Abstract Reasoning (Akyurek 2024), both in your test-time-training area, and DeepSeek-R1, which sits in graphify community 0 as the anchor for reasoning-via-RL. Where Akyurek built a supervision signal by augmenting the target task, TTPO builds it from the model's own rollout distribution, so nothing task-specific has to be constructed. Where DeepSeek-R1 needed a verifiable reward to define the advantage, TTPO substitutes a majority vote and then repairs the substitution's failure mode instead of trying to make the vote more accurate. Sun's TTT layers made the update mechanism internal to the model; TTPO makes the update objective self-supplied. Your library also holds Permutation Self-Consistency (Tang 2024), which already treated cross-sample agreement as a usable signal rather than a decoding trick — that is the piece TTPO promotes from inference-time heuristic to training objective.

This paper extends DeepSeek-R1, which already crossed the reasoning-via-prompting and reasoning-via-RL communities in your library through the bridge to Chain-of-Thought. The new work pushes that bridge further, into training for reasoning with no label at all, which is the direction that matters for any domain where the verifier is the expensive part.

**Why it matters to you.** The constraint TTPO works around is the constraint that limits bio-sensing: labels are scarce, costly, and often arrive long after the signal. The transferable idea is extracting a training signal from agreement across stochastic samples of the same input, with an asymmetric objective so that a wrong consensus degrades only the weaker branch. A wearable model adapting to a new subject or a new device with no annotation is the same problem shape. What would need replacing is the vote, since physiological targets are continuous rather than discrete.

---

## Tier B — TLDR

### The Impact of Temporal Context Length and Encoding Strategies on Self-Supervised ECG Representation Learning
Sameh, Al-Sharawi, Varatharajah. EMBC 2026. arXiv:2608.12695 — https://arxiv.org/abs/2608.12695

A controlled ablation on Icentia11k single-lead ECG that freezes the Transformer backbone and the training protocol and varies only two things: the input horizon at 16 seconds, 1 minute, 5 minutes and 10 minutes, and the front end, comparing continuous convolutional patch embeddings against fixed vector-quantised tokens. Evaluation is by abnormal rhythm detection and by patient-level retrieval across sessions, the second of which tests whether a representation carries individual-specific structure rather than only segment-level structure. Longer context wins, with the 5- and 10-minute models strongest, and continuous patch embeddings beat discretised tokens at every horizon tested. Code and pretrained models are released.

**How this builds on what you know:** PatchTST (Nie 2023) and Chronos (Ansari 2024) are the method parents from your time-series area, and MAE Theory (Zhang 2023) and HeAR (Baur 2024) sit in graphify community 1, the health and self-supervised cluster. Where Chronos made tokenise-then-pretrain the default so that a language-model objective could apply unchanged, this paper measures what the conversion costs on a clinical signal and finds it discards waveform detail at every horizon. Where PatchTST justified patching on efficiency and forecasting error, the justification here is cross-session stability, which is a stricter test because it requires the representation to be about the patient rather than about the segment. HeAR and most physiological encoders inherit their window from clinical reading practice; the retrieval result says the individual-specific structure lives at the minute scale, so the clinically natural unit is the wrong pretraining unit.

---

### PAWBench: How Far Are We from Probabilistically Aligned World Modeling?
Pu et al., Shanghai AI Lab and collaborators. arXiv:2608.27345 — https://arxiv.org/abs/2608.27345

The paper argues that a video generator used as a world model should reproduce the distribution of valid outcomes under a given initial observation and action, not merely one plausible trajectory, and formalises that as probabilistic alignment. PAWBench supplies 50 scenarios where a physical process can legitimately unfold in more than one way; PAWEval turns repeated rollouts into an empirical distribution over outcomes and scores two things that can fail separately, whether the probabilities match and whether the full range of valid outcomes appears at all. Across eleven current systems, none does both consistently. Follow-up experiments test whether prompting, initial noise sampling or training can reshape the predictive distribution.

**How this builds on what you know:** DDPM (Ho 2020) and DiT (Peebles 2023) sit in graphify community 3 and are the family under test; World Model Evaluation (Vafa 2024) from your world-model area made the case that predictive accuracy does not certify a coherent world model. Where Vafa located the problem in the model's internal state, which is hard to probe in a video diffusion model with no symbolic latent, PAWBench relocates the same critique to the output distribution, where sampling makes it directly measurable. This paper extends DDPM, which already crossed the deterministic-translation and distributional-generation communities in your library through the bridge from CycleGAN. The new work pushes that bridge further, into asking whether the learned distribution is the right one — a question the original move made askable but did not answer. Read it against yesterday's Tier A on forecast collapse: same diagnosis in a different modality, where per-unit calibration hides a failure only a distributional metric detects.

---

### Understanding Evolution Strategies for LLM Reasoning: Broader Reasoning Coverage than GRPO
Ba, Zheng et al. arXiv:2608.27351 — https://arxiv.org/abs/2608.27351

Evolution strategies entered LLM post-training as a way to avoid storing gradients and have been judged by how little Pass@1 they give up against GRPO. This paper argues they are a different paradigm rather than a cheaper approximation. Theoretically it shows that Jensen-Shannon diversity across the population, projected through the verifier so it counts only differences the task can see, raises Pass@K. Empirically, evolution strategies raise Pass@1 while also raising Pass@K, where GRPO shows entropy collapse. A second result finds the task gains come from a sparse subset of large-magnitude updates despite substantial whole-model drift, with no catastrophic forgetting on held-out evaluation. A sequential GRPO-then-ES schedule retains both strengths, and larger models are reported to need smaller populations.

**How this builds on what you know:** DeepSeek-R1 (graphify community 0 anchor), PPO (Schulman 2017) from your world-model area, and Latent-GRPO (Deng 2026) from reasoning are the parents. Where GRPO estimates an advantage from token-level log-probability ratios within a rollout group, which concentrates mass on whichever solution path the group currently favours, evolution strategies perturb parameters directly and never form that ratio, so the concentrating pressure has no analogue. Latent-GRPO changes where the objective acts but keeps the estimator, and therefore inherits the collapse. The functional-sparsity result removes the standing objection that gradient-free post-training must be destructive at scale.

---

## Tier C — scan only

| Paper | Hook | Link |
| --- | --- | --- |
| PILOT in the Loop (2608.26530) | Supervisor redirects a worker agent mid-run; +14.6 points and 43 percent fewer output tokens | https://arxiv.org/abs/2608.26530 |
| What Makes Good Agentic Data? An ACE Lens (2608.27260) | Asks which properties of synthetic agent trajectories actually drive downstream gains | https://arxiv.org/abs/2608.27260 |
| WikiSkill (2608.27454, Google) | Compiles agent run experience into persistent reusable skills rather than episodic memory | https://arxiv.org/abs/2608.27454 |
| Zero-WAM (2608.26103) | In-context world-action modelling learned from human video, no task-specific training | https://arxiv.org/abs/2608.26103 |
| Self-OPD (2608.26872) | On-policy distillation for flow matching with no teacher model | https://arxiv.org/abs/2608.26872 |
| TS-RAG (2608.06223) | Retrieval-augmented generation applied to time-series forecasting | https://arxiv.org/abs/2608.06223 |
| CaSKG (2608.25500) | Counterfactual-causal skill graphs for retrieving agent skills at scale | https://arxiv.org/abs/2608.25500 |
| UrbanGround (2608.27456) | Spatial agency benchmark at real city scale, local perception to global navigation | https://arxiv.org/abs/2608.27456 |

---

## Tier D — Time-series and bio-sensing gap watch

**Already ported (closed off).** Masked-autoencoder pretraining with a patch front end is now thoroughly ported into physiological signals, and 2608.12695 is the ablation that settles the remaining design questions on ECG rather than opening new ones. Anything matching the community 4 and community 5 hyperedges in your graphify seed — time-series with LLM integration, wearable sensing and behaviour — should be treated as occupied ground. Retrieval augmentation for forecasting is also now ported, with TS-RAG (2608.06223) landing this month, so the RAG-for-time-series slot is taken.

**Unported opportunity 1 — label-free test-time adaptation for wearable models.** TTPO's structure is a training signal built from agreement across stochastic samples of the same input, with an asymmetric objective so that a wrong consensus damages only the distillation branch. Nothing in that structure is specific to text. Transfer hypothesis: for a wearable classifier facing a new subject or a new device, sample augmented views of the same window, take the modal prediction as a pseudo-label, distil the agreeing views and penalise confidently disagreeing ones — the asymmetry should hold because a view that disagrees with the consensus under a label-preserving augmentation is usually wrong regardless of whether the consensus is right.

**Unported opportunity 2 — outcome-level distributional evaluation for physiological forecasting.** PAWEval converts repeated conditional rollouts into an empirical distribution over enumerable outcomes and scores probability match and coverage separately. Physiological prediction is almost always scored per-sample against a point target, which is exactly the blind spot PAWBench identifies in video and yesterday's Tier A identified in time-series foundation models. Transfer hypothesis: define enumerable clinical outcomes for a given initial physiological state — a rhythm episode occurring or not within a window, a glucose excursion, a sleep-stage transition — sample the generative model repeatedly, and report probability match and coverage as separate numbers. The evaluation cost is small and the failure it would expose is the one that matters clinically.

---

## News

No frontier model release from OpenAI, Anthropic, Google DeepMind, Meta or xAI landed on 28 or 29 August. The most recent entry on the public trackers is GLM-5.3 Flash from Z.AI on 26 August. Quiet day on the release side; nothing here changes any planning assumption.

---

End of digest. Close this tab when done.
