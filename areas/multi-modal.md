## Multi-Modal Learning

### Timeline

2021 | ViT (Dosovitskiy et al.) | 
2022 | DALL-E 2 (Ramesh et al.) | 
2022 | Flamingo (Alayrac et al.) | 
2023 | BLIP-2 (Li et al.) | 
2023 | FLIP (Li et al.) | 
2025 | Machine Mental Imagery (Yang et al.) | 

2026-05 | MicroWorld (2605.10120) | attributed knowledge graph grounds a multimodal LLM in microscopy images
2026-05 | DLLM-VSR (2605.28456) | diffusion-LLM does lip reading by confidence-ordered masked denoising

2026-06 | TIGER (2606.00232) | graph-based evidence routing for multimodal hallucination repair
2026-06 | Layered Knowledge Infusion (2606.06356) | maps four knowledge-injection points in iterative generative models to four intervention layers
2026-06 | ARM (2606.11188) | unified autoregressive multimodal model over discrete tokens for understanding, generation, and editing
2026-06 | UXBench (2606.13192) | multimodal benchmark for fine-grained user-interface experience diagnosis
2026-06 | Multilingual VLA Gap (2606.15714) | first multilingual test for vision-language-action models; MPCA realigns non-English representations after action fine-tuning
2026-06 | IPT (2606.03988) | imaginative perception tokens carry the reasoning trace into a perceptual modality instead of text for spatial tasks

2026-06 | PerceptionDLM (2606.19534) | discrete diffusion language backbone decodes tokens in parallel to describe several masked image regions at once
2026-07 | Perceive-to-Reason (2607.01191) | splits fine-grained visual reasoning into a Perceiver that localizes the region and a Reasoner that answers over the crop
2026-07 | SenseNova-Vision (2607.06560) | poses detection, OCR, segmentation, depth, and pose as one generation problem in a unified multimodal model
2026-07 | MentalThink (2607.03530) | a multimodal model reasons over an executable SVG drawing surface it renders and revises across turns
2026-07 | Light-Omni (2607.05511) | dual-state memory (consolidated global script plus latent action state) gives reflexive long-video answers in near-constant time
2026-07 | VideoChat3 (2607.14935) | fully open 4B video MLLM with an inflated 3D ViT and adaptive frame resolution for cheaper streaming perception
### Paper List

[KNOWN] [2021] Dosovitskiy et al. — ViT. zotero_key:B7F2Q998.
[KNOWN] [2022] Ramesh et al. — DALL-E 2. zotero_key:DUERBZGM.
[KNOWN] [2022] Alayrac et al. — Flamingo. zotero_key:SC8KWYVK.
[KNOWN] [2023] Li et al. — BLIP-2. zotero_key:4N5WXKPI.
[KNOWN] [2023] Li et al. — FLIP. zotero_key:64H6TK5Y.
[KNOWN] [2025] Yang et al. — Machine Mental Imagery. zotero_key:NSI6PVD7.

