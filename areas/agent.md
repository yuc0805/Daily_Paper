## LLM-based Agents

### Timeline

2018 | Machine Theory of Mind (Rabinowitz et al.) | 
2023 | ADaPT (Prasad et al.) | 
2024 | Agent AI Survey (Durante et al.) | 
2024 | LATS (Zhou et al.) | 
2024 | ToolkenGPT (Hao et al.) | 
2025 | PyVision (Zhao et al.) | 
2026 | DeepEyesV2 (Hong et al.) | 
2026 | Memory Mechanisms Survey (Huang et al.) | 

2026-05 | RL for Multi-Agent Orchestration (2605.02801) | formalizes RL over orchestration traces for LLM multi-agent systems
2026-05 | Code as Agent Harness (2605.18747) | treats code as the harness that unifies tool use, memory, and execution-based verification
2026-05 | POLAR (2605.26256) | per-user semantic and episodic knowledge graph for long-term embodied agents
2026-06 | EvoMemBench (2605.18421) | benchmark for agent memory scored under self-evolving, cross-episode conditions
2026-06 | MemForest (2605.23986) | write-efficient temporal memory index for agents; 6x throughput over prior systems
2026-06 | QUEST (2605.24218) | open deep research agents trained with synthetic verifiable tasks; best open-weight agent
2026-06 | Agentic Transformers Search (2606.00183) | formal proof of RL-trained DFS with depth generalization
2026-06 | PROVE (2606.03892) | programmatic rewards for multi-step tool use via 20 stateful MCP servers
2026-06 | ExpWeaver (2606.01041) | latent-space experience retrieval via cross-attention for LLM agents
2026-06 | APB (2606.04874) | diagnostic benchmark separating planning sub-skills across 22 domains
2026-06 | Vivaldi (2603.04142) | multi-agent physiological time-series interpretation
2026-06 | MemoPilot (2606.08656) | plug-in memory copilot trained via multi-turn GRPO for agent test-time learning
2026-06 | LLM-as-an-Investigator (2606.13220) | evidence-first reasoning for robust interactive problem diagnosis
2026-06 | MemToolAgent (2606.07909) | memory loop records past tool-call outcomes and feedback to inform later tool choice
2026-06 | Infini Memory (2606.10677) | topic-structured, revisable memory documents for long-horizon agent memory
2026-06 | Information Self-Locking (2603.12109) | names and patches an exploration-collapse trap in reinforcement-learning training of question-asking agents
2026-06 | Agent Memory Systems (2606.06448) | systems-level cost and latency map of long-horizon agent memory patterns
2026-06 | ARLArena (2602.21534) | unified framework for stable agentic reinforcement learning; standardizes the environment, reward bookkeeping, and policy-update loop
2026-07 | AutoTrainess (2606.31551) | LLM agent for autonomous post-training; wraps the training pipeline as named agent-computer interfaces
2026-07 | AgenticSTS (2607.02255) | bounded-memory agent testbed with fixed-size prompts built by typed retrieval
2026-07 | SkillOpt-Lite (2607.03451) | reframes agent skill self-evolution as zeroth-order optimization over reusable skills and harness
2026-07 | TurnOPD (2607.05804) | turn-aware on-policy distillation budgets rollout depth and shifts KL weight toward deep decision turns
2026-07 | SIRI (2606.02355) | three-phase RL that mines reusable skills from its own successful rollouts and distills only useful skill tokens back, carrying nothing extra at inference
2026-07 | SEED (2607.14777) | self-evolving on-policy distillation turns an agent's own trajectories into hindsight skills and distills their effect into the policy
2026-07 | SearchOS-V1 (2607.15257) | externalizes search progress into shared Frontier Task, Evidence Graph, Coverage Map, and Failure Memory for multi-agent information seeking
2026-07 | Env-free Agent Data (2607.16900) | synthesizes API-calling training trajectories without a live environment, for the long tail of tools with no sandbox
2026-07 | AgentDebugX (2607.18754) | closed Detect-Attribute-Recover-Rerun loop for LLM agent failures with multi-turn root-cause diagnosis and a reusable failure-diagnosis-repair hub
2026-07 | AREX (2607.21461) | deep-research agent that alternates evidence-gathering with constraint-by-constraint audit and re-planning, exploiting a discovery-verification asymmetry
2026-07 | Agentic Context Management (2607.21503) | reframes agent memory as a lifecycle with five primitives and ties each context strategy to a token-cost curve
2026-08 | SkillRise (2607.26784) | RL agent alternates solving a task and curating an evolving skill document, with decoupled per-task and cross-task credit
2026-08 | Shadow Evaluations (2607.27191) | authors grade a frontier agent on the open research question of their own unpublished paper; engineering solved, research judgment not
2026-08 | LycheeMemory V2 (2608.12990) | consolidates agent memory at detected semantic segment boundaries instead of every turn, cutting construction tokens without raising query-time cost

