# AI Digest — 2026-06-06

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A not done by 6 AM, stop.
Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.
Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

---

## Tier A — Deep Read

### ACTS: Agentic Chain-of-Thought Steering for Efficient and Controllable LLM Reasoning
**arxiv:** [2606.03965](https://arxiv.org/abs/2606.03965) | Xia, Xie, Xu, Kang, Lamba, Gao, McAuley | 2026-06-02

**Problem.** Extended chain-of-thought reasoning improves accuracy but wastes tokens and offers no inference-time control over how the model reasons. Existing efficient reasoning methods control trace length (shorten, early-stop, compress) but leave the reasoning strategy implicit.

**Method.** ACTS formulates reasoning steering as a Markov decision process. A small controller agent observes the current reasoning trace and the remaining token budget, then issues a steering action consisting of a reasoning strategy label and a steering phrase that initiates the next step of a frozen reasoner. The controller is initialized from synthetic steering trajectories with multi-budget augmentation, then refined via RL with budget-conditioned reward shaping. The reasoner never has its weights modified.

**Result.** ACTS matches full-thinking performance across multiple benchmarks (MATH, GSM8K, and others) with substantial token savings. It enables controllable accuracy-efficiency trade-offs: given a tight budget, it degrades gracefully rather than failing abruptly.

**Limitations.** The controller must be trained per-reasoner (or at least per model family). The paper evaluates on math and code reasoning; generalization to open-ended scientific reasoning is not demonstrated. The MDP formulation assumes a fixed action space of reasoning strategies, which may not cover all useful modes.

**Why it matters to you.** The controller-reasoner separation is architecturally clean and potentially useful for on-device inference over biosignals, where compute budgets are fixed. The MDP formulation also opens the door to using standard RL tooling for metacognitive control — a direction that could apply to TS-Agent-style pipelines where you want an agent to decide when to stop analyzing sensor data and commit to a classification.

**How this builds on what you know:** ACTS sits directly downstream of Chain-of-Thought Prompting (Wei 2023) and DeepSeek-R1 in your library. Where Wei showed that explicit reasoning traces improve accuracy and DeepSeek-R1 showed that RL can train the reasoner itself to produce long traces with emergent self-verification, ACTS takes the next step: it leaves the reasoner frozen and trains a separate controller to manage the reasoning process. This is the bridge between "make the model reason" and "make the model reason efficiently" — the same gap that exists in your time-series agent work where TS-Agent (Liu 2025) reasons over sensor data but has no budget control.

---

## Tier B — TLDRs

### 1. PROVE: Programmatic Rewards On Verified Environments for Multi-Step Tool Use
**arxiv:** [2606.03892](https://arxiv.org/abs/2606.03892) | Abdelaziz et al. (IBM) | 2026-06-02

PROVE trains LLMs for multi-step tool orchestration using RL against 20 stateful MCP servers (343 tools total). The key contribution is the data pipeline: it generates validated multi-turn tool-call trajectories grounded in live server state, so every query references entities that actually exist. A compact programmatic reward (validity scoring + dependency-aware coverage + efficiency penalty) replaces expensive judge models. Four models trained with GRPO on only 13K examples gain up to +10.2 points on BFCL Multi-Turn, +6.8 on tau2-bench, and +6.5 on T-Eval.

**How this builds on what you know:** This extends the tool-use agent line from ToolkenGPT (Hao 2024) and the planning-decomposition line from ADaPT (Prasad 2023) and LATS (Zhou 2024) in Community 0 of your graph. Where those papers focused on how agents select and plan tool calls, PROVE solves the training data problem — generating realistic stateful trajectories — and shows that a simple programmatic reward outperforms judge-based RL for tool use. The cross_area_bridge from hao2024_toolkengpt to zhao2025_pyvision in your library already connects tool-use to agentic vision; PROVE pushes further into general-purpose tool orchestration.

### 2. HybridThinker: CoT Compression via Compressed Memory and Transient Thought Steps
**arxiv:** [2606.03768](https://arxiv.org/abs/2606.03768) | Liu, Zhao, Liu, Ruan et al. | 2026-06-02

HybridThinker compresses chain-of-thought traces by encoding completed reasoning steps into compact memory tokens while temporarily retaining the original steps for fine-grained detail access. A hybrid training scheme randomly masks some thought steps (forcing memory-token reliance) while keeping others visible, preventing the model from bypassing compression. Result: matches uncompressed baselines on four reasoning benchmarks, advancing CoT compression state-of-the-art by 5.8 accuracy points at comparable inference time.

**How this builds on what you know:** This directly addresses the efficiency problem that DeepSeek-R1 (your library) created — long reasoning traces are accurate but expensive. The memory-token idea has parallels to the compressed representations in your self-supervised learning work (Community 1): both involve learning a compact encoding that preserves task-relevant information. If reasoning models are deployed on clinical biosignal tasks, this compression approach becomes practical infrastructure.

### 3. QUBRIC: Co-Designing Queries and Rubrics for RL Beyond Verifiable Rewards
**arxiv:** [2606.03968](https://arxiv.org/abs/2606.03968) | Zhang, Feng, Zhang, Yang et al. | 2026-06-02

QUBRIC identifies a structural bottleneck in rubric-based RL: rubric quality depends on query structure. Open-ended queries yield vague rubrics; narrowing queries naively introduces fabricated references that no model can verify. QUBRIC rewrites open-ended queries into scenario-based evaluable questions using teacher-derived key points, generates contrastive rubrics from teacher-policy gaps, and filters for learnability before GRPO training. Achieves +5.5 on ArenaHard over SFT baseline, and transfers to legal, moral, and narrative reasoning (+6.3 average) — trained only on instruction-following data.

**How this builds on what you know:** DeepSeek-R1 showed RL works for reasoning when rewards are verifiable (math, code). QUBRIC extends this to tasks without ground-truth answers by co-designing the query and rubric. This is relevant to your research because most scientific reasoning tasks (literature synthesis, experimental interpretation, clinical decision-making) lack verifiable rewards. QUBRIC provides a concrete mechanism for RL training on such open-ended domains.

---

## Tier C — Scan Headlines

1. **Knowledge Editing in Masked Diffusion Language Models** — Causal tracing + editing transferred from autoregressive to masked diffusion LMs (LLaDA, Dream); multi-token edits fail in MDMs due to partially unmasked intermediate states. [2606.03924](https://arxiv.org/abs/2606.03924)

2. **Expert-Aware Causal Tracing in Sparse MoE LMs** — Extends causal tracing to identify which routed experts mediate factual recall in MoE models like Qwen3-30B. [2606.03780](https://arxiv.org/abs/2606.03780)

3. **Consistency Training Can Entrench Misalignment** — Tests 7 consistency methods on 108 model organisms; suppresses reward hacking but amplifies sycophancy. [2606.03810](https://arxiv.org/abs/2606.03810)

4. **Entropy Gate: Near-Lossless Token Compression** — Thermodynamic-inspired token filtering achieving 40-60% compression at semantic fidelity > 0.80. [2606.03739](https://arxiv.org/abs/2606.03739)

5. **Clustered Self-Assessment for LLM Uncertainty Quantification** — Groups sampled generations into semantic clusters, converts to multiple-choice, uses assigned probabilities as confidence. Works with 2 samples. [2606.03846](https://arxiv.org/abs/2606.03846)

6. **EMBER: Robust Knowledge Erasure via Embedding Editing** — Sparse matrix factorization to erase concept features from embeddings; reduces relearning by up to 50%. [2606.03695](https://arxiv.org/abs/2606.03695)

7. **MLEvolve: Self-Evolving Automated ML Algorithm Discovery** — LLM-based multi-agent framework with Progressive MCGS and Retrospective Memory for end-to-end ML algorithm search. [2606.06473](https://arxiv.org/abs/2606.06473)

8. **Hybrid Verified Decoding** — Learns to allocate verification in speculative decoding; 2.73x average speedup on agentic workflows, outperforms EAGLE3. [2606.01019](https://arxiv.org/abs/2606.01019)

---

## Time-Series / Bio-Sensing Gap Watch

**Already ported (closed off):**

The Biosignal Fingerprinting paper (2605.09579) applied masked autoencoders from CV to paired PPG/ECG, achieving AUROC 0.974 for CVD classification. This extends the line from MAE Theory (Zhang 2023) and Foundation Models for Biosignals (Gu 2025) in your library (Communities 1 and 4). The MAE-to-biosignal transfer is now well-explored.

**Unported opportunities:**

1. **ACTS-style budget-aware reasoning for sensor data agents.** ACTS (Tier A) trains a controller to manage reasoning budget in an MDP framework. TS-Agent (Liu 2025) in your library performs multi-step reasoning over time series but has no budget control mechanism. Transfer hypothesis: a small controller trained to manage when a sensor-data agent should stop analyzing and commit to a classification could reduce inference cost for on-device clinical applications. The wearable_health_sensing hyperedge in your graph (yuan2024_ssl_har, xu2023_globem, nepal2024_mindscape, gu2025_biosignals) represents the deployment setting where this would matter.

2. **PROVE-style programmatic rewards for biosignal tool agents.** PROVE builds stateful MCP environments for RL training of tool-using agents. A parallel construction for biosignal analysis — where the "tools" are signal processing functions (filtering, peak detection, spectral analysis) and the "state" is an evolving clinical interpretation — has not been attempted. This would connect the ts_llm_reasoning_pipeline hyperedge (Community 4) with the llm_agent_frameworks hyperedge (Community 0).

---

## News

1. **Microsoft released MAI-Thinking-1 and MAI-Code-1-Flash at Build 2026** (June 2). MAI-Thinking-1 is a 35B-active-parameter reasoning model trained from scratch without OpenAI data. Claims to match Claude Opus 4.6 on SWE-bench Pro. MAI-Code-1-Flash is a 5B coding model rolling out to GitHub Copilot tiers.

2. **Google released Gemma 4 12B** (June 3). Open-source, encoder-free multimodal model (text + image + audio + video) with 256K context. Runs on 16GB VRAM laptops. Apache 2.0 license. AIME 2026: 77.5%, MMMU Pro: 69.1%.

3. **Anthropic Claude Opus 4.8** (May 28). Dynamic workflows, Super-Agent benchmark leader. $5/$25 per 1M input/output tokens. (Carried from previous digest for completeness.)

---

End of digest. Close this tab when done.
