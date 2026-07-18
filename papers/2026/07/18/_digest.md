# AI Digest — 2026-07-18

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A is not done by 6 AM, stop.
Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.
Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

Quiet day for your primary area. No new time-series or bio-sensing paper qualified for Tier A today, so Tier A comes from the agent cluster, where the strongest signal landed. The theme across today's top papers is control of long-horizon behavior: keeping an agent's search state explicit (Tier A), keeping a robot's imagined future aligned with its actions (BadWAM), and scaling context so a policy remembers minutes of history (RoboTTT). The Gap Watch turns two of these into concrete transfer ideas for wearable and physiological data.

---

## Tier A — deep read

### SearchOS-V1: Towards Robust Open-Domain Information-Seeking Agent Collaboration (arXiv 2607.15257)

Problem. Tool-using LLM agents can now call web search, but as the interaction history grows they lose track of what they have already found and what is still missing. When a search returns nothing useful, single-agent and multi-agent systems tend to fall into repetitive loops that burn the search budget and leave the final answer incomplete. The gap is that search progress lives implicitly inside a long, fragile context window rather than in an explicit, shared record.

Method. SearchOS reframes open-domain information seeking as filling in a relational schema with grounded citations: agents find entities, populate attributes across linked tables, and tie every value back to a source. A component called Search-Oriented Context Management (SOCM) writes the changing state out of the context window and into four explicit structures — a Frontier Task, an Evidence Graph, a Coverage Map, and a Failure Memory. On top of this, a pipeline-parallel scheduler overlaps sub-agents and refills freed slots with tasks aimed at coverage gaps, and a Search Tool Middleware Harness intercepts model-tool calls to record grounded evidence, react to stalls or budget exhaustion, and reuse a hierarchical skill library of strategy and access skills so failed search patterns are not repeated across runs.

Result. On the WideSearch and GISA benchmarks, SearchOS leads all reported metrics against the single-agent and multi-agent baselines the authors evaluate. The gains come from two places: the explicit Coverage Map and Failure Memory cut repeated dead-end queries, and the pipeline-parallel scheduler raises throughput by keeping sub-agents busy on unresolved gaps rather than idle.

Limitations. The evaluation is on two information-seeking benchmarks, so it is not yet clear how the schema-completion framing transfers to open-ended research questions that do not map cleanly onto tables. The system has many moving parts (four state structures, a scheduler, a middleware harness, a skill library), and the paper does not fully separate how much each part contributes. Cost and latency of running many overlapped sub-agents are not the focus of the reported numbers.

How this builds on what you know: The direct parents in your library are ADaPT (As-Needed Decomposition and Planning) and LATS (Language Agent Tree Search), both in graphify Community 0 (LLM Agents and Reasoning), plus the Agent AI Survey and the Memory Mechanisms Survey. Where ADaPT decomposes a task on demand and LATS searches a tree of actions at inference time, SearchOS moves the hard part out of the reasoning trace and into persistent external state — an Evidence Graph and a Failure Memory that outlive any single agent step, because the real failure was loss of progress in a growing context, not weak planning. Where the memory-agent work in your library keeps a running store to help one agent remember, SearchOS makes that store shared and structured so several agents can coordinate coverage without colliding. In short, the parents improved how an agent thinks; this paper improves what an agent writes down.

Why it matters to Leo. The reusable idea is the Failure Memory plus Coverage Map: a compact external record of "what has already been tried and failed" and "what remains uncovered." That pattern maps onto sensor-labeling and physiological-analysis agents, where an agent examining ambiguous windows could keep an explicit map of which windows are still unresolved and which feature extractors already failed on them, rather than re-deriving that state from a long transcript.

---

## Tier B — TLDR

### BadWAM: When World-Action Models Dream Right but Act Wrong (arXiv 2607.15207)

World-action models (WAMs) couple action generation with prediction of the future world, and this coupling is often assumed to make them safer because a robot's action can be checked against its imagined future. BadWAM shows that assumption is fragile. It defines World-Action Drift Attacks: small visual perturbations that break the link between what a WAM imagines and what it does. Two variants span a spectrum — an action-only attack that drives the model toward task-failing actions (cutting success from 96.5% to 43.1% in one setting), and a stealthier imagination-preserving attack that keeps the predicted future close to the clean one while still hijacking the action. The second variant is the alarming result: the model appears to imagine a plausible future yet executes a desynchronized action, so the "check action against imagination" safety story does not hold.

How this builds on what you know: The parents in your library are World Models (Ha and Schmidhuber) and Navigation World Models, both in the world-model-rl area, and it speaks directly to yesterday's From Pixels to States, which argued that explicit state matters more than pixel prediction. Where those papers treat the learned or explicit world model as a source of robustness, BadWAM treats it as a new attack surface, because coupling action and imagination creates a seam that an adversary can pry apart. Read it next to From Pixels to States: one argues explicit state helps control, the other shows that if imagination and action are only loosely coupled, the imagination can look right while the action is already wrong.

### RoboTTT: Context Scaling for Robot Policies (arXiv 2607.15275)

RoboTTT (NVIDIA) scales the visuomotor context of a robot policy to 8,000 timesteps — three orders of magnitude beyond typical single-step or short-history policies — without raising inference latency. It does this by putting Test-Time Training inside a Vision-Language-Action policy: the recurrent state is a set of fast weights updated by gradient descent during both training and inference, so history is compressed into weight space rather than a growing token window. The training recipe combines sequence action forcing with truncated backpropagation through time. At this context length the model unlocks one-shot in-context imitation from human video, on-the-fly improvement, and long-horizon tasks: it improves overall performance by 87% over a single-step baseline, completes a five-minute ten-stage assembly task that no baseline finishes, and an 8K-context model beats the same model trained at 1K context by 62%. The headline claim is that context length is a new scaling axis for robot foundation models.

