# AI Digest — 2026-09-10

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A not done by 6 AM, stop.

Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.

Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

---

## Tier A — deep read

### WearableQA: A Benchmark for Health Reasoning over Real-World Wearable Data
Lee, Chen, Chuang, Shenoy, Wei, Ko, Kim, Corda (Meta) — [arXiv:2609.05405](https://arxiv.org/abs/2609.05405)

**Problem.** The claim that a language model can reason over a person's wearable record has been made repeatedly, but the evidence comes from evaluations that use engineered features over short windows or clean synthetic prompts. Neither setting contains what a deployed device produces: sensor noise, missing stretches, and between-person variability large enough that a population rule fails on an individual. So the existing evidence cannot separate a model that reasons over one person's history from one that recites a population prior, and a single accuracy number cannot say whether a failure was arithmetic or physiology.

**Method.** The benchmark is built on the actual longitudinal records of 200 real people, each with up to 500 days of daily wearable measurements alongside blood biomarkers and demographics, with the authentic distributions left in rather than cleaned. It contains 4,084 ten-option multiple-choice questions sorted into 16 types along two axes. The first separates data reasoning, meaning computation over the longitudinal measurements, from health reasoning, meaning physiological interpretation. The second separates single-signal reasoning from cross-signal reasoning, meaning integration across several streams. Items are produced by a dual-grounding procedure: each must be supported both by a published physiological finding and by a statistically validated pattern present in the population data, so the answer key does not rest on an annotator model's judgment.

**Result.** Fourteen proprietary and open-source models were evaluated. Scores range from 19.6 to 72.9 percent against a 10 percent chance floor, which means the benchmark separates systems rather than saturating or flooring. Most models land below 60 percent. The spread is the useful number: a benchmark where everything clusters says nothing, and one where everything fails says nothing either.

**Limitations.** Multiple choice with ten options bounds what can be asked; a model can score by elimination on items where the distractors are physiologically implausible, and the paper's defense is the dual-grounding construction rather than a measured guessing analysis. Two hundred users is a small cohort for claims about between-person variability, and the demographic composition determines which population-grounded patterns survive validation. There is also no ground truth for causes, because the data is observational, so the benchmark can ask what happened but not reliably why.

**Why it matters to Leo.** This is the closest thing yet to a shared yardstick in Leo's working area, and it lands on the claim the whole time-series-plus-LLM line rests on. The 16-type breakdown is worth more than the leaderboard, because it gives a ready-made ablation axis: a method that lifts cross-signal health reasoning while leaving single-signal data reasoning flat is doing something specific, and that is a cleaner result to report than an aggregate delta. It also settles what to build against, since the alternative until now was GLOBEM-style prediction plus an argument about whether the number transferred.

**How this builds on what you know:** The direct parent is *LLMs are Few-Shot Health Learners* (Liu 2023), which sits in Community 1, Health AI and Self-Supervised, and is also one end of the graphify cross-area bridge into bio-sensing. Where Liu 2023 showed a language model can read raw physiological numbers and answer health questions with no task-specific training, this paper keeps the device noise, the missingness and the between-person variability, because the earlier setup measured whether the capability exists rather than whether it survives a real sensor. *Health-LLM* (Kim 2024) evaluated on curated features and short windows, which makes the task feature-vector-to-label; here the model gets the raw 500-day record and must locate the relevant stretch before computing over it. *GLOBEM* (Xu 2023), in Community 5, Wearable Sensing and Behavior, supplied the multi-year multi-cohort dataset design that makes this evaluation possible at all; the addition here is a question schema on top of comparable data.

This paper extends the Sensor2Text-to-Few-Shot-Health-Learners bridge, which already crossed Community 4, Time Series plus LLM Integration, and Community 1, Health AI, in your library. The new work pushes that bridge further toward evaluation: the crossing used to be about how a model is attached to physiological data, and this moves it to how the attachment is scored.

---

## Tier B — TLDRs

### HealthLoopQA: A Context-Aware Question Answering Benchmark for Interpreting Wearable Monitoring Data in Diabetes Care
[arXiv:2609.06976](https://arxiv.org/abs/2609.06976)

Replaces the collected dataset with a simulated hybrid closed-loop insulin delivery testbed, which produces physiological and therapeutic traces under varied patient activity schedules and admits 17 injected fault scenarios covering device failures and security compromises. Question templates cover process mining, anomaly detection and predictive reasoning, graded by reasoning depth from descriptive statistics through causal and inferential reasoning. Every item carries both a numerical answer and a textual rationale, so quantitative accuracy and reasoning fidelity are scored as separate quantities. The point of the simulation is that the generating process is known, which makes causal questions answerable and lets faults be created on demand rather than waited for.

**How this builds on what you know:** *Health-LLM* (Kim 2024) is the short-horizon evaluation this paper argues is too narrow, and the specific thing it could not do is ask a causal question, because an observational wearable record does not contain why a signal moved. *Verifiable Physiological Reasoning* (Wang 2026) established that a physiological answer should be checked against an explicit derivation; where Wang verified one derivation as a method, this paper attaches a rationale to every item and turns verification into an evaluation axis. *TS-Agent* (Liu 2025), a Community 4 anchor, showed that operator calls beat direct reading on time-series reasoning; this supplies the setting where that gap should be widest, since fault attribution needs evidence gathering rather than pattern recall. Read it against WearableQA rather than alone: the two make opposite trades on the same day, one keeping real distributions with no ground-truth causes, the other buying ground-truth causes and faults at the cost of realism, and a method evaluated on only one of them is easy to dismiss.

### Revisiting Complete Reasoning Traces for Post-Training
Hwang, Yun, Heo, Han (NAVER AI Lab) — [arXiv:2609.07103](https://arxiv.org/abs/2609.07103)

Asks whether supervised fine-tuning on complete reasoning trajectories is what makes reasoning post-training work, and reports that it is largely not. A pilot study finds full trajectories give only limited benefit over partial ones, and that partial trajectories stay effective under heavy truncation. Attention-based analysis and controlled token-removal studies then show intermediate tokens contribute minimally to final reasoning quality. The offered reading is that a model handed the endpoints of a trajectory can reconstruct coherent intermediate steps from internal knowledge, so much of the middle of a long chain is redundant supervision rather than necessary supervision. Note which instrument carries the argument: the token-removal intervention is causal, the attention analysis is correlational support.

**How this builds on what you know:** *Chain-of-Thought* (Wei 2023) is a Community 0 anchor and the source of the premise being tested. Where Wei showed that producing intermediate steps at inference time helps, this paper separates that from the claim that consuming them at training time helps, and finds the second much weaker, because the field inferred the second from the first without testing it. Where *DeepSeek-R1* (2025) established long chains as the shape of a strong reasoner, this argues the length is partly incidental to what was learned. Where *CODI* (Shen 2025) compressed the chain into latent form and therefore still had to represent it, this reports that a good deal of the chain can be deleted from the training data outright, which is cheaper and stronger if it holds at scale. For Leo the transferable question is whether the same holds when the intermediate steps are numerical operator calls rather than sentences: in a time-series agent the middle of the trace is where the evidence is gathered, so a model cannot infer it from internal knowledge the way it can infer an arithmetic step. That contrast is a testable claim and a small paper.

### Co-Evolving Harnesses and Models: On-Policy Correction Helps Weaker Models Catch Up Where Imitation Fails
Yu, Bi, Pentyala et al. (Salesforce) — [arXiv:2609.09134](https://arxiv.org/abs/2609.09134)

Evolves an agent harness, meaning the system prompt, tool set, execution hooks and context-management scaffolding, for a weak model, then fine-tunes that model on a stronger expert's complete trajectories under the same harness. Performance regresses on all seven enterprise agent tasks, by 4 to 30 points across Qwen3-Coder and Gemma 4, even though the identical procedure helps under the unevolved harness. The diagnosis is a fit problem rather than a knowledge problem: imitation does transfer knowledge and does raise scaffold usage, but installs the expert's planning strategy in a model that cannot execute it, and that strategy no longer matches a harness shaped around its native planning. The fix changes the provenance of supervision rather than its content, using a meta-level machine-learning agent to localize the failing turn in the weak model's own rollout and asking the expert to rewrite only that turn.

**How this builds on what you know:** *ADaPT* (Prasad 2023) and *LATS* (Zhou 2024) are a graphify cross-area bridge pair inside Community 0, linked as planning-decomposition agents. This paper extends that bridge: where ADaPT matched decomposition depth to executor competence inside a single run, the same mismatch is shown to appear across a training boundary, and where LATS and the wider scaffold line treated harness gains and weight gains as independent and additive, this shows they interact negatively once the harness has been evolved against the weak model. The bridge is pushed from inference-time planning fit into training-time planning fit. It also directly qualifies yesterday's *NeoHorse-1*, which trained on harness-logged trajectories and reported gains: that recipe worked because its trajectories came from the model's own serving traffic, and the on-policy versus off-policy provenance is exactly what flips the sign here. Worth noting the convergence across two days, since yesterday's reverse-distillation paper reached the same on-policy conclusion from the reinforcement learning side while this one reaches it from the scaffolding side.

---

## Tier C — scan

| Paper | Hook |
|---|---|
| [Programmable World Model](https://arxiv.org/abs/2609.10540) | Compiles language instructions into entity-state programs, then renders; 94% count and 98% state accuracy. |
| [Show-Harness: Just a VLM Agent Can Play Robots](https://arxiv.org/abs/2609.10522) | Argues a plain vision-language agent plus harness is enough for robot control. |
| [Φ-Bench: Can LLMs Engineer the Infrastructure That Powers Them?](https://arxiv.org/abs/2609.10226) | Benchmarks models on building the training and serving stack they run on. |
| [Scores Alone Do Not Prove Discovery](https://arxiv.org/abs/2609.09219) | A certification protocol for auditing whether a research agent actually discovered anything. |
| [SAEScientist-Bench](https://arxiv.org/abs/2609.09113) | Tests whether agents can run autonomous sparse-autoencoder interpretability research. |
| [Difficulty-Adaptive Tree-Structured Policy Optimization](https://arxiv.org/abs/2609.08650) | Expands reasoning coverage in RLVR by shaping the rollout tree to problem difficulty. |
| [DF26: We Cannot Tell Fake From Real Anymore](https://arxiv.org/abs/2609.07369) | Deepfake detection benchmark reporting that current detectors have stopped working. |
| [RESCUE-BENCH](https://arxiv.org/abs/2609.09657) | Relation-aware multi-party emotional support conversation, adjacent to the counseling-benchmark line. |

---

## Tier D — Time-series / bio-sensing gap watch

**Already ported (closed off).** Two of them landed today, which is unusual. WearableQA imports LLM benchmark construction methodology into wearables, specifically the multiple-choice-with-distractors format and literature-grounded item validation from medical question answering. HealthLoopQA imports controlled fault injection from systems evaluation. Both fall squarely inside Community 5, Wearable Sensing and Behavior, and Community 4, Time Series plus LLM Integration. Treat both imports as done: a paper whose contribution is "we built a wearable QA benchmark" now has to explain what it adds to these two.

**Unported opportunity 1 — explicit state programs for physiological simulation.** *Programmable World Model* (2609.10540) separates world-state evolution from observation generation: an agent writes an executable program of entity states and transition rules, a light engine maintains a persistent global state including things not currently visible, and a pretrained generative model renders observations conditioned on that state. Nothing in the wearable literature does this. The transfer hypothesis is that a person's physiological state is exactly a persistent global state with off-screen variables, meaning hydration, sleep debt, medication timing, that the sensor never observes directly, and writing that state as an executable program with explicit transition rules would give a generative wearable model the persistence it currently lacks. HealthLoopQA's testbed is a hand-built version of the same idea, which is evidence the framing works and that nobody has made it programmable.

**Unported opportunity 2 — trace truncation for time-series agents.** *Revisiting Complete Reasoning Traces* (2609.07103) reports that intermediate tokens in a reasoning trajectory contribute little, because the model can reconstruct them from internal knowledge given the endpoints. The transfer hypothesis is that this should fail for time-series agents in a measurable way: when the intermediate steps are operator calls that gather numerical evidence, the model has no internal knowledge to reconstruct them from, so truncation should hurt where it did not for mathematical reasoning. A single controlled comparison on TS-Agent-style traces would either confirm that evidence-gathering traces are a different regime or show the redundancy is more general than anyone expected. Either outcome is publishable and the experiment is small.

---

## News

OpenAI announced that an internal system more capable than GPT-6 Astra produced a claimed solution to the Navier-Stokes Millennium Prize Problem, with roughly 10,000 coordinating agents running for 88 hours before emitting an analytical proof. The claim is disputed on attribution rather than on correctness so far, with NYU mathematician Tristan Buckmaster asking whether the effort was accelerated after learning of competing work. Verification status is the thing to watch, not the announcement.

DeepSeek opened a limited beta for V4.1 Flash, an interim model with a new architecture and native multimodal support. Separately, the NSA, CISA and FBI issued a joint advisory alleging that DeepSeek, Moonshot AI, Alibaba, MiniMax, StepFun and Z.AI have run targeted distillation against United States frontier models since late 2024. If that advisory turns into policy, it affects which open weights remain redistributable, which matters for anyone building on them.

This follows a dense first week of September, in which Claude Fable 5.1 and Mythos 5.1 shipped on the 1st, Gemini 3.8 Flash and Muse Spark 1.3 on the 2nd, and GPT-6 Astra on the 3rd.

---

End of digest. Close this tab when done.
