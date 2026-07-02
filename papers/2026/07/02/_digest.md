# AI Digest — 2026-07-02

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A not done by 6 AM, stop.
Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.
Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

---

## Tier A — deep read (1 paper, ~20 min)

### CausalMix: Data Mixture as Causal Inference for Language Model Training
arXiv:2607.01104 (Tang, Zhang, Zheng, Pan, Pei, Jin, Zhou, Wang, Huang — Tsinghua, 01 Jul 2026) — https://arxiv.org/abs/2607.01104

**Problem.** The mix of data domains used to train a language model strongly affects the final model. Recent methods learn good mixture weights by training small proxy models and fitting a function from mixture to loss (RegMix is the reference example). These methods assume the data pool is fixed. When the pool changes, for example when new sources are added or the model is scaled up, the fitted function no longer holds and the whole search has to be rerun from scratch. This makes it hard to carry a mixture found at small scale over to a larger pool or a larger model.

**Method.** The authors recast mixture selection as a causal inference problem. The statistical features of the data pool are treated as covariates, and the domain mixture is treated as the treatment applied to a training run. They run 512 training runs of Qwen2.5-0.5B and fit a causal model that estimates the Conditional Average Treatment Effect (CATE), that is, how much a given mixture changes the outcome given the current pool state. Because the model conditions on pool features rather than memorizing one fixed pool, they can extrapolate the estimated optimal mixture to a much larger 800K-example pool and use it to train a 7B model. They also apply the same framework to selecting long chain-of-thought training data for Qwen3-4B-Base. A CATE interpreter produces a visual read-out of the learned mixing strategy.

**Result.** The mixture chosen by CausalMix improves downstream task performance over RegMix and other baselines across several benchmarks, and the improvement holds after transfer from the 0.5B fitting runs to the 7B target model and from the small pool to the 800K pool. The method also transfers to the long chain-of-thought setting on Qwen3-4B-Base. Gains are reported as consistent across tasks rather than as a single headline number.

**Limitations.** The causal model is fit from 512 runs of one small model (0.5B); the assumption that CATE estimated at that scale transfers to 7B is supported empirically here but not guaranteed for other architectures or much larger targets. The covariate design (which statistical features describe the pool) is a modeling choice that the results depend on. Reported gains are relative to RegMix-style baselines, so the size of the practical benefit depends on how well-tuned those baselines are.

**Why it matters to Leo.** This is a clean case of importing a causal-inference tool (treatment effects, CATE) into a core LLM training decision, and it is one of the two library areas Leo tracks for method transfer. The same "treat the configuration as a treatment, condition on state, extrapolate" pattern is a candidate for choosing pretraining data mixtures in time-series and bio-sensing foundation models, where the "domains" are sensor modalities and datasets.

**How this builds on what you know:**
CausalMix's parent on the causal side is Causal Inference Intro (Pearl 2010, key BB78CC56, Interpretability and Fairness community), which sets up treatment, covariate, and treatment-effect estimation. Where Pearl's framework estimates the effect of a treatment on an outcome in a fixed observational setting, CausalMix makes the data mixture the treatment and the training outcome the response, so it can predict the effect of an unseen mixture on an unseen pool rather than only explaining a fixed one. On the language-model side, the long chain-of-thought extension connects to DeepSeek-R1 (2025, key Z5IWHZAE, LLM community): DeepSeek-R1 showed that long reasoning traces are valuable training data, and CausalMix adds a principled way to decide how much of that data to mix in. There is no direct data-mixture parent in your library — RegMix, the closest predecessor, is external — so on the mixture-optimization axis this paper has no in-library ancestor, and its nearest library neighbors are the causal-inference and LLM anchors named above. This paper is a new bridge in your library between the causal-inference area (Pearl) and the LLM-training area, two clusters that were not previously linked.

---

## Tier B — TLDRs (3 papers, ~10 min)

### Perceive-to-Reason: Decoupling Perception and Reasoning for Fine-Grained Visual Reasoning
arXiv:2607.01191 (Li, Huang, Li, Jiang, Wang, Xu, Zhang, Hong, Huang, Xue, Lu, Xiao, Zhuang, Shen — Zhejiang University, 01 Jul 2026) — https://arxiv.org/abs/2607.01191

