# Healthcare_premium_prediction
## Production-Grade, Risk-Aware & Explainable Machine Learning System
## Streamlit app: https://healthcarepremiumprediction-blecsl3zyk8s4r83ykfbk9.streamlit.app/

> **A complete applied ML case study covering accuracy, tail-risk mitigation, uncertainty estimation, and model explainability — designed for real-world insurance pricing.**

---

## 📌 Project Overview

Predicting insurance premiums is a **high-stakes regression problem**. While many models achieve high average accuracy, they often fail silently on specific customer segments, leading to **catastrophic under- or over-pricing**.

This project was built with a *production mindset*:

* Go beyond single-metric optimization (R²)
* Diagnose and eliminate **extreme relative errors**
* Introduce **risk-aware predictions** and **explainability**

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

Rather than chasing marginal gains in R², this project emphasizes:

* **Error distribution analysis** over mean accuracy
* **Tail-risk mitigation** (reducing extreme relative errors)
* **Hybrid modeling** (interpretability + non-linear power)
* **Explainability and auditability** for regulated domains

> *A model that performs well on average but fails badly for a subset of users is not production-ready.*

---

## 🛠️ Tech Stack

* **Python**
* **Pandas, NumPy** — data processing
* **scikit-learn** — preprocessing, Linear Regression
* **XGBoost** — non-linear and residual learning
* **Matplotlib, Seaborn** — visualization
* **SHAP** — model explainability

---

## 📊 Dataset & Features

### Target Variable

* `annual_premium_amount` → **log-transformed** to stabilize variance

### Feature Categories

* **Demographics**: age, gender, marital status, region
* **Financials**: income (continuous & categorical)
* **Lifestyle**: BMI category, smoking status
* **Risk indicators**: medical history, insurance plan

Categorical features were one-hot encoded. Numeric features were scaled where appropriate.

---

## 📂 Project Structure

```
notebooks/
├── 01_Core_Hybrid_Model.ipynb
│   └── Error-driven modeling & hybrid residual learning
│
├── 02_risk_aware_pricing_quantile_regression.ipynb
│   └── Uncertainty estimation via quantile regression
│
├── 03_SHAP_analysis.ipynb
│   └── Model explainability & interpretability
```

Each notebook has a **clear, independent objective**, making the project easy to review and discuss in interviews.

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

## ✅ Final Results (Core Model)

| Metric                    | Baseline Linear Model | Hybrid Model |
| ------------------------- | --------------------- | ------------ |
| R²                        | ~0.94                 | **0.926**    |
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
* API / Streamlit deployment
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
