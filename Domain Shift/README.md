# Domain Shift

Cross-domain generalization: **train** linear-probing heads on embeddings from
one dataset (source domain) and **test** on another (target domain). Backbones
stay frozen; only the probing head sees the source labels. This measures how well
each pretrained representation transfers across imaging conditions.

## The transfer pairs

Folders are named `SOURCE-TARGET-rank` (train → test).

| Folder | Train (source) | Test (target) | Rank | Shift type |
|---|---|---|---|---|
| [`NHMC-BPZ-genus/`](./NHMC-BPZ-genus) | NHM-Carabids | BeetlePalooza | genus | **lab → lab** (pinned → ethanol-preserved) |
| [`NHMC-I1MC-genus/`](./NHMC-I1MC-genus) | NHM-Carabids | Insect-1M carabids | genus | **lab → in-situ** |
| [`NHMC-I1MC-species/`](./NHMC-I1MC-species) | NHM-Carabids | Insect-1M carabids | species | **lab → in-situ** |
| [`BPZ-I1MC-genus/`](./BPZ-I1MC-genus) | BeetlePalooza | Insect-1M carabids | genus | **lab → in-situ** |
| [`BPZ-I1MC-species/`](./BPZ-I1MC-species) | BeetlePalooza | Insect-1M carabids | species | **lab → in-situ** |

- **Lab → lab** tests robustness to preparation/imaging style within controlled
  settings.
- **Lab → in-situ** is the hard case: clean museum/collection training images vs.
  messy field photographs at test time.

## Models

Each pair evaluates the **same six models**, numbered for ordering:

`1.BioCLIP`, `2.CLIP`, `3.LeViT`, `4.ConvNeXt`, `5.SWINv2`, `6.ViLT`

(A vision–language pair — BioCLIP/CLIP/ViLT — alongside pure-vision transformers
LeViT/ConvNeXt/SWINv2.) The exact checkpoint per model is defined in its notebook.

## Files in each pair folder

| File | Contents |
|---|---|
| `train.csv` | Source-domain split — columns: `ImageFilePath, Genus, ScientificName, Dataset` |
| `test.csv` | Target-domain split — same columns |
| `N.<Model>.ipynb` | Extract embeddings, fit head on `train.csv`, evaluate on `test.csv` |
| `N.<Model>.csv` | Per-image predictions on the target domain |
| `N.<Model>-metrics.csv` | Accuracy, Precision, Recall, F1-Score, Balanced Acc, MCC |


## Running a transfer experiment

1. Build/obtain the source and target datasets (HF for BeetlePalooza; `process*.py`
   for NHMC/I1MC — see the [root README](../README.md#data-provenance)).
2. Confirm `train.csv` / `test.csv` `ImageFilePath` values resolve against your
   local image roots (re-point if needed).
3. Open `N.<Model>.ipynb`, set input/output paths, run all cells → predictions +
   metrics CSVs.

Because the split files are committed, results are fully reproducible given the
images: the same rows train and test every model, so cross-model comparisons are
apples-to-apples.
