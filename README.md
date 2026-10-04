# Repository for the paper "How accurate are DFT forces? Unexpectedly large uncertainties in molecular datasets"

**Domantas Kuryla, Fabian Berger, Gábor Csányi, Angelos Michaelides**

*The Journal of Chemical Physics* **163**, 224313 (2025)  
📄 **Paper:** [https://doi.org/10.1063/5.0296997](https://doi.org/10.1063/5.0296997)


## Contents
Scripts used to obtain net forces for the AIMNet2, ANI-1x, ANI-1xbb, QCM, SPICE, and Transition1x datasets are given in the `net_forces/` directory.

In the `force_discrepancies/` directory, we also provide forces (provided in .xyz files) recomputed with different ORCA for the 1000 configuration random samples of the ANI-1x, Transition1x, AIMNet2, and SPICE datasets. Original reported forces are labelled with the "REF_forces" keyword, recomputed forces with "orca_forces".


## Citation

```bibtex
@article{kuryla2025dftforces,
  title   = {How accurate are {DFT} forces? {U}nexpectedly large uncertainties in molecular datasets},
  author  = {Kuryla, Domantas and Berger, Fabian and Cs{\'a}nyi, G{\'a}bor and Michaelides, Angelos},
  journal = {The Journal of Chemical Physics},
  volume  = {163},
  number  = {22},
  pages   = {224313},
  year    = {2025},
  doi     = {10.1063/5.0296997}
}
```
