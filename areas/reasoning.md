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

### Recent Activity

2026-07-21 | 2607.16850 added | GEPO extends GRPO by estimating per-group entropy from the grouped rollouts already drawn and shaping advantages asymmetrically: it damps positive advantages in low-entropy groups to reduce over-exploitation and damps negative advantages in high-entropy groups to keep exploration, at little added cost because the entropy estimate reuses samples already taken; Tier B
2026-07-20 | 2607.16097 added | uses chess as a closed testbed with an exact reward to separate the contribution of pretraining from the contribution of RL; post-RL performance at a fixed RL compute is predicted by pretraining loss, the RL reward slope rises about linearly with pretraining tokens, and RL surfaces correct hard-puzzle moves that were nearly absent before rather than only sharpening the fine-tuned policy; the pattern reproduces on a 1B model trained on mathematics text; Tier A
2026-07-13 | 2607.03530 added | the model externalizes each reasoning step as executable SVG that it renders and inspects, then rewards good revision of the drawing through multi-turn reinforcement learning; reports 55.1% on VSIBench and 76.0% on MindCube; Tier A
2026-07-13 | 2607.05339 added | on near-zero-pass-rate prompts it pulls verified teacher solutions into the student's range with a short forward-KL phase before resuming on-policy reinforcement learning; Qwen3-8B rises on AIME 2025 (36.9 to 40.3) and ALFWorld (75.8 to 82.8); Tier B
2026-07-01 | 2606.28166 added | a trained strong senior and a frozen weak junior alternate to co-generate each reasoning rollout under a verifiable reward; the senior keeps solo accuracy while its chain of thought stays legible to the junior; Tier B
