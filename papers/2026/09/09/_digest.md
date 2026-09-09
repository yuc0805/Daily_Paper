# AI Digest — 2026-09-09

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A not done by 6 AM, stop.

Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.

Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

---

## Tier A — one deep read

### Kalman Delta Networks: Uncertainty-aware Associative Memory
Bui, Huang, Ying (Yale University) — [arXiv:2609.07816](https://arxiv.org/abs/2609.07816)

**Problem.** Linear attention is used in frontier models because it decodes at constant memory, and that bounded state forces a decision at every token: what to write, and how strongly to overwrite what is already stored, before knowing what future queries will ask for. Delta-rule models learn that write strength from the current token embedding. This means the update cannot depend on how much evidence the memory has already accumulated about the association being overwritten, so a confident memory and an uninformed one are treated identically.

**Method.** The paper writes recurrent associative memory as a linear-Gaussian state-space model, for which the Kalman filter is the optimal recursive estimator, and adopts that filter as the write rule. The transition carries the memory state and its covariance together, so the Kalman gain weights each residual write by accumulated evidence and observation reliability. Delta-style updates then appear as the special case that replaces the predictive covariance with a token-wise isotropic surrogate and drops covariance tracking altogether. Exact tracking requires a dense, state-dependent Riccati recursion, which is sequential and therefore unusable inside a GPU-parallel scan, so the paper supplies two approximations. Diagonal KDN projects each one-step posterior onto the diagonal Gaussian family by online mean-field variational inference; Isotropic KDN keeps one uncertainty scalar per head. Both uncertainty recurrences take the form of Mobius maps, which compose associatively, so the associative scan and its logarithmic parallel depth survive.

**Result.** Across controlled pretraining at 750M and 1.3B parameters, both KDN variants consistently improve perplexity and mean downstream accuracy over state-of-the-art linear-attention models. Code is at github.com/ngocbh/kalman-delta-networks.

**Limitations.** The reported gains are from controlled pretraining at two model sizes, not from a frontier-scale run, and "consistently improve" over linear-attention baselines is a comparison inside that family rather than against full softmax attention. The exact formulation is the principled one and it is precisely the version that cannot be trained, so what is measured is two approximations whose gap to the exact filter is not quantified. Diagonal and isotropic posteriors also discard the cross-terms that would represent interference between stored associations, which is arguably the case where uncertainty tracking should matter most.

**How this builds on what you know:** Where Mamba-2 (JPKDWV2Q) showed that a linear-attention layer and a structured SSM are the same recurrence and then spent its effort making that recurrence fast, this paper asks what the recurrence should be estimating and answers with the Kalman filter, because a linear-Gaussian state-space model has a known optimal estimator that linear attention had not been using. Where HiPPO (5YQ4IKMA) fixed the compression measure in advance and derived a static transition from it, KDN lets effective write strength move with a tracked covariance. Where Attention Is All You Need (PHB9VRVM) kept an unbounded KV cache and therefore never faced the overwrite question, KDN is managing the bounded state that replaced it. Attention Is All You Need is the top anchor of community 2, Transformer and SSM Architectures, and in your library it is filed under both time-series and self-supervised; community 2 also holds HARMamba (HE9X47KN), which already carries this backbone family into wearable sensing and llm-health. The new work pushes that bridge further, in the direction of an uncertainty-aware write rule that no wearable paper in your library has tried.

**Why it matters to you.** This is a Kalman filter placed inside a sequence-model layer, so the estimator you already know from classical time-series work becomes the write rule of a modern backbone. The import runs backwards from the usual direction, out of signal processing and into language modeling rather than the reverse, which is worth noting because it means the transfer opportunity is yours to take rather than one already taken. Physiological streams are where the modeling assumption is actually true: motion artifact on PPG and ECG produces genuinely heteroscedastic observation noise, exactly the condition under which a Kalman gain should downweight a write without being told to.

---

## Tier B — three TLDRs

### Memory in Deep Time-Series Models
Nguyen et al. (Hung Le group) — [arXiv:2609.06006](https://arxiv.org/abs/2609.06006)

A survey that re-reads the whole time-series literature along one axis: how does a model retain and access information beyond its immediate input? Recurrent networks, transformers, state-space models, retrieval-augmented predictors, foundation models and tool-using agents are placed on a spectrum from internal memory, held in parameters and fixed-size states, to external memory that is addressable, retrievable and increasingly maintained by an agent. Three classes of external memory, namely explicit modules, retrieval augmentation and agentic stores, are described with one shared set of questions about what is retained, how it is written and read, and how it persists. The framing is deliberately independent of the backbone, and the closing section argues the open problems are in systems that selectively retain, retrieve, revise and forget as the environment changes.

**How this builds on what you know:** Where LLMs for Time Series: A Survey (N2JLZBY3) organized this literature by interface, asking how a language model is attached to a series, this paper organizes it by state, because the interface taxonomy separates a state-space model from a retrieval-augmented forecaster even though both answer the same finite-window limitation. Where TS-Agent (I2CIT4I7) showed that an external agentic store helps on specific reasoning tasks, this paper places that result as one point on a continuum whose other end is HiPPO-style parameter memory. Where Rethinking Memory Mechanisms of Foundation Agents (BDY3HUCV) built the retain, retrieve, revise and forget vocabulary for language agents over text, this paper carries it to numeric temporal data. That last connection is the notable one for your graph: BDY3HUCV sits in community 0, LLM Agents and Reasoning, and I2CIT4I7 sits in community 4, Time Series plus LLM Integration, and this survey is the first item that explicitly joins them, opening a bridge between those two communities where your library currently has none.

The useful takeaway is the gap it names rather than the taxonomy: every mechanism surveyed is scored on downstream forecasting error, so there is no evidence about whether the memory itself retains, revises or forgets correctly. In bio-sensing the relevant history is months of a person's own baseline, and a model that cannot revise a stale baseline fails in a way forecasting error does not surface.

### Eliciting Weak-to-Strong Generalization with On-Policy Reverse Distillation
Park, Bae et al. (KAIST AI) — [arXiv:2609.08798](https://arxiv.org/abs/2609.08798)

Asks whether a stronger student can learn from a weaker teacher and finish above it, which is the practical situation whenever a new base model should inherit post-training gains without repeating that post-training from scratch. Conventional distillation is the wrong tool because making the teacher's distribution the optimization target transfers the teacher's capacity ceiling along with its knowledge. OPRD instead measures the teacher's policy shift relative to its own reference policy, evaluated on the student's rollouts rather than the teacher's, and amplifies the component of the student's verifier-driven policy gradient lying along that direction. Since only verifier-supported updates are rescaled, and rescaling a gradient adds no term, the student's stationary points are unchanged and only the path to them is shortened. Across successive model transfer and multi-teacher consolidation, OPRD reaches competing methods' final performance in fewer student updates and then exceeds both RL and distillation baselines; response-style analysis finds the students resemble verifier-only RL models more than they resemble their teachers, which is the evidence that guidance accelerated rather than redirected them.

**How this builds on what you know:** Where DeepSeek-R1 (Z5IWHZAE) obtained reasoning purely from verifier reward and paid for it in sample count, OPRD keeps that same verifier signal and spends a weak teacher to reach the same place sooner. Where PPO (KQTIJC4U) constrains updates isotropically to a trust region for stability, OPRD applies an anisotropic rescaling that deliberately stretches one direction and relies on verifier support rather than a trust region to keep it safe. Where Policy Gradient Methods (DAGWCZ67) supplies the stationary-point argument, this paper uses it as the load-bearing claim. DeepSeek-R1 is already a cross-area bridge in your library, connecting reasoning-via-RL to prompting-era Chain-of-Thought (HBLPTRMY); the new work pushes that bridge further into the question of how RL-obtained reasoning is transferred between model generations rather than how it is obtained in the first place.

The transferable idea is separating what a teacher is for from what a teacher is copied into. Its dependency is a verifier, and what plays that role outside math and code is the open question worth carrying into your own area.

### NeoHorse-1: Towards Recursive Self-Improvement via Agentic Post-Training with Routing Harness
NeoHorse Team et al. — [arXiv:2609.08183](https://arxiv.org/abs/2609.08183)

Builds a loop in which serving traffic becomes training data. A heterogeneous model pool sits behind a router, and each turn is logged with the predicted capability demand, the service tier selected and the full interaction; those records become training examples that keep interleaved reasoning, tool calls and harness context intact, admitted through structural validation, six-dimensional semantic evaluation and subscene-level labeling. The same routing signals then organize supervised fine-tuning into a three-stage curriculum and drive routing-guided on-policy distillation, and capability-guided allocation converts evaluation feedback into the next training mixture. Across eleven benchmarks spanning harness-based agents, tool use, coding and instruction following, post-training raises the macro-average from 58.94 to 64.87 at 4B and from 65.60 to 69.04 at 9B, with the post-trained 4B closing much of the gap to the 9B base model.

**How this builds on what you know:** Where LATS (77ERE7HA) searched over agent trajectories at inference time and discarded the search once an answer was produced, NeoHorse retains the trace and feeds it back as supervision, because the expensive part of an agent rollout is the harness context. Where ADaPT (J8DYBKW2) decomposed a task on demand to decide how much planning a step needed, NeoHorse predicts that same demand before the turn and uses the prediction twice, first to route and then to place the example in a curriculum stage. Where DeepSeek-V3 (2JCKA7GI) routed among experts inside one forward pass, leaving the routing decision as internal activations that cannot label anything, the routing here is across separate models at different service tiers, so the decision persists outside the model and becomes a label. ADaPT and LATS are already linked as a cross-area bridge in your graph under planning-decomposition agents; this paper extends both ends of that bridge at once, moving it from inference-time decomposition toward training-time curriculum construction.

Read it for the structure, not the numbers: a routing or triage decision is a free label on incoming data, which is a cheap curriculum when annotation is the bottleneck. Deployed sensing systems already make an equivalent decision about how much computation a window deserves and then discard it. The recursive self-improvement framing is the weakest part; one round of a loop is evidence about one round, and eleven benchmarks with a self-selected data pipeline is a setting where contamination is hard to rule out.

---

## Tier C — scan only

| Paper | Hook |
| --- | --- |
| [Cadence: Error-Bounded Lossy Compression of Demand Time Series](https://arxiv.org/abs/2609.06008) | Pairs a 330M-parameter TimesFM-3 with an adaptive arithmetic coder; a forecaster used as an entropy model. |
| [Procedural Graphs: Self-Evolving Execution Structures for LLM Agents](https://arxiv.org/abs/2609.09153) | Google; agents that rewrite their own execution graph instead of replanning from text each turn. |
| [Environments as Scaffold: Bootstrapping Self-Evolving Agents](https://arxiv.org/abs/2609.08404) | Enriches environment feedback to get long-horizon agent training signal without human labels. |
| [Omni Interaction Agent Technical Report](https://arxiv.org/abs/2609.08977) | Tencent Hunyuan; unified interaction agent spanning modalities and tool surfaces. |
| [Miles v0.1: Production-Level Post-Training](https://arxiv.org/abs/2609.08368) | Open post-training stack; useful as a recipe reference rather than a result. |
| [BeaconKV: KV Cache Compression Guided by Beacon Queries](https://arxiv.org/abs/2609.04971) | Uses probe queries to decide what to evict, for long reasoning traces. |
| [Reason Through the Latent! Making Latent Visual Reasoning Necessary](https://arxiv.org/abs/2609.06746) | Benchmark design that forces latent visual steps instead of letting text shortcut them. |
| [MOLE: Detecting Insider Threats in AI Agents](https://arxiv.org/abs/2609.06966) | CMU; treats a misbehaving agent as an insider-threat detection problem. |

---

## Tier D — Time-series / bio-sensing gap watch

**Already ported (closed off).** Agentic and retrieval-based memory for time series is being closed as a category rather than as a single result. Community 4 in your graph already contains TS-Agent, ChatTS and the LLM-for-TS survey, and today's Memory in Deep Time-Series Models is the survey that consolidates the whole spectrum, including agentic stores, into one taxonomy. When a survey arrives to organize a technique, the straightforward transfer of that technique is no longer the opening. Cadence is a second closure in miniature: using a time-series foundation model as the probability model inside a compressor is the natural information-theoretic application of TSFMs, and it now exists.

**Unported opportunity 1 — uncertainty-tracked associative memory for biosignals.** Kalman Delta Networks add covariance tracking to the recurrent state of a linear-attention layer, and nothing in community 5, Wearable Sensing and Behavior, or in community 4 does anything equivalent. Transfer hypothesis: PPG and ECG under free-living conditions have observation noise whose variance is itself measurable from the signal, so a Kalman gain driven by a motion-artifact or signal-quality estimate would suppress writes during corrupted windows automatically, replacing the hand-tuned quality masks that wearable pipelines currently apply before the model rather than inside it.

**Unported opportunity 2 — verifier-driven weak-to-strong transfer for time-series foundation models.** OPRD assumes a verifier, and the reason it has not reached time series is that forecasting has no obvious one. Transfer hypothesis: physiological plausibility supplies it, since constraints such as heart-rate bounds, respiratory-cardiac coupling ratios and monotone sleep-stage transitions are checkable without labels, which would let an older biosignal model's post-training gains be carried into a new backbone without capping the new model at the old one's accuracy.

---

## News

Three frontier releases landed in the first days of September, according to public release trackers rather than primary announcements, so treat the details as provisional. Anthropic shipped Claude Fable 5.1 and Mythos 5.1 on September 1 at unchanged list pricing, generally available immediately with no preview stage, and with three breaking API changes worth checking if you have code against the previous version. Google released Gemini 3.8 Flash on September 2 at the same introductory price as 3.7 Flash, this time with an end date printed for that price. OpenAI released GPT-6 Astra on September 3, reported as the first model to trigger the company's critical-cyber safeguard threshold, which is the item most likely to matter for how model access is gated going forward.

---

End of digest. Close this tab when done.
