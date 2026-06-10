# AI Digest — 2026-06-10

**Reading budget today:** 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A not done by 6 AM, stop.

**Open-tab rule:** maximum 3 papers open at once. Close one before opening a fourth.

**Two-page test:** if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

---

## Tier A — Deep Read

### NF-CoT: Latent Reasoning with Normalizing Flows
**Tu, Fu, Yu, Tang, Kang, Qin, Zhang, Gu** | arXiv 2606.06447 | 2026-06-04 | cs.CL, cs.LG

**Problem.** Chain-of-thought reasoning in LLMs forces every intermediate step through a discrete token stream. This is wasteful when the underlying reasoning update is semantic, uncertain, or only partially formed. Existing latent-reasoning methods (Coconut, PonderLM, Latent-GRPO) move computation into continuous space but sacrifice one or more of: left-to-right generation, KV-cache compatibility, probabilistic sampling, or tractable likelihoods.

**Method.** NF-CoT instantiates a TARFlow-style normalizing flow inside the LLM backbone. The flow head generates "continuous thought" positions while the standard LM head generates text positions, both within the same causal stream sharing one KV cache. Continuous thoughts are distilled from explicit CoT during training. The normalizing flow provides exact log-likelihoods for latent thoughts, enabling both maximum-likelihood training and direct policy-gradient optimization in latent reasoning space.

**Result.** On code-generation benchmarks, NF-CoT improves pass rates over explicit CoT and prior latent-reasoning baselines (Coconut, CALM) while substantially reducing intermediate-reasoning token cost. The paper reports that latent positions use roughly 4x fewer "tokens" than the equivalent explicit CoT trace.

**Limitations.** Evaluated only on code generation. The normalizing flow adds parameters and training complexity. It is unclear how well the approach transfers to open-ended reasoning (math, science QA) where the CoT structure is less regular than code. The distillation step requires access to explicit CoT traces, which may not always be available.

**How this builds on what you know:** NF-CoT is a direct descendant of the chain-of-thought paradigm (Wei 2023, in your library as graphify node wei2023_cot, Community 0). Where CoT generates all reasoning as text, NF-CoT compresses it into continuous states. It also relates to DeepSeek-R1 (graphify node deepseek2025_r1, Community 0), which improved reasoning via RL over token outputs — NF-CoT replaces the RL-over-tokens approach with a generative model (normalizing flows) over latent states. Your library has several recent latent reasoning papers: CoLaR (Y4ZNT3EC), PonderLM (3TLRP8U5), and Latent-GRPO (U4ZPM5DN). NF-CoT's main advantage over Latent-GRPO is that the flow provides exact densities rather than reward-based approximations, enabling cleaner optimization. For your time-series work, the practical takeaway is: if you build TS-Agent-style systems where each reasoning step currently requires explicit text generation over numeric evidence, latent reasoning could cut the token budget without losing the iterative reasoning structure.

---

## Tier B — TLDRs

### 1. MemoPilot: Test-Time Learning of LLM Agents via RL over Memory
**arXiv 2606.08656** | 2026-06-10

MemoPilot trains a plug-in "memory copilot" that optimizes how a frozen LLM agent updates its memory across sequential interactions. It formulates memory updating as a multi-turn decision problem and solves it with multi-turn GRPO, introducing turn-wise rewards and context-independent advantage estimation. On repeated game-playing benchmarks, MemoPilot achieves the highest Elo ratings (1762 on LHE, 1590 on RPS), outperforming hand-designed memory prompts and proprietary models including DeepSeek-V3.2.

**How this builds on what you know:** This paper extends the Memory Mechanisms survey (Huang 2026, graphify node huang2026_memory, Community 0) from a taxonomy of memory designs to a trainable memory policy. It uses the same GRPO family as DeepSeek-R1 but applies it to the memory layer rather than the reasoning layer. For agent architectures like LATS (graphify node zhou2024_lats) that plan over action trajectories, MemoPilot offers a complementary approach: instead of searching over actions, train the memory that informs future actions.

### 2. Bridging the Last Mile of TS Forecasting with LLM Agents
**arXiv 2606.02497** | 2026-06-01

Time-series foundation models produce statistically plausible zero-shot forecasts, but deployment-ready forecasts require domain-specific adjustments — holiday effects, campaign plans, external events, expert corrections. This paper frames that gap as the "last-mile problem" and builds an LLM agent that wraps around a forecasting backbone. The agent maintains a forecast workspace, retrieves contextual evidence via tool calls, and applies structured revisions with safety constraints that prevent the agent from making unbounded changes to the baseline.

**How this builds on what you know:** This sits squarely in your primary area — Time Series + LLM Integration (Community 4). It extends the TS-Agent paradigm (graphify node liu2025_tsagent) from analysis/reasoning to forecast correction. Where TS-Agent calls operators to understand a series, this agent calls tools to retrieve business context and revise a forecast. It also relates to Sundial (4QQTVIYC) and other TS foundation models in your library as the "backbone" that produces the initial forecast the agent revises.

