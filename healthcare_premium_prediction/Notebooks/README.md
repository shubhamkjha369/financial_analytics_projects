# 📘 Analytical Notebooks Navigation Guide

Welcome to the analytical core of the **Healthcare Premium Prediction** project! This directory contains the analytical research, modeling iterations, uncertainty estimations, and explainability studies.

To help you navigate this folder (especially if you are a recruiter or technical interviewer), the notebooks have been grouped into logical categories below.

---

## 🌟 1. Core Polished Showcases
*These are the clean, heavily commented, publication-grade notebooks designed to demonstrate advanced machine learning engineering and explainability.*

### 1. [01_Core_Hybrid_Model.ipynb](01_Core_Hybrid_Model.ipynb)
* **Purpose**: Addresses baseline model failure modes. Shows how error-driven analysis, target log-transformation, interaction feature engineering, and a **Hybrid Architecture** (Linear Regression + XGBoost learning on residuals) can eliminate high-tail pricing errors.
* **Key Demonstration**: Demonstrates the systematic reduction of extreme pricing errors (>10%) from **~33.7% to 0.8%**.
* **Key Libraries**: `scikit-learn`, `xgboost`, `pandas`, `seaborn`

### 2. [02_risk_aware_pricing_quantile_regression.ipynb](02_risk_aware_pricing_quantile_regression.ipynb)
* **Purpose**: Goes beyond simple point estimation by modeling **uncertainty bounds**. Employs **Quantile Regression** (estimating the 10th, 50th, and 90th percentiles) to produce dynamic pricing intervals.
* **Key Demonstration**: Shows how an insurance company can implement conservative, risk-adjusted pricing boundaries to mitigate financial tail-risk.
* **Key Libraries**: `scikit-learn` (`GradientBoostingRegressor` with quantile loss)

### 3. [03_SHAP_analysis.ipynb](03_SHAP_analysis.ipynb)
* **Purpose**: Resolves the "black-box" issue in tree ensembles. Uses **SHAP (SHapley Additive exPlanations)** to gain global and local interpretability of the residual correction model.
* **Key Demonstration**: Uncovers feature dependencies and validates that non-linear corrections align perfectly with domain logic, ensuring regulatory compliance.
* **Key Libraries**: `shap`, `matplotlib`

---

## ⚙️ 2. Production Model Pipelines
*These notebooks contain the precise pipeline construction, cross-validation, and hyperparameter tuning for the models that are serialized and running live in the Streamlit application.*

### 4. [ml_premium_prediction_young_with_gr.ipynb](ml_premium_prediction_young_with_gr.ipynb)
* **Purpose**: Explores and trains the model for the **Young Adult Cohort (Age ≤ 25)**. Introduces interaction variables and the custom `genetic_risk` feature.
* **Outcome**: Outputs and saves `model_young.joblib` (an optimized Linear Regression model) and `scaler_young.joblib`.

### 5. [ml_premium_prediction_rest_with_gr.ipynb](ml_premium_prediction_rest_with_gr.ipynb)
* **Purpose**: Explores, tunes, and trains the model for the **Standard Adult Cohort (Age > 25)**, incorporating the custom `genetic_risk` feature.
* **Outcome**: Performs `RandomizedSearchCV` hyperparameter tuning on `XGBRegressor` and outputs the serialized production model `model_rest.joblib` and `scaler_rest.joblib`.

---

## 🧪 3. Iterative Baselines & R&D (Legacy)
*These notebooks represent early-stage, messy, or iterative development work. They are preserved for historical context and to demonstrate the engineering journey, but are not the final polished models.*

* **[data_segmentation.ipynb](data_segmentation.ipynb)**: Initial exploratory experiments with splitting the dataset into age and income cohorts.
* **[ml_premium_prediction.ipynb](ml_premium_prediction.ipynb)**: First comprehensive baseline model exploration before engineering specific medical risk features.
* **[ml_premium_prediction_young.ipynb](ml_premium_prediction_young.ipynb)** & **[ml_premium_prediction_rest.ipynb](ml_premium_prediction_rest.ipynb)**: Legacy segmented notebooks prior to the integration of customized `genetic_risk` variables.
* **[ml_premium_prediction_young_with_gr.ipynb](ml_premium_prediction_young_with_gr.ipynb)** & **[ml_premium_prediction_rest_with_gr.ipynb](ml_premium_prediction_rest_with_gr.ipynb)**: Early messy draft notebooks mapping out feature integrations.

---

## 🛠️ 4. Shared Utilities

* **[utils.py](utils.py)**: Contains reusable helper classes and functions utilized across the notebooks, including:
  * `HybridModel` class wrapper (combining Base Linear predictions and Residual XGBoost predictions).
  * `build_interaction_features` function to automate high-impact interaction feature engineering.

---

> [!NOTE]
> All analytical assets and serialized objects in the `artifacts/` folder correspond directly to the research in these notebooks.
