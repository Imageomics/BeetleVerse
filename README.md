# BeetleVerse

**BeetleVerse** is a benchmark suite for evaluating vision models on ground beetle classification. It provides datasets, evaluation notebooks, and results for genus- and species-level classification, domain adaptation, sample-efficient probing, and multimodal extensions. This repository accompanies the paper: [BeetleVerse: A study on taxonomic classification of ground beetles](https://doi.org/10.48550/arXiv.2504.13393).

---

## Table of Contents

- [Repository Structure](#repository-structure)
- [Datasets](#datasets)
- [Experiments](#experiments)
  - [Benchmarking](#benchmarking)
  - [Domain Shift](#domain-shift)
  - [Efficient Probing (NHMC)](#efficient-probing-nhmc)
  - [Multimodality (BeetlePalooza)](#multimodality-beetlepalooza)
- [Software Requirements](#software-requirements)
- [License](#license)
- [Citation](#citation)


---

## Repository Structure
```
  BeetleVerse/
  ├── Benchmarking/
  │ ├── AllCarabids/
  │ ├── Beetle-PUUM/
  │ ├── BeetlePalooza/
  │ ├── I1MC/
  │ ├── I1MC-Filtered/
  │ └── NHMC/
  │
  ├── DomainShift/
  │ ├── BPZ-I1MC-genus/
  │ ├── BPZ-I1MC-species/
  │ ├── NHMC-BPZ-genus/
  │ ├── NHMC-I1MC-genus/
  │ └── NHMC-I1MC-species/
  │
  ├── EfficientProbing_NHMC/
  │ ├── Balanced_14500/
  │ ├── Balanced_2900/
  │ ├── Balanced_5800/
  │ ├── Dataset-Full/
  │ ├── Dataset-Half/
  │ ├── Proportional_14500/
  │ ├── Proportional_2900/
  │ └── Proportional_5800/
  │
  ├── MultiModality_BeetlePalooza/
  │ ├── Full/
  │ └── Subset/
  │
  ├── CITATION.cff
  ├── LICENSE
  ├── README.md
  └── requirements.txt
```


**File conventions**:

- `.ipynb` → Jupyter notebooks with model evaluation code  
- `.csv` → predictions for genus or species  
- `*-metrics.csv` → accuracy metrics derived from predictions  

---

## Datasets

We use four distinctive datasets in this study, totaling **100,885 carabid images**, spanning over **230 genera and 1769 species**.  
We also provide a merged version combining all four datasets for large-scale analyses.

#### **BeetlePUUM** (Hawaii-beetles) 
  A dataset of Hawaiian-endemic carabids, imaged from pinned specimens at the Pu'u Maka'ala site (PUUM) of the National Ecological Observatory Network (NEON).  
  - Controlled high-quality images, rich ecological metadata  
  - Limited taxonomic diversity  
  - Official dataset on Hugging Face: [imageomics/Hawaii-beetles](https://huggingface.co/datasets/imageomics/Hawaii-beetles)

#### **BeetlePalooza** (2018-NEON-beetles) 
  NEON carabid dataset from 30 sites across the continental US, containing beetles preserved in ethanol vials.  
  - Broad taxonomic and geographic diversity (36 genera, 76 species)  
  - Contains ecological metadata  
  - Specimens vary in spacing and orientation  
  - Official dataset on Hugging Face: [imageomics/2018-NEON-beetles](https://huggingface.co/datasets/imageomics/2018-NEON-beetles)

#### **NHM-Carabids**  
  A collection from the Natural History Museum, London.  
  - Expert-verified taxonomy labels  
  - No accompanying metadata  
  - Some images blurry or with lighting inconsistencies  
  - Official dataset on Zenodo: ([Zenodo DOI: 10.5281/zenodo.3549369](https://zenodo.org/record/3549369))

#### **I1MC**  (Insect-1M)
  Filtered subset of carabids from the Insect-1M dataset.  
  - Includes both lab specimens and in-situ images  
  - Offers high taxonomic diversity  
  - Variable image quality, inconsistent specimen orientation, and partial captures  
  - Official dataset: [uark-cviu.github.io/projects/insect-foundation](https://uark-my.sharepoint.com/:f:/g/personal/hn016_uark_edu/Ekg5PAR-5GJKhdd3YTj2kBoBc0mNOcCP5YQqEnxjY4h-qg?e=dnBs5m)  

#### **AllCarabids**  
  Merged dataset combining all four datasets above, enabling large-scale analyses across diverse imaging conditions, taxonomic groups, and ecological contexts.

> **Disclaimer**  
> This repository is **not** associated with the publication or release of any of the datasets listed above.  
> This repository provides **code and evaluation pipelines** for benchmarking models on these datasets.  
> All datasets are maintained and distributed by their respective authors and institutions and should be cited separately as specified by their original sources (See [Dataset Citation](#Dataset-Citation)).


---

## Experiments

### Benchmarking

- Evaluates 12 vision models on beetle genus and species classification  
- Linear probing applied to multiple datasets  
- Provides `.ipynb`, `.csv`, and `-metrics.csv` files for each evaluation  

### Domain Shift

- Tests model generalization across datasets:
  1. **Lab-to-Lab adaptation**: Train on NHMC-Carabids, test on BeetlePalooza (lab collections)  
  2. **Lab-to-In-Situ adaptation**: Train on NHMC-Carabids and BeetlePalooza separately, test on I1MC (in-situ images)  
- Subdirectories include genus- and species-level evaluations

### Efficient Probing (NHMC)

- Sample-efficient linear probing on NHMC dataset  
- Two strategies:
  - **Balanced**: k images per species (k=10, 20, 50)  
  - **Proportional**: proportional sampling by species  
- Each with full and half dataset splits  

### Multimodality (BeetlePalooza)

- Extends image-only models to include additional modalities (traits, weather, etc.)  
- Experiments conducted on:
  - Full dataset  
  - 1000-specimen subset  
- Metrics provided for each classifier and modality combination  

---

## Software Requirements

Install via:

```bash
pip install -r requirements.txt
```


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



