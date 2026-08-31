# AI Digest — 2026-08-31

## Reading discipline

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A not done by 6 AM, stop.

Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.

Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

---

## Tier A — deep read

### Fast Weight Attention for Continual Learning
Zhang, Ta, Yuan, Wang, Gu, Yao et al. — arXiv:2608.27763 — https://arxiv.org/abs/2608.27763

**Problem.** Every architecture that compresses a growing context into a fixed-size recurrent state has to decide what to keep and what to discard, and in current designs that decision lives inside a learned gate whose objective is never written down. Temporal alignment, plasticity, forgetting and bounded rehearsal are entangled in one mechanism, so a failure in one cannot be separated from the others. The paper's specific claim is that the same-step association used by most linear-attention and state-space models, while causal, optimises a different internal objective than the prefix-prediction loss the model is actually trained under.

**Method.** Under read-after-write autoregressive semantics the correctly aligned example revealed at step t is the prefix-aligned pair (phi(k_{t-1}), v_t), not the same-step pair (phi(k_t), v_t). Taking that as the target and applying a first-order update gives normalised rules: Falcon-1 is a scalar normalised least-mean-squares update, Falcon-2 its per-column extension, Falcon-3 a sliding-window mini-batch update, with Falcon-1A/2A/3A as inner-product variants. Normalisation sets an effective step size from the current key magnitude rather than from a learned decay constant, which is the role step-size control plays in adaptive filtering. Recurrent, masked-parallel and chunk-parallel forms are supplied with positive-decay renormalisation, so training cost matches existing linear-attention implementations.

**Result.** Representative variants remain competitive on language modelling and improve length extrapolation on variable-digit addition, a task chosen because train and test lengths separate cleanly. Note the gap: the abstract reports no headline numbers, only the competitive claim and the extrapolation direction. That is the main risk in today's Tier A pick.

**Limitations.** No reported scale beyond the language modelling and addition settings, and no evidence that the alignment fix survives contact with a large pretraining run. Variable-digit addition is a clean but narrow probe for length generalisation. Because the paper is a derivation-first contribution, the ablation that matters — separating the prefix-alignment change from the normalisation change — is the thing to look for early, since the two are independent and the paper's argument only needs the first.

**Why it matters to Leo.** Leo's library carries fourteen Mamba-family papers and nearly all of them apply an existing state-space block to a new modality: HARMamba to wearable accelerometry, Audio Mamba to spectrograms, ClinicalMamba to notes, Bi-Mamba+ to forecasting. None of them touch the update rule. This paper changes the rule, which means every one of those application papers has an untested variant behind it. Biosignal streams are where the diagnosis should bite hardest, because PPG and EDA are long, non-stationary and amplitude-drifting, so a normalised update with data-set step size is a better match to the signal than a fixed learned decay gate.

**How this builds on what you know:** The three closest parents are Attention Is All You Need (Vaswani 2017, graphify anchor for Community 2 with 12 edges), Mamba-2 (Dao 2024) and Mamba (Gu 2024), with S4 and LSSL sitting behind them. Where Vaswani kept every past token in a growing key-value cache and retrieved with softmax, and where Mamba compressed that history into a fixed state governed by a learned selective gate, this paper asks what objective the compression implicitly optimises and finds it is the wrong one. Where Mamba-2 proved that selective state-space models and linear attention are the same computation, this paper takes the duality one level further and treats the shared update as a step of online regression, because that is what makes the four design knobs separable instead of entangled in a single gate. The import runs from adaptive filtering into sequence models, which is the opposite of the usual direction and a source the wearable-sensing literature has not drawn on.

The Community 2 connection is worth naming precisely: HARMamba is the node in your library that already sits in Community 2 by architecture while routing to time-series.md and llm-health.md by topic. It is the shortest path from this paper to your own work.

---

## Tier B — TLDRs

### ContextPilot: Teaching Agents for Proactive Context Management via Fine-grained RL
Pan, Pei, Lu, Lin et al. (Tencent) — arXiv:2608.28476 — https://arxiv.org/abs/2608.28476

Trains a language agent to edit its own working context during long-horizon tasks, widening the toolset past search, delete and summarise to include global planning, long-term memory writes and soft context offloading. The training method is the contribution: context and entropy variation identify the editing decisions where downstream behaviour is actually sensitive to the choice, branch sampling concentrates there, and the advantage for a given edit is estimated from all branched trajectories that pass through it rather than from one trajectory-level reward. Reported outcome is stronger long-context question answering and deep search at a smaller working context across several base models, with weights released as ContextPilot-8B and 14B. The comparison being made at matched or smaller context size is what makes the result meaningful rather than a consequence of retaining more.

