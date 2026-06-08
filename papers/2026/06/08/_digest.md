# AI Digest — 2026-06-08

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A not done by 6 AM, stop.

Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.

Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

---

## Tier A — Deep Read

### SparDA: Sparse Decoupled Attention for Efficient Long-Context LLM Inference
Fu, Xiao, Dong, Han, Villa (NVlabs) — arXiv:2606.04511

**Problem.** Sparse attention for long-context LLM inference saves compute but still suffers from two bottlenecks: the KV cache grows linearly with sequence length (offloading to CPU introduces a PCIe transfer wall), and the sparse block selection step itself remains O(T^2), dominating attention cost at long contexts.

**Method.** SparDA adds a fourth per-layer linear projection called the Forecast alongside the standard Q, K, V. At layer L, the Forecast predicts which KV blocks layer L+1 will need, enabling lookahead prefetch that overlaps CPU-to-GPU transfer with the current layer's attention computation. The Forecast is decoupled from the attention query: one Forecast head per GQA group, adding less than 0.5% parameters. Training is lightweight — only the Forecast projections are trained by matching the original selector's attention distribution.

**Result.** On two 8B sparse-pretrained models: up to 1.25x prefill speedup, 1.7x decode speedup over sparse-attention offload baseline, and 5.3x higher decode throughput than non-offload sparse baseline by enabling larger batch sizes on a single GPU. Accuracy matches or slightly improves over the baseline.

**Limitations.** Evaluated only on 8B models; scaling behavior to 70B+ is unknown. Requires the model to be sparse-pretrained — retrofitting onto dense models is not addressed. The Forecast training assumes access to the original dense-attention distribution, which is expensive to compute at very long contexts.

**Why it matters to you.** The Forecast idea — using one layer's computation to predict the next layer's data access pattern — is a general systems trick. If you run patched Transformer models (PatchTST or similar) on long sensor recordings, this could cut single-GPU inference latency substantially. The architectural pattern is clean enough to reimplement.

**How this builds on what you know:** The paper directly extends the Q/K/V attention mechanism from Attention Is All You Need (Vaswani 2017), which sits at the center of your graphify graph in Community 2 (Transformer & SSM Architectures) with 12 edges. Where Vaswani defined attention as three projections, SparDA adds a fourth that serves a purely systems-level function — it does not change what attention computes, only how memory is managed during that computation. This separates the "what to attend to" question (Q/K/V) from the "where is the data physically" question (Forecast). The Mamba/SSM line in your library (Community 2: HARMamba, AudioMamba) attempts to solve the long-context problem by replacing attention entirely; SparDA takes the opposite approach of keeping attention but making its memory access pattern predictable.

Link: https://arxiv.org/abs/2606.04511

---

## Tier B — TLDR

### 1. Agent Planning Benchmark (APB): A Diagnostic Framework for Planning Capabilities in LLM Agents
Sun, Wang, Song et al. — arXiv:2606.04874

APB is a planning-specific diagnostic benchmark with 4,209 multimodal cases across 22 domains and five settings: holistic planning, step-wise planning with feedback, and robustness under extraneous tools, broken tools, and unsolvable tasks. Testing 12 MLLMs, APB reveals that even the best models fail at long-horizon planning, tool-noise robustness, and calibrated refusal (knowing when to say "I cannot do this"). Validation on ToolSandbox and tau-bench confirms that APB-guided refinement of plans improves downstream execution metrics.

**How this builds on what you know:** APB evaluates the planning capabilities that systems like ADaPT (Prasad 2023, graphify c0), LATS (Zhou 2024, graphify c0), and ToolkenGPT (Hao 2024, graphify c0) claim to provide. Where those papers proposed specific planning algorithms, APB provides the diagnostic to tell you which sub-skill is failing. This sits squarely in your Community 0 (LLM Agents & Reasoning). The cross_area_bridge between ADaPT and LATS in your graph is relevant: APB tests exactly the planning-decomposition capability those two papers address.

Link: https://arxiv.org/abs/2606.04874

### 2. Compress-Distill: Reasoning Trace Compression for Efficient Knowledge Distillation
Griot, Scotti, Abraham — arXiv:2606.05988

Reasoning models produce long chain-of-thought traces that are expensive to use as training data for knowledge distillation. This paper uses instruction-tuned compressor models to shrink traces to 8.6-21.0% of their original length before distilling them into smaller student models. Compressed traces reduce training tokens to 12-30%, speed up training by 2.0-7.6x, and shorten inference outputs by 3-19x. The trade-off is real: raw traces retain the highest downstream accuracy at every scale. However, model-compressed traces beat naive truncation, especially for 0.8B students under LoRA, reaching up to 96% of raw-trace accuracy with 18x per-token efficiency.

