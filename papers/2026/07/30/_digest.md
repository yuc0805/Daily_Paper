# AI Digest — 2026-07-30

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A is not done by 6 AM, stop.

Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.

Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

---

## Tier A — deep read

### Expert-Guided Forecast Editing for Time-Series Foundation Models
arXiv:2607.19659 (Le, M. H. Nguyen, M. Nguyen, H. H. Nguyen, Do) — https://arxiv.org/abs/2607.19659

**Problem.** A time-series foundation model produces a forecast, and that forecast is then fixed. If a domain expert or a downstream evaluator can score how good a candidate future trajectory is, there is no clean way to feed that judgment back without retraining the model. The paper studies this setting under a tight query budget: the expert evaluator is expensive, so only a few candidate trajectories can be scored. Two obvious strategies each fail. Best-of-N only samples from the model's own predictive distribution and never moves beyond what the model already believes. Optimization methods treat the whole forecast horizon as one long unstructured vector and waste queries searching a space that is too large.

**Method.** The paper introduces DEFT. It keeps the foundation model frozen and edits the forecast at test time. First it exploits the model's predictive samples, but in a decomposed trend-and-seasonal space rather than the raw horizon. Then it explores around those samples by refining the trend and seasonal components separately. The key trick is query reuse: DEFT asks the expert to score only complete trajectories, then reuses each score for the trend and seasonal components that appeared in the scored recombinations. So one expert query yields structured, component-level feedback instead of a single scalar on one guess.

**Result.** The authors test DEFT against best-of-N, the cross-entropy method, and Bayesian optimization under matched query budgets. The evaluation covers two forecasting benchmarks totaling 78 datasets, three different time-series foundation models, four feedback types, and seven query budgets. DEFT improves the effectiveness of expert guidance across that grid. A molecular-dynamics case study suggests the same idea carries to more physically grounded feedback, not only forecasting error.

**Limitations.** DEFT assumes the forecast decomposes cleanly into trend and seasonal parts, which holds for many series but not all. It also assumes an expert evaluator exists and is the bottleneck; where feedback is cheap, plain best-of-N may be enough. The paper reports relative gains in guidance effectiveness rather than a single headline accuracy number, so the size of the practical win depends on the budget and feedback type in play.

**Why it matters to Leo.** This is directly in the primary area. It is a test-time method: no retraining, model stays frozen, and the only cost is a handful of expert scores. For bio-signal forecasting where a clinician or a physical constraint can rank candidate trajectories but labeled data is scarce, the component-level query-reuse idea is worth borrowing. It also shows that a search method from reinforcement learning and optimization, the cross-entropy method, is a real baseline to beat in time-series editing, not a curiosity.

**How this builds on what you know:** The nearest parent in your library is Chronos (72DFULQQ), a pretrained time-series foundation model of the exact kind DEFT edits without touching its weights. The second parent is the Sample-efficient Cross-Entropy Method (ZNEMGMWY), which sits in graphify Community 7 (Reinforcement Learning): DEFT uses it as a direct search baseline and argues that pure exploration over the horizon wastes the query budget. Where Chronos produces a fixed forecast and CEM searches the horizon as an unstructured vector, DEFT does neither in isolation; it exploits Chronos-style samples in trend-seasonal space and then explores component-wise, because that is where a scarce expert query buys the most information. This paper also extends the Post-Training in Time Series Foundation Models framework (2607.20002) featured in your 2026-07-27 digest: in that taxonomy DEFT is an instance of output processing with test-time guidance, and it is a concrete method for the "calibrated output processing" open direction that framework named. In effect DEFT bridges Community 4 (Time Series + LLM Integration) and Community 7 (Reinforcement Learning) in your library, pulling a query-efficient search method out of the RL/optimization corner and into forecast editing.

---

## Tier B — TLDRs

### DecoEvo: Score-Decoupled Co-Evolution of Solver and Rubric-Generator Skills in Text Space
arXiv:2607.25675 (Qwen) — https://arxiv.org/abs/2607.25675

DecoEvo improves a language model on open-ended tasks by editing external natural-language artifacts (a solver skill and a rubric that grades it) rather than model weights. The known failure mode is that once the solver improves, a fixed rubric stops discriminating good from bad answers, but simply co-evolving the rubric against the solver's own score is unreliable because the rubric can be made easier to satisfy, which looks like progress but is not. DecoEvo separates the two update signals: the solver is updated with criterion-level feedback, while the rubric generator is revised through audits of requirement coverage and answer discrimination that do not use the solver's aggregate score, so rubric updates focus on newly exposed weaknesses instead of criteria the solver already passes. Under each benchmark's official evaluation it reports 2.8 to 5.0 percent relative gains over SkillOpt averaged across five benchmarks and three backbones.

**How this builds on what you know:** The parents in your library are DeepSeek-R1 (Z5IWHZAE) and Chain-of-Thought Prompting (HBLPTRMY), both in graphify Community 0 (LLM Agents and Reasoning). Where DeepSeek-R1 improves reasoning with a single fixed reward signal and Chain-of-Thought fixes the reasoning format at prompt time, DecoEvo makes the evaluator itself a moving, separately-audited target, because a static reward or rubric stops separating answers once the solver saturates it. This is the same reward-hacking concern that Skill Self-Play (2607.22529) raised in your 2026-07-27 digest, addressed here by decoupling the score that trains the solver from the audit that trains the grader.

### TurboVLA: Real-Time Vision-Language-Action Model at 32 Hz on an RTX 4090 with under 1 GB VRAM
arXiv:2607.27205 (H-EmbodVis) — https://arxiv.org/abs/2607.27205