How this builds on what you know: The direct parent is the Test-Time Training line in your test-time-training area, and it also connects to the Vision-Language-Action model notes you already hold. Where standard TTT adapts a model to a single test instance, RoboTTT uses the same fast-weight update as the policy's working memory across thousands of steps, because a long-horizon robot needs to remember minutes of interaction, not adapt once. This is the clearest demonstration in your library that TTT fast weights can serve as a scalable recurrent memory rather than a one-shot adaptation trick.

### UniVR: Thinking in Visual Space for Unified Visual Reasoning (arXiv 2607.12800)

UniVR (ByteDance) learns complex reasoning, physical dynamics, and long-horizon planning from pure visual demonstrations, with no image-text pairs. Its core is VR-GRPO, a reinforcement learning scheme with two complementary rewards: a global reward for final-answer correctness and a step-level reward that enforces logical and physical consistency along the reasoning process. The authors build VR-X, a benchmark drawn from 16 sources covering long-horizon manipulation, spatial puzzles, and physical reasoning, and evaluate everything under a purely visual protocol. UniVR reports up to 25% improvement on VR-X, and the improved visual reasoning also raises scores on standard multimodal understanding benchmarks. Code, data, and models are released.

How this builds on what you know: The parents are DeepSeek-R1, which established reasoning trained by reinforcement learning with a rule-based reward, and Chain-of-Thought, which established step-by-step reasoning in language, both in Community 0. Where DeepSeek-R1 rewards a correct final answer in text and Chain-of-Thought produces the reasoning trace in language tokens, UniVR moves both the reasoning and the reward into visual space and adds a step-level consistency reward, because a text-only reward cannot check whether an intermediate visual state is physically plausible. It is the reinforcement-learning-for-reasoning recipe you already know, retargeted from language to raw pixels.

---

## Tier C — scan

- SearchOS aside, the agent theme continues: **GRASP: Granularity-Aware Search Policy for Agentic RAG** (arXiv 2607.10463) — learns when to search coarse versus fine to cut wasted retrieval.
- **Concurrent Image Understanding and Generation: Self-Correcting Coupled Markov Jump Processes** (arXiv 2607.13188, Google) — one model that reads and draws images through coupled jump processes with self-correction.
- **Video = World + Event Stream** (arXiv 2607.15038, Wan-AI) — reframes video generation as a persistent world plus a stream of events.
- **KeyFrame-Compass: Comprehensive Evaluation of Keyframe-Conditioned Video Generation** (arXiv 2607.14202, Kling) — a benchmark for video generation conditioned on keyframes.
- **DeepLoop: Depth Scaling for Looped Transformers** (arXiv 2607.13491) — scales effective depth by looping a shared block instead of stacking new layers.
- **Byte-Exact KV-Cache Grafting** (arXiv 2607.14431) — grafts a large model's KV-cache into a frozen small model to raise quality at low cost.
- **Partition, Prompt, Aggregate: Statistical Self-Consistency in Language Models** (arXiv 2607.15277) — a statistical reading of self-consistency via partitioned prompts.
- **Spectral Rewiring for Exploration, Purification, and Model Merging** (arXiv 2607.03065) — uses spectral edits of weights for exploration and merging.

---

## Tier D — Time-series / Bio-sensing Gap Watch

No time-series or bio-sensing paper landed in today's top set, so this section reads today's control and memory papers for transfer ideas.

Already ported (closed off). Sensor-to-LLM translation for on-device human activity recognition is now covered: **STELLA** (arXiv 2607.03089) translates raw sensor streams into an LLM-readable form for on-device HAR, which sits squarely in graphify Community 4 (Time Series + LLM Integration) alongside TS-Agent and ChatTS. Treat "feed a sensor stream to an LLM for activity labels" as done; new work needs a different angle to be worth your time.

Unported opportunity 1 — RoboTTT's fast-weight context as wearable memory. RoboTTT compresses 8,000 timesteps of robot history into fast weights updated by gradient descent, keeping latency flat. No paper in your library applies this to physiological time series. Transfer hypothesis: a wearable foundation model could hold multi-day sensor history in TTT fast weights rather than a fixed context window, so it conditions on a week of context at constant inference cost — a direct answer to the long-context problem in continuous monitoring.

Unported opportunity 2 — SearchOS's Coverage Map and Failure Memory for sensor-labeling agents. The explicit "what is still uncovered / what already failed" state has not been applied to physiological analysis. Transfer hypothesis: an agent labeling ambiguous sensor windows could keep a Coverage Map of unresolved windows and a Failure Memory of feature extractors that already returned nothing, avoiding repeated dead-end analysis on the same segment.

---

## News

Moonshot AI released **Kimi K3**, an open-weight model that immediately placed among the strongest systems for coding and agent tasks, reaching the top of Arena.ai's Frontend Code Arena with a reported 76% pairwise win rate, ahead of Claude Fable 5 and GPT-5.6 on that benchmark. Google DeepMind launched **Gemini 3.5 Pro** after a delay and a ground-up architecture rebuild, adding a 2-million-token context window and a "Deep Think" reasoning layer aimed at mathematical reasoning and image quality. Both are frontier-scale releases; the open-weight Kimi K3 is the one most likely to matter for your own experiments.

---

End of digest. Close this tab when done.
