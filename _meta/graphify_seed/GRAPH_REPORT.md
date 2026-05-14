# Graph Report - /tmp/graphify_zotero_sample  (2026-04-10)

## Corpus Check
- Corpus is ~0 words - fits in a single context window. You may not need a graph.

## Summary
- 65 nodes · 114 edges · 10 communities detected
- Extraction: 79% EXTRACTED · 21% INFERRED · 0% AMBIGUOUS · INFERRED: 24 edges (avg confidence: 0.73)
- Token cost: 0 input · 0 output

## God Nodes (most connected - your core abstractions)
1. `Attention Is All You Need (Vaswani 2017)` - 12 edges
2. `Self-supervised Learning for HAR with 700K Person-days (Yuan 2024)` - 8 edges
3. `Chain-of-Thought Prompting (Wei 2023)` - 7 edges
4. `TS-Agent: Time Series Reasoning Agent (Liu 2025)` - 7 edges
5. `Sensor2Text: NL Interactions for Activity Tracking (Chen 2024)` - 7 edges
6. `HARMamba: Bidirectional Mamba for HAR (Li 2024)` - 6 edges
7. `Foundation Models for Biosignals: A Survey (Gu 2025)` - 6 edges
8. `DALL-E 2: Hierarchical Text-Conditional Image Gen (Ramesh 2022)` - 5 edges
9. `SigLIP: Sigmoid Loss for Language Image Pre-Training (Zhai 2023)` - 5 edges
10. `Denoising Diffusion Probabilistic Models (Ho 2020)` - 4 edges

## Surprising Connections (you probably didn't know these)
- `CycleGAN: Unpaired Image Translation (Zhu 2020)` --semantically_similar_to--> `Denoising Diffusion Probabilistic Models (Ho 2020)`  [INFERRED] [semantically similar]
  Zhu et al_2020_CycleGAN.pdf → Ho et al_2020_Denoising Diffusion Probabilistic Models.pdf
- `Sensor2Text: NL Interactions for Activity Tracking (Chen 2024)` --semantically_similar_to--> `LLMs are Few-Shot Health Learners (Liu 2023)`  [INFERRED] [semantically similar]
  Chen et al. - 2024 - Sensor2Text.pdf → Liu et al. - 2023 - Large Language Models are Few-Shot Health Learners.pdf
- `DeepSeek-R1: Reasoning via RL (2025)` --semantically_similar_to--> `Chain-of-Thought Prompting (Wei 2023)`  [INFERRED] [semantically similar]
  DeepSeek-AI et al. - 2025 - DeepSeek-R1.pdf → Wei et al. - 2023 - Chain-of-Thought Prompting.pdf
- `ADaPT: As-Needed Decomposition and Planning (Prasad 2023)` --semantically_similar_to--> `LATS: Language Agent Tree Search (Zhou 2024)`  [INFERRED] [semantically similar]
  Prasad et al. - 2023 - ADaPT.pdf → Zhou et al. - 2024 - LATS.pdf
- `ToolkenGPT: Tool Embeddings for LLMs (Hao 2024)` --semantically_similar_to--> `PyVision: Agentic Vision with Dynamic Tooling (Zhao 2025)`  [INFERRED] [semantically similar]
  Hao et al. - 2024 - ToolkenGPT.pdf → Zhao et al. - 2025 - PyVision.pdf

## Hyperedges (group relationships)
- **Mamba/SSM Architecture Applications** — li2024_harmamba, erol2024_audiomamba, liu2024_swinumamba, concept_mamba_ssm [EXTRACTED 0.90]
- **Time Series + LLM Reasoning Ecosystem** — xie2025_chatts, liu2025_tsagent, zhang2024_llm_ts_survey, chen2024_sensor2text, concept_ts_llm [INFERRED 0.85]
- **Wearable Sensing for Health & Behavior** — yuan2024_ssl_har, xu2023_globem, nepal2024_mindscape, gu2025_biosignals, baur2024_hear, chen2024_sensor2text [INFERRED 0.85]
- **LLM Agent Architectures** — prasad2023_adapt, zhou2024_lats, hong2026_deepeyesv2, zhao2025_pyvision, hao2024_toolkengpt, huang2026_memory [INFERRED 0.80]
- **Self-Supervised Pretraining Methods** — yuan2024_ssl_har, chen2023_pathology, zhang2023_mae, baur2024_hear, concept_self_supervised [EXTRACTED 0.90]

## Communities

### Community 0 - "LLM Agents & Reasoning"
Cohesion: 0.23
Nodes (14): LLM-based Agents, LLM Reasoning, Tool Use in LLMs, DeepSeek-V3 Technical Report (2024), DeepSeek-R1: Reasoning via RL (2025), Agent AI: Surveying Multimodal Interaction (Durante 2024), ToolkenGPT: Tool Embeddings for LLMs (Hao 2024), DeepEyesV2: Agentic Multimodal Model (Hong 2026) (+6 more)

### Community 1 - "Health AI & Self-Supervised Learning"
Cohesion: 0.31
Nodes (11): HeAR: Health Acoustic Representations (Baur 2024), General-Purpose Self-Supervised Model for Pathology (Chen 2023), Human Activity Recognition, Health AI / Digital Health, Masked Autoencoder, Self-Supervised Learning, Foundation Models for Biosignals: A Survey (Gu 2025), CounselBench: LLM Benchmarking in Mental Health (Li 2025) (+3 more)

