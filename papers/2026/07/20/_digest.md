# AI Digest — 2026-07-20

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A not done by 6 AM, stop.
Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.
Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

---

## Tier A — deep read (1 paper, ~20 min)

### Understanding Reasoning from Pretraining to Post-Training (arXiv:2607.16097)
Shen, Li, Rahman, Sun, Goldblum, Telgarsky, Izmailov. #2 paper of the day on Hugging Face.

**Problem.** Reinforcement learning has become the standard way to raise a language model's reasoning score, but it is almost always studied on its own, cut off from the pretraining that came before it. Two basic questions stay open: how do pretraining choices (model size, amount of data) change the payoff from spending compute on RL, and what does RL actually change inside the model. These questions are hard to answer with ordinary language models because the pretraining corpus is enormous and uncontrolled, so a behavior cannot be traced back to pretraining versus RL, and running full compute sweeps across both stages costs too much.

**Method.** The authors use chess as a controlled testbed. They follow the normal language-model pipeline but on a domain they can measure exactly: pretrain models from 5M to 1B parameters on human chess games, run supervised fine-tuning on synthetic reasoning traces, then run RL on chess puzzles with a verifiable reward (the move is right or wrong). Because the domain is closed and the reward is exact, they can sweep both stages and attribute each behavior to the stage that produced it. They then repeat the key test on a 1B model trained on mathematics text to check that the pattern is not a chess artifact.

**Result.** Post-RL performance at a given RL compute level is well predicted by the pretraining loss, and the slope of the RL reward curve rises roughly linearly with the number of pretraining tokens. So a longer-pretrained checkpoint not only starts higher, it also improves faster once RL begins. On what RL does to the model: it does not simply sharpen the fine-tuned policy. On easy puzzles it amplifies correct moves the fine-tuned policy already favored; on hard puzzles it surfaces correct moves that were nearly absent before RL. The mathematics run reproduces the predictive pattern: longer-pretrained checkpoints reach higher post-RL scores and improve faster.

**Limitations.** Chess and single-domain mathematics are clean but narrow; the reward is exact, which real reasoning tasks rarely are. Model sizes stop at 1B, so the linear-slope relationship is not yet checked at frontier scale where the returns to RL may bend. The study measures outcome accuracy, not whether the surfaced moves reflect a general reasoning skill or memorized puzzle patterns.

**Why it matters to Leo.** This gives a quantitative account of the pretraining-to-RL interface, which is the exact seam Leo watches for porting to time-series and bio-sensing. If pretraining loss predicts post-RL gains for a forecaster, a lab could decide how much to pretrain a numeric time-series model before spending scarce reward budget on RL fine-tuning, rather than guessing. The "hard cases surface new correct moves" finding is a testable claim for time-series reasoning: does RL on rare-event forecasting surface behaviors absent after supervised fine-tuning.

**How this builds on what you know:** The two closest parents in your library are Chain-of-Thought Prompting (Wei 2023, in nlp.md, graphify community 0) and DeepSeek-R1 (2025, in llm.md, community 0). Where Wei showed that reasoning ability could be elicited from a fixed pretrained model through prompting, and DeepSeek-R1 showed that reasoning could be trained in directly through RL with verifiable rewards, this paper does the missing measurement: it asks how the earlier pretraining decides the ceiling and the speed of that RL stage, because neither parent separated the contribution of pretraining from the contribution of RL. This paper extends the DeepSeek-R1 -> Chain-of-Thought bridge, which already crossed the reasoning-via-RL and reasoning-via-prompting communities in your library. The new work pushes the bridge further into the science-of-scaling direction: it replaces the "RL just works" framing with a predictive relationship between pretraining loss and post-RL reward.

---

## Tier B — TLDRs (3 papers, ~10 min)

### Cura 1T: Specialized Model for Agentic Healthcare (arXiv:2607.15314)
actAVA AI et al. Cura 1T is a healthcare-specialized language model trained through a human-gated self-evolution loop. In each round a training agent picks a target capability, trains the model, reads the benchmark trajectories, and rewrites the data mixture from the observed failures, rather than doing one generic medical-data update. This data-centered loop is meant to stop the usual problem where fixing one healthcare skill (consultation, clinical reasoning over text and images, interactive diagnosis, electronic health record tool use) degrades another. Across the healthcare evaluation suite the model ranks at or near the top among frontier baselines while staying competitive on out-of-domain reasoning and agentic benchmarks.

**How this builds on what you know:** The parents in your library are LLMs are Few-Shot Health Learners (Liu 2023, llm-health.md, graphify community 1), CounselBench (Li 2025, llm-health.md, community 1), and Foundation Models for Biosignals (Gu 2025, sits in both time-series.md and llm-health.md, community 1). Where Liu 2023 showed a general model could answer health questions from a few examples and CounselBench measured where such models fail in mental-health advice, this paper does the closed-loop fix: it turns those measured failures into the training signal itself, because a single medical fine-tune cannot cover consultation, imaging, and tool use at once. Where Gu 2025 surveyed static biosignal foundation models, Cura 1T is an agentic system whose data mixture changes each round, so it sits on the self-improving-system branch rather than the fixed-encoder branch.

### On-Policy Delta Distillation (OPD^2) (arXiv:2607.15161)
Heo, Hwang, Yun, Han (NAVER AI Lab). On-policy distillation transfers a teacher's reasoning by giving token-level supervision on the student's own rollouts, which sidesteps the need for a reward model. This paper changes the target: instead of imitating the teacher's full output distribution, it distills the delta signal, the difference between the reasoning-tuned teacher and its base model before instruction tuning. That difference isolates what reasoning tuning actually added, so the student receives a cleaner transfer signal. Across mathematics, science, and code-reasoning benchmarks OPD^2 beats standard on-policy distillation, and the gains hold across several Qwen3 sizes in both thinking and non-thinking modes and transfer to Gemma 4, with only a short post-training period.

