# Domain Shift · BPZ-I1MC-species

**Lab → in-situ** transfer at species level: train on ethanol-preserved collections, test on in-situ field photographs.

| | Dataset | Split file | Rows |
|---|---|---|--:|
| **Train (source)** | BeetlePalooza | `train.csv` | 11,325 |
| **Test (target)** | Insect-1M carabids | `test.csv` | 1,871 |

**Rank:** species

## Data provenance

Datasets used in this pair (see the [root README](../../README.md#data-provenance)
for full details and commands):

- **BeetlePalooza** from [Hugging Face](https://huggingface.co/datasets/imageomics/2018-NEON-beetles) (in-notebook)
- **Insect-1M carabids** via [`processI1MC.py`](../../processI1MC.py)

The committed `train.csv` / `test.csv` fix exactly which rows train and test every
model, so cross-model comparison here is apples-to-apples and reproducible given
the images. Both splits share columns: `ImageFilePath, Genus, ScientificName, Dataset`.

## Models & files

Six models, numbered: `1.BioCLIP`, `2.CLIP`, `3.LeViT`, `4.ConvNeXt`,
`5.SWINv2`, `6.ViLT`. For each:

| File | Contents |
|---|---|
| `N.<Model>.ipynb` | Embed → fit head on `train.csv` → evaluate on `test.csv` |
| `N.<Model>.csv` | Target-domain predictions |
| `N.<Model>-metrics.csv` | Accuracy, Precision, Recall, F1-Score, Balanced Acc, MCC |

> **Filename note:** the ConvNeXt predictions are committed as
> `4.ConvNeXt-species.csv` even here; it is a naming artifact only — contents
> reflect this folder's **species** rank.

## Reproduce

1. Prepare the source and target datasets (links above).
2. Verify `ImageFilePath` values in `train.csv`/`test.csv` resolve against your
   local image roots; re-point if needed.
3. Open `N.<Model>.ipynb`, set paths, run all cells → predictions + metrics CSVs.
