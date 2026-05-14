## Large Language Models

### What

Large language models are neural networks trained on large text corpora using self-supervised objectives (typically next-token prediction). This area covers architecture design, scaling laws, training procedures, and the emergent capabilities that arise at scale, including in-context learning and instruction following.

### Why

LLMs serve as the backbone for most current NLP systems and increasingly for multimodal and agentic applications. Understanding their architecture choices (attention variants, mixture-of-experts routing, positional encoding) and training recipes (data mixing, RLHF, distillation) is necessary for anyone building on or evaluating these models.

### Baseline

Fine-tune a BERT-base model on the target task with a task-specific classification head. The main failure mode is that BERT-scale models lack the capacity for complex reasoning and cannot perform in-context learning, requiring separate fine-tuning for each new task.

### Running Example

Answer a multi-step arithmetic word problem from GSM8K: 'A store sells 40 apples on Monday and twice as many on Tuesday. How many total?' The desired output is 120. BERT-base with a classification head cannot generate free-form answers and would need to be re-framed as a multiple-choice task, losing generality.

### Baseline vs Method Comparison on the Running Example

| Approach | Output on running example | Why it differs from baseline |
|---|---|---|
| Baseline | See running example above | (anchor) |
| Attention Is All You Need | _To be added as papers accumulate._ | Anchor paper for this area |

### Timeline

2024 | DeepSeek-V2 (DeepSeek-AI et al.) | 
2024 | DeepSeek-V3 (DeepSeek-AI et al.) | 
2025 | DeepSeek-R1 (DeepSeek-AI et al.) | 
2025 | SPRINT (Biju et al.) | 

### Key Methods

| Method | Year | Core idea (one clause) | Best benchmark result | Cost / limitation |
|---|---|---|---|---|
| Attention Is All You Need | Vaswani 2017 | Anchor method | _To be filled_ | _To be filled_ |
| DeepSeek-V3 | 2024 | _To be filled_ | _To be filled_ | _To be filled_ |
| DeepSeek-R1 | 2025 | _To be filled_ | _To be filled_ | _To be filled_ |

### Benchmark Results

| Method | Benchmark | Metric | Score | Source paper |
|---|---|---|---|---|
| _To be added as papers accumulate._ | | | | |

### Limitations

_To be added as papers accumulate._

### Paper List

[KNOWN] [2024] DeepSeek-AI et al. — DeepSeek-V2. zotero_key:743XA29Y.
[KNOWN] [2024] DeepSeek-AI et al. — DeepSeek-V3. zotero_key:2JCKA7GI.
[KNOWN] [2025] DeepSeek-AI et al. — DeepSeek-R1. zotero_key:Z5IWHZAE.
[KNOWN] [2025] Biju et al. — SPRINT. zotero_key:BZKDNHD6.

### Recent Activity

2026-05-14 | Area page seeded | 4 papers from Zotero, 2 from graphify seed.
