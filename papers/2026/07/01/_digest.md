# AI Digest — 2026-07-01

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A not done by 6 AM, stop.
Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.
Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

---

## Tier A — deep read (1 paper, ~20 min)

### CAP: Towards PPG Universal Representation Learning with Patient-level Supervision
arXiv:2606.15284 (He et al., KDD 2026) — https://arxiv.org/abs/2606.15284

**Problem.** Photoplethysmography (PPG) is the signal most consumer wearables record, and a reusable PPG encoder would serve many downstream health tasks. Existing self-supervised PPG methods learn from the signal alone. They align samples by waveform shape, so two morphologically similar segments are pulled together even when they come from patients in different physiological states. They also train on short windows (5 to 30 seconds), which cannot capture chronic conditions or long-horizon drift, and common augmentations (masking, morphological transforms) can destroy fine structure that carries clinical meaning.

**Method.** The authors build a paired PPG plus electronic health record (EHR) dataset for 2,279 patients. For each patient, a pretrained language model distills fragmented diagnosis codes and clinical notes into one coherent patient-level record. Their method, Clinical Anchored Pretraining (CAP), then runs cross-modal contrastive alignment that ties PPG representations to this patient-level clinical text, so the encoder learns a patient's overall physiological state rather than only fitting the waveform. Pretraining combines three losses: a morphological reconstruction loss, a physiological stability loss, and the clinical anchoring loss. The encoder also reads longer PPG segments to widen its temporal view. At fine-tune time, a local morphology encoder and a clinical-semantic encoder are combined with gated fusion.

**Result.** Across four downstream tasks (atrial fibrillation detection, heart rate estimation, respiratory rate estimation, blood pressure estimation), CAP beats strong baselines with an average relative improvement of +26.7 percent, and up to +87.6 percent relative on respiratory rate over the best prior method. The paper adds ablations and attention or embedding visualizations to show where the gains come from.

**Limitations.** The clinical text is distilled by a language model from records, so any distortion in that step is inherited by the supervision signal. The cohort is 2,279 patients from specific clinical sources, so transfer to healthy consumer-wearable populations is not shown. Reported gains are relative, and respiratory rate baselines can be weak, so the +87.6 percent figure should be read against absolute error, not on its own.

**Why it matters to Leo.** This is directly in the bio-sensing area. It shows that grounding a physiological encoder in patient-level clinical text, rather than signal-only self-supervision, produces a large jump on standard PPG tasks. The design is a template Leo could reuse for other wearable streams.

**How this builds on what you know:**
CAP's closest parent in your library is Foundation Models for Biosignals (Gu 2025, key 2XWEG7AF, Health AI community), which surveyed signal-only self-supervised encoders for PPG and ECG. Where that line of work learned representations from the signal alone, CAP adds patient-level clinical text as the supervision anchor, because waveform similarity does not imply the same physiological state. The cross-modal contrastive step is the same signal-to-language alignment idea as Sensor2Text (Chen 2024, key ELYUE3NF, Time-Series plus LLM community), but Sensor2Text aligned activity sensors to natural-language activity descriptions, while CAP aligns PPG to structured patient-level EHR semantics. CAP also keeps a masked reconstruction objective, which follows the masked-autoencoder analysis in How Mask Matters (Zhang 2023, key 6INGKIJV). This paper extends the Sensor2Text to Health-LLM bridge in your library (the cross-area link between bio-sensing and clinical language, Sensor2Text to "LLMs are Few-Shot Health Learners", Liu 2023, key JX3X3KH5). The new work pushes that bridge from activity captioning toward patient-level clinical grounding of a raw physiological signal.

---

## Tier B — TLDRs (3 papers, ~10 min)

### Tandem Reinforcement Learning with Verifiable Rewards
arXiv:2606.28166 (Jiao, Singhal, West, Anderson — 26 Jun 2026) — https://arxiv.org/abs/2606.28166

Reinforcement learning with verifiable rewards (RLVR) makes large models strong at math and code reasoning, but the reasoning it produces drifts toward idiosyncratic, hard-to-read traces (poor readability, language mixing) that weaker models and people cannot follow. Tandem Reinforcement Learning (TRL) has a trained strong "senior" and a frozen weaker "junior" alternate stochastically to co-generate each reasoning rollout; the joint output is rewarded and the standard GRPO loss updates only the senior, so the senior is pushed to reason in a way the junior can continue. Training Qwen3-4B-Instruct on competition math, TRL matches plain GRPO on solo accuracy while producing three properties at once: stronger handoff to the junior, less distributional drift from the junior, and a chain of thought the junior finds more legible. The result is a route to reasoning models that keep their skill but stay compatible with weaker models and human readers.

**How this builds on what you know:**
The reward-only reasoning recipe (GRPO) comes from DeepSeek-R1 (2025, key Z5IWHZAE, LLM Agents and Reasoning community). Where DeepSeek-R1 optimized a single model for correctness and let the reasoning style go where it would, TRL adds a second frozen model to the rollout and rewards the pair, because a correct but unreadable trace is of little use to a weaker consumer. This sits on the DeepSeek-R1 to Chain-of-Thought bridge in your library (reasoning-via-RL versus reasoning-via-prompting, Wei 2023, key HBLPTRMY): Chain-of-Thought asked for legible steps by prompting, DeepSeek-R1 dropped that constraint for reward, and TRL brings legibility back as an emergent effect of the training structure rather than a prompt.

