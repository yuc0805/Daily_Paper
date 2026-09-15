# AI Digest — 2026-09-15

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A not done by 6 AM, stop.

Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.

Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

---

## Tier A — deep read

### When Agents Slow Down: Understanding LLM Agents' Test-Time Strategies via Elo-per-token Analysis
Liu, Mang, Peng, Chai, Li, Pimpalgaonkar, Zettlemoyer, Dimakis, Cheung — https://arxiv.org/abs/2609.15309

**Problem.** Agents decide for themselves how much test-time compute to spend: they revise, call tools, explore alternatives, and choose when to stop. That adaptivity is exactly why ordinary scaling curves do not apply, because the compute axis is no longer under the experimenter's control and what gets reported is a single end-of-run score. A final number cannot distinguish an agent still improving from one that stopped improving at ten percent of its budget and then burned the rest, and it gives no guidance on whether a budget should go into one long session or several parallel ones.

**Method.** The paper proposes Elo-per-token analysis for open-ended tasks that produce a continuous score for every intermediate submission. For each task it records the best solution found at each token budget, then fits a Bradley-Terry model so that within-task orderings aggregate into Elo ratings comparable across tasks whose raw scores live on different scales. Independent sampling supplies the reference curve, chosen because its behaviour is derivable rather than estimated: Elo grows linearly with log compute. The scaling inflection point is then defined as the per-session budget at which the agent's marginal Elo gain falls to the independent-sampling rate. The analysis covers four general-purpose agents on four open-ended benchmarks with sessions up to 100 million tokens, plus three feedback-driven optimization harnesses under controlled single-task interventions.

**Result.** Agents initially convert tokens into Elo faster than independent sampling, but marginal gains diminish and eventually drop below the reference. Using the inflection point as the per-session budget and splitting 100 million tokens across parallel sessions on FrontierCS Polyomino Packing gained 264 Elo over a single long session and 355 Elo over ten short sessions, so both over-long and over-short sessions are measurably wasteful and the right session width can be determined in advance. The strongest historical AtCoder Heuristic Contest contestants improve superlinearly over contest time on the same tasks, which places the slowdown in the agents rather than in the tasks and indicates substantial remaining headroom.

**Limitations.** The method requires intermediate submissions that can be scored continuously, which rules out most benchmarks with a single binary outcome. Bradley-Terry aggregation assumes transitive comparisons. The parallel-session result is demonstrated on one task, so the size of the gain should not be taken as general even though the direction is well supported.

**How this builds on what you know:** LATS (Zhou 2024, agent.md, graphify Community 0) and DeepSeek-R1 (2025, Community 0) each propose a way to spend test-time compute and report the score at the end of the run; where they measure the endpoint, this paper measures the derivative, because the endpoint hides where the spending stopped paying. Where TTT for Abstract Reasoning (Akyurek 2024, test-time-training.md) treats test-time adaptation as one knob, this work makes budget allocation itself the decision variable, so session count and session length become measurable choices rather than defaults. The graphify seed already records DeepSeek-R1 and Chain-of-Thought (Wei 2023) as a cross-area bridge, reasoning-via-RL against prompting; that bridge is precisely an argument about how test-time compute should be spent, and this paper supplies the instrument that would settle it empirically rather than by benchmark score.

**Why it matters to you.** The contribution is a measurement protocol, not an architecture, so it transfers to any long-horizon loop with a continuous intermediate score. Time-series and bio-sensing agent loops qualify directly: a forecasting error or held-out AUROC is exactly the continuously scorable intermediate the method needs, and no one has reported a scaling inflection point in that setting. It also gives a defensible way to justify compute budgets in a proposal — rather than asserting that more search helps, measure where it stops helping and argue for parallel sessions at that width.

---

## Tier B — TLDR

### Dream-RSI: Recursive Self-Improvement through Evolving Worlds
Zheng, Wu, Zhang, He et al. (Google) — https://arxiv.org/abs/2609.14858

A lightweight orchestration layer sits above an unchanged coding agent and makes the exploration strategy explicit and programmable. The accumulated discovery history, stored as trees of attempted and scored solutions, is reused as a replay simulator over the region of the search space that was actually visited, so candidate exploration policies can be evaluated off-policy without invoking the real evaluator. The improved policy is redeployed online, which reaches new regions and expands the simulator, closing the loop. Across algorithm engineering, mathematical optimization, and GPU kernel engineering the method matches or improves discovery quality while substantially cutting discovery cost in several settings, where cost is counted in online evaluation calls.

