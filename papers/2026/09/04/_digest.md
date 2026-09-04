# AI Digest — 2026-09-04

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A is not done by 6 AM, stop.

Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.

Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

Note on today's signal: the Hugging Face daily list had not rolled over at run time, so the candidate pool was the tail of the 3 September batch plus a targeted search of the health-sensing literature. That search turned up one paper that is more relevant to your primary area than anything in the trending list, so Tier A goes to it even though it was posted on 27 August. The three Tier B entries are papers from the 3 September batch that yesterday's digest did not feature.

---

## Tier A — deep read

### BALMS: Benchmarking Agentic LLMs for Longitudinal Mental Health Sensing
Wu, Pillai, Chen, Zhang, Regmi, Griffin, Heinz, Marsch, Jacobson, Campbell (Dartmouth). EMNLP 2026 Main. https://arxiv.org/abs/2608.27219

**Problem.** Mental health assessment runs on episodic self-report scales, which produce a number at sparse intervals. Wearables supply the continuous behavioural and physiological signal that would fill the gaps, and personal-health agents supply a natural-language interface over that signal. What those agents have been shown to do, though, is short-window retrieval: the highest step count in a week. Nobody had tested whether the same agent can reason over months of history to predict a wellbeing score and give a rationale that is grounded in the evidence rather than merely plausible.

**Method.** BALMS fixes three real-world longitudinal datasets and two task families, closed-form wellbeing-score prediction and rationale generation graded by an LLM judge, then varies three agentic paradigms across five open and closed backbones. Score prediction is compared against the per-subject mean, which is the baseline that matters because wellbeing scores are strongly autocorrelated within a person. Grading the number and the rationale separately is what makes the result legible: it separates failure to predict from failure to ground.

**Result.** Zero-shot agents rarely beat the mean baseline. They beat it only with the strongest backbones, or when the input is a compact set of semantically meaningful features rather than the raw stream. Chain-of-thought prompting improves reasoning-oriented backbones but does not produce temporal grounding or numerical correctness. The temporal-scaling analysis shows where the loss is: agents given more history do not retrieve from it selectively, so additional context buys tokens rather than accuracy.

**Limitations.** The scope is mental health and self-report wellbeing scores, so the result does not directly transfer to physiological endpoints with objective labels. Everything evaluated is zero-shot or prompted; no agent is trained for the retrieval policy, which means the paper measures the current practice rather than the ceiling. Rationale grading depends on an LLM judge, so the rationale numbers inherit whatever that judge is systematically wrong about.

**Why it matters to you.** This is a negative result on the exact setup a lot of wearable-plus-LLM work assumes, published at a main conference with the mean baseline included. The honest starting point for new work in your primary area is no longer whether an agent can do this, but what an agent needs in order to beat the mean. The paper names three requirements: selective history retrieval, grounded temporal evidence, and interpretable behavioural features rather than raw streams. Each of those is a research program, and none of them is claimed.

**How this builds on what you know:** The parents are GLOBEM (Xu 2023, Graphify Community 5, Wearable Sensing and Behavior), LLMs are Few-Shot Health Learners (Liu 2023, Community 1, Health AI and Self-Supervised), HEARTS (2603.06638, time-series area, added March), and MindScape (Nepal 2024, Community 5). Where GLOBEM fixed the datasets and the cross-cohort protocol for supervised wellbeing prediction, BALMS keeps the datasets and removes the training, so the object being scored moves from model accuracy to agent policy quality. Where Few-Shot Health Learners showed that a general LLM can read a short window of physiological features, BALMS asks whether that reading survives at month-long horizons, and finds that it does not. Where HEARTS showed single-shot LLM reasoning over health series degrading with sequence length, BALMS shows that wrapping the model in an agentic loop does not repair the degradation, because the loop does not retrieve selectively. Where MindScape pointed the LLM back at the participant as a writing interface, BALMS points it at a held-out number and grades it.

This paper extends Few-Shot Health Learners, which already crossed Community 5 and Community 1 in your library through its Sensor2Text bridge. The new work pushes that bridge further into evaluation: the crossing is no longer a demonstration that language models can touch sensor data, it is a measurement of how poorly they do so over long horizons.

---

## Tier B — TLDR

### Cliff: Learning Process Rewards from the First Mistake
Han, Wang, Ramaneti, Hao, Friedland, Kong. https://arxiv.org/abs/2609.02817

