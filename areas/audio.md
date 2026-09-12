## Audio Representation Learning

### Timeline

2020 | TRILL (Shor et al.) | 
2021 | AST (Gong et al.) | 
2021 | FRILL (Peplinski et al.) | 
2021 | PSLA (Gong et al.) | 
2022 | Audio MAE (Huang et al.) | 
2022 | CLAP (Elizalde et al.) | 
2023 | LTU (Gong et al.) | 
2024 | HeAR (Baur et al.) | 
2024 | OPERA (Zhang et al.) | 

2026-09 | X-AuT (2609.11412) | audio-encoder layers chosen for removal by behavioral probes and repaired by cross-scale distillation; 18 to 16 layers cut macro-average error from 5.61 to 5.27 percent

### Paper List

[KNOWN] [2020] Shor et al. — TRILL. zotero_key:WJQ5APZU.
[KNOWN] [2021] Gong et al. — AST. zotero_key:7J6K6W8I.
[KNOWN] [2021] Peplinski et al. — FRILL. zotero_key:4A2A73JF.
[KNOWN] [2021] Gong et al. — PSLA. zotero_key:MB3HH9SR.
[KNOWN] [2022] Huang et al. — Audio MAE. zotero_key:65EDEWIJ.
[KNOWN] [2022] Elizalde et al. — CLAP. zotero_key:KNGZCC5J.
[KNOWN] [2023] Gong et al. — LTU. zotero_key:ESEEEH85.
[KNOWN] [2024] Baur et al. — HeAR. zotero_key:3LA8GNCU.
[KNOWN] [2024] Zhang et al. — OPERA. zotero_key:T2T4DUKA.

[2026] 2609.11412 — X-AuT: Progressive Audio-Encoder Compression for Speech LLMs with Cross-Scale Distillation. [https://arxiv.org/abs/2609.11412](https://arxiv.org/abs/2609.11412). external.

### Recent Activity

2026-09-11 | 2609.11412 added | X-AuT removes layers from the audio encoder of a speech language model without the deletion and premature end-of-sequence errors that whole-block pruning normally produces: layer combinations are chosen by short behavioral probes rather than weight-magnitude heuristics, and the pruned encoder is repaired by representation alignment, cross-scale distillation from a larger teacher, scheduled student-policy supervision and LoRA finetuning while the language backbone stays frozen. Compressing Qwen3-ASR-0.6B from 18 to 16 encoder layers reduced macro-average error from 5.61 to 5.27 percent across ten Chinese-English benchmarks, and the 14-layer model reached 5.75 percent with 20.7 percent fewer audio-tower parameters against 6.73 percent for direct rather than progressive pruning. Where Audio Mamba (6VTXUZEG) attacked encoder cost by replacing attention with a state-space model and retraining from scratch, X-AuT keeps the trained transformer and removes depth from it, because a pretrained encoder attached to a frozen language model is an asset that an architecture swap discards; where HeAR (3LA8GNCU) established that a general health-acoustic encoder transfers across tasks and left inference cost alone, this supplies the compression recipe such an encoder would need on a device; and where Attention Is All You Need (PHB9VRVM) made stacked depth the unit of encoder capacity, the finding that 18 to 16 layers improved accuracy says the original depth sat on the wrong side of the capacity-noise trade-off for this decoder. The methodological point is the path rather than the endpoint, since progressive and direct pruning reach the same final depth at 5.75 against 6.73 percent, so the intermediate depths carry information the endpoint does not. The reusable pattern is frozen backbone, prune the encoder, distill across scales, which is the shape of most wearable-plus-language-model systems, and the behavioral-probe selection step matters more than the pruning, since choosing which layers to drop by measuring downstream behavior rather than weight statistics has not been applied to physiological encoders, where the equivalent probe would test whether a pruned encoder still separates clinically distinct signal patterns. Treat the 0.34-point improvement as suggestive rather than established, because the abstract reports single-run results and states that the effect varies across benchmarks; Tier B

2026-05-14 | Area page seeded | 9 papers from Zotero, 1 from graphify seed.
