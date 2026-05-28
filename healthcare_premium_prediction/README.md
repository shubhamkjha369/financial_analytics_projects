# Healthcare Premium Prediction

## Production-Grade, Risk-Aware & Explainable Machine Learning System
[![Streamlit App](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://healthcare-premium-prediction-skjha369.streamlit.app/)
[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-181717?style=flat&logo=github&logoColor=white)](https://github.com/shubhamkjha369/financial_analytics_projects/tree/main/healthcare_premium_prediction)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

> **A complete applied ML case study covering accuracy, tail-risk mitigation, uncertainty estimation, and model explainability — designed for real-world insurance pricing.**

---

## 📌 Project Overview

Predicting insurance premiums is a **high-stakes regression problem**. While many models achieve high average accuracy, they often fail silently on specific customer segments, leading to **catastrophic under- or over-pricing**.

This project was built with a *production mindset*:

* Go beyond single-metric optimization ($R^2$)
* Diagnose and eliminate **extreme relative errors**
* Introduce **risk-aware predictions** and **explainability**
* Deploy a fully functional, live **Streamlit web application** utilizing a segmented risk architecture

The final system achieves **strong global accuracy**, **near-elimination of tail errors**, and **transparent decision logic**, making it suitable for real insurance and fintech use cases.

---

## 🎯 Problem Statement

Given customer demographic, lifestyle, and financial attributes, predict the **annual insurance premium amount** as accurately and robustly as possible.

### Core Challenges Addressed

* Highly skewed target distribution
* Sparse and high-dimensional categorical features
* Large percentage errors despite good average metrics
* Disproportionate impact of errors on low-premium customers

---

## 🧠 Modeling Philosophy

Rather than chasing marginal gains in $R^2$, this project emphasizes:

* **Error distribution analysis** over mean accuracy
* **Tail-risk mitigation** (reducing extreme relative errors)
* **Segmented modeling** (tailored architectures based on demographic risk profiles)
* **Explainability and auditability** for regulated domains

> *A model that performs well on average but fails badly for a subset of users is not production-ready.*

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit** — Web deployment and UI
* **Pandas, NumPy** — Data processing
* **scikit-learn** — Preprocessing, Baseline Linear Regression
* **XGBoost** — Non-linear learning and residual modeling
* **SHAP** — Model explainability and feature attribution
* **Matplotlib, Seaborn** — Visualization
* **Joblib** — Model serialization

---

## 🚀 Production Deployed Architecture

While the analytical core in the notebooks explores a hybrid residual learning approach (combining Linear Regression and XGBoost on residuals) specifically for the **Young Adult** cohort, the production-deployed Streamlit application uses an **Age-Segmented Modeling Approach** to optimize prediction quality and business rules across distinct demographic groups:

### 1. Young Adult Policy (Age ≤ 25)
* **Model**: A regularized **Linear Regression** model (`model_young.joblib`) with a robust scaler (`scaler_young.joblib`).
* **Rationale**: Linear models generalize beautifully on this clean demographic segment, avoiding the risk of overfitting and ensuring simple, transparent risk calculations.
* **Features**: Leverages engineered features including **Genetic Risk Factors** and normalized medical history risk scores.

### 2. Standard Adult Policy (Age > 25)
* **Model**: A tuned **XGBoost Regressor** (`model_rest.joblib`) with a robust scaler (`scaler_rest.joblib`).
* **Rationale**: The adult cohort exhibits highly complex, non-linear relationships and risk structures that require the expressive power of tree-boosting methods.

---

## 📊 Dataset & Features

### Target Variable

* `annual_premium_amount` → **log-transformed** to stabilize variance

### Feature Categories

* **Demographics**: Age, gender, marital status, region
* **Financials**: Income (continuous & categorical)
* **Lifestyle**: BMI category, smoking status
* **Risk indicators**: Medical history, insurance plan type, genetic risk factors

Categorical features were one-hot encoded. Numeric features were scaled where appropriate.

---

## 📂 Project Structure

The repository is structured as follows:

```
├── Notebooks/                                    # Analytical and training notebooks (focused on Young Adult cohort)
│   ├── 01_Core_Hybrid_Model.ipynb                # Error-driven modeling & hybrid residual learning
│   ├── 02_risk_aware_pricing_quantile_regression # Uncertainty estimation via quantile regression
│   ├── 03_SHAP_analysis.ipynb                    # Model explainability & interpretability (SHAP)
│   ├── ml_premium_prediction_young_with_gr.ipynb # Training pipeline for the young cohort model
│   ├── ml_premium_prediction_rest_with_gr.ipynb  # Training pipeline for the adult cohort model
│   └── utils.py                                  # Shared utility functions and custom hybrid model class
│
├── app/                                          # Production-deployed Streamlit web application
│   ├── main.py                                   # Streamlit dashboard and user interface
│   └── prediction_helper.py                      # Input preprocessing, dynamic scaling, and model prediction
│
├── artifacts/                                    # Serialized model and preprocessor objects
│   ├── model_young.joblib                        # Linear Regression model for the young adult cohort (Age ≤ 25)
│   ├── model_rest.joblib                         # Tuned XGBoost Regressor model for the adult cohort (Age > 25)
│   ├── scaler_young.joblib                       # Preprocessing scaler for the young cohort
│   └── scaler_rest.joblib                        # Preprocessing scaler for the adult cohort
│
└── requirements.txt                              # Production app dependencies
```

---

## 🔄 Notebook-Wise Workflow

### 📘 Notebook 01 — Core Hybrid Model

**Objective:** Eliminate catastrophic prediction failures

* Exploratory data analysis and target transformation
* Baseline Linear Regression (strong global fit)
* Deep error analysis revealing ~33% extreme relative errors
* Interaction feature engineering
* **Hybrid architecture:**
  * Linear Regression → global structure & interpretability
  * XGBoost on residuals → non-linear corrections

**Key Result:**
* Extreme error rate reduced from **~33.7% → 0.8%**

---

### 📙 Notebook 02 — Risk-Aware Pricing (Quantile Regression)

**Objective:** Estimate uncertainty and tail risk

* Trained quantile regression models (10th, 50th, 90th percentiles)
* Generated prediction intervals instead of single point estimates
* Enabled conservative pricing strategies for high-risk customers

**Business Value:**
* Supports risk-aware decision-making
* Highlights uncertainty in premium estimates

---

### 📗 Notebook 03 — SHAP Explainability

**Objective:** Make the model transparent and defensible

* Applied SHAP to the residual XGBoost model
* Identified global and local feature contributions
* Validated that non-linear corrections align with domain intuition

**Production Relevance:**
* Regulatory compliance
* Stakeholder trust
* Debugging and model governance

---

## ✅ Final Results (Core Hybrid Model)

| Metric                    | Baseline Linear Model | Hybrid Model |
| ------------------------- | --------------------- | ------------ |
| $R^2$                     | ~0.94                 | **0.926**    |
| RMSE (log scale)          | ~0.20                 | **0.157** ↓  |
| Extreme Error Rate (>10%) | ~33.7%                | **0.8%** 🔥  |

### Key Takeaway

The hybrid approach **nearly eliminates catastrophic errors** while preserving strong explanatory power.

---

## 📉 Error Analysis Highlights

* Residual diagnostics exposed heteroscedasticity in baseline models
* Extreme errors were concentrated in low-income and sparse feature regions
* Post-hybrid modeling showed **no systematic concentration** of extreme errors
* KDE plots were replaced with rug plots where data scarcity made density estimation invalid

This ensured **honest and statistically sound visualizations**.

---

## 🧪 Why This Matters in Production

In real insurance systems:

* A small number of bad predictions can cause outsized financial or regulatory impact
* Tail-risk matters more than marginal improvements in average accuracy

This project demonstrates:

* Metric-driven debugging
* Robust pipeline design
* Risk-aware and explainable ML engineering

---

## 📈 Future Extensions

* Cost-sensitive loss functions for asymmetric pricing risk
* Drift detection and monitoring in production
* API endpoint wrapping (FastAPI) for enterprise integration
* Policy-year or macro-economic scenario analysis

---

## 🏁 Conclusion

This project shows how **error-aware modeling, hybrid architectures, uncertainty estimation, and explainability** can transform a strong baseline into a **production-ready insurance pricing system**.

It reflects real-world ML work: diagnosing failures, iterating intelligently, and prioritizing robustness over vanity metrics.

---

## 👤 Author

**Shubham Jha**
Aspiring Data Scientist | Machine Learning Enthusiast

---

⭐ *If you find this project insightful, feel free to star the repository or reach out for discussion.*
