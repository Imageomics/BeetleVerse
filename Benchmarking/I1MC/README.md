# Benchmarking · I1MC (Insect-1M carabids)

Carabid subset of the **Insect-1M** dataset — a mix of lab specimens and **in-situ** field photographs. High taxonomic diversity but variable image quality, inconsistent orientation, and partial captures.

**Rank(s) evaluated:** species
**Models benchmarked:** 12 (see list below)

## Data provenance & preparation

Built from the raw Insect-1M JSON with [`processI1MC.py`](../../processI1MC.py) (filters to Carabidae, downloads images, prunes corrupted files). See the root README for the exact command.

> **Preparation:** **Run `processI1MC.py` first** to produce the manifest CSV (and optionally download the images).

## Pipeline

Each notebook freezes the backbone, extracts image embeddings, and trains
scikit-learn linear-probing heads, then writes predictions and metrics. See the
[common pipeline](../../README.md#common-evaluation-pipeline) for the shared
four-step recipe.

**Prediction columns:** `ImageFilePath`, label column(s), then `Pred_NaiveBayes`, `Pred_LogisticRegression`, `Pred_NearestNeighbor`, `Pred_MLP_Baseline`.
**Metrics columns:** `Model, Accuracy, Precision, Recall, F1-Score, Balanced Acc, MCC`.

## Files

For every model below there is a `<Model>.ipynb` (notebook), a `<Model>.csv`
(per-image predictions), and a `<Model>-metrics.csv` (scores).

### Models in this folder

- `BeIT-species`
- `BioCLIP-species`
- `CLIP-species`
- `ConvNeXt-species`
- `DINOv2-species`
- `LeViT-species`
- `MoCov3-species`
- `SWINv2-species`
- `SigLIP-species`
- `SwAV-species`
- `ViLT-species`
- `ViTMAE-species`

## Reproduce

1. Prepare the dataset as described above.
2. Open a `<Model>` notebook, replace the `/path/to/...` placeholders with your manifest CSV (in) and output paths (out).
3. Run all cells → predictions + metrics CSVs, which should match the committed results.
