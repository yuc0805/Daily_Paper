## Natural Language Processing

### What

NLP covers methods for processing and generating human language, including tokenization, language modeling, instruction tuning, and few-shot prompting. This area page focuses on the NLP-specific techniques (BERT, instruction tuning, data generation) rather than the LLM architectures themselves (covered in llm.md).

### Why

NLP methods are the interface through which humans interact with language models. Instruction tuning and data synthesis determine how well models follow user intent. Understanding these techniques is necessary for building reliable text-based applications.

### Baseline

Fine-tune BERT on a task-specific labeled dataset with a classification head. The main failure mode is that fine-tuning requires thousands of labeled examples per task, and the resulting model cannot generalize to new tasks without re-training.

### Running Example

Classify movie reviews as positive or negative (SST-2 binary sentiment). BERT fine-tuned on 67k labels achieves 93.5% accuracy. GPT-3 with 2-shot in-context learning (no fine-tuning) achieves 95.0% accuracy.

### Baseline vs Method Comparison on the Running Example

| Approach | Output on running example | Why it differs from baseline |
|---|---|---|
| Baseline | See running example above | (anchor) |

### Timeline

2019 | BERT (Devlin et al.) | 
2020 | GPT-3 (Brown et al.) | 
2022 | Flamingo (Alayrac et al.) | 
2023 | Chain-of-Thought (Wei et al.) | 
2023 | GPT-4 Instruction (Peng et al.) | 
2023 | Self-Instruct (Wang et al.) | 

### Key Methods

| Method | Year | Core idea (one clause) | Best benchmark result | Cost / limitation |
|---|---|---|---|---|
| Chain-of-Thought | 2023 | _To be filled_ | _To be filled_ | _To be filled_ |

### Benchmark Results

| Method | Benchmark | Metric | Score | Source paper |
|---|---|---|---|---|
| _To be added as papers accumulate._ | | | | |

### Limitations

_To be added as papers accumulate._

### Paper List

[KNOWN] [2019] Devlin et al. — BERT. zotero_key:WQRB4TUT.
[KNOWN] [2020] Brown et al. — GPT-3. zotero_key:ZT8Y3ABF.
[KNOWN] [2022] Alayrac et al. — Flamingo. zotero_key:SC8KWYVK.
[KNOWN] [2023] Wei et al. — Chain-of-Thought. zotero_key:HBLPTRMY.
[KNOWN] [2023] Peng et al. — GPT-4 Instruction. zotero_key:LJ3CTGDF.
[KNOWN] [2023] Wang et al. — Self-Instruct. zotero_key:WAB8J2FQ.

### Recent Activity

2026-05-14 | Area page seeded | 6 papers from Zotero, 1 from graphify seed.