[2026] 2605.10120 — MicroWorld: Bridging the Microscopic Domain Gap for Multimodal LLMs. [https://arxiv.org/abs/2605.10120](https://arxiv.org/abs/2605.10120). external.
[2026] 2605.28456 — Diffusion Large Language Models for Visual Speech Recognition (DLLM-VSR). [https://arxiv.org/abs/2605.28456](https://arxiv.org/abs/2605.28456). external.

[2026] 2606.00232 — TIGER: Traceable Inference with Graph-Based Evidence Routing for Mitigating Hallucinations. [https://arxiv.org/abs/2606.00232](https://arxiv.org/abs/2606.00232). external.
[2026] 2606.06356 — Where Should Knowledge Enter? A Layered Framework for Knowledge Infusion in Multimodal Iterative Generative Models. [https://arxiv.org/abs/2606.06356](https://arxiv.org/abs/2606.06356). external.

[2026] 2606.11188 — ARM: An AutoRegressive Large Multimodal Model with Unified Discrete Representations. [https://arxiv.org/abs/2606.11188](https://arxiv.org/abs/2606.11188). external.
[2026] 2606.13192 — Reasoning for Mobile User Experience with Multimodal LLMs: Task, Benchmark, and Approach. [https://arxiv.org/abs/2606.13192](https://arxiv.org/abs/2606.13192). external.
[2026] 2606.15714 — Beyond English: Uncovering the Multilingual Gap in Vision-Language-Action Models. [https://arxiv.org/abs/2606.15714](https://arxiv.org/abs/2606.15714). external.
[2026] 2606.03988 — Imaginative Perception Tokens Enhance Spatial Reasoning in Multimodal Language Models. [https://arxiv.org/abs/2606.03988](https://arxiv.org/abs/2606.03988). external.

[2026] 2606.19534 — PerceptionDLM: Parallel Region Perception with Multimodal Diffusion Language Models. [https://arxiv.org/abs/2606.19534](https://arxiv.org/abs/2606.19534). external.
[2026] 2607.01191 — Perceive-to-Reason: Decoupling Perception and Reasoning for Fine-Grained Visual Reasoning. [https://arxiv.org/abs/2607.01191](https://arxiv.org/abs/2607.01191). external.
[2026] 2607.06560 — Vision as Unified Multimodal Generation (SenseNova-Vision). [https://arxiv.org/abs/2607.06560](https://arxiv.org/abs/2607.06560). external.

[2026] 2607.03530 — MentalThink: Shaping Thoughts in Mental SVG World. [https://arxiv.org/abs/2607.03530](https://arxiv.org/abs/2607.03530). external.
[2026] 2607.05511 — Light-Omni: Reflex over Reasoning in Agentic Video Understanding with Long-Term Memory. [https://arxiv.org/abs/2607.05511](https://arxiv.org/abs/2607.05511). external.
[2026] 2607.14935 — VideoChat3: Fully Open Video MLLM for Efficient and Generalist Video Understanding. [https://arxiv.org/abs/2607.14935](https://arxiv.org/abs/2607.14935). external.

### Recent Activity

2026-07-17 | 2607.14935 added | VideoChat3 is a fully open 4B video multimodal LLM that introduces an Inflated 3D Vision Transformer and Adaptive Frame Resolution to cut the cost of turning video into tokens, releases a video data synthesis pipeline plus general, long-form, and streaming training sets, and reports beating prior open-source models of equal or larger size across those benchmarks; Tier B
2026-07-14 | 2607.05511 added | Light-Omni keeps two states in one forward pass, a consolidated global script from hierarchical memory merging and a latent action state, so it answers long-video questions reflexively without search-then-aggregate loops; against M3-Agent it reports a 2.4% accuracy gain, a 12.1x speedup, 2.6x better GPU memory use, and near-constant ~2.3s latency regardless of video length; Tier B
2026-07-13 | 2607.03530 added | a multimodal model writes SVG code as an intermediate reasoning step, renders it deterministically, reads the image back, and revises over several turns under reinforcement learning; reports 55.1% on VSIBench and 76.0% on MindCube; Tier A
2026-07-09 | 2607.06560 added | SenseNova-Vision poses many vision tasks (detection, OCR, keypoints, segmentation, depth, normals, camera pose) as one generation problem with no task-specific heads, training on a 50M instruction-response corpus converted from standard annotations and matching leading task-specialized systems; Tier B
2026-07-02 | 2607.01191 added | P2R separates a Perceiver that localizes the question-relevant region from a Reasoner that answers over the crop, trained with alternating PRA-GRPO from final-answer reward alone and no bounding-box labels, reaching 93.2% on V-Star and 80.5% on HR-Bench-8K; Tier B
2026-06-25 | 2606.19534 added | multimodal model on a discrete diffusion language backbone; parallel token decoding with structured masking describes several regions at once for an inference-efficiency gain; Tier B
