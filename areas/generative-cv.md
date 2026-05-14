## Generative Computer Vision

### What

Generative computer vision covers models that synthesize images, videos, or 3D content. The field has progressed from GANs through VAEs to diffusion models, with recent work on transformer-based diffusion (DiT) and latent diffusion (Stable Diffusion). Applications include image generation, inpainting, style transfer, and super-resolution.

### Why

Generative models enable data augmentation, creative tools, and scientific simulation (e.g., generating synthetic medical images for training). The shift from GANs to diffusion models improved training stability and sample diversity, but diffusion models remain computationally expensive at inference time.

### Baseline

Train a GAN (generator + discriminator) on the target image domain. The main failure mode is mode collapse: the generator learns to produce only a few distinct outputs, failing to cover the full data distribution.

### Running Example

Generate a 256x256 image of a bedroom from the LSUN Bedrooms dataset. The GAN baseline achieves FID of 12.4 but produces nearly identical layouts. DDPM achieves FID of 4.9 with much greater diversity in furniture arrangement and lighting.

### Baseline vs Method Comparison on the Running Example

| Approach | Output on running example | Why it differs from baseline |
|---|---|---|
| Baseline | See running example above | (anchor) |
| DALL-E 2 | _To be added as papers accumulate._ | Anchor paper for this area |
| DDPM | _To be added as papers accumulate._ | Anchor paper for this area |

### Timeline

2014 | GAN (Goodfellow et al.) | 
2015 | Nonequilibrium Thermodynamics (Sohl-Dickstein et al.) | 
2018 | FID (Heusel et al.) | 
2019 | StyleGAN (Karras et al.) | 
2020 | CycleGAN (Zhu et al.) | 
2020 | DDPM (Ho et al.) |  [anchor]
2021 | Diffusion Beats GANs (Dhariwal et al.) | 
2021 | Score SDE (Song et al.) | 
2021 | TimeGrad (Rasul et al.) | 
2022 | DDIM (Song et al.) | 
2022 | Palette (Saharia et al.) | 
2022 | Stable Diffusion (Rombach et al.) | 
2022 | StyTr2 (Deng et al.) | 
2023 | BLIP-Diffusion (Li et al.) | 
2023 | CTG++ (Zhong et al.) | 
2023 | DiT (Peebles et al.) | 
2023 | LED (Mao et al.) | 
2024 | l-DAE (Chen et al.) | 

### Key Methods

| Method | Year | Core idea (one clause) | Best benchmark result | Cost / limitation |
|---|---|---|---|---|
| DALL-E 2 | Ramesh 2022 | Anchor method | _To be filled_ | _To be filled_ |
| DDPM | Ho 2020 | Anchor method | _To be filled_ | _To be filled_ |
| CycleGAN | 2020 | _To be filled_ | _To be filled_ | _To be filled_ |
| DiT | 2023 | _To be filled_ | _To be filled_ | _To be filled_ |

### Benchmark Results

| Method | Benchmark | Metric | Score | Source paper |
|---|---|---|---|---|
| _To be added as papers accumulate._ | | | | |

### Limitations

_To be added as papers accumulate._

### Paper List

[KNOWN] [2014] Goodfellow et al. — GAN. zotero_key:GG7GSYUJ.
[KNOWN] [2015] Sohl-Dickstein et al. — Nonequilibrium Thermodynamics. zotero_key:ZPY5XD8Y.
[KNOWN] [2018] Heusel et al. — FID. zotero_key:IMBVAAFD.
[KNOWN] [2019] Karras et al. — StyleGAN. zotero_key:IFU2GS2W.
[KNOWN] [2020] Zhu et al. — CycleGAN. zotero_key:XBYZMQ6D.
[KNOWN] [2020] Ho et al. — DDPM. zotero_key:GX7WR7KA.
[KNOWN] [2021] Dhariwal et al. — Diffusion Beats GANs. zotero_key:MVWM4TZJ.
[KNOWN] [2021] Song et al. — Score SDE. zotero_key:NMJXW3GJ.
[KNOWN] [2021] Rasul et al. — TimeGrad. zotero_key:RILRU5H6.
[KNOWN] [2022] Song et al. — DDIM. zotero_key:9UA578GP.
[KNOWN] [2022] Saharia et al. — Palette. zotero_key:FZBCF7MH.
[KNOWN] [2022] Rombach et al. — Stable Diffusion. zotero_key:DULT32HM.
[KNOWN] [2022] Deng et al. — StyTr2. zotero_key:SNSMLW7Z.
[KNOWN] [2023] Li et al. — BLIP-Diffusion. zotero_key:BRHAE43A.
[KNOWN] [2023] Zhong et al. — CTG++. zotero_key:S4EZPJHE.
[KNOWN] [2023] Peebles et al. — DiT. zotero_key:YJ9TK993.
[KNOWN] [2023] Mao et al. — LED. zotero_key:G4MF7DQQ.
[KNOWN] [2024] Chen et al. — l-DAE. zotero_key:DZ2UYXUL.

### Recent Activity

2026-05-14 | Area page seeded | 18 papers from Zotero, 3 from graphify seed.
