## Reasoning in Language Models

### What

Reasoning research studies how language models perform multi-step inference, including arithmetic, logical deduction, planning, and commonsense reasoning. Methods range from prompting strategies (chain-of-thought, self-consistency) to architectural changes (latent reasoning in continuous space) and training-time interventions (reinforcement learning for reasoning traces).

### Why

Standard LLMs often fail on tasks requiring more than pattern matching: multi-hop questions, constraint satisfaction, or mathematical derivations. Improving reasoning ability is necessary for reliable use in scientific, legal, and medical settings where answers must follow from premises rather than statistical correlation.

### Baseline

Prompt the LLM with a direct question (no intermediate steps). The main failure mode is that the model produces a plausible-sounding but incorrect answer because it skips intermediate reasoning steps that would expose errors.

### Running Example

Solve the GSM8K problem: 'Janet has 16 eggs per day. She eats 3 for breakfast and bakes 4 into muffins. She sells the rest at $2 each. How much does she earn daily?' The correct answer is $18. Direct prompting of a mid-sized LLM often yields $26 or $32 because the model conflates subtraction steps.

### Baseline vs Method Comparison on the Running Example

| Approach | Output on running example | Why it differs from baseline |
|---|---|---|
| Baseline | See running example above | (anchor) |
| Chain-of-Thought Prompting | _To be added as papers accumulate._ | Anchor paper for this area |

### Timeline

2025 | CODI (Shen et al.) | 
2025 | Large Multimodal Reasoning Survey (Li et al.) | 
2025 | Latent Reasoning Survey (Zhu et al.) | 
2025 | Machine Mental Imagery (Yang et al.) | 
2025 | Soft Thinking (Zhang et al.) | 
2026 | Chain of Superposition (Deng et al.) | 
2026 | CoLaR (Tan et al.) | 
2026 | Latent Space Survey (Yu et al.) | 
2026 | Latent-GRPO (Deng et al.) | 
2026 | PonderLM (Zeng et al.) | 

### Key Methods

| Method | Year | Core idea (one clause) | Best benchmark result | Cost / limitation |
|---|---|---|---|---|
| Chain-of-Thought Prompting | Wei 2023 | Anchor method | _To be filled_ | _To be filled_ |

### Benchmark Results

| Method | Benchmark | Metric | Score | Source paper |
|---|---|---|---|---|
| _To be added as papers accumulate._ | | | | |

### Limitations

_To be added as papers accumulate._

### Paper List

[KNOWN] [2025] Shen et al. — CODI. zotero_key:FFWLYL3J.
[KNOWN] [2025] Li et al. — Large Multimodal Reasoning Survey. zotero_key:FPEC4PIH.
[KNOWN] [2025] Zhu et al. — Latent Reasoning Survey. zotero_key:EMXEJYHV.
[KNOWN] [2025] Yang et al. — Machine Mental Imagery. zotero_key:PDAMP7VF.
[KNOWN] [2025] Zhang et al. — Soft Thinking. zotero_key:EGRXFZU9.
[KNOWN] [2026] Deng et al. — Chain of Superposition. zotero_key:CXGMDHJ3.
[KNOWN] [2026] Tan et al. — CoLaR. zotero_key:Y4ZNT3EC.
[KNOWN] [2026] Yu et al. — Latent Space Survey. zotero_key:KRVDKDGH.
[KNOWN] [2026] Deng et al. — Latent-GRPO. zotero_key:U4ZPM5DN.
[KNOWN] [2026] Zeng et al. — PonderLM. zotero_key:3TLRP8U5.

### Recent Activity

2026-05-14 | Area page seeded | 10 papers from Zotero, 0 from graphify seed.