**How this builds on what you know:** The parents are DeepSeek-R1 (2025, llm.md, community 0) and Chain-of-Thought Prompting (Wei 2023, nlp.md, community 0). Where DeepSeek-R1 produced reasoning ability through RL and left an expensive teacher, this paper does cheap transfer of exactly that ability, because copying the whole teacher distribution also copies its base-model behavior that the student already has. The delta idea, subtracting the base model from the tuned teacher, is the same "measure what tuning added" move that the Tier A chess paper makes by comparing fine-tuned and post-RL policies, so the two papers point at the same question from opposite ends.

### S1-Omni: A Unified Multimodal Reasoning Model for Scientific Understanding, Prediction, and Generation (arXiv:2607.15686)
Zhao, Liu, Xu et al. (ScienceOne-AI). S1-Omni maps heterogeneous scientific objects (crystal structure files, molecular SMILES strings, protein sequences, spectra, and scientific images) plus natural-language instructions into one shared representation, then uses task-specific decoders for property prediction, spectrum-to-molecule generation, protein site and structure prediction, and scientific image generation and editing. It is trained on a corpus covering 200 scientific tasks with millions of reasoning samples and evaluated on more than 60 benchmarks, where it reportedly outperforms GPT-5.5 and Gemini-3.1-Pro on most and matches domain-specific models on several. The claim is that scientific model capabilities, today split across many narrow tools, can be consolidated into a single reasoning model.

**How this builds on what you know:** The parents in your library are DALL-E 2 (Ramesh 2022, multi-modal.md, graphify community 3) and DiT (Peebles 2023, generative-cv.md, community 3). Where DALL-E 2 aligned text and images in one embedding space and DiT showed a transformer backbone could drive diffusion generation, this paper does the same shared-space-plus-decoder move but across many scientific modalities at once, because a spectrum or a protein sequence needs a domain-native decoder rather than a pixel decoder. No direct scientific-modality parent sits in your library yet; the closest neighbors are these two generative vision-language anchors in community 3.

---

## Tier C — scan headlines (8 papers, ~5 min)

- xHC: Expanded Hyper-Connections (arXiv:2607.14530) — widens residual hyper-connections into a larger mixing space for cheaper depth scaling. https://arxiv.org/abs/2607.14530
- Xiaomi-Robotics-1 (arXiv:2607.15330) — vision-language-action model scaled on 100K+ hours of real-world robot trajectories. https://arxiv.org/abs/2607.15330
- Recursive Harness Self-Improvement (arXiv:2607.15524, Sakana AI) — agent rewrites its own evaluation harness to keep improving. https://arxiv.org/abs/2607.15524
- DSWorld: A Data Science World Model for Efficient Autonomous Agents (arXiv:2607.15901) — learned world model of data-science workflows for planning. https://arxiv.org/abs/2607.15901
- Audio-Visual Flamingo (arXiv:2607.16107, NVIDIA) — open audio-visual model for long and complex video understanding. https://arxiv.org/abs/2607.16107
- VideoRAE (arXiv:2607.14088) — adapts video foundation models for generation via representation autoencoders. https://arxiv.org/abs/2607.14088
- RAGU (arXiv:2607.11683) — multi-step GraphRAG engine with a compact domain-adapted language model. https://arxiv.org/abs/2607.11683
- RecGPT-V3 Technical Report (arXiv:2607.15591) — generative recommendation model scaled to production. https://arxiv.org/abs/2607.15591

---

## Tier D — Time-series / Bio-sensing Gap Watch

No time-series or bio-sensing paper qualified from today's Hugging Face front page, so the reference lists for "already ported" (graphify Community 4, Time Series + LLM Integration; Community 5, Wearable Sensing and Behavior) are unchanged. Two unported opportunities stand out from today's top language and multimodal papers.

Delta-signal distillation (OPD^2, above) is unported to time-series foundation models. Transfer hypothesis: take a reasoning-tuned forecaster and its base forecaster, distill only the difference between them into a small student, so the student picks up the added forecasting-reasoning behavior without re-copying the base numeric backbone it already has. Community 4 covers attaching a language model to a time series, but not delta distillation of a reasoning-tuned forecaster, so this is open.

Unified heterogeneous-modality representation (S1-Omni, above) is unported to wearable sensing. Transfer hypothesis: map heterogeneous wearable streams (PPG, IMU, ECG, temperature) plus natural-language instructions into one shared space with per-signal decoders, the way S1-Omni handles spectra, sequences, and images. Community 5 covers single-stream wearable sensing and behavior modeling, but not a single shared-space model with signal-native decoders across all wearable channels at once.

---

## News (major releases only)

xAI released Grok 4.5, a 1.5-trillion-parameter mixture-of-experts model trained partly on coding-tool interaction data; on Terminal-Bench 2.1 it reportedly scored 83.3% while using about a quarter of the output tokens that Opus 4.8 used on similar tasks. This is relevant to the MoE area in your library. Meta released Muse Spark 1.1, a 1M-token-context agentic model with its first paid developer API in public preview and desktop, browser, and mobile computer use. Anthropic reported an interpretability result: a Jacobian-based method (the J-lens) located a small internal subspace of about 25 active concepts, under 10% of activation variance, whose removal collapses multi-step reasoning while leaving fluency intact, and open-sourced the method with a demo.

---

End of digest. Close this tab when done.
