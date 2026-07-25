# AI Digest — 2026-07-25

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A not done by 6 AM, stop.
Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.
Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

---

## Tier A — deep read (1 paper)

### Signal or Noise? Understanding Generative Models for Real-World Sensor Time Series
Shuai, Xu, Wu, Li, Li, Yang — arXiv:2607.04245 — Area: time-series (generative-cv bridge)

**Problem.** Generative models are well understood for text and images, but real-world systems are recorded as continuous, high-dimensional, noisy sensor time series. Work on generating sensor signals is scattered across modalities, datasets, and task definitions, so there is no systematic account of when generation works, how it works, and why it fails. This is Leo's primary area, and the paper is the first attempt to answer these questions under one controlled protocol.

**Method.** The authors build SensorGen, a study of sensor-signal generation covering 14 settings across 4 domains, 7 datasets, and 12 signal modalities. They evaluate five families of generative models (including GAN, diffusion, and flow-matching approaches) under a shared protocol, and measure both signal fidelity and the usefulness of the generated signals for downstream prediction.

**Result.** Three findings. First, flow-matching models give the strongest overall performance across most settings. Second, signal properties decide which design choices matter: demographic covariates improve longitudinal generation, and time-frequency modeling improves high-frequency signal generation. Third, generated signals carry practical value beyond looking realistic — quality improves with scale, and adding synthetic data improves downstream task accuracy.

**Limitations.** The study is empirical rather than theoretical; it reports which families work in which settings but does not derive why flow-matching wins. The 14 settings, while broad, are still a sample of the sensor landscape, and the downstream-utility gains depend on the specific task heads used.

**Why it matters to Leo.** This is a direct map of the generative-modeling toolbox onto sensor time series, which is exactly the ground Leo works on. It tells him which family to reach for (flow-matching), which conditioning signals pay off (demographics for slow trends, time-frequency for fast components), and that synthetic sensor data is worth generating for augmentation, not just for display.

**How this builds on what you know:** The paper's parents in your library sit in the Vision-Language and Generative community (community 3): DDPM (Ho 2020) [GX7WR7KA] defined the denoising diffusion objective, and Diffusion Beats GANs (Dhariwal 2021) [MVWM4TZJ] showed diffusion overtakes GANs on image fidelity. Its sensor-side parents are Foundation Models for Biosignals (Gu 2025) [2XWEG7AF] and Sensor2Text (Chen 2024) [ELYUE3NF], both in the bio-sensing part of your library. Where DDPM and Diffusion Beats GANs settled the generative question for images, this paper asks the same question for physiological and sensor signals and finds a different answer — flow-matching, not diffusion, is the strongest default — because sensor signals carry noise and time-frequency structure that images do not. This paper extends the generative line that the CycleGAN-to-DDPM bridge already drew inside community 3, and pushes that bridge across into the time-series and wearable communities (communities 4 and 5), which is a cross-community link your library did not have before.

---

## Tier B — TLDRs (3 papers)

### AREX: Towards a Recursively Self-Improving Agent for Deep Research
Lu, Li, Luo et al. (BAAI) — arXiv:2607.21461 — Area: agent / reasoning

AREX is a family of deep-research agents that treat answer-finding and answer-checking as asymmetric: discovery is costly, but verification splits into cheap constraint-wise checks. The agent alternates an inner loop that gathers evidence and drafts a provisional answer with an outer loop that audits the draft constraint by constraint and launches targeted follow-up research on the unresolved parts. To keep this going over long horizons, it learns a context-update tool that compresses interaction history into a compact state holding verified evidence and open constraints, with no external model. It is trained with agentic mid-training and long-horizon reinforcement learning, released as a dense 4B model and a 122B-A10B mixture-of-experts model, and it beats comparable-scale baselines on BrowseComp, WideSearch, DeepSearchQA, and Humanity's Last Exam.

**How this builds on what you know:** The parents in your library are Agent AI Survey (Durante 2024) [Z9WZPMNU], LATS (Zhou 2024) [77ERE7HA], and ToolkenGPT (Hao 2024) [6RDHVVA2], all in the LLM Agents and Reasoning community (community 0). Where LATS searches a tree of actions and backtracks within a single problem-solving pass, AREX adds an outer self-improvement loop that verifies intermediate answers and re-plans from the partially verified state, because deep research rewards checking constraints more than searching longer. This extends the planning-decomposition bridge (Adapt to LATS) already in your library toward verification-guided refinement, and it reuses the tool-using idea from ToolkenGPT for its learned context-update tool.

### Visual Contrastive Self-Distillation
Liang, Tian, Li et al. (University of Maryland) — arXiv:2607.21556 — Area: multi-modal / self-supervised

VCSD is an on-policy self-distillation method for vision-language models that removes the external teacher and the privileged supervision that earlier self-distillation needed. At each student-generated response prefix, an exponential-moving-average teacher produces two next-token distributions under the same prompt and prefix: one conditioned on the original image, one on a content-erased control. The token-wise log-probability difference marks tokens whose likelihood rises specifically because of the image content, and that contrast sharpens the teacher's original-image distribution, which is then distilled into the student. On ViRL39K it improves seven-benchmark aggregates on Qwen3-VL by roughly 5 points at 2B, 2 points at 4B, and 4 points at 8B, with no external teacher, answer hints, or extra inference cost.

