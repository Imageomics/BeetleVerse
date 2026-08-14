# Benchmarking · NHMC (NHM-Carabids)

Expert-verified carabids from the **Natural History Museum, London**. Authoritative taxonomy labels but no accompanying metadata; some images are blurry or unevenly lit.

**Rank(s) evaluated:** species

**Models benchmarked:** 12 (see list below)

## Data provenance & preparation

Built from the raw Zenodo release ([10.5281/zenodo.3549369](https://zenodo.org/record/3549369)) with [`processNHMC.py`](../../processNHMC.py), which resolves taxonomy per GBIF species key via the GBIF API.

> **Preparation:** **Run `processNHMC.py` first** to produce the manifest CSV.

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
