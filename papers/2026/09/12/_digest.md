# AI Digest — 2026-09-12

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A not done by 6 AM, stop.

Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.

Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

---

## Tier A — deep read

### Gradients Know What Outcomes Don't: Unlocking Reinforcement Learning for LLM Reasoning with Gradient-Aligned Rewards
Zheng, Su, Niu, Wang, Wang, Zhang, Yan, Wu, Kang, Fu, Zhang · arXiv:2609.03342 · https://arxiv.org/abs/2609.03342

**Problem.** Reinforcement learning from verifiable rewards gives one bit per rollout: correct or not correct. Among the rollouts that reach the right answer the reward is flat, so the policy receives no gradient separating a clean derivation from a lucky guess that happened to land. The existing dense alternatives are unattractive for different reasons. Surface heuristics such as length or formatting penalties do not measure reasoning. Process reward models do measure reasoning, but they require step-level annotation that has to be bought, and they add a second model to the training loop. Meanwhile the training corpora already contain written-out expert solutions that neither approach uses.

**Method.** Gradient-Aligned Reward turns each expert solution into an anchor gradient, then scores a rollout by how closely the rollout's own gradient points in the same direction. The trick that makes this affordable is truncation: backpropagation runs only through the output projection layer, which yields a compact gradient vector per rollout rather than a full model-sized one. The reward is the cosine similarity between the rollout vector and the expert-anchor vector, and it is dense because every rollout gets a real number rather than a bit. The authors prove that this cosine decomposes multiplicatively into a prediction-error factor and an activation-pattern factor, so the signal can be read as how wrong the token predictions were, multiplied by how similarly the network was engaged while producing them. That decomposition is the part worth reading closely, because it tells you what the reward is actually rewarding.

**Result.** Wall-clock overhead is under 9 percent relative to the base reinforcement learning loop. On Qwen3-4B and Qwen3-8B, the method improves over GRPO and over the other dense-reward baselines on competition-level mathematics benchmarks. The gains transfer to GPQA Diamond and to MMLU-Pro with no domain-specific reward data added, which is the result that matters most: the anchor gradients were built from mathematics solutions and the benefit still appeared on science and general-knowledge reasoning. Code and data are released at https://github.com/LQgdwind/GAR.

**Limitations.** The reward is only as good as the expert anchor, so the method needs a corpus with written-out solutions. That condition holds for olympiad mathematics and holds poorly for most applied domains. The evaluation stops at 8B parameters, and the paper does not test whether the gradient cosine stays informative once the policy is already close to the expert, which is exactly the regime where a dense reward would be most useful. The theoretical contribution characterizes what the cosine measures but does not bound the policy improvement that follows from optimizing it. Finally, a single expert anchor per problem imposes one solution path; problems with several valid approaches may be penalized for taking the unanchored one.

**Why it matters to you.** This is the cheapest dense-reward construction published so far, and the cost structure is what makes it portable. You do not need a reward model, you do not need step labels, and you do not need more than 9 percent extra compute. If you have paired signal and expert interpretation — an ECG trace with a cardiologist's written reading, an accelerometer window with a labelled activity rationale, a sleep record with a scored report — you can build anchor gradients directly from the expert text. That makes this the most plausible route to dense rewards for time-series reasoning models, which currently train against forecast error or against a binary classification hit.

**How this builds on what you know:** DeepSeek-R1 [Z5IWHZAE, graphify `deepseek2025_r1`, Community 0 "LLM Agents and Reasoning"] established that a binary verifiable reward is enough to train long chain-of-thought behaviour at scale, and it is your anchor paper for reasoning-via-reinforcement-learning. Latent-GRPO [U4ZPM5DN, reasoning area] is the GRPO family member in your library that this paper is measured against. Where DeepSeek-R1 accepted a flat reward across all correct trajectories and absorbed the cost in long, noisy traces, this paper keeps the same verifiable setup but adds an ordering *within* the correct set, taken from the policy's own gradients, because the gradient direction already carries the trajectory-quality information that the outcome bit discards. This also extends the graphify cross-area bridge `deepseek2025_r1` to `wei2023_cot`, which already crossed reasoning-via-reinforcement-learning and reasoning-via-prompting in your library. The new work pushes that bridge further into supervision derived from expert text that is already sitting in the corpus, rather than from prompt engineering on one side or outcome checking on the other.

---

## Tier B — TLDR

### An Open Recipe for IMO Gold: Training Nemotron for Olympiad Mathematics
Moshkov, Ge, Armstrong, Du, Mahdavi, Gitman (NVIDIA) · arXiv:2609.10712 · https://arxiv.org/abs/2609.10712

