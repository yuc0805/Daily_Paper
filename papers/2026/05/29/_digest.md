# AI Digest — 2026-05-29

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A is not done by 6 AM, stop.

Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.

Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

---

## Tier A — Deep read (~20 min)

### LLM Pretraining Shapes a Generalizable Manifold: Insights into Cross-Modal Transfer to Time Series
arXiv:2605.20449 · Roger et al. · https://arxiv.org/abs/2605.20449

**Problem.** A line of work in your library (GPT4TS, FPT, Time-LLM) shows that a language model, with most weights frozen, can be repurposed for time-series forecasting and often beats models built only for time series. The puzzling part is why. Language and numeric sequences look unrelated, so it is not obvious what a model trained on text carries over to a forecasting task. The paper sets out to give a mechanism rather than another benchmark number.

**Method.** The authors treat the question geometrically. They probe the hidden states of a frozen language model fed with time-series inputs and ask three things: whether the representation already contains time-series structure before any fine-tuning, whether the pretrained starting point changes how training proceeds, and what fine-tuning actually moves. They use a linear probe on frozen states, nearest-neighbor retrieval in the projected space, and an analysis of the loss surface comparing pretrained against random initialization.

**Result.** A linear probe on the frozen states decodes realistic time-series trajectories without any paired supervision, and retrieval in that projected space already yields competitive forecasts. So structure and dynamics are present before fine-tuning, not created by it. Pretrained initialization also changes optimization: it produces coherent gradients and a sharply anisotropic loss surface, where random initialization does not. The picture the paper argues for is that language pretraining builds a reusable manifold, and fine-tuning projects numerical dynamics onto the task-relevant directions of that manifold.

**Limitations.** The evidence is mostly geometric and probing-based; it explains a mechanism but does not turn it into a forecasting method that beats a strong dedicated model. The probes are linear, so nonlinear structure the model uses may be undercounted. The work does not yet say which properties of text pretraining (token statistics, long-range dependence, scale) are responsible, so the account is descriptive rather than predictive.

**Why it matters to Leo.** This is directly in your primary area. It gives a concrete reason behind the "frozen LLM helps time series" result your library already records, and it suggests a practical lever: if the useful structure lives in a low-dimensional manifold present before fine-tuning, then probing and retrieval may be a cheaper path than full fine-tuning for biosignal forecasting, and the same manifold view could be tested on PPG or ECG sequences.

**How this builds on what you know:** The closest parents in your library are GPT4TS / FPT (the "One Fits All" frozen-LLM-for-time-series line) and Time-LLM, all in your time-series collection (graphify Community 4, Time Series + LLM Integration). Where GPT4TS showed that freezing language-model blocks and training only thin input and output layers gives strong forecasting, and Time-LLM showed that reprogramming the series into the language input space works, this paper does not propose a new transfer recipe; it explains why those recipes work, because the language manifold already encodes sequence structure that fine-tuning only has to rotate into place. It also touches the MAE Theory paper (Zhang 2023, Community 1) in your library, which made a similar geometric argument for masked autoencoders; here the argument is moved from vision pretraining to language-to-time-series transfer.

---

## Tier B — TLDR (~10 min)

### 1. Rethinking RL for LLM Reasoning: It is Sparse Policy Selection, Not Capability Learning
arXiv:2605.06241 · Akgül, Kannan, Neiswanger, Prasanna · https://arxiv.org/abs/2605.06241

Reinforcement learning is often described as teaching a model new reasoning strategies. This paper argues the opposite through token-level analysis across several model families and RL algorithms. The effect of RL is sparse: only 1 to 3 percent of token positions change, those positions sit at high-entropy decision points where the base model was unsure which branch to take, and the promoted token is almost always already inside the base model's top-5 candidates. The authors conclude that RL redistributes probability mass over solutions the base model already contains, and suggest that targeted corrections at those few uncertain points could stand in for a full RL loop.

**How this builds on what you know:** The direct parents are DeepSeek-R1 (reasoning via RL, graphify Community 0) and Chain-of-Thought Prompting (Wei 2023, Community 0) in your library. There is a graphify cross-area bridge from DeepSeek-R1 to Chain-of-Thought, marked as "reasoning-via-RL versus prompting." This paper extends that bridge: where DeepSeek-R1 treated RL as the source of new reasoning ability, and Chain-of-Thought elicited reasoning through prompting alone, this work argues the RL gain is small and local, closer to selecting among options the prompted base model could already reach. It also continues the debate from yesterday's "Beyond Reasoning: RL Unlocks Parametric Knowledge" and "Can RL Teach Long-Horizon Reasoning," now from the mechanistic, token-level side.

### 2. Personalizing Embodied Multimodal LLM Agents over Long-term User Interactions (POLAR)
arXiv:2605.26256 · Lee, Park, Lee · https://arxiv.org/abs/2605.26256

POLAR is a memory-augmented framework for embodied agents that have to serve the same user across many sessions. It organizes prior interactions into a multimodal knowledge graph that separates semantic memory (stable facts about the user and environment) from episodic memory (specific past events), then conditions the agent's actions on retrieved memory so behavior reflects the user's history rather than a generic policy.

