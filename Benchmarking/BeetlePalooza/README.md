# Benchmarking · BeetlePalooza (2018-NEON-beetles)

NEON carabids from 30 continental-US sites, **preserved in ethanol vials**. Broad taxonomic/geographic diversity with ecological metadata; specimens vary in spacing and orientation.

**Rank(s) evaluated:** genus **and** species

**Models benchmarked:** 25 (see list below)

## Data provenance & preparation

Loaded directly from Hugging Face [`imageomics/2018-NEON-beetles`](https://huggingface.co/datasets/imageomics/2018-NEON-beetles) inside each notebook — **no preparation script required.**


## Pipeline

Each notebook freezes the backbone, extracts image embeddings, and trains
scikit-learn linear-probing heads, then writes predictions and metrics. See the
[common pipeline](../../README.md#common-evaluation-pipeline) for the shared
four-step recipe.

**Prediction columns:** `ImageFilePath`, label column(s), then `Pred_NaiveBayes`, `Pred_LogisticRegression`, `Pred_NearestNeighbor`, `Pred_MLP_Baseline`.
**Metrics columns:** `Model, Accuracy, Precision, Recall, F1-Score, Balanced Acc, MCC`.

## Files

For every model below there is a `<Model>.ipynb` (notebook), a `<Model>.csv`
(per-image predictions), and a `<Model>-metrics.csv` (scores) — at both genus and species level where present.

### Models in this folder

- `BeIT-species`
- `BioCLIP-genus`
- `BioCLIP-species`
- `CLIP-genus`
- `CLIP-species`
- `ConvNeXt-species`
- `DINOv2-species`
- `LeViT-genus`
- `LeViT-species`
- `MoCov3-genus`
- `MoCov3-species`
- `RegNet-species`
- `SWINv2-species`
- `SigLIP-genus`
- `SigLIP-species`
- `SimCLR-species`
- `SimMIM-genus`
- `SimMIM-species`
- `SwAV-genus`
- `SwAV-species`
- `ViLT-genus`
- `ViLT-species`
- `ViT-genus`
- `ViT-species`
- `ViTMAE-species`

## Reproduce

1. Prepare the dataset as described above.
2. Open a `<Model>` notebook, replace the `/path/to/...` placeholders with your manifest CSV (in) and output paths (out).
3. Run all cells → predictions + metrics CSVs, which should match the committed results.
