## Interpretable Machine Learning

### What

Interpretable ML studies how to make model predictions understandable to humans. It covers inherently interpretable models (decision trees, rule lists, risk scores), post-hoc explanation methods (SHAP, LIME, concept-based explanations), and the meta-question of what interpretability means and how to evaluate it. Sub-areas include XAI methods, framing/philosophy of interpretability, and predictive multiplicity.

### Why

In high-stakes domains (healthcare, criminal justice, lending), stakeholders need to understand why a model made a particular prediction. Post-hoc explanations can be misleading or unstable, and the field lacks consensus on evaluation criteria. Predictive multiplicity (multiple models with similar accuracy but different individual predictions) further complicates the picture.

### Baseline

Train a black-box gradient boosted tree and inspect feature importances from the tree structure. The main failure mode is that global feature importance does not explain individual predictions and can be misleading when features are correlated.

### Running Example

Predict whether a loan applicant will default (binary classification on the FICO dataset). The gradient boosted tree achieves AUC 0.79 and reports 'income' as the top feature. But for a specific applicant who was denied, the user wants to know which features to change to get approved. SHAP values reveal that 'number of recent inquiries' was the decisive factor for this individual, and Ustun et al.'s actionable recourse method finds the minimum-cost set of changes.

### Baseline vs Method Comparison on the Running Example

| Approach | Output on running example | Why it differs from baseline |
|---|---|---|
| Baseline | See running example above | (anchor) |

### Timeline

2001 | Two Cultures (Breiman et al.) | 
2011 | Submodular Maximization (Feige et al.) | 
2014 | Comprehensible Models (Freitas et al.) | 
2014 | GAN (Goodfellow et al.) | 
2015 | Explanatory Debugging (Kulesza et al.) | 
2015 | ResNet (He et al.) | 
2016 | Decision Sets (Lakkaraju et al.) | 
2016 | LIME (Ribeiro et al.) | 
2017 | Mythos of Interpretability (Lipton et al.) | 
2017 | Right for Right Reasons (Ross et al.) | 
2017 | SHAP (Lundberg et al.) | 
2019 | Actionable Recourse (Ustun et al.) | 
2019 | Risk Scores (Ustun et al.) | 
2019 | Stop Explaining (Rudin et al.) | 
2020 | Concept Bottleneck (Koh et al.) | 
2020 | Human Factors IML (Hong et al.) | 
2020 | Predictive Multiplicity (Marx et al.) | 
2020 | Sanity Checks (Adebayo et al.) | 
2021 | Manipulating Interpretability (Poursabzi-Sangdeh et al.) | 
2021 | User Study IML (Sixt et al.) | 
2022 | Model Indeterminacy (Brunet et al.) | 
2023 | Consistent Explanations (Ley et al.) | 
2023 | Explanation Constraints (Pukdee et al.) | 
2023 | Post-hoc CBM (Yuksekgonul et al.) | 

### Key Methods

| Method | Year | Core idea (one clause) | Best benchmark result | Cost / limitation |
|---|---|---|---|---|
| Comprehensible Models | 2014 | _To be filled_ | _To be filled_ | _To be filled_ |
| SHAP | 2017 | _To be filled_ | _To be filled_ | _To be filled_ |
| Actionable Recourse | 2019 | _To be filled_ | _To be filled_ | _To be filled_ |

### Benchmark Results

| Method | Benchmark | Metric | Score | Source paper |
|---|---|---|---|---|
| _To be added as papers accumulate._ | | | | |

### Limitations

_To be added as papers accumulate._

### Paper List

[KNOWN] [2001] Breiman et al. — Two Cultures. zotero_key:DQD2J9KR.
[KNOWN] [2011] Feige et al. — Submodular Maximization. zotero_key:VZ5NCDN7.
[KNOWN] [2014] Freitas et al. — Comprehensible Models. zotero_key:JLX2PPVN.
[KNOWN] [2014] Goodfellow et al. — GAN. zotero_key:GG7GSYUJ.
[KNOWN] [2015] Kulesza et al. — Explanatory Debugging. zotero_key:Q4LYVFY8.
[KNOWN] [2015] He et al. — ResNet. zotero_key:3INBF8ND.
[KNOWN] [2016] Lakkaraju et al. — Decision Sets. zotero_key:YJAJHV5A.
[KNOWN] [2016] Ribeiro et al. — LIME. zotero_key:CFDS9G6C.
[KNOWN] [2017] Lipton et al. — Mythos of Interpretability. zotero_key:FN9DST5B.
[KNOWN] [2017] Ross et al. — Right for Right Reasons. zotero_key:6XPE47QI.
[KNOWN] [2017] Lundberg et al. — SHAP. zotero_key:46WR27KQ.
[KNOWN] [2019] Ustun et al. — Actionable Recourse. zotero_key:A362GCCM.
[KNOWN] [2019] Ustun et al. — Risk Scores. zotero_key:QQ29DMJU.
[KNOWN] [2019] Rudin et al. — Stop Explaining. zotero_key:T264MQTK.
[KNOWN] [2020] Koh et al. — Concept Bottleneck. zotero_key:TUIUJY92.
[KNOWN] [2020] Hong et al. — Human Factors IML. zotero_key:4Z8VSMFY.
[KNOWN] [2020] Marx et al. — Predictive Multiplicity. zotero_key:FW3ZISUV.
[KNOWN] [2020] Adebayo et al. — Sanity Checks. zotero_key:SKKD9UXV.
[KNOWN] [2021] Poursabzi-Sangdeh et al. — Manipulating Interpretability. zotero_key:6GBGGUEZ.
[KNOWN] [2021] Sixt et al. — User Study IML. zotero_key:C284A7ZR.
[KNOWN] [2022] Brunet et al. — Model Indeterminacy. zotero_key:SF6V4MPG.
[KNOWN] [2023] Ley et al. — Consistent Explanations. zotero_key:8T8LJMTW.
[KNOWN] [2023] Pukdee et al. — Explanation Constraints. zotero_key:C48LQQN7.
[KNOWN] [2023] Yuksekgonul et al. — Post-hoc CBM. zotero_key:CKEAV8EA.

### Recent Activity

2026-05-14 | Area page seeded | 24 papers from Zotero, 3 from graphify seed.
