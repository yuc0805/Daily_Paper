# AI Digest — 2026-06-23

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A is not done by 6 AM, stop.
Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.
Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

Quiet day for fresh time-series and bio-sensing work — nothing new dated today qualified for Tier A in your primary area, so today's Tier A and Tier B come from reasoning and agents, which sit in your secondary watch list for porting. The Gap Watch below turns those into transfer opportunities for time series. The strongest thread today is reinforcement learning with verifiable rewards (RLVR): three separate June papers each attack a different weak point of the DeepSeek-R1 training recipe you already have in your library.

---

## Tier A — deep read (~20 min)

### ReSum: Synergizing LLM Reasoning and Summarization with Reinforcement Learning
arXiv:2606.13316 — https://arxiv.org/abs/2606.13316

**Problem.** RLVR is the standard way to train long reasoning, but it rewards ever longer rollouts. Long traces fill the context window and let an early mistake propagate to the end. Prior fixes manage the rollout from outside the model rather than letting the model manage its own trace.

**Method.** ReSum keeps the RLVR setup and adds a learned action: the model writes a short summary of its work so far and continues from that summary. A summarization-aware adaptive rollout builds contrastive branches — it masks the summary phrase where the model produced one, and injects it where the model did not — and a summarization-aware advantage scores whether summarizing actually helped. The update then rewards summarization only when it improves the trajectory. Pilot studies report that self-summarization lowers token-level entropy and that a summary phrase reduces errors carried from a wrong prefix.

**Result.** Average accuracy improves by 4 percent while rollout length drops by 18.6 percent. The gain comes with shorter chains, not longer ones, which is the opposite of the usual RLVR length drift.

**Limitations.** The reported gains are averages over benchmarks; the paper does not show that summarization helps uniformly across task types, and the contrastive branching adds rollout cost during training. Whether the learned summary points transfer to domains with non-text state (such as numeric series) is untested.

**Why it matters to you.** Any agent that runs many steps under a fixed context window — including a time-series reasoning agent that calls operator after operator — hits the same length problem ReSum solves. A model that learns to compress its own evidence log mid-run is directly relevant to the operator-loop agents in your time-series community.

**How this builds on what you know:** The direct parents in your library are DeepSeek-R1 (Z5IWHZAE, community 0, reasoning-via-RL) and Chain-of-Thought (HBLPTRMY, community 0, prompting). Where DeepSeek-R1 used verifiable rewards to make a model produce long reasoning chains, and Chain-of-Thought showed that writing intermediate steps helps, neither gives the model a way to bound the length of its own trace. ReSum does, because it adds a learned summarize-and-restart action and rewards it only when it helps. This paper extends the DeepSeek-R1 to Chain-of-Thought bridge already in your library (the "reasoning-via-RL versus prompting" edge): the reinforcement signal now shapes not just whether the model reasons step by step, but how it budgets the length of that reasoning.

---

## Tier B — TLDRs (~10 min)

### Beyond Entropy: Learning from Token-Level Distributional Deviations for LLM Reasoning
arXiv:2606.19771 — https://arxiv.org/abs/2606.19771

RLVR swings between entropy collapse (premature convergence) and entropy explosion (incoherent chains), and controlling a single scalar entropy term needs careful tuning. This paper's ICT framework instead updates only the roughly 10 percent of tokens whose logit distributions deviate most, measured by Jensen-Shannon divergence, treating them as the branching points that matter. It proves, using Shannon and second-order Renyi entropy, that this selective update stabilizes training without a separate entropy schedule. On Qwen2.5 (0.5B, 1.5B, 7B) it reports an average pass@4 gain of 4.58 percent and a maximum of 14.9 percent over GRPO and entropy-control baselines across seven benchmarks.

How this builds on what you know: The parents are DeepSeek-R1 (Z5IWHZAE, community 0) and Latent-GRPO (U4ZPM5DN, reasoning), both GRPO-style RLVR in your library. Where DeepSeek-R1 and standard GRPO apply one outcome reward across all tokens, ICT changes which tokens receive the gradient, not the reward, because a small set of high-divergence tokens is enough to regulate exploration. It is a credit-assignment rule layered on the recipe you already track, aimed squarely at the training-stability problem that blocks porting RLVR to new domains.

### Process-Verified Reinforcement Learning for Theorem Proving via Lean
arXiv:2606.20068 — https://arxiv.org/abs/2606.20068

RLVR usually relies on one binary reward per attempt, which is sound but sparse: a long correct prefix that ends in one bad step scores the same zero as a proof that was wrong from the start. This work uses the Lean proof assistant as a process-level reward oracle. Each attempt is parsed into tactics, and Lean's elaboration marks the sound steps and the earliest failing step, giving a dense, type-checked credit signal. With first-error propagation and first-token credit inside a GRPO-style objective, tactic-level supervision beats outcome-only baselines on MiniF2F and ProofNet using STP-Lean and DeepSeek-Prover-V1.5.