Starting from Nemotron 3 Ultra, the authors train two specialist checkpoints by supervised fine-tuning and by reinforcement learning, then assemble a test-time pipeline in which three checkpoints generate, verify, and refine natural-language proofs, with a separate high-compute stage selecting the final submission. The system uses no formal prover, no external tools, and no internet access, and it scored 30 out of 42 points at IMO 2026, above the gold-medal threshold. The release includes both post-trained checkpoints, the training data, the training and inference code, the submitted solutions, and Nemotron-IMO-Bench, a new set of 200 novel olympiad problems. The value here is not the medal but the ablation: the paper separates how much came from checkpoint choice, how much from verification, and how much from refinement, which is the decomposition anyone budgeting test-time compute needs.

**How this builds on what you know:** DeepSeek-R1 [Z5IWHZAE, graphify `deepseek2025_r1`, Community 0] showed that reinforcement learning on verifiable answers produces long reasoning traces, and SPRINT [BZKDNHD6, LLM area] showed that those traces can be restructured into planning rounds plus parallel execution to cut sequential tokens by up to 39 percent. Where DeepSeek-R1 put the compute into training a single policy and SPRINT put it into reorganizing one trajectory, this paper puts it into an outer loop over several specialist checkpoints, because verification and refinement turn out to buy more at fixed compute than a better single generator does. Read it against SPRINT specifically: both are test-time-compute papers, but SPRINT parallelizes within a trajectory while this one searches across trajectories, and the two are composable.

### SpatialBlock: Enhancing Spatial Intelligence in LVLMs via Synthetic Block-Stacking Problem
Ryu, Kim, Yang (KAIST AI) · arXiv:2609.07064 · https://arxiv.org/abs/2609.07064

Large vision-language models describe what a scene contains but reconstruct its 3D structure poorly, and the usual fix — real-scene spatial question answering with dense geometric annotation — is expensive and noisy because the labels come from external perception modules. This paper trains on block play instead: SpatialBlock-15k is 15,000 fully synthetic block-stacking problems covering 3D-to-2D projection, viewpoint transformation, and structural combination, with controlled colour modulation added so the model learns to anchor its reasoning on task-relevant blocks rather than on global appearance. Two training strategies are released, one predicting the answer directly and one reasoning before answering, and both transfer to real-scene spatial benchmarks despite the synthetic and compact training set. The interesting claim is the transfer itself: 15,000 synthetic items beat annotation-heavy real-scene supervision.

**How this builds on what you know:** BLIP-2 [4N5WXKPI, multi-modal area, graphify Community 3 "Vision-Language and Generative"] established the frozen-encoder plus query-transformer recipe that most current vision-language models still follow, and Machine Mental Imagery [PDAMP7VF / NSI6PVD7, reasoning and multi-modal areas] argued that these models need an internal visual scratchpad to reason about structure rather than appearance. Where BLIP-2 aligned an image encoder to a language model on captions and web pairs, and Machine Mental Imagery proposed changing the model's internal representation, this paper changes the *data*: a synthetic curriculum of controlled geometric transformations, on the argument that spatial skill is a learnable curriculum rather than an architectural property. The cheap-synthetic-curriculum result is the transferable part.

### EvoSafeHarness: Evolving Model- and Domain-Specific Harnesses for Securing Agents
Li, Ma, Cao, Suh, Li, Song, Xiao · arXiv:2609.05903 · https://arxiv.org/abs/2609.05903

Safety harnesses for tool-using agents are normally written once by experts and reused across models and domains, which fails in both directions: a harness strict enough for one model over-blocks another, and a policy written for a file system does not know what a wash trade is. This paper searches for the harness instead, jointly optimizing a natural-language policy and the executable code that enforces it on every tool call, with the model itself frozen and a fresh-context adversarial review step used to reject rules that only fit the benchmark. On DecodingTrust-Agent the average attack success rate falls from 45.6 percent to 10.0 percent at a cost of 3.3 utility points, and the method wins 14 of 15 cells. On AgentDojo it reaches 82.8 percent utility at 0.0 percent attack success, twice CaMeL's utility at the same operating point, and transfers unchanged to the unseen AgentDyn suites. Mean attack success stays below 20 percent under adaptive PAIR attacks at a refinement budget of 16.