**How this builds on what you know:** The parents are the Memory Mechanisms Survey (Huang 2026) and the Agent AI Survey (Durante 2024), both in your agent collection and graphify Community 0 (LLM Agents and Reasoning). Where the Memory Mechanisms Survey catalogued how agents store and recall state, and the Agent AI Survey mapped multimodal interaction broadly, POLAR commits to a specific structure, a semantic-versus-episodic knowledge graph tied to one user over time, because long-term personalization needs both durable facts and recallable events rather than a single flat memory store.

### 3. Code as Agent Harness
arXiv:2605.18747 · Ning et al. · https://arxiv.org/abs/2605.18747

This is a position-and-survey paper that reframes code as the substrate that connects an agent to reasoning, action, environment modeling, and execution-based verification, rather than treating code only as an output to be generated. It organizes the design space into three layers: the harness interface (how code links the agent to its world), harness mechanisms (planning, memory, and tool use for long-horizon execution, plus feedback-driven control), and scaling considerations.

**How this builds on what you know:** The parents are ToolkenGPT (tool embeddings for LLMs) and PyVision (agentic vision with dynamic tooling), both in your agent collection and graphify Community 0. There is a graphify cross-area bridge linking ToolkenGPT and PyVision, marked "tool-using agents." This paper extends that bridge: where ToolkenGPT made tools callable as learned tokens and PyVision let an agent write and run vision code on the fly, this survey treats code itself as the general harness that unifies tool use, memory, and verification, pushing the bridge from "agents that call tools" toward "code as the operating layer the whole agent runs on."

---

## Tier C — Scan headlines (~5 min)

- Aligning LLMs with Human Uncertainty: A Beta-Bernoulli Calibrator for LLM Forecasting — turns any point-estimate forecast into a calibrated event distribution. https://arxiv.org/abs/2605.27668
- LANG: RL for Multilingual Reasoning with Language-Adaptive Hint Guidance — hints steer exploration on non-English reasoning. https://arxiv.org/abs/2605.22567
- From Reasoning Chains to Verifiable Subproblems (SCRL) — curriculum RL that derives checkable subproblems for credit assignment. https://arxiv.org/abs/2605.22074
- Is Grep All You Need? How Agent Harnesses Reshape Agentic Search — retrieval-strategy choice interacts with agent architecture. https://arxiv.org/abs/2605.15184
- Cattle Trade: A Multi-Agent Benchmark for LLM Bluffing, Bidding, and Bargaining — strategic-reasoning benchmark for agents. https://arxiv.org/abs/2605.14537
- Predictive Maps of Multi-Agent Reasoning — successor-representation view of agent communication topologies. https://arxiv.org/abs/2605.11453
- STARFlow2: Bridging Language Models and Normalizing Flows for Unified Multimodal Generation — interleaves a VLM stream with a normalizing-flow stream. https://arxiv.org/abs/2605.08029
- Squeezing Capacity from Multimodal LLMs for Subject-driven Generation — conditions diffusion on an MLLM plus VAE identity features. https://arxiv.org/abs/2605.26111

---

## Tier D — Time-series / Bio-sensing Gap Watch

Already ported (closed off). Today's two strongest time-series papers both sit inside the LLM-integration story your library already tracks. The Tier A manifold paper and the Nexus agentic-forecasting line are squarely in graphify Community 4 (Time Series + LLM Integration); applying language-model representations and agent loops to numeric series is no longer an open transfer, it is the active center of that community. The Beta-Bernoulli calibrator (Tier C) ports forecast calibration onto LLM outputs, which is also within the same ported region.

Unported opportunity. Two methods landing today have not yet reached time-series or bio-sensing, and both look transferable:

First, normalizing-flow plus language-model interleaving (STARFlow2). Generative work on biosignals in your library leans on diffusion (TimeGrad). A flow-based stream gives exact likelihoods rather than a sampling approximation, which matters for anomaly scoring on PPG or ECG, where you want a calibrated density rather than a sample. Transfer hypothesis: replace the diffusion stream in a biosignal generator with a TarFlow-style normalizing-flow stream conditioned on a sensor encoder, and read the exact likelihood as the anomaly score.

Second, sparse high-entropy correction (Rethinking RL, Tier B). The finding that RL only moves 1 to 3 percent of tokens at uncertain decision points has no time-series analogue yet. Transfer hypothesis: in a time-series reasoning agent, identify the few high-uncertainty operator-selection steps (which statistic or change-point test to call) and apply targeted correction there, instead of fine-tuning the whole controller.

---

## News

Quiet week for model releases. The major labs appear to be pausing after the late-April cycle (OpenAI GPT-5.5 on April 24, Anthropic Claude Opus 4.7 on April 16). The most recent notable release is Google DeepMind's Gemini 3.5 Flash (around May 19), a lightweight variant aimed at low-cost, fast inference. No frontier-model announcements in the last 24 to 48 hours.

---

End of digest. Close this tab when done.
