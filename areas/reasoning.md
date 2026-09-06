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
2026-08 | CaRL / Knowing When to Quit (2607.29211) | capability-aligned RL that shapes rewards so refusal scores above futile reasoning, with hindsight refusal augmentation built from observed failures
2026-08 | ES for LLM Reasoning (2608.27351) | evolution strategies raise Pass@K by keeping population diversity where GRPO collapses entropy
2026-08 | J-Zero (2608.26582) | a Judge co-evolves with the Challenger-Solver pair, trained on preference pairs whose ordering comes from how each response was produced, extending self-evolution to unverifiable domains
2026-09 | OPSA / Does On-Policy Distillation Really Distill? (2608.31046) | teacher token-level scores are largely noise; entropy-adaptive negative advantages with no teacher beat on-policy distillation

2026-09 | Cliff (2609.02817) | a teacher marks the first reasoning error; positive token advantage before it, negative after, beating GRPO by 7 percent

2026-09 | One Training Example OPD (2609.04172) | one query recovers most of full-data on-policy distillation; state coverage is the instrument that explains why

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

[2026] 2607.29211 — Knowing When to Quit: Diagnosing and Training LLMs to Abort Futile Reasoning. [https://arxiv.org/abs/2607.29211](https://arxiv.org/abs/2607.29211). external.
[2026] 2608.27351 — Understanding Evolution Strategies for LLM Reasoning: Broader Reasoning Coverage than GRPO. [https://arxiv.org/abs/2608.27351](https://arxiv.org/abs/2608.27351). external.
[2026] 2608.26582 — J-Zero: Unified Challenger--Solver--Judge Co-Evolution from Zero Data. [https://arxiv.org/abs/2608.26582](https://arxiv.org/abs/2608.26582). external.
[2026] 2608.31046 — Does On-Policy Distillation Really Distill? From Noisy Teacher to Self-Improvement. [https://arxiv.org/abs/2608.31046](https://arxiv.org/abs/2608.31046). external.

[2026] 2609.02817 — Cliff: Learning Process Rewards from the First Mistake. [https://arxiv.org/abs/2609.02817](https://arxiv.org/abs/2609.02817). external.

[2026] 2609.04172 — Rethinking On-Policy Distillation of Large Language Models II: One Training Example. [https://arxiv.org/abs/2609.04172](https://arxiv.org/abs/2609.04172). external.

### Recent Activity

2026-09-05 | 2609.04172 added | this paper trains on-policy distillation at the data-minimal limit, a single query, and finds that one-shot OPD keeps improving for hundreds of steps and recovers most of full-data OPD's gain across task domains and model families; the explanation offered is state coverage, the fraction of states full-data OPD visits that a query set's rollouts reach, where one query already reaches 71.5 percent, most of it within the first 100 steps, and 16 semantically distinct queries reach 98.9 percent and match full-data training, while alignment slows at a similar rate whether the run trains on one query or the whole dataset, so the method is data-overfed and algorithm-starved, and content-light templates and off-domain WildChat queries also approach the real-query baseline, which separates task content from induced state coverage; where Does On-Policy Distillation Really Distill? (2608.31046) removed the teacher and kept the data, this paper keeps the teacher and removes the data, and both recover most of the gain, so read together they place the remaining contribution of on-policy distillation in the student's own rollout distribution and in the slow rate at which the student absorbs a fixed set of states rather than in the teacher's per-token scores or in dataset scale, where Cliff (2609.02817) accepted the teacher and improved the placement of the signal by splitting each rollout at the first error, this paper removes the data instead, so the three now bracket on-policy distillation from the data side, the supervision side and the credit-assignment side, and DeepSeek-R1 (deepseek2025_r1) supplies the reinforcement-learning-with-verifiable-rewards regime that on-policy distillation is measured against; the state-coverage measurement is the new instrument and the reusable part, since it is a general way to ask whether a training set adds anything beyond the states the model would have visited anyway, which applies to any small-data domain including health time series where labelled data is the binding constraint, and this is the second paper in a week to find that a headline mechanism is not carrying the reported gain; Tier B

2026-09-04 | 2609.02817 added | Cliff is a reward-shaping rule for reinforcement learning with verifiable rewards in which an off-the-shelf language model acting as teacher reads each rollout and marks the position of the first reasoning error, and that single index splits the rollout into a correct prefix and an incorrect suffix, with positive token-level advantage assigned to the prefix and negative advantage after the break; across 12 scenarios it beats on-policy distillation by 15 percent and standard GRPO by 7 percent, and the gain holds with teachers of modest capability; where DeepSeek-R1 (Z5IWHZAE) gave one scalar per rollout and let the optimiser spread that credit over every token, Cliff spends one teacher call to locate the single point where the trace goes wrong, on the argument that everything after the first error is conditioned on an invalid prefix and therefore carries almost no additional information, where Chain-of-Thought Prompting (HBLPTRMY) established the reasoning trace as an object with internal structure, Cliff uses that structure to make per-token credit assignment meaningful, and where Does On-Policy Distillation Really Distill? (2608.31046) asked how much signal the teacher actually supplies, Cliff answers by reducing the teacher's job to the smallest useful output, an index rather than a shared reasoning pattern, which is why a weak teacher still works; the assumption the method rests on, that error is absorbing so post-error tokens are uninformative, is a property of sequential decision processes rather than of language, and it transfers to any agent whose trace is a sequence of steps that can each be checked against evidence, including time-series reasoning agents, where the first operator call whose numeric claim is not supported by the evidence log is exactly a first-mistake index; no one has done this in the time-series or bio-sensing setting; Tier B

2026-09-01 | 2608.31046 added | audits on-policy distillation by measuring supervision quality during training, finding substantial noise in the teacher's per-token scores that grows as the teacher gets larger, that removing the noisy supervision leaves student performance essentially unchanged, and that replacing the teacher's per-token advantages with a single fixed negative advantage matches full on-policy distillation; from that it builds On-Policy Self-Adaptation, which uses entropy-adaptive negative advantages and no teacher at all, raising Avg@32 on AIME24 by 35.41 points over base Qwen3-1.7B and beating on-policy distillation by 16.77 points; where DeepSeek-R1 (Z5IWHZAE) accepted sparse outcome-level advantages as the price of avoiding a teacher and on-policy distillation was proposed as the dense alternative that buys token-level signal from a stronger model, this paper shows the dense signal is largely uninformative and that what drives improvement is a policy-internal quantity, the suppression of low log-probability tokens the student can identify from its own entropy, so the distinction is teacher-versus-self rather than sparse-versus-dense; Chain-of-Thought (HBLPTRMY) fixed the intermediate token sequence as the object on-policy distillation claims to transfer, and DeepSeek-V3 (2JCKA7GI) supplies the large-teacher regime whose scale makes the supervision noisier rather than cleaner; the portable part is the negative control, replacing a teacher's signal with a constant or a self-computed statistic to test whether the teacher carries information, which applies directly to distilling physiological foundation models into small on-device students where the teacher's value is rarely isolated; Tier A

2026-08-31 | 2608.26582 added | extends self-evolving language model training past the verifiable domains where a checker exists, keeping the Challenger-Solver adversarial pair and adding a Judge that co-adapts alongside them, trained on preference pairs whose ordering is fixed by how each response was produced rather than by any model score: the Solver's answer is taken as better than the Challenger's, and a decomposed-then-recombined answer as better than a one-shot answer, so the label is known before either response is read and the Judge neither freezes nor drifts on its own opinions; where DeepSeek-R1 obtained reasoning gains by reinforcement learning against a verifier and therefore stopped wherever no verifier exists, this paper substitutes a trained Judge for the verifier, and where Chain-of-Thought used decomposition to improve a single answer at inference time, J-Zero turns decomposition into a source of free preference labels; reported gains are 4.2 points on average in verifiable domains and 8.0 in unverifiable ones, with improvement continuing through at least ten iterations where baselines degrade after two, which is the claim to check first; Tier B

2026-08-29 | 2608.27351 added | the paper studies evolution strategies as a post-training method for reasoning rather than as a memory-saving substitute for gradient-based reinforcement learning, showing theoretically that verifier-projected Jensen-Shannon diversity across the population raises Pass@K and empirically that evolution strategies improve Pass@1 while avoiding the entropy collapse group relative policy optimisation exhibits, and reporting that although the model drifts substantially in parameter space the task gains come from a sparse subset of large-magnitude updates with no catastrophic forgetting on held-out evaluation; where DeepSeek-R1 and its descendants estimate a gradient from token-level log-probability ratios within a group of rollouts, evolution strategies perturb parameters directly and never form that gradient, so the mechanism that concentrates a GRPO policy onto a single solution path has no analogue; a sequential GRPO-then-ES schedule combines the Pass@1 strength of one with the Pass@K strength of the other, which is the setting that matters wherever a verifier or a human reviews several candidates; Tier B
