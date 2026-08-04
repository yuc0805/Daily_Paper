## Reasoning in Language Models

### Timeline

2025 | CODI (Shen et al.) | 
2025 | Large Multimodal Reasoning Survey (Li et al.) | 
2025 | Latent Reasoning Survey (Zhu et al.) | 
2025 | Machine Mental Imagery (Yang et al.) | 
2025 | Soft Thinking (Zhang et al.) | 
2026 | Chain of Superposition (Deng et al.) | 
2026 | CoLaR (Tan et al.) | 
2026 | Latent Space Survey (Yu et al.) | 
2026 | Latent-GRPO (Deng et al.) | 
2026 | PonderLM (Zeng et al.) | 

2026-05 | ScaleLogic (2605.06638) | RL training compute scales as a power law with reasoning depth; expressiveness sets the exponent
2026-05 | RL Unlocks Parametric Knowledge (2605.07153) | RL redistributes probability mass to surface latent facts
2026-05 | Sparse Policy Selection (2605.06241) | RL changes only 1 to 3 percent of tokens, at high-entropy points already in the base top-5
2026-05 | Reward-Function Search RL (2605.02073) | a frontier model searches the RL reward function instead of the policy for math reasoning
2026-06 | MemReread (2605.10268) | linear-cost long-context reasoning via a running memory plus on-demand rereading of source text
2026-06 | Agentic Transformers Search (2606.00183) | formal proof of RL-trained DFS with depth generalization
2026-06 | GRAIL (2606.04889) | token-wise saliency reweighting for RLVR advantage signals
2026-06 | E2H Reasoner (2506.06632) | curriculum RL from easy to hard enables reasoning in 1.5B-3B models
2026-06 | GURU (2506.14965) | 92K cross-domain RL corpus; transfer works for pretrained domains, fails for underrepresented ones
2026-06 | ACTS (2606.03965) | MDP controller steers frozen reasoner with budget-aware inference
2026-06 | HybridThinker (2606.03768) | CoT compression via memory tokens plus transient thought steps
2026-06 | QUBRIC (2606.03968) | co-designed queries and rubrics extend RL beyond verifiable rewards
2026-06 | NF-CoT (2606.06447) | normalizing flow head replaces explicit CoT with compact latent thought states
2026-06 | PauseRec (2606.14142) | implicit pause-step reasoning for LLM generative recommendation; cheaper than explicit CoT
2026-06 | RLVR Correct Reasoning (2506.14245) | CoT-Pass@K scores intermediate-step correctness, not only the final answer; RLVR extends the reasoning boundary
2026-06 | Agentic Reasoning (2601.12538) | reasoning framed as a plan-act-observe-revise loop rather than one chain of thought
2026-07 | Tandem RL (2606.28166) | strong senior co-generates with a frozen weak junior so the reasoning trace stays legible and transferable
2026-07 | MentalThink (2607.03530) | a multimodal model reasons by writing, rendering, and revising executable SVG sketches, trained with multi-turn reinforcement learning
2026-07 | TREK (2607.05339) | distills verified off-support solutions into the student with a short forward-KL phase, then returns to on-policy reinforcement learning to fix a GRPO exploration stall
2026-07 | Pretraining-to-RL Reasoning (2607.16097) | pretraining loss predicts post-RL reward; pretraining tokens set the RL reward slope
2026-07 | GEPO (2607.16850) | per-group entropy shaping of GRPO advantages so mixed-difficulty prompts get matched exploration pressure
2026-07 | Stale but Stable (2607.18722) | staleness-adaptive trust region tightens only the sign-selected PPO clip endpoint on high-mismatch tokens so asynchronous reinforcement learning holds accuracy as rollout lag grows
2026-07 | Predictive Divergence Masks (2607.10848) | replaces PPO's ratio-based direction test with a predicted change in the trust-region divergence, in closed form for softmax policies
2026-07 | AREX (2607.21461) | deep-research agent that alternates evidence-gathering with constraint-by-constraint audit and re-planning, exploiting a discovery-verification asymmetry
2026-07 | Skill Self-Play (2607.22529) | proposer-solver-controller RL loop that co-evolves an agent skill library as a self-generated curriculum
2026-07 | DecoEvo (2607.25675) | co-evolves a solver skill and its grading rubric in text space, training each from a separate signal to limit reward hacking
2026-08 | CAST (2607.25308) | adds dense per-turn credit to RLVR for game-playing language agents using a game solver's value changes as per-step advantages
2026-08 | CoRT (2607.25659) | token-level credit for rubric-conditioned GRPO from rubric-versus-criteria-free log-likelihood contrasts