**How this builds on what you know:** The closest parent in your library is DINO (Caron 2021) [DVUL4GU6], which introduced the EMA-teacher self-distillation setup that VCSD reuses. Where DINO builds its teacher-student asymmetry from two augmented crops of the same image, VCSD builds the asymmetry from input conditioning — original image versus content-erased image under a fixed text prefix — because for a vision-language model the useful signal is which tokens the image content actually raises. DINO sits in the computer-vision part of your library; VCSD carries its self-distillation idea into the vision-language and generation setting.

### Predictive Divergence Masks for LLM RL
Zhou, Yao, Qi et al. — arXiv:2607.10848 — Area: reasoning / llm

Reinforcement learning for language models uses trust-region masks to stabilize off-policy updates, with a proximity criterion (has the policy moved too far) and a direction criterion (does this update push it farther). The recent DPPO method improved the proximity test by using a probability divergence instead of PPO's importance ratio, but kept PPO's ratio-based direction test. The authors show that this single-sample ratio can disagree in sign with the change of the very divergence the proximity test uses, and propose a predictive divergence mask that asks whether the next gradient step will raise or lower that divergence, derived in closed form for softmax policies. Because rollout engines expose only a truncated top-K vocabulary, they add two lightweight top-K estimators, and the masks improve RL training across model scales and precision settings.

**How this builds on what you know:** The parents in your library are PPO (Schulman 2017) [KQTIJC4U], which defined the ratio-based trust region this paper repairs, DeepSeek-R1 (2025) [Z5IWHZAE], which made RL-from-verifiable-rewards the standard recipe for reasoning models, and Latent-GRPO (Deng) [U4ZPM5DN], a group-relative variant in your reasoning collection. Where PPO clips on a single-sample importance ratio, this paper replaces the direction test with a predicted change in the trust-region divergence itself, because the ratio is a noisy proxy that can point the wrong way. It sharpens the same RL machinery DeepSeek-R1 relies on, and connects the world-model-RL community (PPO) to the reasoning community (DeepSeek-R1, Latent-GRPO) in your library.

---

## Tier C — scan (headlines)

- ReferTrack: Referring Then Tracking for Embodied Visual Tracking (Tencent) — language-referred target tracking for embodied agents. arXiv:2607.20061
- Show, Don't Tell: Evaluating Spatial Cognition in Generative Pixels Rather Than LLM Text (ZJU) — tests spatial reasoning by having models draw, not describe. arXiv:2607.21072
- Tencent WorkBuddy Bench — multi-domain coding-agent benchmark with contamination-resistant task construction. arXiv:2607.20911
- LLMs Get Lost in Evolving User Intent (Microsoft) — models lose track when user goals shift mid-conversation. arXiv:2607.20734
- Sample-Efficient Learning from Agent Experience — reuses past agent trajectories to cut training cost. arXiv:2607.21051
- Streaming Multi-Agent Autoregressive Diffusion Model with World State Registers — shared world state for streaming multi-agent generation. arXiv:2607.21594
- Recurrent Sinusoidal INRs for Efficient High-Fidelity Representation — compact sinusoidal implicit representations for signals. arXiv:2607.21485
- Agora: Enhancing LLM Agent Reasoning Via Auction-Based Task Allocation — an auction mechanism assigns tasks to expert models and tools. arXiv:2607.09600

---

## Tier D — Time-series / Bio-sensing Gap Watch

**Ported, now closing.** Generative modeling of sensor signals moved from scattered attempts to a controlled map today. SensorGen (Tier A) ports five generative families — including diffusion and flow-matching — to sensor time series across 14 settings, and reports that flow-matching is the strongest default with time-frequency conditioning for high-frequency signals. This matches the direction of community 4 (Time Series plus LLM Integration) and closes off "apply generative model family X to sensor data" as easy, unclaimed ground: the systematic comparison now exists. The remaining opening here is theoretical, not empirical — explaining why flow-matching wins on noisy physiological signals.

**Unported opportunity.** Visual Contrastive Self-Distillation (Tier B) builds a label-free training signal from a contrast between the original input and a content-erased control, read through an EMA teacher. Community 5 (Wearable Sensing and Behavior) does not yet use this. Transfer hypothesis: replace "original image versus content-erased image" with "full sensor window versus channel-masked or band-masked window," and use the token-wise or step-wise likelihood difference from an EMA teacher as a self-distillation target for wearable representation learning — an asymmetry that needs no labels and no external teacher, which suits large unlabeled sensor corpora.

---

## News (major releases)

Google publicly released SensorFM on July 10, a wearable-health foundation model pretrained on more than one trillion minutes of sensor data from five million people, reporting wins on 34 of 35 health and behavioral tasks with frozen-embedding linear probes. Note for the record: the underlying paper, "Towards a General Intelligence and Interface for Wearable Health Data" (arXiv:2605.22759), is already in your knowledge graph from the May 21 digest, so this is a product-side release of work you have already filed, not a new paper.

Anthropic released Claude Opus 5 on July 24. Google released Gemini 3.6 Flash on July 21.

---

End of digest. Close this tab when done.
