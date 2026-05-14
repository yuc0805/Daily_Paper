## LLM-based Agents

### What

LLM-based agents are systems where a language model acts as the central controller, making decisions about which tools to call, how to decompose tasks, and when to revise plans. This area covers architectures for tool use, memory mechanisms, planning algorithms, and multi-agent coordination.

### Why

Single-turn LLM interactions cannot handle tasks that require external information retrieval, code execution, or multi-step planning. Agent frameworks extend LLMs into iterative problem solvers, but current systems are brittle: they hallucinate tool calls, get stuck in loops, and lack reliable self-correction.

### Baseline

Use a single LLM call with all instructions in the prompt (no tool use, no planning loop). The main failure mode is that the model cannot access external data or verify its own outputs, leading to stale or fabricated answers on any task requiring real-time information.

### Running Example

Answer the question: 'What is the current stock price of AAPL and is it above its 50-day moving average?' The single-call baseline hallucinates a price from training data. An agent system would call a finance API, compute the moving average, and compare.

### Baseline vs Method Comparison on the Running Example

| Approach | Output on running example | Why it differs from baseline |
|---|---|---|
| Baseline | See running example above | (anchor) |

### Timeline

2018 | Machine Theory of Mind (Rabinowitz et al.) | 
2023 | ADaPT (Prasad et al.) | 
2024 | Agent AI Survey (Durante et al.) | 
2024 | LATS (Zhou et al.) | 
2024 | ToolkenGPT (Hao et al.) | 
2025 | PyVision (Zhao et al.) | 
2026 | DeepEyesV2 (Hong et al.) | 
2026 | Memory Mechanisms Survey (Huang et al.) | 

### Key Methods

| Method | Year | Core idea (one clause) | Best benchmark result | Cost / limitation |
|---|---|---|---|---|
| Machine Theory of Mind | 2018 | _To be filled_ | _To be filled_ | _To be filled_ |
| ADaPT | 2023 | _To be filled_ | _To be filled_ | _To be filled_ |
| Agent AI Survey | 2024 | _To be filled_ | _To be filled_ | _To be filled_ |
| LATS | 2024 | _To be filled_ | _To be filled_ | _To be filled_ |
| ToolkenGPT | 2024 | _To be filled_ | _To be filled_ | _To be filled_ |
| PyVision | 2025 | _To be filled_ | _To be filled_ | _To be filled_ |
| DeepEyesV2 | 2026 | _To be filled_ | _To be filled_ | _To be filled_ |
| Memory Mechanisms Survey | 2026 | _To be filled_ | _To be filled_ | _To be filled_ |

### Benchmark Results

| Method | Benchmark | Metric | Score | Source paper |
|---|---|---|---|---|
| _To be added as papers accumulate._ | | | | |

### Limitations

_To be added as papers accumulate._

### Paper List

[KNOWN] [2018] Rabinowitz et al. — Machine Theory of Mind. zotero_key:NFNV9QGH.
[KNOWN] [2023] Prasad et al. — ADaPT. zotero_key:TQIRSRQE.
[KNOWN] [2024] Durante et al. — Agent AI Survey. zotero_key:PJZ76NJE.
[KNOWN] [2024] Zhou et al. — LATS. zotero_key:76XQKFGW.
[KNOWN] [2024] Hao et al. — ToolkenGPT. zotero_key:26QNAFQG.
[KNOWN] [2025] Zhao et al. — PyVision. zotero_key:3JCCQCMG.
[KNOWN] [2026] Hong et al. — DeepEyesV2. zotero_key:RDKGJ9PT.
[KNOWN] [2026] Huang et al. — Memory Mechanisms Survey. zotero_key:BDY3HUCV.

### Recent Activity

2026-05-14 | Area page seeded | 8 papers from Zotero, 8 from graphify seed.
