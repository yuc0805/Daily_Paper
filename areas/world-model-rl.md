## World Models and Reinforcement Learning

### Timeline

1999 | Policy Gradient (Sutton et al.) | 
2000 | IS Eligibility Traces (Precup et al.) | 
2013 | DQL Atari (Mnih et al.) | 
2013 | Deep CCA (Andrew et al.) | 
2015 | DQN (Mnih et al.) | 
2017 | DRL Sepsis (Raghu et al.) | 
2017 | PPO (Schulman et al.) | 
2018 | TD3 (Fujimoto et al.) | 
2018 | World Models (Ha et al.) | 
2020 | CEM (Pinneri et al.) | 
2020 | Offline RL (Levine et al.) | 
2020 | Optimistic Offline RL (Agarwal et al.) | 
2020 | RL Healthcare Survey (Yu et al.) | 
2021 | Decision Transformer (Chen et al.) | 
2021 | OPE Study (Voloshin et al.) | 
2023 | AIVE (Lee et al.) | 
2023 | LAW (Hu et al.) | 
2023 | OPE for RecSys (Deffayet et al.) | 
2023 | VIP (Ma et al.) | 
2024 | Coconut (Hao et al.) | 
2024 | DT RL Vitamin (Yan et al.) | 
2024 | Navigation World Models (Bar et al.) | 
2024 | TD-MPC2 (Hansen et al.) | 
2024 | World Model Eval (Vafa et al.) | 
2025 | Brain Science FMs (Serre et al.) | 

2026-06 | GURU (2506.14965) | 92K cross-domain RL corpus; domain-conditional transfer for LLM reasoning

2026-07 | TREK (2607.05339) | a staged forward-KL warm start on verified off-support solutions precedes on-policy reinforcement learning, fixing the exploration stall of GRPO on hard prompts
2026-07 | Pixels to States (2607.14076) | reframes interactive world models as a game engine with an explicit persistent state; releases a Black Myth: Wukong dataset with ground-truth states
2026-07 | BadWAM (2607.15207) | world-action drift attacks; small visual perturbations split a model's imagined future from its executed action

2026-08 | DreamX-Phi 1.0 (2608.13489) | action-conditioned video world model injecting per-arm SE(3) geometry into attention for manipulation
2026-08 | PAWBench (2608.27345) | benchmark asking whether a video world model reproduces the distribution of valid outcomes rather than one plausible outcome
2026-08 | Code as Worlds (2608.27549) | a physical scene is written as executable code, recovered by an agentic propose-execute-render-verify loop and reused as verified supervision

2026-09 | ZimaBlue (2609.00188) | three-stage curriculum from action-free egocentric video to robot control; zero-shot success 36.1 to 77.8 percent as the unlabelled corpus grows
2026-09 | SolarWM (2609.02886) | one frame-aligned data contract over 1.43 million clips, four backbones from 5B to 33B under a shared recipe, hours-long rollout from 5-second training clips

### Paper List

[KNOWN] [1999] Sutton et al. — Policy Gradient. zotero_key:DAGWCZ67.
[KNOWN] [2000] Precup et al. — IS Eligibility Traces. zotero_key:JKQ3USCI.
[KNOWN] [2013] Mnih et al. — DQL Atari. zotero_key:6XBKXTFZ.
[KNOWN] [2013] Andrew et al. — Deep CCA. zotero_key:SCJHA35S.
[KNOWN] [2015] Mnih et al. — DQN. zotero_key:2FRGIK77.
[KNOWN] [2017] Raghu et al. — DRL Sepsis. zotero_key:QAKMF2J4.
[KNOWN] [2017] Schulman et al. — PPO. zotero_key:KQTIJC4U.
[KNOWN] [2018] Fujimoto et al. — TD3. zotero_key:6GKDVDPY.
[KNOWN] [2018] Ha et al. — World Models. zotero_key:938DAXZT.
[KNOWN] [2020] Pinneri et al. — CEM. zotero_key:ZNEMGMWY.
[KNOWN] [2020] Levine et al. — Offline RL. zotero_key:ZULLM3UF.
[KNOWN] [2020] Agarwal et al. — Optimistic Offline RL. zotero_key:2HAUL3B9.
[KNOWN] [2020] Yu et al. — RL Healthcare Survey. zotero_key:JMNZD5RT.
[KNOWN] [2021] Chen et al. — Decision Transformer. zotero_key:3J97GWND.
[KNOWN] [2021] Voloshin et al. — OPE Study. zotero_key:Y2MKM9Y3.
[KNOWN] [2023] Lee et al. — AIVE. zotero_key:NUTRKPSL.
[KNOWN] [2023] Hu et al. — LAW. zotero_key:ERFKSNIC.
[KNOWN] [2023] Deffayet et al. — OPE for RecSys. zotero_key:PGAG7J5S.
[KNOWN] [2023] Ma et al. — VIP. zotero_key:BT2MFL2J.
[KNOWN] [2024] Hao et al. — Coconut. zotero_key:2BJAGQ5K.
[KNOWN] [2024] Yan et al. — DT RL Vitamin. zotero_key:YPRGQZRB.
[KNOWN] [2024] Bar et al. — Navigation World Models. zotero_key:JQ7JD8AR.
[KNOWN] [2024] Hansen et al. — TD-MPC2. zotero_key:A4WGRRQ9.
[KNOWN] [2024] Vafa et al. — World Model Eval. zotero_key:P92FLHJ2.
[KNOWN] [2025] Serre et al. — Brain Science FMs. zotero_key:M963842L.
[KNOWN] [2025] Shen et al. — CODI. zotero_key:FFWLYL3J.
[KNOWN] [2025] Zhou et al. — DINO-WM. zotero_key:W44RSJJI.
[KNOWN] [2025] Kuzina et al. — KaVa. zotero_key:XH2XHIL5.
[KNOWN] [2025] Zhang et al. — Soft Thinking. zotero_key:EGRXFZU9.
[KNOWN] [2026] Yu et al. — Latent Space Survey. zotero_key:KRVDKDGH.
[KNOWN] [2026] Dupoux et al. — Why AI Doesnt Learn. zotero_key:YREEFKLG.

