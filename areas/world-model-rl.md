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

### Recent Activity

2026-07-17 | 2607.14076 added | reviews interactive world models through the lens of a game engine's action-state-observation loop, organizes methods along four axes (action control, state dynamics, state-observation persistence, real-time generation), and releases a Black Myth: Wukong data engine with over 90 hours of gameplay carrying frame-aligned actions and ground-truth states; Tier B
2026-07-13 | 2607.05339 added | targets the exploration failure of Group Relative Policy Optimization on hard prompts by importing verified off-support solutions through a short distillation phase before returning to on-policy updates; ScienceWorld rises 12.5 to 26.7; Tier B
2026-06-05 | 2506.14965 added | 92K cross-domain RL corpus; RL is a domain-conditional skill activator; GURU-7B/32B SOTA among open RL-trained models; Tier A
2026-05-14 | Area page seeded | 31 papers from Zotero, 3 from graphify seed.