**How this builds on what you know:** Parents are the Memory Mechanisms survey (Huang 2026, `huang2026_memory`), ToolkenGPT (Hao 2024, `hao2024_toolkengpt`) and LATS (Zhou 2024, `zhou2024_lats`) — all three in graphify Community 0, LLM Agents and Reasoning. Where the Memory survey argued memory is a design axis rather than a storage detail, this paper makes the memory operations trainable actions with their own reward, because naming the axis does not tell you when to write or drop. Where ToolkenGPT learned which external tool to call, this learns which internal edit to make, so the context becomes the object acted on rather than the medium the action lives in. Where LATS branched trajectories at inference time to search for a better answer, ContextPilot branches at training time and uses branch outcomes to attribute credit to one specific edit, converting LATS's tree from a decoding procedure into a variance-reduction device.

This paper extends ToolkenGPT, which already crossed tool-using agents and agentic vision through its bridge to PyVision in your library. The new work pushes that bridge inward, from actions that fetch external information to actions that restructure information already held.

### J-Zero: Unified Challenger--Solver--Judge Co-Evolution from Zero Data
Chu, Jeon, Yang (KAIST AI) — arXiv:2608.26582 — https://arxiv.org/abs/2608.26582

Carries self-evolving training into domains where no verifier exists. A Challenger raises task difficulty and a Solver learns against it, which is standard; the addition is a Judge that co-adapts on preference pairs whose ordering is known in advance from how each response was produced rather than from the Judge's own scores. Two constructions supply the labels: the Solver's answer over the Challenger's, and a decomposed-then-recombined answer over a one-shot answer. Reported gains average 4.2 points on verifiable and 8.0 on unverifiable domains, and improvement continues through at least ten iterations where baselines degrade after two. The iteration count is the number that carries the argument, since two-iteration collapse is the known failure of judge-based self-evolution.

**How this builds on what you know:** Parents are DeepSeek-R1 (`deepseek2025_r1`) and Chain-of-Thought Prompting (Wei 2023, `wei2023_cot`, the reasoning anchor with 7 edges), both Community 0. Where DeepSeek-R1 obtained reasoning by reinforcement learning against a verifier, and therefore stopped wherever verifiers stop, this paper replaces the verifier with a Judge and then fixes the circularity that move creates: a frozen Judge caps the Solver, and a self-scored Judge drifts, so the supervision is sourced from the generation procedure instead. Where Chain-of-Thought used decomposition to improve a single answer at inference, J-Zero keeps the comparison and discards the improved answer, treating "decomposed beats one-shot" as a free label.

This paper extends the DeepSeek-R1 to Chain-of-Thought bridge already in your library, which crosses reasoning-by-prompting and reasoning-by-reinforcement-learning. The new work pushes that bridge into the unverifiable case, which is the normal case for health language work: CounselBench in your library measures that gap without offering a training answer to it.

### Code as Worlds: Agentic Discovery of Executable World Representations for Physical Reasoning
Wang, Cai, Chen, Liu, Long, Wu et al. (MirroS Lab) — arXiv:2608.27549 — https://arxiv.org/abs/2608.27549

Represents a physical scene as executable code rather than pixels or a learned latent, so object composition, dynamics and appearance are all program text that can be run forward, queried for a parameter, or edited to pose a counterfactual. Recovering such a program from video or a description uses an abductive loop: propose a world program, execute it, render, verify against the observation, refine. Verified programs then become scalable quantitative supervision for a vision-language model, and Code-as-World-VL reaches state of the art on QuantiPhy above leading proprietary models, with 4B and 9B weights released. The coverage question is the one to hold onto: rendering agreement shows a program is consistent with the evidence, not that it is the right mechanism, so distinct programs can pass on the same video.

**How this builds on what you know:** Parents are World Models (Ha 2018), Evaluating World Models (Vafa 2024) and PyVision (Zhao 2025, `zhao2025_pyvision`, Community 0). Where Ha compressed observations into a latent state and rolled it forward, this writes the state and dynamics as source code, because a latent vector cannot be checked against physics or queried for a parameter. Where Vafa showed that accurate prediction does not imply a coherent world model and left the diagnosis without a construction, this makes coherence enforceable: a program either renders to match or it does not, so verification is an execution rather than a probing experiment. Where PyVision wrote throwaway analysis code to answer a visual question, here the code is the persistent representation, which is what lets it become training data.

This paper extends PyVision, which already crossed tool-using agents and agentic vision in your library through its bridge to ToolkenGPT. The new work pushes that bridge into world modelling, joining Community 0 to the world-model cluster in Community 7 — a crossing your library does not yet contain.