[2026] 2506.14965 — GURU: Revisiting RL for LLM Reasoning from A Cross-Domain Perspective. [https://arxiv.org/abs/2506.14965](https://arxiv.org/abs/2506.14965). external.

[2026] 2607.05339 — TREK: Distill to Explore, Reinforce to Refine. [https://arxiv.org/abs/2607.05339](https://arxiv.org/abs/2607.05339). external.
[2026] 2607.14076 — From Pixels to States: Rethinking Interactive World Models as Game Engines. [https://arxiv.org/abs/2607.14076](https://arxiv.org/abs/2607.14076). external.
[2026] 2607.15207 — BadWAM: When World-Action Models Dream Right but Act Wrong. [https://arxiv.org/abs/2607.15207](https://arxiv.org/abs/2607.15207). external.

[2026] 2608.13489 — DreamX-Phi 1.0: Action-Conditioned Video World Model for Robotic Manipulation. [https://arxiv.org/abs/2608.13489](https://arxiv.org/abs/2608.13489). external.
[2026] 2608.27345 — PAWBench: How Far Are We from Probabilistically Aligned World Modeling?. [https://arxiv.org/abs/2608.27345](https://arxiv.org/abs/2608.27345). external.
[2026] 2608.27549 — Code as Worlds: Agentic Discovery of Executable World Representations for Physical Reasoning. [https://arxiv.org/abs/2608.27549](https://arxiv.org/abs/2608.27549). external.

[2026] 2609.00188 — ZimaBlue: Evolving Generalizable World Action Models through Scalable Video Pre-training. [https://arxiv.org/abs/2609.00188](https://arxiv.org/abs/2609.00188). external.

[2026] 2609.02886 — SolarWM: Open Data and Scalable Training for Long-Horizon Video World Models. [https://arxiv.org/abs/2609.02886](https://arxiv.org/abs/2609.02886). external.

### Recent Activity

2026-09-03 | 2609.02886 added | SolarWM separates the data problem from the modeling problem in video world models, since datasets differ in temporal scale, camera geometry, visual quality, motion statistics and captioning style while video generators differ in representation and objective, so naive mixing produces inconsistent supervision and results that cannot be compared; a reconfigurable data engine converts 1.43 million canonical clips from 10 datasets into one frame-aligned contract covering observations, metric camera geometry, captions, quality metadata, selection decisions and provenance, and decouples source processing from mixture construction so the mixture becomes an experimental variable rather than a preprocessing accident, after which four models from 5B to 33B parameters are instantiated on Wan2.2, LTX-2.5 and MiniMax-H3 under a shared three-stage recipe of bidirectional adaptation, teacher-forced autoregressive initialization and distribution matching distillation; where World Models (938DAXZT) learned dynamics in a single environment and treated the corpus as given, this paper treats the data contract itself as the object of study, because the current obstacle is not learning dynamics but comparing models trained on incommensurable corpora, where Navigation World Models (JQ7JD8AR) pushed video world models toward controllable long-horizon rollout under camera and action conditioning, SolarWM supplies the corpus-level camera geometry that such conditioning assumes rather than improving the conditioning itself, and where DINO-WM (W44RSJJI) held the representation fixed and let the task vary in order to make world models comparable, SolarWM holds the data fixed and lets the representation vary across four backbones, which is the complementary control and the one that isolates the training recipe; the causal models support real-time rollouts from minutes to hours after training on only 5-second sequences, with no long-sequence fine-tuning and no attention-sink mechanism, and data, weights, recipes and framework are released; the transferable part is the methodological move of standardizing the data contract before varying the backbone, because wearable corpora differ in sampling rate, device, wear position, label protocol and missingness in the same way and are mixed naively for the same reason; Tier B

2026-09-02 | 2609.00188 added | ZimaBlue orders three stages so that dynamics are learned before actions are attached, causal embodied video pre-training on human and robot egocentric video, video-action mid-training that grounds those dynamics in heterogeneous robot trajectories under a unified action representation, then specialization to a target robot, with an asynchronous slow-fast split that runs a high-capacity world model for representation and a light branch for 30 Hz action prediction on a single RTX 4090; real-robot zero-shot success rises from 36.1 percent when training on target-robot data alone to 77.8 percent as the action-free corpus grows past 120,000 hours while the action-labelled portion is held fixed, which is what makes the ordering credible rather than merely plausible, since the video is evidently carrying dynamics and not only visual variety; where World Models (938DAXZT) learned the predictive model from the agent's own interaction data and DINO-WM (W44RSJJI) took the representation as given and put the learning into planning, this paper learns the model from video the agent never generated and never labelled, then attaches actions in a short second stage; the slow-fast split answers the standing objection that sampling from a generative world model is too slow to close a control loop, by decoupling the rate at which representations are refreshed from the rate at which actions are emitted; the paper also joins the Video Action Recognition and Reinforcement Learning communities of the seed graph, which the seed graph does not connect, so it opens a bridge rather than extending one; Tier B

2026-08-31 | 2608.27549 added | represents a physical scene as executable code rather than as pixels or a latent vector, writing object composition, governing dynamics and visual appearance as a program that can be run forward to answer how the scene evolves or responds to an intervention, and recovers such a program from a video or a natural-language description through an agentic loop modeled on abductive reasoning that proposes a candidate program, executes it, renders the result, compares against the observation and refines; where Ha and Schmidhuber compressed observations into a learned latent state and rolled that state forward, this paper writes the state and its dynamics as source code, because a latent vector cannot be read, checked against physics or queried for a parameter, and where Vafa showed that accurate next-step prediction does not imply a coherent internal world model but supplied no construction, here an executable program either renders to match the observation or it does not, so verification is a program execution rather than a probing experiment; verified programs are then reused as scalable supervision for a vision-language model, and Code-as-World-VL reports state of the art on QuantiPhy above leading proprietary models, with weights released at 4B and 9B; the pipeline rather than any single component is the contribution, since none of the three parents produce supervision; Tier B

2026-08-29 | 2608.27345 added | PAWBench argues that a video generator used as a world model should reproduce the distribution of valid outcomes under a given initial state and action rather than one plausible outcome, formalises that requirement as probabilistic alignment, supplies 50 scenarios in which a physical process can unfold in more than one legitimate way, and converts repeated rollouts into an empirical outcome distribution through PAWEval; across eleven current systems none consistently matches the reference probabilities while still covering the range of valid behaviours, and the authors then test whether prompting, initial noise sampling or training can reshape the predictive distribution; where World Model Eval (P92FLHJ2) showed that sequence accuracy does not certify a coherent internal model, this paper makes the same point at the level of the output distribution and supplies a measurable criterion for it, and where DDPM and DiT are trained as samplers they are in practice judged one sample at a time, so the sampling property the training objective optimises is never checked; Tier B

2026-08-16 | 2608.13489 added | DreamX-Phi separates visual realism from action faithfulness and treats the second as the property a world model needs for planning, since a rollout can look convincing while moving the wrong arm or losing the object mid-grasp; three mechanisms enforce faithfulness, per-arm SE(3) transformations injected into attention through PRoPE-style geometric encoding, a light depth branch constraining scene geometry, and SAM3 object masks with a frozen V-JEPA teacher holding the manipulated object consistent through the grasp, after which the multi-step generator is distilled into a few-step student by distribution-matching distillation; the evidence is first place on Track 1 and second on Track 2 of the WorldArena 2.0 Challenge rather than a component ablation, so the three mechanisms cannot be separated; Tier B