Vision-language models still fail when a small but decisive detail is buried in a high-resolution image. Prior fixes repeatedly crop the image or run a test-time visual search, but they do not separate the act of finding the evidence from the act of reasoning about it. Perceive-to-Reason (P2R) splits the task in two: the model first acts as a Perceiver that localizes the question-relevant region, then acts as a Reasoner that answers using the annotated image and the cropped region. Training uses Perception-Reasoning Alternating GRPO (PRA-GRPO), which alternates perception-focused and reasoning-focused updates using only final-answer supervision, so no bounding-box labels are needed. Built on Qwen3-VL-Instruct at 2B/4B/8B, P2R-4B reaches 93.2 percent on V-Star, 81.9 percent on HR-Bench-4K, and 80.5 percent on HR-Bench-8K, well above the backbone, and the gains carry over to broader multimodal reasoning tasks.

**How this builds on what you know:**
The training method is a variant of GRPO, the same reward-based reasoning optimizer behind DeepSeek-R1 (key Z5IWHZAE) and refined in Latent-GRPO (Deng 2026, key U4ZPM5DN, Reasoning community). Where plain GRPO applies one undifferentiated reward signal to the whole reasoning trace, PRA-GRPO alternates between rewarding perception steps and rewarding reasoning steps, because a single reward cannot tell the model whether it failed at finding the evidence or at reasoning over it. It also sits alongside the Large Multimodal Reasoning Survey (Li 2025, key FPEC4PIH, Reasoning community), which mapped the multimodal-reasoning landscape that this paper's decoupled design refines.

### AutoTrainess: Teaching Language Models to Improve Language Models Autonomously
arXiv:2606.31551 (Yu, Yin, Gao, He, Cai, Zhang — 30 Jun 2026) — https://arxiv.org/abs/2606.31551

Training a language model is still mostly manual, even though agents are now good at software tasks. Autonomous post-training is more than coding: the agent has to plan iterations, build benchmark-aligned data, run stable training jobs, evaluate checkpoints, and keep experiment state across many hours. AutoTrainess exposes each of these as an agent-computer interface, so the agent works through explicit workflows, rules, and execution constraints rather than a raw command line with an open-ended action space. On PostTrainBench it scores 26.94 on average with GPT-5.4 (Codex) against 23.21 for a command-line-only baseline, and it transfers across harnesses, lifting DeepSeek-V4-Flash (OpenCode) from 12.13 to 19.58.

**How this builds on what you know:**
The design descends from decomposition-and-planning agents in your library, ADaPT (Prasad 2023, key J8DYBKW2) and LATS (Zhou 2024, key 77ERE7HA), both in the Agent area, which is exactly the planning-decomposition bridge already recorded between those two papers. Where ADaPT decomposed a task on demand and LATS searched over action trees, AutoTrainess fixes the action space ahead of time by wrapping the messy training pipeline in named interfaces, because a long-horizon training run needs reliable, repeatable operations more than open-ended search. It also extends the tool-using line of ToolkenGPT (key 6RDHVVA2) from calling atomic tools to driving a full multi-hour training workflow.

### AtomiMed: Hierarchical Atomic Fact-Checking for Universal Clinical-Aware Medical Report Evaluation
arXiv:2606.31292 (Wang, Chang, Jiang, Gao, Zhang, Yuan, Cao, Shi, Zhang, Liu, Zhang — Zhejiang University, 30 Jun 2026) — https://arxiv.org/abs/2606.31292

Automatic scoring of generated medical reports mostly relies on n-gram overlap, which misses whether the report is clinically correct and can wave through serious diagnostic errors. AtomiMed breaks a report into a hierarchy of atomic clinical facts, disease-level entities and attribute-level descriptors such as location, morphology, and severity, and then runs an agentic cross-verification loop between the ground-truth report and the predicted report, imitating a multi-radiologist peer review. This separates detection accuracy (did it find the finding) from descriptive accuracy (did it describe it correctly). The authors release MRGEvalKit for automated hierarchical extraction and OmniMRG-Bench, a benchmark spanning X-ray, CT, MRI, and ultrasound. Across expert-annotated reader studies, AtomiMed correlates with radiologist judgment better than n-gram and model-based metrics.

