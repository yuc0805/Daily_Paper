## LLM and AI for Health

### Timeline

2023 | GLOBEM (Xu et al.) | 
2023 | LLMs Few-Shot Health (Liu et al.) | 
2023 | UNI Pathology (Chen et al.) | 
2024 | HARMamba (Li et al.) | 
2024 | HeAR (Baur et al.) | 
2024 | Health-LLM (Kim et al.) | 
2024 | MindScape (Nepal et al.) | 
2024 | SSL for HAR (Yuan et al.) | 
2024 | Sensor2Text (Chen et al.) | 
2025 | CounselBench (Li et al.) | 
2025 | Foundation Models Biosignals (Gu et al.) |  [anchor]
2025 | HealthAgent (Sun et al.) | 
2026 | Verifiable Physio Reasoning (Wang et al.) | 

2026-05 | Wearable Health FM (2605.22759) | largest wearable health FM; LLM-agent AutoML over frozen sensor embeddings
2026-05 | xMAE (2605.00973) | physiology-aware masked cross-modal reconstruction across ECG and PPG
2026-06 | Uncertainty Anomaly Detection (2605.13816) | smartwatch-based psychotic relapse detection via forecasting uncertainty and multi-task fusion
2026-06 | Biosignal Fingerprinting (2605.09579) | cross-modal MAE for paired ECG and PPG; single-modality inference at test time
2026-06 | Vivaldi (2603.04142) | multi-agent physiological TS interpretation with clinical evaluation
2026-06 | Uncertainty-Aware Clinical FM (2604.04175) | represents each patient as a distribution over latent states and marks the unobserved part as epistemic uncertainty
2026-06 | AnyPPG (2511.01747) | ECG-guided PPG foundation model pretrained on over 100,000 hours of synchronized PPG and ECG
2026-07 | CAP (2606.15284) | PPG encoder anchored to patient-level clinical text rather than the signal alone
### Paper List

[KNOWN] [2023] Xu et al. — GLOBEM. zotero_key:ICD9EG8Q.
[KNOWN] [2023] Liu et al. — LLMs Few-Shot Health. zotero_key:JX3X3KH5.
[KNOWN] [2023] Chen et al. — UNI Pathology. zotero_key:6T29JLTN.
[KNOWN] [2024] Li et al. — HARMamba. zotero_key:HE9X47KN.
[KNOWN] [2024] Baur et al. — HeAR. zotero_key:3LA8GNCU.
[KNOWN] [2024] Kim et al. — Health-LLM. zotero_key:7RHTW5L3.
[KNOWN] [2024] Nepal et al. — MindScape. zotero_key:K4PR34NU.
[KNOWN] [2024] Yuan et al. — SSL for HAR. zotero_key:RTMH75VW.
[KNOWN] [2024] Chen et al. — Sensor2Text. zotero_key:ELYUE3NF.
[KNOWN] [2025] Li et al. — CounselBench. zotero_key:GST6E6A6.
[KNOWN] [2025] Gu et al. — Foundation Models Biosignals. zotero_key:2XWEG7AF.
[KNOWN] [2025] Sun et al. — HealthAgent. zotero_key:R2D2W9DD.
[KNOWN] [2026] Wang et al. — Verifiable Physio Reasoning. zotero_key:2BGP9QJL.

[2026] 2605.22759 — Towards a General Intelligence and Interface for Wearable Health Data. [https://arxiv.org/abs/2605.22759](https://arxiv.org/abs/2605.22759). external.
[2026] 2605.00973 — Physiology-Aware Masked Cross-Modal Reconstruction for Biosignal Representation Learning (xMAE). [https://arxiv.org/abs/2605.00973](https://arxiv.org/abs/2605.00973). external.
[2026] 2605.13816 — Uncertainty-Driven Anomaly Detection for Psychotic Relapse Using Smartwatches. [https://arxiv.org/abs/2605.13816](https://arxiv.org/abs/2605.13816). external.
[2605] 2605.09579 — Biosignal Fingerprinting: A Cross-Modal PPG-ECG Foundation Model. [https://arxiv.org/abs/2605.09579](https://arxiv.org/abs/2605.09579). external.
[2026] 2603.04142 — Vivaldi: A Multi-Agent Framework for Interpreting Multivariate Physiological Time Series. [https://arxiv.org/abs/2603.04142](https://arxiv.org/abs/2603.04142). external.
[2026] 2604.04175 — Uncertainty-Aware Foundation Models for Clinical Data. [https://arxiv.org/abs/2604.04175](https://arxiv.org/abs/2604.04175). external.
[2026] 2511.01747 — AnyPPG: An ECG-Guided PPG Foundation Model Trained on Over 100,000 Hours of Recordings. [https://arxiv.org/abs/2511.01747](https://arxiv.org/abs/2511.01747). external.

[2026] 2606.15284 — CAP: Towards PPG Universal Representation Learning with Patient-level Supervision. [https://arxiv.org/abs/2606.15284](https://arxiv.org/abs/2606.15284). external.

### Recent Activity

2026-07-01 | 2606.15284 added | CAP anchors a PPG encoder to patient-level clinical text distilled from records rather than to the waveform alone, reporting an average relative gain of +26.7 percent across four cardiorespiratory tasks; Tier A
2026-06-29 | 2511.01747 added | AnyPPG uses synchronized ECG to guide a PPG encoder pretrained on over 100,000 hours of paired recordings from 58,796 participants, reporting average gains of 12.8% on regression and 9.1% on classification across eleven physiological tasks; Tier B
2026-06-25 | 2604.04175 added | clinical foundation model that emits a set-valued distribution per patient rather than a point embedding, mixing reconstruction, contrastive, and distributional terms; better calibration under missing data; Tier B
2026-06-09 | 2603.04142 added | role-structured multi-agent system for physiological TS explanation; validated with EM clinicians; Tier B
2026-06-04 | 2605.09579 added | Multi-modal Masked Autoencoder on 3.4M paired ECG and PPG segments; cross-modal contrastive + reconstruction; AUROC 0.97; Tier B