**How this builds on what you know:** Where LATS (Zhou 2024, agent.md, Community 0) pays full online cost for every node it expands and keeps its search policy fixed for a whole run, this paper treats the tree it has already built as a dataset and improves the search policy against it offline, because the expensive part of agentic discovery is evaluation rather than proposal. That is the move Offline RL (Levine 2020, world-model-rl.md, Community 7) established, applied one level up: the policy being improved chooses where to search, not what action to take. OPE Study (Voloshin 2021, Community 7) is the reason for caution, since off-policy estimates degrade exactly when the evaluated policy drifts from the logged behaviour, and a replay simulator covers only what was visited. This paper joins Community 0 (LLM Agents and Reasoning) to Community 7 (Reinforcement Learning), which your seed graph does not currently connect directly.

### Omni-Streaming Thinking
Du, Liu, Zheng, Li, Guo, Zhang, Zou — https://arxiv.org/abs/2609.15128

Streaming omni-modal models must decide what to answer and when, from the video chunks and synchronized audio seen so far. Visual cues often support an interpretation before the corresponding utterance finishes, and once that interpretation enters memory as a fact, later reasoning keeps relaying it even after audio contradicts it — the paper calls this premature cross-modal commitment. The method emits structured states holding evidence, forecasts, and claims; each claim is marked pending and bound to a verification interval and to the modality that would settle it, with audio and visual evidence kept in separate stores so refutation can be selective. On a frozen Qwen3-Omni-30B-A3B-Instruct backbone with lightweight adaptation it beats the strongest open baselines by more than 10 percent relative on five streaming and audio-visual benchmarks, and on the new OST-DiagBench, which holds video fixed while editing audio, it reaches d-prime 2.95 against at most 1.38 for open baselines.

**How this builds on what you know:** Where Where Does the Sound Go? (Jo 2026, 2609.05871, audio.md, featured here on 2026-09-13) showed by layer-wise probing that acoustic information survives to the last hidden layer and concluded that audio underuse is a readout problem, this paper supplies a mechanism that forces the evidence to be used, because a model whose last layer holds the acoustic evidence will still repeat an earlier visual claim once that claim has been committed. Where LTU (Gong 2023, audio.md) conditions on a finished clip and Flamingo (Alayrac 2022, multi-modal.md) writes each arriving observation straight into the language stream, here writing is deferred and reversible, because in a stream the order evidence arrives in is an artifact of timing rather than of weight. This paper extends 2609.05871, which already bridged your audio and multi-modal areas; the new work pushes that bridge from diagnosis into correction.

### PhysBrain 1.5: From Vision-Language Models to Physical Foundation Models
DeepCybo Team et al. (53 authors) — https://arxiv.org/abs/2609.14973

Starting from a general vision-language model, the system encodes language responses, end-effector motion, and dense visual targets as discrete token sequences and optimizes all three jointly with autoregressive next-token prediction, so one backbone handles understanding, action generation, and future-state prediction. Embodied supervision in pre-training comes entirely from human interaction videos organized into task-centered episodes, with motion recovered rather than recorded; supervised fine-tuning then mixes human demonstrations, robot trajectories, and simulated experience. The 8B model averages 72.5 across 28 embodied understanding benchmarks, is best among open models on 14, and is reported on par with GPT-6-Astra and Gemini 3.6 Flash while retaining general multimodal ability. Open 8B and 2B weights were released the same day.

**How this builds on what you know:** Where World Models (Ha 2018, world-model-rl.md) learns its latent from interaction collected in a simulator, this paper takes supervision from human interaction video, because robot trajectories are the scarce resource and video of people manipulating objects is not. Where DINO-WM (Zhou 2025, world-model-rl.md) keeps understanding and prediction in separate modules above a frozen encoder, here the three capabilities are token streams under one objective, so the same parameters answer a question, emit a trajectory, and render the next frame. Flamingo (Alayrac 2022, multi-modal.md) survives as the initialization rather than the architecture, and the claim worth checking is the retention of general multimodal ability, since narrow embodied fine-tuning usually destroys it. Treat the 28-benchmark average and the parity claim with care, as suite composition moves such averages easily, and note that future-state prediction is shown qualitatively with no held-out prediction error.

