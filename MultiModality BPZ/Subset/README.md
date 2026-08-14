# Multimodality · Subset

Runs the image / image+traits / image+traits+weather comparison on a **~1,000-specimen subset** of BeetlePalooza.

**Notebooks present:** `-imageOnly`, `-traits`, and `-traits-weather` per model — the full modality ladder, including the explicit image-only notebook.

## Models

- `BioCLIP`
- `ConvNeXt`
- `DINOv2`
- `ViLT`

## Modality variants & files

| Variant | Notebook | Features |
|---|---|---|
| Image only | `<Model>-imageOnly.ipynb` *(Subset)* / baseline `<Model>.csv` *(Full)* | image embedding |
| Image + traits | `<Model>-traits.ipynb` | image + length, width |
| Image + traits + weather | `<Model>-traits-weather.ipynb` | image + traits + site weather |

Each notebook writes `<Model>*-...csv` (per-image predictions) and
`<Model>*-metrics.csv` (Accuracy, Precision, Recall, F1-Score, Balanced Acc, MCC).

## Feature source

Tabular features come from the manifests in the
[parent folder](../README.md#feature-manifests-folder-root):
`Beetlepalooza_beetles_image_only.csv`, `_image_measurements.csv`, and
`_trait_weather.csv`. Images load from
[🤗 `imageomics/2018-NEON-beetles`](https://huggingface.co/datasets/imageomics/2018-NEON-beetles)
in-notebook (no preparation script needed).

## Reproduce

1. Obtain BeetlePalooza from Hugging Face (in-notebook).
2. Point each variant notebook at the matching feature manifest and set output paths.
3. Run all cells; compare `-metrics.csv` across the three variants to read off the
   lift from traits and weather.
