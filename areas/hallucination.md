## Hallucination in Language Models

### What

Hallucination refers to model outputs that are fluent but factually incorrect or unsupported by the input. This area covers detection methods (consistency checks, retrieval-based verification), mitigation strategies (constrained decoding, retrieval augmentation), and domain-specific benchmarks (medical hallucination).

### Why

Hallucination is the primary reliability failure of LLMs in high-stakes applications. A medical QA system that fabricates drug interactions or a legal assistant that invents case citations can cause real harm. Reducing hallucination is necessary before LLMs can be deployed in safety-critical settings.

### Baseline

Generate an answer with a standard LLM and present it to the user without verification. The main failure mode is that the model confidently states incorrect facts, and the user has no way to distinguish correct from hallucinated content.

### Running Example

Answer the medical question: 'What is the recommended first-line treatment for stage II hypertension?' The unverified LLM baseline might state a specific drug with fabricated dosage guidelines. A retrieval-augmented system grounds its answer in clinical guidelines and flags when no source supports a claim.

### Baseline vs Method Comparison on the Running Example

| Approach | Output on running example | Why it differs from baseline |
|---|---|---|
| Baseline | See running example above | (anchor) |

### Timeline

2023 | Med-HALT (Pal et al.) | 
2024 | Med-VQA Hallucination (Wu et al.) | 
2024 | Permutation Self-Consistency (Tang et al.) | 

### Key Methods

| Method | Year | Core idea (one clause) | Best benchmark result | Cost / limitation |
|---|---|---|---|---|

### Benchmark Results

| Method | Benchmark | Metric | Score | Source paper |
|---|---|---|---|---|
| _To be added as papers accumulate._ | | | | |

### Limitations

_To be added as papers accumulate._

### Paper List

[KNOWN] [2023] Pal et al. — Med-HALT. zotero_key:2IV8EKL2.
[KNOWN] [2024] Wu et al. — Med-VQA Hallucination. zotero_key:ATEFZQA4.
[KNOWN] [2024] Tang et al. — Permutation Self-Consistency. zotero_key:GAP6JAK9.

### Recent Activity

2026-05-14 | Area page seeded | 3 papers from Zotero, 0 from graphify seed.