### Paper List

[KNOWN] [2025] Shen et al. — CODI. zotero_key:FFWLYL3J.
[KNOWN] [2025] Li et al. — Large Multimodal Reasoning Survey. zotero_key:FPEC4PIH.
[KNOWN] [2025] Zhu et al. — Latent Reasoning Survey. zotero_key:EMXEJYHV.
[KNOWN] [2025] Yang et al. — Machine Mental Imagery. zotero_key:PDAMP7VF.
[KNOWN] [2025] Zhang et al. — Soft Thinking. zotero_key:EGRXFZU9.
[KNOWN] [2026] Deng et al. — Chain of Superposition. zotero_key:CXGMDHJ3.
[KNOWN] [2026] Tan et al. — CoLaR. zotero_key:Y4ZNT3EC.
[KNOWN] [2026] Yu et al. — Latent Space Survey. zotero_key:KRVDKDGH.
[KNOWN] [2026] Deng et al. — Latent-GRPO. zotero_key:U4ZPM5DN.
[KNOWN] [2026] Zeng et al. — PonderLM. zotero_key:3TLRP8U5.

[2026] 2605.06638 — Can RL Teach Long-Horizon Reasoning to LLMs? Expressiveness Is Key. [https://arxiv.org/abs/2605.06638](https://arxiv.org/abs/2605.06638). external.
[2026] 2605.07153 — Beyond Reasoning: Reinforcement Learning Unlocks Parametric Knowledge in LLMs. [https://arxiv.org/abs/2605.07153](https://arxiv.org/abs/2605.07153). external.
[2026] 2605.06241 — Rethinking RL for LLM Reasoning: It is Sparse Policy Selection, Not Capability Learning. [https://arxiv.org/abs/2605.06241](https://arxiv.org/abs/2605.06241). external.
[2026] 2605.02073 — Enhanced LLM Reasoning by Optimizing Reward Functions with Search-Driven Reinforcement Learning. [https://arxiv.org/abs/2605.02073](https://arxiv.org/abs/2605.02073). external.
[2026] 2605.10268 — MemReread: Enhancing Agentic Long-Context Reasoning via Memory-Guided Rereading. [https://arxiv.org/abs/2605.10268](https://arxiv.org/abs/2605.10268). external.
[2606] 2606.00183 — Agentic Transformers Provably Learn to Search via RL. [https://arxiv.org/abs/2606.00183](https://arxiv.org/abs/2606.00183). external.
[2606] 2606.04889 — GRAIL: Gradient-Reweighted Advantages for RL with Verifiable Rewards. [https://arxiv.org/abs/2606.04889](https://arxiv.org/abs/2606.04889). external.
[2026] 2506.06632 — E2H Reasoner: Curriculum RL from Easy to Hard Tasks. [https://arxiv.org/abs/2506.06632](https://arxiv.org/abs/2506.06632). external.
[2026] 2506.14965 — GURU: Revisiting RL for LLM Reasoning from A Cross-Domain Perspective. [https://arxiv.org/abs/2506.14965](https://arxiv.org/abs/2506.14965). external.
[2026] 2606.03965 — ACTS: Agentic Chain-of-Thought Steering for Efficient and Controllable LLM Reasoning. [https://arxiv.org/abs/2606.03965](https://arxiv.org/abs/2606.03965). external.
[2026] 2606.03768 — HybridThinker: Efficient Chain-of-Thought Reasoning via Compressed Memory and Transient Thought Steps. [https://arxiv.org/abs/2606.03768](https://arxiv.org/abs/2606.03768). external.
[2026] 2606.03968 — QUBRIC: Co-Designing Queries and Rubrics for RL Beyond Verifiable Rewards. [https://arxiv.org/abs/2606.03968](https://arxiv.org/abs/2606.03968). external.
[2026] 2606.06447 — Latent Reasoning with Normalizing Flows (NF-CoT). [https://arxiv.org/abs/2606.06447](https://arxiv.org/abs/2606.06447). external.
[2026] 2606.14142 — PauseRec: Implicit Reasoning for LLM-based Generative Recommendation. [https://arxiv.org/abs/2606.14142](https://arxiv.org/abs/2606.14142). external.

[2026] 2506.14245 — Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs. [https://arxiv.org/abs/2506.14245](https://arxiv.org/abs/2506.14245). external.

[2026] 2601.12538 — Agentic Reasoning for Large Language Models. [https://arxiv.org/abs/2601.12538](https://arxiv.org/abs/2601.12538). external.

[2026] 2606.28166 — Tandem Reinforcement Learning with Verifiable Rewards. [https://arxiv.org/abs/2606.28166](https://arxiv.org/abs/2606.28166). external.

[2026] 2607.03530 — MentalThink: Shaping Thoughts in Mental SVG World. [https://arxiv.org/abs/2607.03530](https://arxiv.org/abs/2607.03530). external.
[2026] 2607.05339 — TREK: Distill to Explore, Reinforce to Refine. [https://arxiv.org/abs/2607.05339](https://arxiv.org/abs/2607.05339). external.
[2026] 2607.16097 — Understanding Reasoning from Pretraining to Post-Training. [https://arxiv.org/abs/2607.16097](https://arxiv.org/abs/2607.16097). external.
[2026] 2607.16850 — Group Entropy-Controlled Policy Optimization (GEPO). [https://arxiv.org/abs/2607.16850](https://arxiv.org/abs/2607.16850). external.

[2026] 2607.18722 — Stale but Stable: Staleness-Adaptive Trust Regions for Stabilizing Asynchronous Reinforcement Learning. [https://arxiv.org/abs/2607.18722](https://arxiv.org/abs/2607.18722). external.

[2026] 2607.10848 — Predictive Divergence Masks for LLM RL. [https://arxiv.org/abs/2607.10848](https://arxiv.org/abs/2607.10848). external.

[2026] 2607.21461 — AREX: Towards a Recursively Self-Improving Agent for Deep Research. [https://arxiv.org/abs/2607.21461](https://arxiv.org/abs/2607.21461). external.
[2026] 2607.22529 — Skill Self-Play: Pushing the Frontier of LLM Capability with Co-Evolving Skills. [https://arxiv.org/abs/2607.22529](https://arxiv.org/abs/2607.22529). external.
[2026] 2607.25675 — DecoEvo: Score-Decoupled Co-Evolution of Solver and Rubric-Generator Skills in Text Space. [https://arxiv.org/abs/2607.25675](https://arxiv.org/abs/2607.25675). external.

[2026] 2607.25308 — CAST: Game Solvers as Turn-Level Teachers for LLM Agents. [https://arxiv.org/abs/2607.25308](https://arxiv.org/abs/2607.25308). external.

[2026] 2607.25659 — CoRT: Counterfactual Replay for Token-Level Rubric-Guided Policy Optimization. [https://arxiv.org/abs/2607.25659](https://arxiv.org/abs/2607.25659). external.

### Recent Activity

2026-08-03 | 2607.25659 added | CoRT rescores the same sampled response twice, once under the rubric-conditioned prompt and once under a matched criteria-free prompt, and uses the token-by-token log-likelihood difference as a proxy for how much each token depends on the rubric, mapping those differences to bounded response-normalized weights that redistribute the GRPO advantage across tokens with no auxiliary scoring model and no change to the response-level reward; it improves over matched response-level GRPO by 4.4 percentage points on average; Tier B

2026-08-02 | 2607.25308 added | CAST adds dense turn-level credit to reinforcement learning from verifiable rewards for long-horizon game agents, using a game solver's state-value estimate so that a rise in the solver's value after an action marks that action as progress; under a soft-optimal solver assumption, maximizing the solver advantage equals on-policy distillation from the solver using only scalar values rather than teacher logits; Tier B

2026-07-30 | 2607.25675 added | DecoEvo improves a language model on open-ended tasks by editing external natural-language artifacts, a solver skill and the rubric that grades it, rather than model weights; it separates the two update signals so the solver learns from criterion-level feedback while the rubric generator is revised through audits of requirement coverage and answer discrimination that do not use the solver's aggregate score, reporting 2.8 to 5.0 percent relative gains over SkillOpt across five benchmarks and three backbones; Tier B

2026-07-27 | 2607.22529 added | trains a language model through self-play with agent skills as the unit of practice, running a proposer that writes tasks conditioned on a sampled skill, a solver that answers them, and a skill controller that reads execution feedback and grows a skill library, so the training distribution moves with the model while each skill keeps verification local; it raises the ceiling of strong backbones and recovers misaligned models on tool-use and reasoning benchmarks; Tier B

2026-07-25 | 2607.21461 added | AREX builds deep-research agents on a discovery-verification asymmetry, alternating an inner loop that gathers evidence and drafts a provisional answer with an outer loop that audits the draft constraint by constraint and launches targeted follow-up research; it learns a context-update tool that compresses history into verified evidence and open constraints, ships as a 4B dense model and a 122B-A10B mixture-of-experts model, and outperforms comparable-scale baselines on BrowseComp, WideSearch, DeepSearchQA, and Humanity's Last Exam; Tier B
