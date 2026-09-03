## Mixture of Experts

### Timeline

2022 | ST-MoE (Zoph et al.) | 
2023 | MoE+Instruction (Shen et al.) | 
2024 | WaveToken (Masserano et al.) | 
2025 | MoE Explained (Unknown) | 

2026-09 | SMELT (2609.01343) | loops the middle half of a sparse mixture-of-experts Transformer twice at matched FLOPs, parameters and KV cache; 6.8 to 18.0 percent training-FLOP saving

### Paper List

[KNOWN] [2022] Zoph et al. — ST-MoE. zotero_key:WIGLUNFZ.
[KNOWN] [2023] Shen et al. — MoE+Instruction. zotero_key:UBDCML5N.
[KNOWN] [2024] Masserano et al. — WaveToken. zotero_key:MXKVRSKK.
[KNOWN] [2025] Unknown — MoE Explained. zotero_key:497XVFB6.

[2026] 2609.01343 — SMELT: Scaling Laws for Compute-Matched MoE Looped Transformers. [https://arxiv.org/abs/2609.01343](https://arxiv.org/abs/2609.01343). external.

### Recent Activity

2026-09-02 | 2609.01343 added | SMELT asks what a second visit to the same layers is worth once nothing else is allowed to grow, matching per-token FLOPs, total non-embedding parameters and KV cache at the same time on sparse mixture-of-experts Transformers rather than dense ones, and settling by ablation on a recipe that loops the middle half of the layers twice; fitting a separate Chinchilla-style scaling law per architecture across four sizes up to 54B non-embedding parameters, the looped frontier saves 6.8 to 18.0 percent of training FLOPs, and the downstream benchmark gain is larger than the validation-loss gap predicts, which is the second sighting in two weeks of loss and accuracy coming apart; where the Transformer (PHB9VRVM) fixed depth by stacking distinct layers, and where DeepSeek-V3 (2JCKA7GI) and ST-MoE (WIGLUNFZ) separated total parameters from activated parameters and treated that as the capacity dial, SMELT adds a third separation, between how many parameters exist and how many times each is used, and shows the two are not substitutes at fixed compute; the mechanistic account is that the second visit reduces the attention sink and moves attention mass onto content tokens, which predicts the observed growth of the advantage with sample length and with the number of in-context examples but is a correlation rather than a manipulation; budget matching is three-way and not four-way, so wall-clock and memory traffic are untested, and the fits stop below the sizes the recipe would be used at; Tier A

2026-05-14 | Area page seeded | 4 papers from Zotero, 0 from graphify seed.
