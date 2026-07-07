# Multimodality (BeetlePalooza)

Does adding **non-visual context** — morphological **traits** (body length/width)
and **weather** at the collection site — improve beetle **genus** classification
over images alone? This track answers that on the **BeetlePalooza**
(2018-NEON-beetles) dataset, which uniquely ships rich specimen- and site-level
metadata alongside the images.

## Modality variants

Each model is evaluated in up to three configurations, so you can isolate the
contribution of each extra signal:

| Variant | File suffix | Features fed to the probe |
|---|---|---|
| **Image only** | *(none)* / `-imageOnly` | Image embedding only |
| **Image + traits** | `-traits` | Image embedding **+** length & width |
| **Image + traits + weather** | `-traits-weather` | Image embedding **+** traits **+** site weather |

## Feature manifests (folder root)

These CSVs define the tabular features that get concatenated with image
embeddings. They are the provenance backbone of this experiment.

| File | Delimiter | Columns |
|---|---|---|
| `Beetlepalooza_beetles.csv` | tab | Full raw table: image path, `beetleID`, `pictureID`, `length_distance_cm`, `width_distance_cm`, taxonomy, full site info, and the complete weather block (temp, precipitation, radiation, wind, snowfall, …) |
| `Beetlepalooza_beetles_image_only.csv` | tab | `ImageFilePath, Genus, ScientificName` |
| `Beetlepalooza_beetles_image_measurements.csv` | tab | image + `Length, Width` |
| `Beetlepalooza_beetles_image_df_weather.csv` | tab | image + site lat/long + full weather columns |
| `Beetlepalooza_beetles_trait_weather.csv` | comma | Model-ready: `ImageFilePath, Genus, ScientificName, Length, Width, TempMin, TempMax, Precipitation, Rain, Snowfall, WindGust, WindSpeed, TempAvg` |

> The `-traits` notebooks draw length/width; the `-traits-weather` notebooks add
> the weather columns. `Beetlepalooza_beetles_trait_weather.csv` is the tidy,
> ready-to-probe join used by the trait+weather runs.

## `Full/` vs `Subset/`

| Folder | Scope | Notebooks present | README |
|---|---|---|---|
| [`Full/`](./Full) | Entire BeetlePalooza dataset | `-traits` and `-traits-weather` per model | [→](./Full/README.md) |
| [`Subset/`](./Subset) | ~1,000-specimen subset | `-imageOnly`, `-traits`, and `-traits-weather` per model | [→](./Subset/README.md) |

**Models:** BioCLIP, ConvNeXt, DINOv2, ViLT.

> [!NOTE]
> The explicit **image-only notebook lives in `Subset/`** (`<Model>-imageOnly.ipynb`).
> In `Full/`, the image-only result is committed as the baseline `<Model>.csv` /
> `<Model>-metrics.csv` (produced by the same pipeline) while the notebooks focus
> on the `-traits` and `-traits-weather` variants.

## Files in each variant

| File | Contents |
|---|---|
| `<Model>.ipynb` / `<Model>-traits.ipynb` / `<Model>-traits-weather.ipynb` | Embed → concat features → probe → score |
| `<Model>*.csv` | Per-image predictions |
| `<Model>*-metrics.csv` | Accuracy, Precision, Recall, F1-Score, Balanced Acc, MCC |

## Running a multimodal experiment

1. Obtain BeetlePalooza from
   [🤗 `imageomics/2018-NEON-beetles`](https://huggingface.co/datasets/imageomics/2018-NEON-beetles)
   (loaded in-notebook — no preparation script needed).
2. Pick the variant notebook, point it at the matching feature manifest
   (`_image_only`, `_image_measurements`, or `_trait_weather`) and set output paths.
3. Run all cells and compare `-metrics.csv` across variants to read off the
   lift (or lack thereof) from traits and weather.