How this builds on what you know: The parents are DeepSeek-R1 (Z5IWHZAE, community 0) and Chain-of-Thought (HBLPTRMY, community 0). Where DeepSeek-R1 used a single binary verifiable reward, this paper turns the verifier into a dense process reward by reading Lean's per-tactic output, because the structured feedback was already there and only used at evaluation time. The reward stays sound — it comes from type theory, not a learned critic — but becomes fine-grained.

### MetaForge: A Self-Evolving Multimodal Agent that Retrieves, Adapts, and Forges Tools On Demand
arXiv:2606.01801 — https://arxiv.org/abs/2606.01801

Tool-using agents usually work from a fixed library or generate a tool for one task and discard it, so they re-solve the same sub-problems and cannot accumulate capability. MetaForge retrieves a related tool, adapts it, or writes a new one when nothing fits, and then retains the result for future retrieval, so its tool set grows across tasks. The work targets open-ended visual and multimodal tasks where the needed operations cannot be listed in advance. (Summary from the abstract and listing; concrete benchmark numbers were not available at digest time.)

How this builds on what you know: The parents are PyVision (XQTY5MPI, community 0), ToolkenGPT (6RDHVVA2, community 0), and DeepEyesV2 (4XXXYXS9, community 0), all agent papers you track. Where PyVision forges a vision tool for the current problem and then discards it, MetaForge adds a retain-and-reuse loop, because capability should carry over between tasks. The change is in tool persistence, not in the act of tool generation.

---

## Tier C — scan headlines (~5 min)

- HEARTS: Benchmarking LLM Reasoning on Health Time Series — tests whether LLMs reason over health time series or memorize. https://arxiv.org/abs/2603.06638
- SignalMC-MED: A Multimodal Benchmark for Biosignal Foundation Models on Single-Lead ECG and PPG — shared eval for ECG/PPG foundation models. https://arxiv.org/abs/2603.09940
- SIGMA-PPG: Statistical-prior Informed Generative Masking for PPG Foundation Model — bakes signal statistics into the masking objective. https://arxiv.org/abs/2601.21031
- Time Series Reasoning via Process-Verifiable Thinking Data Synthesis — builds verifiable reasoning traces for time-series question answering. https://arxiv.org/abs/2602.07830
- Foundation Models Defining a New Era in Sensor-based Human Activity Recognition: A Survey — current map of foundation models for HAR. https://arxiv.org/abs/2604.02711
- ActivityNarrated: An Open-Ended Narrative Paradigm for Wearable Human Activity Understanding — frames HAR as open-ended narration rather than fixed labels. https://arxiv.org/abs/2604.00767
- Seg-MoE: Multi-Resolution Segment-wise Mixture-of-Experts for Time Series Forecasting — routes time-series segments to resolution-specific experts. https://arxiv.org/abs/2601.21641
- Agentic Reasoning for Large Language Models — survey of agent-style reasoning loops. https://arxiv.org/abs/2601.12538

---

## Tier D — Time-Series / Bio-Sensing Gap Watch

No new time-series or bio-sensing method landed today that imports a CV/NLP technique, so there is nothing to mark as newly "ported." Community 4 (Time Series + LLM Integration) and Community 5 (Wearable Sensing & Behavior) remain the reference for what is already closed off. Today's signal is on the RLVR side, which is still mostly unported. Two opportunities:

Unported opportunity 1 — Process-verified rewards for time-series reasoning agents. The Lean paper (2606.20068) replaces a single end-of-episode reward with a dense, sound, externally computed process signal. A time-series reasoning agent in the style of TS-Agent has the same structure: a sequence of operator calls ending in an answer. Transfer hypothesis: use statistical-consistency checks on each operator output (does the claimed change-point match the detected one, does a summary statistic match the recomputed value) as a dense process reward, instead of grading only the final answer. This would give verifier-grounded intermediate credit without paired training data.

Unported opportunity 2 — Self-summarization for long operator logs. ReSum (2606.13316) teaches a model to compress its own reasoning trace under RLVR. Time-series agents accumulate long evidence logs across many operator calls and hit the same context-budget limit. Transfer hypothesis: train the agent to summarize its evidence log mid-run, keeping the numeric findings and dropping the raw operator transcripts, which should let it run more analysis steps within a fixed window.

---

## News

Three model storylines landed in June 2026: Google released Gemini 3.5 Pro, Anthropic released Claude Mythos 1, and xAI released Grok 5. Treat the specifics as reported rather than confirmed here; none changes a research decision today, and none is a time-series or bio-sensing release.

---

End of digest. Close this tab when done.
