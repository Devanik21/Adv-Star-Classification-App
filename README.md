# Adv Star Classification APP

![Language](https://img.shields.io/badge/Language-Python-3776AB?style=flat-square) ![Stars](https://img.shields.io/github/stars/Devanik21/Adv-Star-Classification-App?style=flat-square&color=yellow) ![Forks](https://img.shields.io/github/forks/Devanik21/Adv-Star-Classification-App?style=flat-square&color=blue) ![Author](https://img.shields.io/badge/Author-Devanik21-black?style=flat-square&logo=github) ![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

> Classify stellar objects from photometric survey data — from main-sequence stars to quasars, with interpretable ML.

---

**Topics:** `classification` · `astronomy` · `astrophysics-ml` · `deep-learning` · `machine-learning` · `neural-networks` · `stellar-classification` · `streamlit` · `resnet-embeddings` · `spectral-type`

## Overview

This application applies supervised machine learning to the problem of automated stellar object classification — one of the foundational challenges of large-scale photometric sky surveys like the Sloan Digital Sky Survey (SDSS). Given a set of photometric magnitudes (u, g, r, i, z bands) and the spectroscopic redshift of an observed object, the model classifies it as a Star, Galaxy, or Quasar (QSO) with calibrated probability scores.

The Streamlit interface provides two modes: interactive single-object classification with visual output, and batch classification from an uploaded CSV file containing multi-object survey data. The model is trained on the SDSS DR17 photometric-spectroscopic catalogue and achieves classification accuracy exceeding 97% on the held-out test set, with the highest confusion between faint galaxies and quasars at high redshift — a known challenge in observational astronomy.

Beyond classification, the application includes an interactive colour-magnitude diagram (CMD) visualisation and a 2D/3D feature space projection (PCA or UMAP) coloured by class label, giving users intuition for the photometric separability of the three object classes in the training data.

---

## Motivation

Modern sky surveys generate billions of stellar observations — far more than can be manually reviewed by astronomers. Automated photometric classification is therefore a critical pipeline step in survey astronomy, enabling efficient targeting of follow-up spectroscopic observations for objects of scientific interest. This project demonstrates that a well-engineered ML pipeline can achieve spectroscopic-grade classification accuracy from photometric features alone.

---

## Architecture

```
Input: u, g, r, i, z magnitudes + redshift z
        │
  Colour Index Engineering (u-g, g-r, r-i, i-z)
        │
  StandardScaler normalisation
        │
  Multi-class Classifier (RF / SVM / XGBoost)
        │
  ┌──────────────────────────┐
  │ Class: Star / Galaxy / QSO│
  │ Confidence: [0.0 – 1.0]   │
  └──────────────────────────┘
        │
  CMD + PCA Visualisation
```

---

## Features

### Photometric Feature Input
Enter u, g, r, i, z apparent magnitudes and spectroscopic redshift through validated number inputs. Colour indices (u-g, g-r, etc.) are computed automatically as derived features.

### Three-Class Stellar Classifier
Outputs class probabilities for Star, Galaxy, and Quasar using a trained multi-class classifier with >97% accuracy on SDSS DR17 data.

### Colour-Magnitude Diagram
Interactive CMD plot with training data points, colour-coded by class, with the user's input object overlaid for visual context.

### PCA / UMAP Feature Projection
2D and 3D projections of the feature space coloured by class label, helping users understand the photometric separability of stellar object classes.

### Confusion Matrix and Metrics
Full evaluation panel: confusion matrix, per-class precision/recall/F1, and macro/weighted averages on the test split.

### Batch CSV Classification
Upload a CSV of photometric observations for bulk classification with a downloadable results table including class labels and confidence scores.

### Redshift Distribution Plot
Histogram of the training redshift distribution by class, contextualising the user's input object within the population.

### Model Selection Sidebar
Toggle between trained classifiers (RF, SVM, KNN, XGBoost) and observe how class boundaries and accuracy metrics change.

---

## Tech Stack

| Library / Tool | Role | Why This Choice |
|---|---|---|
| **Streamlit** | Web application framework | Interactive UI with sidebar model selection |
| **scikit-learn** | ML pipeline | RandomForestClassifier, SVM, preprocessing, metrics |
| **XGBoost** | Gradient boosting | High-accuracy multi-class classification on photometric data |
| **pandas** | Data handling | Survey CSV loading and feature engineering |
| **Plotly** | Interactive astronomy plots | CMD, PCA scatter, confusion matrix heatmap |
| **NumPy** | Array operations | Colour index computation and scaling |
| **Astropy (optional)** | Astronomy utilities | Coordinate transformations and FITS file reading |
| **UMAP-learn (optional)** | Dimensionality reduction | Non-linear 2D projection of photometric feature space |

> **Key packages detected in this repo:** `scikit-learn` · `numpy` · `pandas` · `matplotlib` · `seaborn` · `scipy` · `xgboost` · `lightgbm` · `catboost` · `tensorflow`

---

## Getting Started

### Prerequisites

- Python 3.9+ (or Node.js 18+ for TypeScript/JS projects)
- `pip` or `npm` package manager
- Relevant API keys (see Configuration section)

### Installation

```bash
git clone https://github.com/Devanik21/Adv-Star-Classification-App.git
cd Adv-Star-Classification-App
python -m venv venv && source venv/bin/activate
pip install streamlit scikit-learn xgboost pandas plotly numpy umap-learn
streamlit run app.py
```

---

## Usage

```bash
# Launch the application
streamlit run app.py

# Batch classify a catalogue file
python batch_classify.py --input sdss_catalogue.csv --output classified.csv

# Retrain on updated SDSS data
python train.py --data sdss_dr17.csv --model rf
```

---

## Configuration

| Variable | Default | Description |
|---|---|---|
| `MODEL_PATH` | `star_classifier.pkl` | Serialised multi-class classifier |
| `FEATURE_COLS` | `u,g,r,i,z,redshift` | Input feature columns |
| `CLASS_LABELS` | `STAR,GALAXY,QSO` | Target class names |
| `CONFIDENCE_THRESHOLD` | `0.6` | Minimum confidence to display result as definitive |

> Copy `.env.example` to `.env` and populate all required values before running.

---

## Project Structure

```
Adv-Star-Classification-App/
├── README.md
├── requirements.txt
├── about.py
├── analyze.py
├── feedback.py
├── gallery.py
├── insights.py
├── star_classification.csv
└── ...
```

---

## Roadmap

- [ ] Integration with the SDSS SkyServer API for live object lookup by RA/Dec coordinates
- [ ] Photometric redshift estimation as a parallel regression task
- [ ] Deep learning backbone (1D-CNN on photometric time-series for variable stars)
- [ ] FITS image thumbnail display for classified objects
- [ ] Cross-matching with Gaia DR3 proper motion catalogue for star/galaxy disambiguation

---

## Contributing

Contributions, issues, and feature requests are welcome. Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'feat: add your feature'`)
4. Push to your branch (`git push origin feature/your-feature`)
5. Open a Pull Request

Please follow conventional commit messages and ensure any new code is documented.

---

## Notes

Classification accuracy varies with survey depth and photometric noise. The model performs best on well-measured objects (low photometric uncertainty). High-redshift QSOs may be confused with compact blue galaxies.

---

## Author

**Devanik Debnath**  
B.Tech, Electronics & Communication Engineering  
National Institute of Technology Agartala

[![GitHub](https://img.shields.io/badge/GitHub-Devanik21-black?style=flat-square&logo=github)](https://github.com/Devanik21)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-devanik-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/devanik/)

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

*Crafted with curiosity, precision, and a belief that good software is worth building well.*