**How this builds on what you know:**
The closest parent is Med-VQA Hallucination (Wu 2024, key ATEFZQA4, Hallucination area), which showed that medical vision-language models assert findings that are not supported by the image. Where that work measured hallucination on question answering, AtomiMed turns fact-level checking into an evaluation metric for full report generation, decomposing the report into atomic facts and verifying each, because a report-level overlap score cannot localize which specific claim is wrong. It also connects to Verifiable Physio Reasoning (Wang 2026, key 2BGP9QJL, LLM-Health area), which pushed for checkable outputs in health models; AtomiMed applies the same "make each claim verifiable" principle to the evaluation side rather than the generation side.

---

## Tier C — scan headlines (up to 8)

- Domain Arithmetic: One-Shot VLA Adaptation under Environmental Shifts (arXiv:2607.00666) — adapts a vision-language-action policy to a new environment from a single demonstration by arithmetic in domain space. https://arxiv.org/abs/2607.00666
- The State-Prediction Separation Hypothesis (arXiv:2607.01218, Cornell LIL Lab) — argues world models separate state tracking from next-step prediction, with evidence. https://arxiv.org/abs/2607.01218
- ELDR: Expert-Locality-Aware Decode Routing for PD-Disaggregated MoE Serving (arXiv:2607.00466, Microsoft Research) — cuts MoE serving cost by routing decode to where experts already sit. https://arxiv.org/abs/2607.00466
- MemSyco-Bench: Benchmarking Sycophancy in Agent Memory (arXiv:2607.01071) — measures when an agent's stored memory makes it agree with the user against the evidence. https://arxiv.org/abs/2607.01071
- When LLMs Read Tables Carelessly (arXiv:2606.32029, AWS) — measures and reduces cell-referencing errors when models read tables. https://arxiv.org/abs/2606.32029
- Valdi: Value Diffusion World Models (arXiv:2607.00917) — a world model that diffuses value estimates for planning. https://arxiv.org/abs/2607.00917
- BioInsight: Multi-Agent Orchestration for Interactive Biomedical Knowledge Discovery (arXiv:2606.20997) — coordinates several agents to search and reason over biomedical knowledge. https://arxiv.org/abs/2606.20997
- Multimodal Continuous Reasoning via Asymmetric Mutual Variational Learning (arXiv:2607.00461) — reasons in a continuous latent space across modalities rather than in discrete tokens. https://arxiv.org/abs/2607.00461

---

## Tier D — Time-series / Bio-sensing Gap Watch

**Already ported (closing off).** No time-series or bio-sensing paper qualified for Tier A or Tier B today, and none of today's front-page papers apply a Community 4 (Time Series + LLM) or Community 5 (Wearable Sensing) method to a new signal. Nothing new closes off inside those communities today. AtomiMed (Tier B) touches medical imaging, not physiological time series, so it does not affect the sensing gap map.

**Unported opportunity 1 — CATE-based data mixing for sensor foundation models.** CausalMix (Tier A) treats the training data mixture as a causal treatment and extrapolates the optimal mixture across pool sizes and model scales. This has not been applied to time-series or bio-sensing pretraining. Transfer hypothesis: treat the mix of sensor modalities and source datasets (PPG, ECG, accelerometer, different cohorts) as the treatment, describe each pool by simple signal statistics as covariates, fit CATE on small encoders, and extrapolate the best modality mixture before committing compute to a large wearable foundation model.

**Unported opportunity 2 — decoupled perceive-then-reason for physiological signals.** P2R (Tier B) splits a task into a Perceiver that localizes evidence and a Reasoner that answers, trained with alternating role-aware GRPO and only final-answer supervision. This has not been applied to signal reasoning. Transfer hypothesis: have a Perceiver stage localize the diagnostically relevant window or channel in a long multichannel recording, then a Reasoner stage answer the clinical question over that window, and train the pair with alternating updates using only the final label, avoiding per-window annotation.

---

## News — model and product releases

Reported this period from secondary trackers, not verified against primary announcements: ByteDance Seed posted a Seed2.0 model card (surfaced on Hugging Face today, arXiv:2607.00248); Google Gemini 3.5 Pro is reported as cleared for a July general-availability launch after slipping from June; Anthropic is reported to have redeployed Claude Fable 5 on 1 July after an export-control order was lifted, and to have made Claude Sonnet 5 its default model on 30 June. Treat these as leads to confirm, not settled facts.

---

End of digest. Close this tab when done.
