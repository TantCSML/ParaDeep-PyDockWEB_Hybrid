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

---

## Installation & Setup Instructions

Follow these steps to install and run ParaDeep on your machine:


### 1. Clone the Repository
        git clone https://github.com/PiyachatU/ParaDeep.git
        cd ParaDeep
### 2. Set Up a Python Environment (Recommended)
### Option A: Using Conda:
        conda create -n paradeep python=3.9
        conda activate paradeep
### Option B: Using venv:
        python -m venv paradeep_env
        source paradeep_env/bin/activate   # macOS/Linux
        paradeep_env\Scripts\activate      # Windows
### 3. Install Python Dependencies
### From the project root folder, run:
    cd paradeep
    pip install -r requirements.txt
### 4. Ready to Predict
    python paradeep.py \
    --input data/sample_input.csv \
    --modelH models/Best_Model_H.pt \
    --modelL models/Best_Model_L.pt
### 5. View usage instructions at any time
    python paradeep.py --help

Expected output:

```
usage: paradeep.py [-h] --input INPUT --modelH MODELH --modelL MODELL
                   [--output OUTPUT] [--no-vis]

ParaDeep: Chain-aware paratope prediction using BiLSTM-CNN

options:
  -h, --help       show this help message and exit
  --input INPUT    Input file (.csv, .fasta, .txt)
  --modelH MODELH  Path to trained H-chain model (.pt)
  --modelL MODELL  Path to trained L-chain model (.pt)
  --output OUTPUT  Path to output .csv
  --no-vis         Disable per-sequence visualization
```

## Try ParaDeep in Colab

Click below to open the notebook in Google Colab and run ParaDeep:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](
https://colab.research.google.com/github/PiyachatU/ParaDeep/blob/main/ParaDeep_Colab.ipynb)
