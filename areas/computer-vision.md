## Computer Vision

### What

Computer vision covers models for image classification, object detection, segmentation, and visual representation learning. The field has moved from CNNs (ResNet) through vision transformers (ViT, Swin) to foundation models (SAM, DINOv2). This area focuses on the backbone architectures and pre-training strategies rather than generative models (covered in generative-cv.md).

### Why

Visual understanding is required in autonomous driving, medical imaging, robotics, and surveillance. Transformer-based architectures now match or exceed CNNs on most benchmarks, but the choice of architecture, pre-training data, and fine-tuning strategy still matters for domain-specific applications.

### Baseline

Train a ResNet-50 from scratch on the target dataset with supervised cross-entropy loss. The main failure mode is that ResNet requires large labeled datasets and its fixed receptive field limits performance on tasks requiring global context (e.g., scene understanding).

### Running Example

Classify ImageNet images into 1000 categories. ResNet-50 trained from scratch achieves 76.1% top-1 accuracy. ViT-B/16 pre-trained on ImageNet-21k and fine-tuned achieves 84.0% top-1 accuracy.

### Baseline vs Method Comparison on the Running Example

| Approach | Output on running example | Why it differs from baseline |
|---|---|---|
| Baseline | See running example above | (anchor) |

### Timeline

2014 | GAN (Goodfellow et al.) | 
2016 | YOLO (Redmon et al.) | 
2017 | DeepLabV3 (Chen et al.) | 
2020 | DETR (Carion et al.) | 
2020 | MoCo (He et al.) | 
2020 | SimCLR (Chen et al.) | 
2021 | CrossViT (Chen et al.) | 
2021 | DINO (Caron et al.) | 
2021 | DPT (Ranftl et al.) | 
2021 | DeiT (Touvron et al.) | 
2021 | MAE (He et al.) | 
2021 | MaskFormer (Cheng et al.) | 
2021 | SegFormer (Xie et al.) | 
2021 | Swin Transformer (Liu et al.) | 
2021 | ViT (Dosovitskiy et al.) | 
2022 | DALL-E 2 (Ramesh et al.) | 
2022 | Mask DINO (Li et al.) | 
2022 | Mask2Former (Cheng et al.) | 
2022 | VAE (Kingma et al.) | 
2023 | BLIP-2 (Li et al.) | 
2023 | FLIP (Li et al.) | 
2023 | MAE Theory (Zhang et al.) | 
2023 | SAM (Kirillov et al.) | 
2024 | DiChaViT (Pham et al.) | 
2024 | MedSAM (Ma et al.) | 

### Key Methods

| Method | Year | Core idea (one clause) | Best benchmark result | Cost / limitation |
|---|---|---|---|---|
| DETR | 2020 | _To be filled_ | _To be filled_ | _To be filled_ |
| Swin Transformer | 2021 | _To be filled_ | _To be filled_ | _To be filled_ |
| DALL-E 2 | 2022 | _To be filled_ | _To be filled_ | _To be filled_ |
| MAE Theory | 2023 | _To be filled_ | _To be filled_ | _To be filled_ |

### Benchmark Results

| Method | Benchmark | Metric | Score | Source paper |
|---|---|---|---|---|
| _To be added as papers accumulate._ | | | | |

### Limitations

_To be added as papers accumulate._

### Paper List

[KNOWN] [2014] Goodfellow et al. — GAN. zotero_key:NJ5BZCFJ.
[KNOWN] [2016] Redmon et al. — YOLO. zotero_key:PN27XKD6.
[KNOWN] [2017] Chen et al. — DeepLabV3. zotero_key:P5Q5TRVY.
[KNOWN] [2020] Carion et al. — DETR. zotero_key:QTFCR4G9.
[KNOWN] [2020] He et al. — MoCo. zotero_key:BMA3ALHC.
[KNOWN] [2020] Chen et al. — SimCLR. zotero_key:EQ3FJMPY.
[KNOWN] [2021] Chen et al. — CrossViT. zotero_key:EW4CUT2S.
[KNOWN] [2021] Caron et al. — DINO. zotero_key:DVUL4GU6.
[KNOWN] [2021] Ranftl et al. — DPT. zotero_key:YXTBME7X.
[KNOWN] [2021] Touvron et al. — DeiT. zotero_key:Y2C9BISN.
[KNOWN] [2021] He et al. — MAE. zotero_key:A5HBRQB9.
[KNOWN] [2021] Cheng et al. — MaskFormer. zotero_key:BNKLHAQM.
[KNOWN] [2021] Xie et al. — SegFormer. zotero_key:MYSZ5BCQ.
[KNOWN] [2021] Liu et al. — Swin Transformer. zotero_key:AVF27QK7.
[KNOWN] [2021] Dosovitskiy et al. — ViT. zotero_key:B7F2Q998.
[KNOWN] [2022] Ramesh et al. — DALL-E 2. zotero_key:DUERBZGM.
[KNOWN] [2022] Li et al. — Mask DINO. zotero_key:EAIQ4KD3.
[KNOWN] [2022] Cheng et al. — Mask2Former. zotero_key:PM4XDV56.
[KNOWN] [2022] Kingma et al. — VAE. zotero_key:MTXFCQX6.
[KNOWN] [2023] Li et al. — BLIP-2. zotero_key:4N5WXKPI.
[KNOWN] [2023] Li et al. — FLIP. zotero_key:64H6TK5Y.
[KNOWN] [2023] Zhang et al. — MAE Theory. zotero_key:6INGKIJV.
[KNOWN] [2023] Kirillov et al. — SAM. zotero_key:PQNM49GJ.
[KNOWN] [2024] Pham et al. — DiChaViT. zotero_key:5WKSNRIH.
[KNOWN] [2024] Ma et al. — MedSAM. zotero_key:UXDYEMP4.
[KNOWN] [2024] Sun et al. — TTT. zotero_key:SFYVQXEG.

### Recent Activity

2026-05-14 | Area page seeded | 26 papers from Zotero, 4 from graphify seed.