### MetaWorld: Scaling Multi-Agent Video World Models from Single-view Video Data
arXiv:2606.02753 (Hu, Lu et al. — Jun 2026) — https://arxiv.org/abs/2606.02753

Video world models so far simulate a scene from a single agent and a single view. Extending them to several agents needs coordinated multi-view recordings, which are expensive, and independently generated views can disagree about the same shared world. MetaWorld trains multi-agent world models from ordinary single-view videos. It decomposes each monocular clip into the camera operator's ego-motion and the visible subject's trajectory (Monocular World-State Unrolling), which recovers synchronized multi-agent motion inside one 3D space without any multi-camera rig. A Subject-Aware World Generator conditions on per-agent identity images, and a World-State Alignment module inserts per-frame cross-attention at every layer of the video diffusion transformer so the two views denoise together and stay geometrically and dynamically consistent. Experiments report better cross-view consistency and identity fidelity than prior single-view approaches.

**How this builds on what you know:**
The generative backbone is the diffusion transformer, DiT (Peebles 2023, key YJ9TK993, Vision-Language and Generative community), and the denoising process is standard DDPM (Ho 2020, key GX7WR7KA, same community). Where DiT generates one view by denoising a single latent stream, MetaWorld runs two coupled streams and ties them together with cross-attention at every transformer layer, because independent denoising cannot keep a shared world consistent across views. The delta is a coupling mechanism added on top of the DiT and DDPM machinery already in your library.

### Prisma-World: Camera-Controllable Multi-Agent Video World Model
arXiv:2606.09507 (Sun, Peng et al. — 08 Jun 2026) — https://arxiv.org/abs/2606.09507

Prisma-World attacks the same problem as MetaWorld, multi-agent video generation where overlapping views must agree, but takes a different route. It processes all agent videos in one full-attention sequence, uses a multi-agent rotary position design (RoPE) to keep agent identities separate while sharing a synchronized time axis, and injects relative camera geometry into attention so overlapping viewpoints are biased toward the same scene evidence. Training uses an overlap-decaying curriculum and minimap-conditioned structural guidance. The authors release PrismaDataset, a large synthetic (UE5) set with panoramic capture, composable multi-agent view groups, and precise camera and action labels. One model can then generate high-fidelity multi-agent video with flexible agent counts, camera control, and better cross-view consistency.

**How this builds on what you know:**
Like MetaWorld, Prisma-World builds on the DiT (Peebles 2023, key YJ9TK993) and DDPM (Ho 2020, key GX7WR7KA) generative stack in your library. Where MetaWorld couples two views with per-frame cross-attention learned from real single-view video, Prisma-World puts all views in one full-attention sequence and injects explicit camera geometry, and it trains on a synthetic dataset with exact camera labels. The two papers are a matched pair this month: same consistency problem, one solving it with learned cross-view attention from real data, the other with geometry-conditioned full attention on synthetic data.

---

## Tier D — Time-series / Bio-sensing Gap Watch

**Already ported (closing off).** CAP (above) ports cross-modal contrastive alignment (the sensor-to-language idea from Sensor2Text, Community 4) into PPG and adds patient-level EHR text as the anchor. After this paper, "align a physiological signal to clinical text by contrastive learning" is demonstrated for PPG on standard cardiorespiratory tasks. The room that remains inside this idea is other wearable modalities (accelerometer and IMU behavioral streams, multimodal sensor fusion) and process-level reasoning over the aligned representation, not the alignment itself.

**Unported opportunity 1 — Tandem RL for on-device time-series reasoning.** Tandem RL co-trains a strong senior with a frozen weak junior so the junior can follow the reasoning. This has not been applied to time-series or health-signal reasoning models. Transfer hypothesis: co-train a large time-series reasoning model with a frozen small model that can actually run on a watch, so the reasoning trace hands off cleanly to the on-device model for continuous monitoring, and drift toward unreadable traces is reduced.

**Unported opportunity 2 — World-state alignment across sensor modalities.** MetaWorld and Prisma-World enforce consistency across several camera views of one physical scene by coupling their denoising. This has not been applied to physiological sensing. Transfer hypothesis: treat simultaneously recorded PPG, ECG, and accelerometer as different "views" of one physiological state, and use a cross-view consistency loss (per-frame cross-attention or geometry-style coupling) to enforce that a single latent physiological state explains all channels, improving robustness when one channel is noisy or missing.

---

## News — model and product releases

Reported this period from secondary trackers, not verified against primary announcements: Google Gemini 3.5 Pro; Meta "Muse Spark" (first model from Meta Superintelligence Labs); continued reporting around an OpenAI GPT-5.5 release and an OpenAI confidential S-1 filing dated 8 June 2026. Treat these as leads to confirm, not settled facts.

---

End of digest. Close this tab when done.
