## World Models and Reinforcement Learning

### What

This area covers reinforcement learning algorithms and world models: learned simulators that predict environment dynamics. It spans value-based methods (DQN), policy gradient methods (PPO), offline RL, model-based RL with learned world models, and decision transformers that cast RL as sequence modeling.

### Why

RL enables agents to learn optimal behavior from interaction, but sample efficiency remains a core bottleneck. World models address this by allowing the agent to plan in imagination rather than requiring real environment steps. Offline RL further reduces the need for online interaction by learning from pre-collected datasets.

### Baseline

Train a DQN agent with online interaction in the environment, using an epsilon-greedy exploration strategy. The main failure mode is sample inefficiency: DQN requires millions of environment steps to learn a reasonable policy, which is infeasible in real-world settings (robotics, healthcare).

### Running Example

Learn a control policy for the DMControl Walker-Walk task from 500k environment steps. DQN achieves average return of 400. TD-MPC2 with a learned world model achieves average return of 900 because it can plan ahead using predicted future states.

### Baseline vs Method Comparison on the Running Example

| Approach | Output on running example | Why it differs from baseline |
|---|---|---|
| Baseline | See running example above | (anchor) |

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

### Key Methods

| Method | Year | Core idea (one clause) | Best benchmark result | Cost / limitation |
|---|---|---|---|---|
| CEM | 2020 | _To be filled_ | _To be filled_ | _To be filled_ |
| Offline RL | 2020 | _To be filled_ | _To be filled_ | _To be filled_ |
| OPE Study | 2021 | _To be filled_ | _To be filled_ | _To be filled_ |

### Benchmark Results

| Method | Benchmark | Metric | Score | Source paper |
|---|---|---|---|---|
| _To be added as papers accumulate._ | | | | |

### Limitations

_To be added as papers accumulate._

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

### Recent Activity

2026-05-14 | Area page seeded | 31 papers from Zotero, 3 from graphify seed.
