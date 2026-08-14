# Efficient Probing (NHMC)

How much labeled data does linear probing actually need before accuracy falls
apart? This track runs a **sample-efficiency sweep** on the **NHM-Carabids**
dataset at the **species** level, comparing two ways of shrinking the training
set. Backbones stay frozen; only the training budget and sampling strategy change.

## The two sampling strategies

| Strategy | How it selects training images | What it tests |
|---|---|---|
| **Balanced** | Same number of images **per species** | Performance when rare species are protected from under-representation |
| **Proportional** | Images sampled **in proportion to each species' natural frequency** | Performance under realistic, long-tailed class imbalance |

Each strategy is run at **three budgets — 2,900 / 5,800 / 14,500 images** — plus
**full** and **half** dataset references, so you can trace the accuracy-vs-budget
curve and see where balanced and proportional sampling diverge.

## Folder layout

```
Efficient Probing NHMC/
├── Data/     # the sampling manifests (which images are in each training budget)
└── Runs/     # the linear-probing notebooks + committed predictions/metrics
```

### `Data/` — sampling manifests

All are species-level manifests with columns
`ImageFilePath, Genus, ScientificName, Dataset`.

| File | Rows (excl. header) | Meaning |
|---|--:|---|
| `Balanced_2900.csv` | 2,900 | Balanced sample, 2.9k images |
| `Balanced_5800.csv` | 5,800 | Balanced sample, 5.8k images |
| `Balanced_14500.csv` | 14,500 | Balanced sample, 14.5k images |
| `Proportional_2900.csv` | 2,900 | Proportional sample, 2.9k images |
| `Proportional_5800.csv` | 5,800 | Proportional sample, 5.8k images |
| `Proportional_14500.csv` | 14,500 | Proportional sample, 14.5k images |
| `probing_half_dataset.csv` | 30,000 | Half-dataset |
| `probing_full_dataset.csv` | 63,077 | Full-dataset |

### `Runs/` — models and results

Six models, numbered: `1.BioCLIP`, `2.CLIP`, `3.LeViT`, `4.ConvNeXt`,
`5.SWINv2`, `6.ViLT`.

| File | Contents |
|---|---|
| `N.<Model>-LinearProbing-Species.ipynb` | Embed → probe → score notebook |
| `N.<Model>-species.csv` | Per-image predictions — columns: `ImageFilePath, ScientificName, Pred_NaiveBayes, Pred_LogisticRegression, Pred_NearestNeighbor, Pred_MLP_Baseline` |
| `N.<Model>-species-metrics.csv` | Accuracy, Precision, Recall, F1-Score, Balanced Acc, MCC |

## Running the sweep

1. Prepare NHM-Carabids and build its manifest with
   [`processNHMC.py`](../README.md#processnhmcpy--build-the-nhm-carabids-manifest).
2. In `N.<Model>-LinearProbing-Species.ipynb`, choose which `Data/` manifest to
   train on (e.g. `Balanced_5800.csv`) and set output paths.
3. Run all cells → predictions + metrics CSVs.

To reproduce the full curve, run each model across all eight `Data/` manifests
and compare the resulting `-metrics.csv` files. Because the manifests are
committed, the exact images in every budget are fixed and reproducible.