**How this builds on what you know:** ToolkenGPT [6RDHVVA2, graphify `hao2024_toolkengpt`, Community 0] made tool invocation a learned token-level decision, and ADaPT [J8DYBKW2, graphify `prasad2023_adapt`, Community 0] made task decomposition adaptive to what the executor can actually do. Where those two papers made the agent's *capability* adaptive, this paper makes the agent's *constraint* adaptive, and it does so at the same granularity — the tool call — because the enforcement point has to sit where the effect is produced. This extends the graphify cross-area bridge `hao2024_toolkengpt` to `zhao2025_pyvision`, which already crossed learned tool invocation and agentic vision with dynamic tooling in your library; the new work pushes that bridge into the governance direction, adding a searched policy layer over the tool interface that both bridge endpoints assume is open.

---

## Tier C — scan only

| Paper | Hook |
| --- | --- |
| [TempCloze: Can Video-LLMs Identify the Missing Middle?](https://arxiv.org/abs/2609.01515) | Video cloze over 1,521 clips; temporal alignment, not semantics, is the bottleneck. |
| [Recursive Code World Models](https://arxiv.org/abs/2609.11499) | Builds complex worlds by recursively composing scene programs instead of one flat generator. |
| [World in World: Explore the World with World Models](https://arxiv.org/abs/2609.11548) | Evaluates world models by embodied exploration rather than by frame prediction error. |
| [Generative Late-Interaction Embeddings for Visual Document Retrieval](https://arxiv.org/abs/2609.11808) | Generative decoder produces multi-vector late-interaction embeddings for page retrieval. |
| [UniH^3: All-in-One Medical Image Restoration](https://arxiv.org/abs/2609.11156) | One model for heterogeneous medical degradations via hierarchical homogeneity sharing. |
| [MetroLLM-Bench: Language Models as Transit Kiosk Runtimes](https://arxiv.org/abs/2609.10016) | Benchmarks models as always-on kiosk runtimes, where latency and refusal both count. |
| [HyQuant: Hybrid-Precision Quantization for LLM Attention](https://arxiv.org/abs/2608.27875) | Mixes precision inside the attention block rather than across whole layers. |
| [DRG-MAPPO: Hierarchical Dynamic Role-Graph Multi-Agent RL](https://arxiv.org/abs/2609.11155) | Roles become a graph that rewires during the episode, applied to cooperative air combat. |

---

## Tier D — Time-series / bio-sensing gap watch

No time-series or bio-sensing paper qualified today, so both entries below are unported opportunities taken from the day's top computer-vision and language work. Nothing today matched the hyperedges of graphify Community 4 (Time Series and LLM Integration) or Community 5 (Wearable Sensing and Behavior), so nothing closed off.

**Unported opportunity 1 — gradient-aligned rewards for time-series reasoning.** The Tier A method builds a dense reward from expert solution text that already exists in the corpus. Nothing in Community 4 does this: TS-Agent [I2CIT4I7] and ChatTS train against forecast error or against a binary task hit, and no paper in your library derives a dense reward from clinician or annotator prose. Transfer hypothesis: take paired traces and written interpretations (ECG with a cardiologist's reading, accelerometer windows with scored activity rationales, polysomnography with a sleep report), build the anchor gradient from the interpretation text, and use the gradient cosine as the reward for a time-series reasoning policy — the annotation you would need is the clinical text you already have.

**Unported opportunity 2 — cloze-style benchmarks for physiological signals.** TempCloze removes the middle of a video and forces a model to pick the true continuation from same-source distractors built along three axes: what should happen, when it should happen, and how it should unfold. No equivalent exists for biosignals; the Community 5 datasets in your library (GLOBEM, the wearable sensing line) evaluate by downstream label accuracy, which a model can reach by memorizing subject-level priors. Transfer hypothesis: build a signal-cloze benchmark where the model selects the true missing segment of an ECG, PPG, or accelerometer trace from same-subject distractors that are semantically plausible but temporally misaligned. Because the distractors come from the same subject, subject-level shortcuts are removed, and the separate axes would tell you whether a biosignal foundation model has learned event timing or only event identity. TempCloze's finding that alignment is the bottleneck for video suggests the same diagnosis is waiting for physiological models.

---

## News

Two releases from the past 48 hours. Sakana AI shipped Fugu Ultra v2.0 and Fugu Max on 11 September, and DeepSeek released V4.1 Flash on 10 September. On the tooling side, OpenAI's Agents API entered public beta with United States data residency but no Zero Data Retention support, which is the detail to check before routing anything sensitive through it. Nothing was announced on 12 September at the time of writing.

---

End of digest. Close this tab when done.
