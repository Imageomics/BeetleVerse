# Benchmarking

Head-to-head evaluation of pretrained vision backbones on beetle **genus** and
**species** classification, one folder per dataset. Every model is **frozen** and
**linear-probed** (see the [common pipeline](../README.md#common-evaluation-pipeline)),
so results measure representation quality on equal footing.

## Datasets in this track

| Folder | Source dataset | Provenance | Ranks evaluated | # model notebooks | README |
|---|---|---|---|:--:|---|
| [`AllCarabids/`](./AllCarabids) | Merged superset of all four | Built from the four manifests below | species | 12 | [→](./AllCarabids/README.md) |
| [`Beetle-PUUM/`](./Beetle-PUUM) | Hawaii-beetles | 🤗 Hugging Face (in-notebook) | genus **+** species | 38 | [→](./Beetle-PUUM/README.md) |
| [`BeetlePalooza/`](./BeetlePalooza) | 2018-NEON-beetles | 🤗 Hugging Face (in-notebook) | genus **+** species | 25 | [→](./BeetlePalooza/README.md) |
| [`I1MC/`](./I1MC) | Insect-1M carabids | `processI1MC.py` manifest | species | 12 | [→](./I1MC/README.md) |
| [`I1MC-Filtered/`](./I1MC-Filtered) | Insect-1M carabids (quality-filtered) | Filtered `processI1MC.py` manifest | species | 12 | [→](./I1MC-Filtered/README.md) |
| [`NHMC/`](./NHMC) | NHM-Carabids | `processNHMC.py` manifest | species | 12 | [→](./NHMC/README.md) |


## Model zoo

Backbones span four families. The **exact checkpoint for each model is defined in
that model's notebook** (the model-loading cell) — treat the notebook as the
source of truth for the precise weights used.

- **Supervised CNN / transformer:** ConvNeXt, RegNet, ResNeXt, ResNet152,
  EfficientNet, MobileNet, LeViT, SWINv2, ViT
- **Self-supervised:** DINOv2, MoCo v3, SwAV, SimCLR, SimMIM, ViT-MAE, BeiT
- **Vision–language:** CLIP, SigLIP, BioCLIP (`hf-hub:imageomics/bioclip` via
  `open_clip`), ViLT
- **Wildlife re-ID:** MegaDescriptor

Not every model appears in every dataset folder — the richest sweep is in
**Beetle-PUUM**. See each folder's README for its exact model list.

## Files in each dataset folder

| File | Contents |
|---|---|
| `<Model>-species.ipynb` / `<Model>-genus.ipynb` | Embed → probe → score notebook |
| `<Model>-species.csv` / `<Model>-genus.csv` | Per-image predictions |
| `<Model>-*-metrics.csv` | Accuracy, Precision, Recall, F1-Score, Balanced Acc, MCC |
| `AllCarabids.csv` *(AllCarabids only)* | The merged manifest itself |

**Predictions columns:** `ImageFilePath`, `Genus` and/or `ScientificName`, then
`Pred_NaiveBayes`, `Pred_LogisticRegression`, `Pred_NearestNeighbor`,
`Pred_MLP_Baseline` (Beetle-PUUM adds SVM and Random Forest heads).

## Running a benchmark

1. Prepare the dataset (HF datasets load in-notebook; **I1MC**/**NHMC** need their
   `process*.py` manifest first — see the [root README](../README.md#dataset-preparation-scripts)).
2. Open `<Model>-<rank>.ipynb`, replace the `/path/to/...` placeholders with your
   manifest CSV (in) and output paths (out).
3. Run all cells → `<Model>-<rank>.csv` + `<Model>-<rank>-metrics.csv`.

## Reproducibility notes

- The **`AllCarabids.csv`** manifest is tab-separated with columns
  `kingdom, phylum, cls, order, family, genus, species, common_name, filepath,
  class`; `filepath` values are only meaningful relative to your local image
  root, so re-point them after assembling the four datasets locally.
- `I1MC` vs `I1MC-Filtered` share the same models; the **Filtered** set drops the samples where one or more taxa is undefined.