### 3. ExpWeaver: LLM Agents Learn from Experience via Latent RAG
**arXiv 2606.01041** | 2026-06-01

ExpWeaver eliminates the separate RAG module for agent experience retrieval by encoding past experiences using the LLM's own hidden states and retrieving them in latent space at each decoding step through cross-attention and gated residuals. The full pipeline is optimized end-to-end with RL. This removes the context-window bottleneck of text-based experience retrieval and couples retrieval tightly with generation.

**How this builds on what you know:** ExpWeaver implements a latent-space version of the retrieval-augmented memory pattern catalogued in the Memory Mechanisms survey (Huang 2026, graphify node huang2026_memory). It also echoes the ToolkenGPT idea (graphify node hao2024_toolkengpt, Community 0) of embedding external knowledge into the LLM's representation space. This paper bridges the agent community (where ToolkenGPT and LATS sit) and the latent reasoning direction (where NF-CoT and Latent-GRPO sit): experience retrieval in latent space is a form of implicit reasoning over past interactions.

---

## Tier C — Scan Headlines

1. **Geometric Latent Reasoning Induces Shorter Generations** (2606.02248) — Lightweight transition head predicts direction updates in embedding space; latent reasoning produces shorter outputs without explicit length penalty. [arxiv](https://arxiv.org/abs/2606.02248)

2. **Persistent Memory for Continuous Latent Reasoning (CoCoNuT extension)** (2606.07720) — Extends the CoCoNuT continuous-thought paradigm with persistent memory across the residual stream. [arxiv](https://arxiv.org/abs/2606.07720)

3. **Test-Time Compute Scaling for ASR (LARM)** (2606.04678) — Depth-conditioned looped transformer turns encoder depth into a controllable test-time compute axis for speech recognition. [arxiv](https://arxiv.org/abs/2606.04678)

4. **Mechanistic Insights into Functional Sparsity in MLLMs (CoRe Heads)** (2606.05843) — Identifies localized sparsity patterns in multimodal LLMs; leveraging them accelerates inference with minimal performance loss. [arxiv](https://arxiv.org/abs/2606.05843)

5. **Spatial Lexical Bias in MLLM Spatial Reasoning** (2606.01914) — Mechanistic interpretability study of why MLLMs fail at spatial multiple-choice questions. [arxiv](https://arxiv.org/abs/2606.01914)

6. **TS Foundation Models for Cold-Start PV Forecasting** (2606.07457) — Zero-shot pipeline using synthetic production history from plant metadata; applies TSFMs to solar energy forecasting without historical data. [arxiv](https://arxiv.org/abs/2606.07457)

7. **Network Time Series Models for Multivariate Volatility** (2606.03828) — Extends time-series models with network structure for financial volatility forecasting. [arxiv](https://arxiv.org/abs/2606.03828)

8. **Why Do Time Series Models Need Long Context Windows?** (2606.01999) — Separates two objectives in grouped TS forecasting: generative process identification vs. conditional forecasting. [arxiv](https://arxiv.org/abs/2606.01999)

---

## Tier D — Time-Series / Bio-Sensing Gap Watch

No dedicated TS/bio-sensing papers landed today with novel method transfers. Here are unported opportunities from today's top papers:

**Unported Opportunity 1: Normalizing flows for latent reasoning in time-series agents.** NF-CoT (Tier A) shows that normalizing flows can replace discrete CoT in code generation. This has not been applied to time-series reasoning agents (TS-Agent, ChatTS). Transfer hypothesis: replace the explicit text-based evidence-log loop in TS-Agent with NF-CoT-style continuous thoughts, reducing token overhead while preserving the iterative analysis structure. The flow's exact likelihoods could also serve as a confidence measure for each reasoning step over numeric data.

**Unported Opportunity 2: Latent experience retrieval for clinical monitoring agents.** ExpWeaver (Tier B) moves experience retrieval into latent space. This has not been applied to wearable/bio-sensing agents that process repeated patient sessions. Transfer hypothesis: a clinical monitoring agent (following the MindScape or GLOBEM paradigm) could encode past patient encounters in latent space and retrieve them at decoding time, avoiding the context-window cost of text-based patient histories. This would be particularly useful for longitudinal biosignal analysis where the number of past sessions grows large.

---

## News

**Anthropic expands Project Glasswing.** Anthropic added approximately 150 organizations in 15+ countries to Project Glasswing, which uses Claude Mythos Preview to find software vulnerabilities. The program has surfaced over 10,000 high- or critical-severity vulnerabilities since its April launch. Claude Mythos Preview is available at $25/$125 per million input/output tokens.

**Google Gemini 3.1 Flash-Lite GA.** Gemini 3.1 Flash-Lite reached general availability in May, priced at $0.25/M input tokens with 2.5x faster response times than earlier Gemini versions. It is the most cost-efficient model in the Gemini 3 series.

**OpenAI crosses $25B annualized revenue.** OpenAI has surpassed $25 billion in annualized revenue and is reportedly exploring a public listing as early as late 2026.

---

End of digest. Close this tab when done.