**How this builds on what you know:** This directly addresses the cost of distilling the kind of long reasoning traces that DeepSeek-R1 (graphify c0) produces. Where Chain-of-Thought (Wei 2023, graphify c0) showed longer reasoning improves accuracy and DeepSeek-R1 showed RL can train models to generate such traces, Compress-Distill asks: can we keep the reasoning quality but cut the distillation cost? The answer is a clear trade-off, not a free lunch.

Link: https://arxiv.org/abs/2606.05988

### 3. Ultralytics YOLO26: Unified Real-Time End-to-End Vision Models
Ultralytics — arXiv:2606.03748

YOLO26 is a new family of real-time object detectors (five scales, n/s/m/l/x) with three innovations: a dual-head NMS-free design removing DFL entirely, MuSGD (a Muon-SGD hybrid optimizer imported from LLM training), and STAL (a label assignment strategy guaranteeing positive coverage for small objects). Results: 40.9-57.5 mAP on COCO at 1.7-11.8 ms on T4 TensorRT. An open-vocabulary extension, YOLOE-26, handles text, visual, and prompt-free inference in a single pipeline.

**How this builds on what you know:** YOLO26 inherits from two lines in your Community 2. From DETR (Carion 2020, graphify c2), it takes the idea of NMS-free detection but achieves it without DETR's slow convergence. From Swin Transformer (Liu 2021, graphify c2), it draws on hierarchical feature processing. The most interesting cross-pollination is MuSGD: an optimizer technique from the LLM training community adapted for vision. This kind of method transfer is what your gap-watch tracks.

Link: https://arxiv.org/abs/2606.03748

---

## Tier C — Scan

1. **Predictable Scaling Laws of Optimal Hyperparameters for LLM Continued Pre-training** — Optimal hyperparameters follow stable scaling laws during continued pre-training. https://arxiv.org/abs/2606.05610

2. **AdaPlanBench: Evaluating Adaptive Planning in LLM Agents under World and User Constraints** — 307 household tasks with progressively revealed dual constraints; best model reaches only 67.75%. https://arxiv.org/abs/2606.05622

3. **UniCanvas: A Diffusion-based Unified Model for Text-in-Image Joint Generation** — Addresses the AR-vs-diffusion gap for unified text and image generation. https://arxiv.org/abs/2606.04264

4. **ExpWeaver: LLM Agents Learn from Experience via Latent RAG** — Stores past interaction traces in a latent space for experience-based agent planning. https://arxiv.org/abs/2606.01041

5. **RL Elicits Contextual Learning of Unseen Language Translation** — RL training lets LLMs leverage linguistic context for zero-shot translation of new languages. https://arxiv.org/abs/2606.06428

6. **LLM Compression with Jointly Optimizing Architectural and Quantization Choices** — Differentiable NAS for joint architecture and mixed-precision quantization of LLMs. https://arxiv.org/abs/2606.04063

---

## Time-Series / Bio-Sensing Gap Watch

No new time-series or bio-sensing papers appeared on arxiv from June 5-8 in the 2606 batch. Here are unported opportunities from this week's top papers:

**Unported Opportunity 1: SparDA's Forecast Projection for Long-Horizon Sensor Inference.** SparDA's idea of adding a lightweight Forecast projection to predict future memory access patterns (arXiv:2606.04511) has not been applied to time-series Transformers. For patched models like PatchTST processing recordings of 10,000+ timesteps, a Forecast-based KV cache manager could reduce single-GPU inference latency without changing the core attention computation. Transfer hypothesis: replace the per-layer Forecast with a per-patch-group predictor that forecasts which historical patch KV blocks are relevant for the next layer's cross-temporal attention.

**Unported Opportunity 2: YOLO26's STAL Label Assignment for Rare Event Detection in Biosignals.** YOLO26's STAL strategy guarantees positive coverage for small objects during training (arXiv:2606.03748). In biosignal event detection — arrhythmia episodes, seizure onsets, micro-sleep events — the analogous problem is that rare, short-duration events get overwhelmed by normal-activity training examples. Transfer hypothesis: adapt STAL's coverage guarantee to a 1D temporal detection head, ensuring that every annotated rare event receives at least one positive anchor assignment during training.

---

## News

1. **Apple WWDC 2026 (today, June 8).** Tim Cook is expected to announce a Gemini-powered Siri redesign, a multi-AI Extensions system bringing Claude as an iPhone option for the first time, and iOS 27 with third-party AI services configurable as defaults for Apple Intelligence features like Writing Tools.

2. **Microsoft Foundry catalog finalized** with 11,000 models including Claude Opus 4.8. Gemini 3.5 Pro and Claude Sonnet 4.8 are both expected before end of June.

3. **OpenAI GPT-5.5** variants (Pro, Instant) are in deployment; xAI released Grok 4.20 with multi-agent capabilities.

---

End of digest. Close this tab when done.