### Community 2 - "Transformer & SSM Architectures"
Cohesion: 0.33
Nodes (10): DETR: End-to-End Object Detection with Transformers (Carion 2020), Mamba / State Space Models, Self-Attention Mechanism, Transformer Architecture, Audio Mamba: Bidirectional SSM for Audio (Erol 2024), Wavelet Convolutions for Large Receptive Fields (Finder 2024), HARMamba: Bidirectional Mamba for HAR (Li 2024), Swin Transformer (Liu 2021) (+2 more)

### Community 3 - "Vision-Language & Generative Models"
Cohesion: 0.46
Nodes (8): Contrastive Learning, Diffusion Models, Vision-Language Models, Denoising Diffusion Probabilistic Models (Ho 2020), DiT: Scalable Diffusion Models with Transformers (Peebles 2023), DALL-E 2: Hierarchical Text-Conditional Image Gen (Ramesh 2022), SigLIP 2: Multilingual Vision-Language Encoders (Tschannen 2025), SigLIP: Sigmoid Loss for Language Image Pre-Training (Zhai 2023)

### Community 4 - "Time Series + LLM Integration"
Cohesion: 0.9
Nodes (5): Sensor2Text: NL Interactions for Activity Tracking (Chen 2024), Time Series + LLM Integration, TS-Agent: Time Series Reasoning Agent (Liu 2025), ChatTS: Aligning Time Series with LLMs (Xie 2025), LLMs for Time Series: A Survey (Zhang 2024)

### Community 5 - "Wearable Sensing & Behavior"
Cohesion: 0.5
Nodes (5): Wearable Sensor Data, Adam Optimizer (Kingma & Ba 2017), MindScape: LLM + Behavioral Sensing Journaling (Nepal 2024), GLOBEM: Multi-Year Human Behavior Datasets (Xu 2023), CycleGAN: Unpaired Image Translation (Zhu 2020)

### Community 6 - "Model Interpretability & Fairness"
Cohesion: 0.6
Nodes (5): Model Interpretability, Comprehensible Classification Models (Freitas 2014), SHAP: Unified Model Interpretation (Lundberg 2017), Introduction to Causal Inference (Pearl 2010), Actionable Recourse in Linear Classification (Ustun 2019)

### Community 7 - "Reinforcement Learning"
Cohesion: 1.0
Nodes (4): Reinforcement Learning, Offline Reinforcement Learning Tutorial (Levine 2020), Sample-efficient Cross-Entropy Method (Pinneri 2020), Off-Policy Policy Evaluation Study (Voloshin 2021)

### Community 8 - "Sparse Matrix Methods"
Cohesion: 1.0
Nodes (2): L1 Minimization for Sparse Representation (Donoho 2003), CUR Matrix Decompositions (Mahoney 2009)

### Community 9 - "Video Action Recognition"
Cohesion: 1.0
Nodes (1): Deep Video Action Recognition Survey (Zhu 2020)

## Knowledge Gaps
- **8 isolated node(s):** `DeepSeek-V3 Technical Report (2024)`, `CounselBench: LLM Benchmarking in Mental Health (Li 2025)`, `Introduction to Causal Inference (Pearl 2010)`, `Deep Video Action Recognition Survey (Zhu 2020)`, `Wavelet Convolutions for Large Receptive Fields (Finder 2024)` (+3 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Sparse Matrix Methods`** (2 nodes): `L1 Minimization for Sparse Representation (Donoho 2003)`, `CUR Matrix Decompositions (Mahoney 2009)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Video Action Recognition`** (1 nodes): `Deep Video Action Recognition Survey (Zhu 2020)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Attention Is All You Need (Vaswani 2017)` connect `Transformer & SSM Architectures` to `Health AI & Self-Supervised Learning`, `Vision-Language & Generative Models`, `Time Series + LLM Integration`?**
  _High betweenness centrality (0.354) - this node is a cross-community bridge._
- **Why does `Sensor2Text: NL Interactions for Activity Tracking (Chen 2024)` connect `Time Series + LLM Integration` to `Health AI & Self-Supervised Learning`, `Transformer & SSM Architectures`, `Wearable Sensing & Behavior`?**
  _High betweenness centrality (0.272) - this node is a cross-community bridge._
- **Why does `TS-Agent: Time Series Reasoning Agent (Liu 2025)` connect `Time Series + LLM Integration` to `LLM Agents & Reasoning`?**
  _High betweenness centrality (0.241) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `Self-supervised Learning for HAR with 700K Person-days (Yuan 2024)` (e.g. with `General-Purpose Self-Supervised Model for Pathology (Chen 2023)` and `HeAR: Health Acoustic Representations (Baur 2024)`) actually correct?**
  _`Self-supervised Learning for HAR with 700K Person-days (Yuan 2024)` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `TS-Agent: Time Series Reasoning Agent (Liu 2025)` (e.g. with `Tool Use in LLMs` and `ChatTS: Aligning Time Series with LLMs (Xie 2025)`) actually correct?**
  _`TS-Agent: Time Series Reasoning Agent (Liu 2025)` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Are the 4 inferred relationships involving `Sensor2Text: NL Interactions for Activity Tracking (Chen 2024)` (e.g. with `Time Series + LLM Integration` and `LLMs are Few-Shot Health Learners (Liu 2023)`) actually correct?**
  _`Sensor2Text: NL Interactions for Activity Tracking (Chen 2024)` has 4 INFERRED edges - model-reasoned connections that need verification._
- **What connects `DeepSeek-V3 Technical Report (2024)`, `CounselBench: LLM Benchmarking in Mental Health (Li 2025)`, `Introduction to Causal Inference (Pearl 2010)` to the rest of the system?**
  _8 weakly-connected nodes found - possible documentation gaps or missing edges._