2026-08 | Spatial Memory Agent (2608.12743) | training-free procedure memory whose lessons carry a reliability score updated from retrieval outcomes
2026-08 | ContextPilot (2608.28476) | context edits become trainable actions, with branch points chosen by entropy variation and advantages estimated per edit
2026-09 | CAST (2608.30147) | synthesised trajectory rationales train a critique model that supplies action-level supervision, scored by pass^4 rather than single-run success
2026-09 | DisCo / Repo-To-Skill (2609.02749) | distills repository operating procedure into verified skills; a 5,000-skill library lifts a fixed agent on four benchmarks
2026-09 | EarlyEval (2609.02783) | two calibrated classifiers halt evaluation runs whose outcome is already predictable, removing 13 to 26 percent of agent steps

### Paper List

[KNOWN] [2018] Rabinowitz et al. — Machine Theory of Mind. zotero_key:NEKX3K3N.
[KNOWN] [2023] Prasad et al. — ADaPT. zotero_key:J8DYBKW2.
[KNOWN] [2024] Durante et al. — Agent AI Survey. zotero_key:Z9WZPMNU.
[KNOWN] [2024] Zhou et al. — LATS. zotero_key:77ERE7HA.
[KNOWN] [2024] Hao et al. — ToolkenGPT. zotero_key:6RDHVVA2.
[KNOWN] [2025] Zhao et al. — PyVision. zotero_key:XQTY5MPI.
[KNOWN] [2026] Hong et al. — DeepEyesV2. zotero_key:4XXXYXS9.
[KNOWN] [2026] Huang et al. — Memory Mechanisms Survey. zotero_key:BDY3HUCV.

