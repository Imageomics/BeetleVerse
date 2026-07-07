# Benchmarking · AllCarabids

**AllCarabids** is the merged superset combining all four source datasets (BeetlePUUM, BeetlePalooza, NHM-Carabids, Insect-1M carabids) into one species-level manifest, `AllCarabids.csv`. It stresses each backbone across every imaging condition at once.

**Rank(s) evaluated:** species
**Models benchmarked:** 12 (see list below)

## Data provenance & preparation

`AllCarabids.csv` (tab-separated) with columns `kingdom, phylum, cls, order, family, genus, species, common_name, filepath, class`. Assemble the four datasets locally first, then re-point `filepath` to your image root.

> **Preparation:** Requires all four datasets prepared locally (HF for PUUM/BeetlePalooza; `processI1MC.py` and `processNHMC.py` for I1MC and NHMC), then merged.

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

The merged manifest itself is committed here as `AllCarabids.csv`.

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
