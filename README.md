# BeetleVerse
 
**BeetleVerse** is a benchmark suite for evaluating vision (and vision–language)
models on **ground-beetle taxonomic classification**. It bundles the dataset
manifests, evaluation notebooks, per-image predictions, and accuracy metrics for
four experiment tracks: **benchmarking**, **domain shift**, **sample-efficient
probing**, and **multimodal** classification.
 
This repository accompanies the paper
[**BeetleVerse: A study on taxonomic classification of ground beetles**](https://doi.org/10.48550/arXiv.2504.13393).
 
> [!IMPORTANT]
> This repo distributes **code, evaluation manifests, and results** — **not** the
> imagery. Every image dataset is owned and released by its original authors and
> must be obtained and cited from its official source (see
> [Data Provenance](#data-provenance)). This README is the **overview**; each
> experiment folder has its own detailed README with exact inputs, file
> inventories, and run instructions.
 
---
 
## Table of Contents
 
- [What the paper studies](#what-the-paper-studies)
- [The four experiment tracks](#the-four-experiment-tracks)
- [Common evaluation pipeline](#common-evaluation-pipeline)
- [Data provenance](#data-provenance)
  - [Dataset preparation scripts](#dataset-preparation-scripts)
- [Repository structure](#repository-structure)
- [File & naming conventions](#file--naming-conventions)
- [Reproducing a result end-to-end](#reproducing-a-result-end-to-end)
- [Software requirements](#software-requirements)
- [License](#license)
- [Citation](#citation)
---
 
## What the paper studies
 
Ground beetles (family **Carabidae**) are a large, ecologically important group
that is hard to identify at scale: specimens are imaged under very different
conditions (pinned museum vouchers, ethanol-preserved field collections, and
in-situ photographs), and the label space is enormous (**230+ genera, 1,700+
species**). BeetleVerse asks a focused question:
 
> **How well do modern pretrained vision backbones classify beetles at the genus
> and species level, and how does that ability hold up across imaging domains,
> shrinking training budgets, and added non-visual context?**
 
Rather than fine-tuning end-to-end, BeetleVerse **freezes each backbone and
linear-probes** its embeddings. This isolates *representation quality* — how much
taxonomically useful signal each pretrained model already encodes — and makes
dozens of models directly comparable on equal footing and modest compute.
 
The study spans **~100,885 carabid images** drawn from four datasets, plus a
merged superset, and evaluates a broad model zoo: supervised CNNs and
transformers (ResNet, ConvNeXt, RegNet, LeViT, SWINv2, ViT …), self-supervised
models (DINOv2, MoCo v3, SwAV, SimCLR, SimMIM, ViT-MAE), vision–language models
(CLIP, SigLIP, BioCLIP, ViLT), and a wildlife re-ID descriptor (MegaDescriptor).
 
---
 
## The four experiment tracks
 
| Track | Folder | Question it answers | Detailed README |
|---|---|---|---|
| **Benchmarking** | [`Benchmarking/`](./Benchmarking) | Which backbones best classify beetles, per dataset, at genus & species level? | [Benchmarking/README.md](./Benchmarking/README.md) |
| **Domain Shift** | [`Domain Shift/`](./Domain%20Shift) | Do models trained on one imaging domain generalize to another (lab→lab, lab→in-situ)? | [Domain Shift/README.md](./Domain%20Shift/README.md) |
| **Efficient Probing (NHMC)** | [`Efficient Probing NHMC/`](./Efficient%20Probing%20NHMC) | How little labeled data is needed before accuracy collapses (balanced vs. proportional sampling)? | [Efficient Probing NHMC/README.md](./Efficient%20Probing%20NHMC/README.md) |
| **Multimodality (BeetlePalooza)** | [`MultiModality BPZ/`](./MultiModality%20BPZ) | Does adding morphological traits and weather to images improve classification? | [MultiModality BPZ/README.md](./MultiModality%20BPZ/README.md) |
 
---
 
## Common evaluation pipeline
 
Every notebook in every track follows the **same four steps**. Understanding this
once explains the entire repository:
 
1. **Load a manifest CSV.** A table of image paths plus labels (`Genus` and/or
   `ScientificName`). Which manifest feeds which notebook is documented in each
   track's README.
2. **Extract frozen embeddings.** The pretrained backbone is loaded and run in
   inference mode to produce one feature vector per image. Backbones are **never
   fine-tuned**.
3. **Linear-probe with lightweight classifiers.** Scikit-learn heads are trained
   on the embeddings — typically **Gaussian Naive Bayes, Logistic Regression,
   k-Nearest-Neighbors (k=11), and an MLP baseline**; richer datasets
   (Beetle-PUUM) additionally include **SVMs and Random Forest**.
4. **Write two CSVs.** Per-image predictions (`<Model>.csv`) and aggregated
   metrics (`<Model>-metrics.csv`) reporting **Accuracy, Precision, Recall,
   F1-Score, Balanced Accuracy, and MCC**.
> [!NOTE]
> Notebooks ship with **placeholder paths** such as
> `/path/to/your/directory/AllCarabids.csv`. Before running, point these at the
> manifest CSV described in the relevant folder README. This placeholder-path
> issue is exactly what the provenance/reproducibility cleanup addresses.
 
---
 
## Data provenance
 
Four source datasets feed BeetleVerse. **Two are pulled directly from Hugging
Face inside the notebooks; two require a preparation script** that converts a raw
download into a manifest CSV. This split is the crux of reproducibility — know
which path applies before you start.
 
| Dataset (repo name) | Official source | How it enters this repo | Cite as |
|---|---|---|---|
| **BeetlePUUM** (Hawaii-beetles) | [🤗 `imageomics/Hawaii-beetles`](https://huggingface.co/datasets/imageomics/Hawaii-beetles) | **Loaded from Hugging Face in the notebooks** | Hawaii-beetles dataset + NEON records |
| **BeetlePalooza** (2018-NEON-beetles) | [🤗 `imageomics/2018-NEON-beetles`](https://huggingface.co/datasets/imageomics/2018-NEON-beetles) | **Loaded from Hugging Face in the notebooks** | 2018 NEON Ethanol-preserved Ground Beetles |
| **NHMC** (NHM-Carabids) | [Zenodo `10.5281/zenodo.3549369`](https://zenodo.org/record/3549369) | **Raw download → [`processNHMC.py`](./processNHMC.py) → manifest CSV** | Hansen et al., 2019 |
| **I1MC** (Insect-1M carabids) | [Insect-1M project](https://uark-cviu.github.io/projects/insect-foundation) | **Raw JSON → [`processI1MC.py`](./processI1MC.py) → manifest CSV** | Nguyen et al., 2024 |
| **AllCarabids** | — | Merge of all four manifests above | Cite all four sources |
 
> [!TIP]
> **BeetlePUUM and BeetlePalooza need no preparation script** — their notebooks
> read the images and labels straight from Hugging Face. Only **NHMC** and
> **I1MC** require running a preparation script first, because their raw releases
> are not shipped as ready-to-use manifests.
 
Full BibTeX for every dataset is in [`CITATION.cff`](./CITATION.cff) and in the
[Citation](#citation) section below.
 
### Dataset preparation scripts
 
Both scripts live at the repository root and turn a **raw, official download**
into the **manifest CSV** the notebooks consume.
 
#### `processNHMC.py` — build the NHM-Carabids manifest
 
The NHM-Carabids release is organized as one subfolder per **GBIF species key**.
This script walks that directory, calls the **GBIF Species API**
(`https://api.gbif.org/v1/species/{key}`) to resolve the full taxonomy
(kingdom → species) for each key, pairs every image with its resolved labels,
verifies no image is corrupted, and writes a single manifest CSV.
 
```bash
python processNHMC.py \
    --data_dir   /path/to/NHM-Carabids/           # folders named by GBIF species key
    --output_csv /path/to/NHMC.csv
```
 
**Output columns:** `ImageFileName, ImageFilePath, Kingdom, Phylum, Class,
Order, Family, Genus, Species, CanonicalName`.
Requires network access (GBIF API). The CSV is only written if **every** image
passes the corruption check.
 
#### `processI1MC.py` — build the Insect-1M carabid manifest
 
Insect-1M ships as a large JSON of insect records. This script filters to
**Carabidae**, normalizes taxon names (unwrapping the `Name (Canonical)`
format), assigns a UUID per image, and can optionally **download** the images
(organized into a `Phylum/Class/Order/Family/Genus/Species/` tree) and **prune**
corrupted files.
 
```bash
# 1) Build the raw carabid manifest from the Insect-1M JSON
python processI1MC.py \
    --json_path              /path/to/insect_1m.json \
    --image_dir              /path/to/I1MC/images/ \
    --output_csv_raw         /path/to/I1MC_raw.csv \
    --output_csv_downloaded  /path/to/I1MC_downloaded.csv \
    --output_csv_final       /path/to/I1MC.csv \
    --download \        # download images to --image_dir
    --clean             # remove + drop corrupted images, write final CSV
```
 
**Raw output columns:** `id, Phylum, Subphylum, Class, Order, Suborder, Family,
Subfamily, Tribe, Genus, Species, image_url, image_uuid` — with
`image_local_path` added after `--download`. Downloading is resumable per image
and retries failed URLs. The **I1MC-Filtered** benchmark is a quality-filtered
subset of this manifest.
 
---
 
## Repository structure
 
```
BeetleVerse/
├── processI1MC.py                # raw Insect-1M JSON  -> I1MC manifest CSV
├── processNHMC.py                # raw NHM-Carabids     -> NHMC manifest CSV
│
├── Benchmarking/                 # per-dataset model benchmark (genus + species)
│   ├── AllCarabids/              #   merged 4-dataset superset (species)
│   ├── Beetle-PUUM/              #   Hawaii-beetles      (HF; genus + species)
│   ├── BeetlePalooza/            #   2018-NEON-beetles   (HF; genus + species)
│   ├── I1MC/                     #   Insect-1M carabids  (processI1MC.py)
│   ├── I1MC-Filtered/            #   quality-filtered I1MC subset
│   └── NHMC/                     #   NHM-Carabids        (processNHMC.py)
│
├── Domain Shift/                 # train on domain A, test on domain B
│   ├── BPZ-I1MC-genus/  BPZ-I1MC-species/
│   ├── NHMC-BPZ-genus/
│   └── NHMC-I1MC-genus/ NHMC-I1MC-species/
│
├── Efficient Probing NHMC/       # sample-efficiency sweep on NHMC
│   ├── Data/                     #   sampling manifests (balanced/proportional)
│   └── Runs/                     #   linear-probing notebooks + results
│
├── MultiModality BPZ/            # image + traits + weather on BeetlePalooza
│   ├── Full/                     #   full dataset
│   ├── Subset/                   #   1k-specimen subset (incl. image-only)
│   └── Beetlepalooza_beetles*.csv#   feature manifests (image/traits/weather)
│
├── CITATION.cff
├── LICENSE
├── README.md                     # this file
└── requirements.txt
```
 
---
 
## File & naming conventions
 
| Pattern | Meaning |
|---|---|
| `*.ipynb` | Evaluation notebook (embed → probe → score) |
| `<Model>.csv` or `<Model>-species.csv` / `-genus.csv` | Per-image predictions |
| `<Model>-metrics.csv` | Aggregated metrics for that model/dataset/rank |
| `train.csv` / `test.csv` | Fixed train/test splits (Domain Shift) |
| `Balanced_* / Proportional_*` | Sampling manifests (Efficient Probing) |
| `-traits`, `-traits-weather`, image-only | Modality variants (Multimodality) |
 
**Prediction CSV columns:** `ImageFilePath`, label column(s) (`Genus` and/or
`ScientificName`), then one `Pred_<Classifier>` column per probing head.
**Metrics CSV columns:** `Model, Accuracy, Precision, Recall, F1-Score,
Balanced Acc, MCC`.
 
---
 
## Reproducing a result end-to-end
 
1. **Get the images** for the dataset you want (see [Data provenance](#data-provenance)).
   - HF datasets (PUUM, BeetlePalooza): nothing to prepare — the notebook loads them.
   - NHMC / I1MC: run `processNHMC.py` / `processI1MC.py` to build the manifest CSV.
2. **Open the track's README** (`Benchmarking/`, `Domain Shift/`,
   `Efficient Probing NHMC/`, `MultiModality BPZ/`) and find the notebook for
   your model.
3. **Set the paths** at the top of the notebook (manifest CSV in, predictions +
   metrics CSV out), replacing the `/path/to/...` placeholders.
4. **Run the notebook.** It extracts embeddings, trains the probing heads, and
   writes `<Model>.csv` and `<Model>-metrics.csv` — which should match the
   committed results.
---
 
## Software Requirements
 
```bash
pip install -r requirements.txt
```
 
Core stack: PyTorch, Hugging Face `transformers` + `datasets`, `open_clip_torch`
(for BioCLIP/CLIP), `scikit-learn` (probing heads + metrics), `pandas`, `numpy`,
`Pillow`, `tqdm`. `processNHMC.py` additionally uses `requests` (GBIF API).
 
## License
 
`BeetleVerse` is distributed under the terms of the
[MIT](https://spdx.org/licenses/MIT.html) license.
 
---

## License

`BeetleVerse` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

## Citation

If you use BeetleVerse, please cite **both the paper and this software**.

### Paper Citation
```bibtex
@article{rayeed2025beetleverse,
  title={BeetleVerse: A study on taxonomic classification of ground beetles},
  author={Rayeed, SM and East, Alyson and Stevens, Samuel and Record, Sydne and Stewart, Charles V},
  journal={arXiv preprint arXiv:2504.13393},
  year={2025}
}
```

### Software Citation
```bibtex
@software{beetleverse,
  author={Rayeed, S.M. and East, Alyson and Stevens, Samuel and Record, Sydne and Stewart, Charles V.},
  title={BeetleVerse},
  version={v1.0},
  year={2026},
  url={https://github.com/Imageomics/BeetleVerse}
}
```

### Dataset Citation

This repository does not publish and is not associated to the publication of any of the listed dataset. If you use any datasets in your work, please cite them appropriately:

  - If you use the [`BeetlePUUM` dataset](#BeetlePUUM), please cite the dataset, with associated specimen- and trap-level metadata :
```bibtex
@dataset{rayeed2025HawaiiBeetles,
  title={Hawaii Beetles (Revision a6a3ee5)},
  author={S M Rayeed and Mridul Khurana and Alyson East and Samuel Stevens and Iuliia Zarubiieva and Jiaman (Lisa) Wu and Scott C. Lowe and Elizabeth G. Campolongo and Evan D. Donoso and Tanya Berger-Wolf and Charles V Stewart and Graham W. Taylor and Sydne Record},
  year={2025},
  url={https://huggingface.co/datasets/imageomics/Hawaii-beetles},
  note={Revision a6a3ee5, CC-BY-4.0; DOI: 10.57967/hf/7272},
}
```
```bibtex
@misc{NEON-pinned-specimens,
  title     =  {{NEON} biorepository Carabid collection (pinned vouchers, ID: b33569cb-c4aa-4acd-83d6-d6d1e04c4c90)},
  author    =  {{Bernice Pauahi Bishop Museum}},
  publisher =  {National Ecological Observatory Network (NEON)},
  month     =  {jan},
  year      =  {2025},
  note      =  {Accessed on-site, at Domain 20, in January 2025},
  url       =  {https://biorepo.neonscience.org/portal/collections/misc/collprofiles.php?collid=97}
}
```
```bibtex
@misc{NEON-pinned-beetles-metadata,
  url = {https://data.neonscience.org/data-products/DP1.10022.001},
  author = {{National Ecological Observatory Network (NEON)}},
  keywords = {diversity, taxonomy, community composition, species composition, population, invertebrates, abundance, beetles, Carabidae, insects, DNA sequences, COI, DNA barcoding, ground beetles, pitfall traps, material samples, archived samples, bet, introduced species, invasive species, native species, biodiversity},
  language = {en},
  title = {Ground beetles sampled from pitfall traps (DP1.10022.001), provisional data},
  publisher = {National Ecological Observatory Network (NEON)},
  year = {2025},
  note = {Accessed January 2025}
}
```

- If you use the [`BeetlePalooza` dataset](#BeetlePalooza), please cite the dataset, with associated metadata :
```bibtex
@misc{Fluck2018_NEON_Beetle,
  author={Isadora E. Fluck and Isha Chinniah and Riley Wolcheski and Mridul Khurana and S M Rayeed and Benjamin Baiser and
            Elizabeth G. Campolongo and Anuj Karpatne and Charles V. Stewart and Sydne Record},
  title={2018 {NEON} Ethanol-preserved Ground Beetles (Revision a596e65)},
  year={2025},
  url={https://huggingface.co/datasets/imageomics/2018-NEON-beetles},
  doi={10.57967/hf/7272},
  publisher={Hugging Face}
}
```
```bibtex
@misc{Portal2022-ho,
  title     = {{NEON} Biorepository Carabid Collection (Trap Sorting)},
  author    = {{NEON Biorepository Portal}},
  publisher = {National Ecological Observatory Network},
  year      = {2022},
  doi       = {10.15468/mjtykf}
}
```
```bibtex
@misc{Portal2022-qu,
  title     = {{NEON} Biorepository Carabid Collection (Archive Pooling)},
  author    = {{NEON Biorepository Portal}},
  publisher = {National Ecological Observatory Network},
  year      = {2022},
  doi       = {10.15468/xicbza}
}
```  

  - If you use the [`NHMC` dataset](#NHM-Carabids), please cite:
```bibtex
@dataset{hansen_2019_3549369,
  author       = {Hansen, Oskar Liset Pryds and Svenning, Jens-Christian and Olsen, Kent and Dupont, Steen and Garner, Beulhah H. and Iosifidis, Alexandros and Price, Benjamin W. and Høye, Toke T.},
  title        = {Image data used for publication "Species-level image classification with convolutional neural network enable insect identification from habitus images"},
  month        = nov,
  year         = 2019,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.3549369}
}
``` 

  - If you use the [`I1MC` dataset](#I1MC), consider citing the paper that introduced the dataset:
```bibtex
@inproceedings{nguyen2024insect,
  title={Insect-foundation: A foundation model and large-scale 1m dataset for visual insect understanding},
  author={Nguyen, Hoang-Quan and Truong, Thanh-Dat and Nguyen, Xuan Bac and Dowling, Ashley and Li, Xin and Luu, Khoa},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={21945--21955},
  year={2024}
}
``` 