TurboVLA reports a vision-language-action policy that runs at 32 Hz on a single consumer RTX 4090 while using under 1 GB of GPU memory. The contribution is on the deployment side of the VLA line of work rather than new task capability: prior open VLA models are accurate but too heavy and too slow for closed-loop control on commodity hardware, which keeps them off real robots. The paper's claim is that a VLA can be made small and fast enough for real-time on-robot inference without a datacenter GPU. For a reader outside robotics, the number to watch is the memory footprint: sub-1 GB continuous inference is the regime that on-device and edge sensing also need.

**How this builds on what you know:** No direct parent in your library, since you do not track vision-language-action models. The closest neighbor is Flamingo (SC8KWYVK), an early vision-language model in graphify Community 3 (Vision-Language and Generative), which established the image-plus-text encoder that VLA policies extend with an action head. Where Flamingo answered questions about an image, TurboVLA maps image and instruction to motor actions and does so under a hard latency and memory budget, because control has to close the loop many times per second.

### Forecasting Realized Volatility with Time Series Foundation Models: A Comparison with Econometric Benchmarks
arXiv:2607.05291 — https://arxiv.org/abs/2607.05291

This paper tests whether pretrained time-series foundation models beat classical econometric models at forecasting realized volatility. The finding is that performance varies a lot across foundation-model architectures, and that picking the right architecture matters more than the broad choice between a foundation model and an econometric baseline. In other words, "foundation model" is not one thing here, and a poorly matched one can lose to a simple statistical model. It is included today because it is directly in the primary area and it pairs with the Tier A paper: DEFT edits a foundation model's forecast at test time, while this paper is a reminder that the base model you choose to edit already decides much of the outcome.

**How this builds on what you know:** The parent is Chronos (72DFULQQ), one of the pretrained forecasters this study evaluates zero-shot. Where Chronos is presented as a general zero-shot forecaster, this paper measures where that generality holds and where it does not on a hard, non-stationary financial target, and connects to the Post-Training in Time Series Foundation Models framework (2607.20002) from your 2026-07-27 digest by showing why post-training or test-time editing is needed at all: the frozen model's architecture, not just its weights, sets the ceiling.

---

## Tier C — scan headlines

- SkillRise: Agentic Reinforcement Learning for Cross-Task Skill Evolution — grows a reusable skill library so an agent carries skills across tasks. arXiv:2607.26784
- DecoEvo's cousin, Skill Self-Play revisited: today's HF list is dominated by proposer-solver-skill co-evolution methods. arXiv:2607.22529
- HumanCLAW: Can Vision-Language Models Act Through a Body? (Meta) — benchmark for whether a VLM can control an embodied agent. arXiv:2607.27180
- CAST: Game Solvers as Turn-Level Teachers for LLM Agents — uses solved-game policies to supervise agent decisions turn by turn. arXiv:2607.25308
- CoRT: Counterfactual Replay for Token-Level Rubric-Guided Policy Optimization — token-level credit assignment from replayed counterfactuals. arXiv:2607.25659
- Can AI agents conduct open-ended AI research? Early evidence from two case studies — 24-author report on autonomous research agents. arXiv:2607.27191
- OmegaUse-OfficeVal: Benchmarking LLM Agents on Long-Horizon Office-Suite Tasks with Economic Grounding — cost-aware agent benchmark. arXiv:2607.27155
- Evaluating Time Series Foundation Models for Electricity Price Forecasting — zero-shot TSFMs struggle under covariate-driven, non-stationary load. arXiv:2607.02623

---

## Tier D — Time-series / Bio-sensing Gap Watch

Today's time-series papers are DEFT (Tier A) and two foundation-model evaluation papers (Tier B and Tier C). No bio-sensing paper landed today.

Already ported (closed off). DEFT ports test-time search and expert-guided editing, methods from the reinforcement-learning and optimization side (best-of-N, cross-entropy method, Bayesian optimization), into time-series foundation model forecasting. Query-efficient test-time editing of a frozen forecaster should now be treated as done for the general forecasting case; matching graphify Community 4 (Time Series + LLM Integration), this is no longer low-hanging fruit.

Unported opportunity 1. Score-decoupled co-evolution of a solver and its grader (DecoEvo, from NLP open-ended evaluation) has not been applied to time-series reasoning agents. Transfer hypothesis: co-evolve a forecast-explanation solver against a separately-audited rubric so that time-series reasoning benchmarks stop rewarding memorized or hand-wavy explanations, addressing the same evaluation-gaming problem TS-Agent (I2CIT4I7) flagged in your library.

Unported opportunity 2. Sub-1 GB real-time model serving (TurboVLA, from robotics VLA deployment) has not been pushed into wearable bio-sensing foundation models. Transfer hypothesis: apply the same aggressive memory and latency budgeting to an on-device sensing model so a wearable can run continuous inference without offloading raw signal to a phone or server, which matters for both battery and privacy; this sits next to Community 5 (Wearable Sensing and Behavior).

---

## News

Anthropic released Claude Opus 5 on 2026-07-24. It took the top of Artificial Analysis's Intelligence Index at 61 and its Agentic Index at 55.3, priced at 5 dollars per million input tokens and 25 dollars per million output tokens.

Google shipped Gemini 3.6 Flash on 2026-07-21, a cheaper and faster Flash tier now served to the free Gemini app, alongside Nano Banana 2 Lite for low-cost image generation.

xAI took Grok 4.5 public on 2026-07-08 as a low-cost coding model at 2 dollars per million input and 6 dollars per million output tokens.

---

End of digest. Close this tab when done.
