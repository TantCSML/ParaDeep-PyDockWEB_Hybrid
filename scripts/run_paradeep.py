At https://github.com/PiyachatU/ParaDeep

ParaDeep: Sequence-Based Paratope Prediction with BiLSTM-CNN
ParaDeep is a chain-aware, sequence-only deep learning model for predicting paratope residues (antigen-binding sites) directly from antibody sequences.
It uses a lightweight BiLSTM-CNN architecture and supports both one-hot and embedding encodings for L and H chains respectively.

It requires only amino acid sequences — no structural input or large pretrained models. Predictions are per-residue, human-readable, and designed for practical use in early-stage antibody discovery and analysis.

Installation & Setup Instructions
Follow these steps to install and run ParaDeep on your machine:

1. Clone the Repository
    git clone https://github.com/PiyachatU/ParaDeep.git
    cd ParaDeep
2. Set Up a Python Environment (Recommended)
Option A: Using Conda:
    conda create -n paradeep python=3.9
    conda activate paradeep
Option B: Using venv:
    python -m venv paradeep_env
    source paradeep_env/bin/activate   # macOS/Linux
    paradeep_env\Scripts\activate      # Windows
3. Install Python Dependencies
From the project root folder, run:
cd paradeep
pip install -r requirements.txt
4. Ready to Predict
python paradeep.py \
--input data/sample_input.csv \
--modelH models/Best_Model_H.pt \
--modelL models/Best_Model_L.pt
5. View usage instructions at any time
python paradeep.py --help