---

## Tier C — scan

| Paper | Hook | Link |
| --- | --- | --- |
| Atria Dawn: The Dawn of Agentic Superintelligence (InternLM) | Day's most upvoted release; agentic system claims framed as a capability threshold. | https://arxiv.org/abs/2609.15818 |
| Vidu S2: Real-Time Interactive, Editable, Spatial Video Generation (Tsinghua) | Video generation moves to interactive editing at inference rather than one-shot sampling. | https://arxiv.org/abs/2609.11638 |
| ZGCM-1: Fully Open Efficient Foundation Model for Math and Agentic Search | Fully open weights and data aimed at math plus search, not general chat. | https://arxiv.org/abs/2609.13356 |
| Discovery Foundation Models: Toward Open-Ended Discovery Intelligence | Position paper defining seven capabilities for models that formulate their own problems. | https://arxiv.org/abs/2609.15973 |
| RSIAgent: Autonomous Exploration for Recursive Self-improvement | Companion theme to Dream-RSI; self-improvement driven by environment exploration. | https://arxiv.org/abs/2609.15364 |
| BVB: Benchmarking Agentic Video Understanding via Blender Reconstruction | Scores video understanding by whether the agent can rebuild the scene programmatically. | https://arxiv.org/abs/2609.15478 |
| LLaDA-UI: Block-wise Diffusion for Vision-Language GUI Agents | Applies discrete diffusion instead of autoregression to GUI action prediction. | https://arxiv.org/abs/2609.13287 |
| Pick Your Poison: Selecting Poison Sets for Stronger LLM Backdoors (Anthropic) | Poison set selection, not poison volume, drives backdoor strength. | https://arxiv.org/abs/2609.15029 |

---

## Tier D — Time-series / Bio-sensing Gap Watch

No time-series or bio-sensing papers landed in today's candidate pool. The Hugging Face daily list was entirely agents, embodied models, and video generation, and targeted searches for September 2026 arXiv work on wearable sensing, HAR, and physiological foundation models returned nothing newer than the June benchmark work already in your library. Two unported opportunities from today's top papers follow.

**Unported opportunity 1 — scaling inflection points for time-series agent loops.** Elo-per-token analysis (2609.15309) has been applied to coding and heuristic-contest agents only. Nothing in Community 4 (Time Series + LLM Integration) measures marginal return per token; TS-Agent and ChatTS both report end-of-run task scores. Transfer hypothesis: run a TS-Agent-style loop on forecasting or wearable classification where held-out MASE or AUROC provides the continuous intermediate score, locate the scaling inflection point, and test whether parallel short sessions beat one long session as they do in the coding setting.

**Unported opportunity 2 — deferred-claim verification for streaming physiological sensing.** The pending-claim and verification-interval construction in Omni-Streaming Thinking (2609.15128) is modality-agnostic but appears nowhere in Community 5 (Wearable Sensing and Behavior). Transfer hypothesis: in a streaming accelerometer-plus-PPG pipeline the fast motion channel routinely commits to an activity label before the slower cardiac channel can contradict it, which is the same premature commitment failure; keeping per-modality evidence stores and deferring the label until the heart-rate response window has elapsed is a direct port, and an OST-DiagBench analogue that holds motion fixed while editing the cardiac channel would quantify the effect in d-prime.

Already ported, for contrast: LLM narration over sensor streams is closed off — Sensor2Text (Chen 2024) and MindScape (Nepal 2024) in Community 5, and ChatTS (Xie 2025) in Community 4, cover that hyperedge.

---

## News

A quiet day for frontier releases. The notable event is that PhysBrain 1.5 shipped open 8B and 2B weights on Hugging Face alongside the paper, which matters mainly because the parity claim against proprietary models is now checkable rather than asserted.

The September wave has otherwise already passed. Anthropic released Claude Fable 5.1 and Claude Mythos 5.1 on September 1, Google released Gemini 3.8 Flash on September 2, and OpenAI released GPT-6 Astra on September 3, all reported before this digest window.

---

End of digest. Close this tab when done.