---

## Tier C — scan

| Paper | Hook | Link |
|---|---|---|
| Revisiting Local Context for Long-Horizon Streaming 3D Reconstruction (Alibaba AMAP) | Local context, not global memory, is what streaming reconstruction was missing | https://arxiv.org/abs/2608.27529 |
| Beyond Data Scaling: Representation-Centric Continued Pre-training for VLA Models | More robot data stops helping; better representations do not | https://arxiv.org/abs/2608.27550 |
| Blind Men and the Elephant: Epistemic Myopia of LLMs under Long-Tail Divergent Knowledge (Tencent) | Models commit to one shard of a contested fact and never notice | https://arxiv.org/abs/2608.28478 |
| LayerRecall: State-Conditioned Memory Router for Long-Horizon Video Generation | Routes memory per layer to hold consistency across long generated video | https://arxiv.org/abs/2608.28460 |
| StepGuard: Learning Step-Level Guardrails with Scalable Supervision | Safety checks per reasoning step, with the utility cost measured | https://arxiv.org/abs/2608.24777 |
| Puro-2B: Poor Lab's Qwen2-1.5B Trained on RTX 5090 within $5090 | Full 2B pretraining reproduced on one consumer GPU for the price of the GPU | https://arxiv.org/abs/2608.27370 |
| Rubric-to-Code Credit Assignment for Reinforcement Learning (Ant Group) | Compiles a grading rubric into executable reward code | https://arxiv.org/abs/2608.27906 |
| DART-SD: Retrieval and Tuning for Self-Distillation of Multi-Turn Tool-Calling Agents (ByteDance) | Self-distillation for tool-calling agents without a stronger teacher | https://arxiv.org/abs/2608.18524 |

---

## Tier D — Time-series / bio-sensing gap watch

No time-series or bio-sensing paper landed today, so this section is entirely unported opportunities drawn from the day's top work.

**Already ported, and now closed off.** Two areas confirmed shut this week rather than today. The LLM-agent framing for time series is finished as a novelty: graphify Community 4 already holds TS-Agent, ChatTS and the Zhang 2024 survey, and yesterday's LLM Agents for Time-Series survey was itself the closing move, reorganising the field by task because the attachment method had stopped being the informative variable. Masked autoencoding for biosignals is likewise closed, carried in Community 1 by the mask-matters theory paper and the biosignals foundation-model survey, and reconfirmed by Wednesday's CardioState-JEPA. Neither is worth a new paper unless the contribution is a dataset.

**Unported opportunity 1 — normalised fast-weight updates for non-stationary biosignals.** Every state-space paper in your library keeps the update rule fixed and swaps the modality; HARMamba, Bi-Mamba+ and ClinicalMamba are all the same move applied three times. Nothing in Community 2 or Community 5 changes what gets written into the recurrent state. Transfer hypothesis: replacing a learned decay gate with a normalised least-mean-squares update, where step size is set from the current key magnitude, should hold calibration across the amplitude drift and baseline wander that make long PPG and EDA recordings hard, and the test is length extrapolation from short training windows to multi-day rollouts rather than in-window accuracy.

**Unported opportunity 2 — learned context editing for long-horizon sensing agents.** TS-Agent accumulates an evidence log and never prunes it, and Sensor2Text keeps sensor history in context, so both carry the growing-context problem ContextPilot attacks, at a horizon far longer than any deep-search benchmark. Transfer hypothesis: fine-grained credit assignment over context edits gives a way to learn which sensor windows are worth retaining, replacing the heuristic downsampling used throughout the wearable literature, and the stakes differ from web search because dropping the wrong window discards a physiological event rather than a page.

---

## News

Quiet stretch for model releases. The most recent frontier release remains GLM-5.3 Flash from Z.AI on 26 August; nothing shipped from OpenAI, Anthropic, Google DeepMind, Meta or xAI overnight. What did land today is open weights attached to two of the papers above: Tencent released ContextPilot-8B and ContextPilot-14B, and MirroS Lab released Code-as-World-VL at 4B and 9B with a demo space. Both are usable today if either transfer hypothesis in Tier D is worth a quick experiment.

---

Quiet day on your primary area — no time-series or bio-sensing paper qualified, and Tier A is an architecture paper rather than a signal paper. If the two-page test kills Fast Weight Attention, the backlog promotion is CardioState-JEPA (arXiv:2608.12944) from Wednesday, which is the strongest unread item in your own area from the past week.

End of digest. Close this tab when done.