[2026] 2605.02801 — RL for LLM-based Multi-Agent Systems through Orchestration Traces. [https://arxiv.org/abs/2605.02801](https://arxiv.org/abs/2605.02801). external.
[2026] 2605.18747 — Code as Agent Harness. [https://arxiv.org/abs/2605.18747](https://arxiv.org/abs/2605.18747). external.
[2026] 2605.26256 — Personalizing Embodied Multimodal LLM Agents over Long-term User Interactions (POLAR). [https://arxiv.org/abs/2605.26256](https://arxiv.org/abs/2605.26256). external.
[2026] 2605.18421 — EvoMemBench: Benchmarking Agent Memory from a Self-Evolving Perspective. [https://arxiv.org/abs/2605.18421](https://arxiv.org/abs/2605.18421). external.
[2026] 2605.23986 — MemForest: An Efficient Agent Memory System with Hierarchical Temporal Indexing. [https://arxiv.org/abs/2605.23986](https://arxiv.org/abs/2605.23986). external.
[2026] 2605.24218 — QUEST: Training Frontier Deep Research Agents with Fully Synthetic Tasks. [https://arxiv.org/abs/2605.24218](https://arxiv.org/abs/2605.24218). external.
[2606] 2606.00183 — Agentic Transformers Provably Learn to Search via RL. [https://arxiv.org/abs/2606.00183](https://arxiv.org/abs/2606.00183). external.
[2026] 2606.03892 — PROVE: Programmatic Rewards On Verified Environments for Multi-Step Tool Use. [https://arxiv.org/abs/2606.03892](https://arxiv.org/abs/2606.03892). external.
[2026] 2606.01041 — ExpWeaver: LLM Agents Learn from Experience via Latent RAG. [https://arxiv.org/abs/2606.01041](https://arxiv.org/abs/2606.01041). external.

[2026] 2606.04874 — Agent Planning Benchmark: A Diagnostic Framework for Planning Capabilities in LLM Agents. [https://arxiv.org/abs/2606.04874](https://arxiv.org/abs/2606.04874). external.

[2026] 2603.04142 — Vivaldi: A Multi-Agent Framework for Interpreting Multivariate Physiological Time Series. [https://arxiv.org/abs/2603.04142](https://arxiv.org/abs/2603.04142). external.

[2026] 2606.08656 — MemoPilot: Enhancing Test-Time Learning of LLM Agents via RL over Memory. [https://arxiv.org/abs/2606.08656](https://arxiv.org/abs/2606.08656). external.

[2026] 2606.13220 — LLM-as-an-Investigator: Evidence-First Reasoning for Robust Interactive Problem Diagnosis. [https://arxiv.org/abs/2606.13220](https://arxiv.org/abs/2606.13220). external.

[2026] 2606.07909 — MemToolAgent: Leveraging Memory for Tool-Using Agents Based on Environment and User Feedback. [https://arxiv.org/abs/2606.07909](https://arxiv.org/abs/2606.07909). external.
[2026] 2606.10677 — Infini Memory: Maintainable Topic Documents for Long-Term LLM Agent Memory. [https://arxiv.org/abs/2606.10677](https://arxiv.org/abs/2606.10677). external.
[2026] 2603.12109 — On Information Self-Locking in Reinforcement Learning for Active Reasoning of LLM Agents. [https://arxiv.org/abs/2603.12109](https://arxiv.org/abs/2603.12109). external.
[2026] 2606.06448 — Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads. [https://arxiv.org/abs/2606.06448](https://arxiv.org/abs/2606.06448). external.

[2026] 2602.21534 — ARLArena: A Unified Framework for Stable Agentic Reinforcement Learning. [https://arxiv.org/abs/2602.21534](https://arxiv.org/abs/2602.21534). external.
[2026] 2606.31551 — AutoTrainess: Teaching Language Models to Improve Language Models Autonomously. [https://arxiv.org/abs/2606.31551](https://arxiv.org/abs/2606.31551). external.

[2026] 2607.02255 — AgenticSTS: A Bounded-Memory Testbed for Long-Horizon LLM Agents. [https://arxiv.org/abs/2607.02255](https://arxiv.org/abs/2607.02255). external.

[2026] 2607.03451 — SkillOpt-Lite: Agent Self-evolution via Zeroth-Order Optimization. [https://arxiv.org/abs/2607.03451](https://arxiv.org/abs/2607.03451). external.
[2026] 2607.05804 — TurnOPD: Making On-Policy Distillation Turn-Aware for Efficient Long-Horizon Agent Training. [https://arxiv.org/abs/2607.05804](https://arxiv.org/abs/2607.05804). external.
[2026] 2606.02355 — SIRI: Self-Internalizing Reinforcement Learning with Intrinsic Skills for LLM Agent Training. [https://arxiv.org/abs/2606.02355](https://arxiv.org/abs/2606.02355). external.
[2026] 2607.14777 — SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement Learning. [https://arxiv.org/abs/2607.14777](https://arxiv.org/abs/2607.14777). external.
[2026] 2607.15257 — SearchOS-V1: Towards Robust Open-Domain Information-Seeking Agent Collaboration. [https://arxiv.org/abs/2607.15257](https://arxiv.org/abs/2607.15257). external.
[2026] 2607.16900 — Environment-free Synthetic Data Generation for API-Calling Agents. [https://arxiv.org/abs/2607.16900](https://arxiv.org/abs/2607.16900). external.

[2026] 2607.18754 — AgentDebugX: An Open-Source Toolkit for Failure Observability, Attribution, and Recovery in LLM Agents. [https://arxiv.org/abs/2607.18754](https://arxiv.org/abs/2607.18754). external.

[2026] 2607.21461 — AREX: Towards a Recursively Self-Improving Agent for Deep Research. [https://arxiv.org/abs/2607.21461](https://arxiv.org/abs/2607.21461). external.
[2026] 2607.21503 — Agentic Context Management: Solving Agent Memory and Cost by Treating Them as Lifecycle and Architecture Problems. [https://arxiv.org/abs/2607.21503](https://arxiv.org/abs/2607.21503). external.

[2026] 2607.26784 — SkillRise: Agentic Reinforcement Learning for Cross-Task Skill Evolution. [https://arxiv.org/abs/2607.26784](https://arxiv.org/abs/2607.26784). external.
[2026] 2607.27191 — Can AI agents conduct open-ended AI research? Early evidence from two case studies. [https://arxiv.org/abs/2607.27191](https://arxiv.org/abs/2607.27191). external.

[2026] 2608.12990 — LycheeMemory V2: Efficient Long-Term Memory for LLM Agents via Semantic Segment-Level Consolidation. [https://arxiv.org/abs/2608.12990](https://arxiv.org/abs/2608.12990). external.

[2026] 2608.12743 — Spatial Memory Agent: Experience-Grounded Procedure Memory for Spatial Intelligence. [https://arxiv.org/abs/2608.12743](https://arxiv.org/abs/2608.12743). external.
[2026] 2608.28476 — ContextPilot: Teaching Agents for Proactive Context Management via Fine-grained RL. [https://arxiv.org/abs/2608.28476](https://arxiv.org/abs/2608.28476). external.
[2026] 2608.30147 — CAST: Critique-Aware Supervision for Training Reliable Long-Horizon Tool-Calling Agents. [https://arxiv.org/abs/2608.30147](https://arxiv.org/abs/2608.30147). external.

[2026] 2609.02749 — Repo-To-Skill / DisCo: Distilling GitHub Repositories Into AI4AI Skills. [https://arxiv.org/abs/2609.02749](https://arxiv.org/abs/2609.02749). external.
[2026] 2609.02783 — EarlyEval: Cheaper Agent Evaluation via Early Outcome Prediction. [https://arxiv.org/abs/2609.02783](https://arxiv.org/abs/2609.02783). external.

### Recent Activity

2026-09-03 | 2609.02749 added | DisCo names a missing layer in autonomous research agents, operational knowledge, the know-how that separates knowing a method from making it work, and distills it from repositories and papers into compact verified skills through a task-agnostic pass over widely used repositories and a task-oriented pass for a specific job; the task-agnostic pass over 1,000 repositories yields the AREX-Skill Library of more than 5,000 verified skills across 20 areas and 178 capability families, and with backbone, harness and execution budget held fixed the skill-equipped agent scores 134.3 percent higher on MLE-bench, 34.4 percent higher on PaperBench, 9.2 percent higher on FrontierCS and 14.0 percent higher on PassNet; where ToolkenGPT (6RDHVVA2) compressed a tool's interface into a learned token so the model could call it, DisCo compresses a repository's operating procedure so the model can configure it correctly, because the bottleneck attacked is not invocation but correct use, where Rethinking Memory Mechanisms of Foundation Agents (BDY3HUCV) treated memory as an episodic trace built during a run and therefore useful only after the agent has met a similar problem, DisCo builds a curated and verified library offline and shares it across tasks, which removes that dependency, and where the Agent AI Survey (Z9WZPMNU) placed know-how outside the architecture by assumption, this paper argues the harness is already complete and the missing piece is the content loaded into it, and supports that by varying only the skills; the work pushes the existing hao2024_toolkengpt to zhao2025_pyvision bridge from tool invocation toward tool operation, so the crossing now covers how a tool is used and not only that it is used; the transfer to bio-sensing is direct and unported, since filter cutoffs, artifact rejection thresholds, resampling conventions and normalization choices decide whether a physiological pipeline works and live in repository code rather than in method sections, and Community 5 contains no analogue; Tier B

2026-09-03 | 2609.02783 added | EarlyEval attacks the within-task axis of agent evaluation cost, which benchmark distillation leaves untouched because it reduces how many tasks are run without changing the price of each retained task, on the observation that an agent's final outcome is usually evident from its intermediate behavior well before the run completes; two LightGBM classifiers, one for success and one for failure, read behavioral, textual and reference-solution features at each step and halt the run when either crosses a calibrated confidence threshold, at negligible per-step overhead, and on SWE-bench Verified, TerminalBench and Toolathlon this removes 13 to 26 percent of agent steps and up to 44.1 percent of input tokens and 29.4 percent of output tokens at 89 to 97 percent prediction accuracy, while perturbing per-agent resolve rates by one to two percentage points on average; where Evaluating World Models (P92FLHJ2) asked whether an evaluation measures the capability it claims to measure, this paper accepts the measurement as correct and asks how much of each run can be discarded before the estimate degrades, which converts a validity question into a sequential-sampling question with an explicit accuracy-against-savings trade-off, and where the Agent AI Survey (Z9WZPMNU) catalogued agent capabilities without costing their measurement, this paper makes evaluation cost a first-class quantity and reports the exchange rate; the structural move matches the same day's Tier A paper on Declarative Attention, spending a cheap predictor to avoid a large amount of work, over trajectory steps here and over context positions there, and because the features are behavioral and textual rather than code-specific the method should carry to agent pipelines built over time-series operators; Tier B

2026-09-01 | 2608.30147 added | CAST converts sparse end-of-task outcomes into action-level supervision for long-horizon tool-calling agents by analysing trajectories and synthesising structured rationales that explain why a given action was valid or invalid under partial observability, training a critique model on those rationales and then using the critique model to generate training data for the policy; fine-tuned Qwen3-family models exceed GPT-OSS-120B by more than 10 percent pass^4 on Retail tasks and gain a further 9 percent on Telehealth, which is held out of domain; where LATS (77ERE7HA) caught a bad action by searching alternatives and scoring them at inference, which costs compute at every deployment and leaves the base policy unchanged, CAST moves that judgement into training, so the deployed agent is cheaper and the improvement transfers to a domain it was not trained on, and where ToolkenGPT (6RDHVVA2) made the tool call a token the model could emit, this work supplies the missing per-action credit signal given that the only ground truth available is whether the whole episode succeeded; Rethinking Memory Mechanisms of Foundation Agents (BDY3HUCV) frames what an agent must retain across a long trajectory to judge a current action; the evaluation matters as much as the method, since pass^4 scores success across four independent trials rather than one and therefore measures reliability rather than best-case capability, which is the right target for clinical decision-support agents where an occasional irreversible action is the binding constraint, and the Telehealth result is the closest an agent-reliability paper has come to the health setting; Tier B

2026-08-31 | 2608.28476 added | trains a language agent to edit its own working context during long-horizon tasks, widening the editing toolset past search, delete and summarize to include global planning, long-term memory writes and soft context offloading, and training those edits with reinforcement learning built for the credit-assignment problem: context and entropy variation locate the editing decisions that actually change the outcome, branch sampling is concentrated at those points, and advantages are estimated per action from all branched trajectories passing through an edit rather than from a single trajectory-level reward; where the Memory Mechanisms survey argued that agent memory should be designed rather than accumulated, this paper makes the memory operations themselves trainable actions with their own reward signal, where ToolkenGPT learned which external tool to call, this paper learns which internal edit to make to the context, and where LATS branched trajectories at inference time to search for a better answer, ContextPilot branches at training time and converts that tree into a variance-reduction device; the reported result is stronger long-context question answering and deep search with a smaller working context across several base models, with weights released as ContextPilot-8B and ContextPilot-14B; the selection of branch points by entropy variation has no parent in the library; Tier B

2026-08-16 | 2608.12743 added | SMA gives a frozen vision-language model spatial competence through a read-only procedure memory rather than parameter updates or inference-time depth and reconstruction tools: verifier-guided reflection in a checkable environment distils each episode into a short transferable lesson, and each lesson carries a Transfer Reliability Score recalibrated from whether later retrievals of it produced correct answers, so ranking combines embedding similarity with past reliability and a closely matching but unreliable lesson can be outranked; across five spatial benchmarks and four base vision-language models it holds the highest macro average in every base-model block and the best accuracy in most of the twenty evaluations, and no ablation separates the score from lesson distillation; Tier B
