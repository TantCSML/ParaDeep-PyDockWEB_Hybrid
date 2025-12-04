# ParaDeep–PyDockWEB Hybrid Docking Pipeline
**A reproducible implementation of the ParaDeep-guided, restraint-based antibody–antigen docking workflow.**  
This repository contains all scripts, Jupyter notebooks, input templates, and example data needed to run the hybrid ParaDeep–PyDockWEB method described in the manuscript *"A Hybrid Deep Learning and Physics-Based Framework for High-Precision Antibody–Antigen Docking"*.

---

## 🔬 Overview
This pipeline integrates:
1. **ParaDeep** — a sequence-based paratope prediction model (BiLSTM + MLP + attention)
2. **PyDockWEB / PyDock3** — physics-based rigid-body docking
3. **DockQ** — CAPRI-compliant quality evaluation

The workflow converts DL-derived residue probabilities into spatial restraints, guiding PyDock toward biologically meaningful antibody interfaces.

---

## 🚀 Quick Start

### **1. Clone this repository**
```bash
git clone https://github.com/TantCSML/ParaDeep-PyDockWeb_pipeline.git
cd ParaDeep-PyDockWeb_pipeline
## Try ParaDeep in Colab

Click below to open the notebook in Google Colab and run ParaDeep:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](
https://colab.research.google.com/github/PiyachatU/ParaDeep/blob/main/ParaDeep_Colab.ipynb)
