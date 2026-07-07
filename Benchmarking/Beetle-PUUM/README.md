# Benchmarking · Beetle-PUUM (Hawaii-beetles)

Hawaiian-endemic carabids imaged from **pinned specimens** at the Puʻu Makaʻala (PUUM) NEON site. Controlled, high-quality images with rich ecological metadata but limited taxonomic diversity — the cleanest imaging domain in BeetleVerse, and the folder with the **widest model sweep**.

**Rank(s) evaluated:** genus **and** species
**Models benchmarked:** 38 (see list below)

## Data provenance & preparation

Loaded directly from Hugging Face [`imageomics/Hawaii-beetles`](https://huggingface.co/datasets/imageomics/Hawaii-beetles) inside each notebook — **no preparation script required.**

## Pipeline

Each notebook freezes the backbone, extracts image embeddings, and trains
scikit-learn linear-probing heads, then writes predictions and metrics. See the
[common pipeline](../../README.md#common-evaluation-pipeline) for the shared
four-step recipe.

**Prediction columns:** `ImageFilePath`, label column(s), then `Pred_NaiveBayes`, `Pred_LogisticRegression`, `Pred_NearestNeighbor`, `Pred_MLP_Baseline` (plus SVM and Random Forest heads on this dataset).
**Metrics columns:** `Model, Accuracy, Precision, Recall, F1-Score, Balanced Acc, MCC`.

## Files

For every model below there is a `<Model>.ipynb` (notebook), a `<Model>.csv`
(per-image predictions), and a `<Model>-metrics.csv` (scores) — at both genus and species level where present.

### Models in this folder

- `BeIT-genus`
- `BeIT-species`
- `BioCLIP-genus`
- `BioCLIP-species`
- `CLIP-genus`
- `CLIP-species`
- `ConvNeXt-species`
- `DINOv2-genus`
- `DINOv2-species`
- `EfficientNet-species`
- `LeViT-genus`
- `LeViT-species`
- `MegaDescriptor-genus`
- `MegaDescriptor-species`
- `MoCov3-genus`
- `MoCov3-species`
- `MobileNet-species`
- `RegNet-genus`
- `RegNet-species`
- `ResNeXt-genus`
- `ResNeXt-species`
- `ResNet152-species`
- `SWINv2-genus`
- `SWINv2-species`
- `SigLIP-genus`
- `SigLIP-species`
- `SimCLR-genus`
- `SimCLR-species`
- `SimMIM-genus`
- `SimMIM-species`
- `SwAV-genus`
- `SwAV-species`
- `ViLT-genus`
- `ViLT-species`
- `ViT-genus`
- `ViT-species`
- `ViTMAE-genus`
- `ViTMAE-species`

## Reproduce

1. Prepare the dataset as described above.
2. Open a `<Model>` notebook, replace the `/path/to/...` placeholders with your manifest CSV (in) and output paths (out).
3. Run all cells → predictions + metrics CSVs, which should match the committed results.