Reinforcement learning with verifiable rewards trains on one scalar per rollout, so credit for a long reasoning trace is spread over tokens that had nothing to do with the outcome. Cliff has an off-the-shelf LLM mark the position of the first reasoning error, splits the rollout there into a correct prefix and an incorrect suffix, and assigns positive token-level advantage before the break and negative feedback after it. The justification is that once a trace has gone wrong, grading the rest adds little, because everything downstream is conditioned on an invalid prefix. Across 12 scenarios it beats on-policy distillation by 15 percent and standard GRPO by 7 percent, and the gain holds with teachers of modest capability, which follows from the teacher's job being reduced to producing one index.

**How this builds on what you know:** Parents are DeepSeek-R1 (Community 0, LLM Agents and Reasoning), Chain-of-Thought Prompting (Community 0), and the on-policy distillation audit added to your library on 1 September (2608.31046). Where DeepSeek-R1 established that verifiable outcome rewards alone can train strong reasoning, Cliff keeps that setup and refines where the credit lands, because a scalar per rollout cannot distinguish three hundred correct tokens from the ten that broke. Where on-policy distillation needs teacher and student to share a reasoning pattern for token-level matching to mean anything, Cliff needs the teacher only to point at a position, which is why it survives a weak teacher; the audit paper in your library measured how much of distillation's gain really comes from the teacher, and Cliff answers by shrinking the teacher's contribution to the smallest useful output.

### Aspire: Can Models Self-Evolve from Vague Goals?
Wu, Zhang, Shi, Lei, Zhou et al. (ByteDance Seed). https://arxiv.org/abs/2608.31111

ASPIRE gives an agent only a natural-language capability goal such as "improve at research", with the downstream evaluation tasks hidden. The agent must interpret the goal, find its own capability gaps, choose data and an update method, construct its own validation signal, and decide when to stop; both weight-level and harness-level evolution run in one environment, scored afterwards on 520 expert-authored items across six goals. Agents complete the training and harness-editing loops reliably, but weight-level gains are sparse and unstable, the strongest evolved harness stays below the engineered Qwen-Agent reference, agents often train on data that does not match the hidden target, and continued search can erase earlier improvements. The measured quantity is really the gap between self-reported progress and held-out score.

**How this builds on what you know:** Parents are the Memory Mechanisms survey (Huang 2026, Community 0), the Agent AI survey (Durante 2024, Community 0), and Repo-To-Skill, which yesterday's digest added to your agent page. Where both surveys assume the objective is given and ask how the agent should be built, ASPIRE removes the objective and asks whether the agent can construct one, because writing down the metric is the part of research work that humans currently do and that self-evolution claims implicitly cover. Where Repo-To-Skill lifted a fixed agent by 134.3 percent on MLE-bench using verified skills mined from an external corpus, ASPIRE denies the agent both the corpus and the verification target, and the failure lands exactly there: agents trust narrow self-evaluations, so local gains do not transfer. Read together, two consecutive days bracket one question, with Repo-To-Skill showing what external verified knowledge buys and ASPIRE showing what its absence costs.

### CRISP: Cliff-awaRe Input-adaptive Sparse Prefilling with Structural-Mass-Motivated Routing
Nguyen, Nguyen, Dernoncourt, Rossi, Ngo Van, Chen, Nguyen. https://arxiv.org/abs/2609.01925

Dynamic sparse attention routes heads to sparse patterns at run time, but pays for the routing decision through an indirect proxy and allocates budget with cumulative coverage thresholds. CRISP changes both. It shows the routing decision can be read straight off the structure of the proxy attention map through C_struct, a measure of mass at Vertical-Slash compatible positions that reproduces the Jensen-Shannon routing decisions without the pooled matrix multiply or the KL evaluation. It then formalises a post-softmax mass cliff and proves that cumulative coverage thresholds accumulate O(n) background noise at long context, replacing them with a sink-aware threshold anchored at the noise floor. Across InfiniteBench, RULER and LongBench on two model families it is the strongest sparse method, matches or exceeds dense attention on retrieval-heavy tasks, recovers up to 28.0 percentage points on retrieval, and reaches a 5.30x attention speedup at 512k tokens.

**How this builds on what you know:** Parents are Attention Is All You Need (Community 2, Transformer and SSM Architectures), Declarative Attention, which was yesterday's Tier A and is now on your LLM page, and DeepSeek-V3 (Community 0). Where Vaswani made the attention pattern a fixed property of the architecture, CRISP chooses it per input and makes the choice nearly free. Where Declarative Attention moved selection inside the model and applied it during decoding, CRISP keeps selection outside the model, derives it from the attention map, and applies it at prefill, which is the phase Declarative Attention does not touch; the two are complementary and neither paper tests them together. Where DeepSeek-V3 compressed each cache entry, CRISP declines to read most entries, and its distinctive contribution over other dynamic routers is diagnostic rather than architectural: the retrieval accuracy that sparse methods were losing was being lost to background mass admitted past the cliff, not to sparsity being too aggressive.

---

## Tier C — scan

| Paper | Hook | Link |
| --- | --- | --- |
| HarnessDev (ByteDance Seed) | Asks whether an LLM can write and evolve its own agent harness | https://arxiv.org/abs/2609.01437 |
| S3Gym (ByteDance Seed) | Turns self-testing and self-judging into a self-improvement loop | https://arxiv.org/abs/2608.31100 |
| Post-Training for Gold-Medal Coding (NVIDIA) | Recipe for competition-programming performance from post-training alone | https://arxiv.org/abs/2609.02849 |
| It Takes Two to Match (Apple) | Co-evolves a generative retriever and its corpus with reinforcement learning | https://arxiv.org/abs/2609.00638 |
| Influence-Directed Distillation | Fixes the diversity bottleneck in sampled-token on-policy distillation | https://arxiv.org/abs/2608.29846 |
| Pixel Text Representation Learning | Design study for rendering text as pixels instead of tokenising it | https://arxiv.org/abs/2609.01147 |
| PaperCompiler | Compiles a paper into a repository-level specification, then into code | https://arxiv.org/abs/2609.02272 |
| VibeVoice-ASR-Streaming (Microsoft) | Streaming speech recognition on the VibeVoice continuous tokenizer | https://arxiv.org/abs/2609.02812 |

---

## Tier D — Time-series and bio-sensing gap watch

**Already ported (closed off).** BALMS ports agentic LLM evaluation from the agent literature into longitudinal wearable sensing, and the port is now measured and published, so the demonstration that a prompted agent can be pointed at a long sensor stream is no longer a contribution. It matches Community 4 (Time Series and LLM Integration) and Community 5 (Wearable Sensing and Behavior) hyperedges directly: GLOBEM supplies the data protocol, Few-Shot Health Learners the reading capability, HEARTS the benchmark form. Treat zero-shot agentic prompting over longitudinal sensing as done and near the mean baseline.

**Unported opportunity 1 — first-mistake reward shaping for time-series reasoning agents.** Cliff's assumption is that error is absorbing, so a trace carries almost all its information at one boundary. TS-Agent (I2CIT4I7) already produces exactly the structure that assumption needs: an explicit evidence log in which each operator call makes a numeric claim that can be checked against the data. Transfer hypothesis: have a teacher locate the first operator call whose numeric claim is not supported by the evidence log, shape token-level advantages around that index, and train the retrieval and operator-selection policy that BALMS shows is currently missing. This connects the two strongest results in today's digest and is, as far as the graph shows, unbuilt.

**Unported opportunity 2 — mass-cliff threshold analysis for long physiological context.** CRISP's finding is that at long context a cumulative coverage threshold spends its budget on background noise growing linearly with sequence length. Minute-resolution multi-day wearable streams sit squarely in that regime, and BALMS reports the matching symptom on the other side: agents given more history do not use it. Transfer hypothesis: apply the sink-aware threshold analysis to attention over long physiological sequences and test whether the reported failure to use long history is a selection artefact rather than a reasoning limit. The analysis is signal-processing reasoning applied to attention maps, so it should read directly for you.

---

## News

OpenAI released GPT-6 Astra on 3 September as a limited preview for trusted partners, with public availability planned for 5 September across ChatGPT Plus, Pro, Business and Enterprise, the API, and AWS. The company frames it as a generational step for cybersecurity, software engineering and science, and president Greg Brockman has said publicly that it may come to be seen as the arrival of artificial general intelligence. Treat the AGI framing as a company claim rather than a measured result; the useful thing to watch is whether independent long-horizon agent benchmarks move, which the release itself does not establish.

Release trackers also record three other frontier launches in the first days of September, listed as Claude Fable 5.1, Gemini 3.8 Flash, and Muse Spark 1.3, and two large open-weight drops, Tencent's Hy4 preview (770B mixture of experts, 49B active, 1M context) and an NVFP4-quantised Qwen3.8 from NVIDIA at 2.4T parameters for 4-bit inference. These come from aggregator pages rather than primary announcements, so confirm before citing.

---

End of digest. Close this tab when done.
