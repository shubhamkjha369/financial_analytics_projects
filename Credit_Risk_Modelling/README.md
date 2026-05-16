# Credit Risk Modelling
# Streamlit app: https://creditriskmodelling-wlf3p7xb2m6kdjildhxvef.streamlit.app/

## Overview

This project builds a **machine learning pipeline to predict loan default risk** using customer, loan, and credit bureau data. The goal is to identify borrowers who are likely to default so that financial institutions can make better lending decisions and manage risk more effectively.

The workflow includes:

* Data loading and exploration
* Data preprocessing and feature preparation
* Handling class imbalance
* Training and evaluating machine learning models

---

## Project Structure

```
project/
│
├── artifacts/
│
├── dataset/
│   ├── customers.csv
│   ├── loans.csv
│   └── bureau_data.csv
│
├── notebooks/
│   └── credit_risk_model.ipynb
├── LICENSE
└── README.md
```

### Files

* **customers.csv** – Customer demographic and financial information
* **loans.csv** – Loan-specific details
* **bureau_data.csv** – Credit bureau history and related financial records
* **credit_risk_model.ipynb** – Full machine learning workflow implemented in a Jupyter Notebook

---

## Problem Statement

Loan default prediction is a **binary classification problem** where the model predicts whether a borrower will:

* `0` → Not Default
* `1` → Default

Financial institutions use such models to:

* Reduce financial risk
* Improve credit scoring systems
* Automate loan approval processes

---

## Dataset Description

The dataset consists of multiple tables:

### 1. Customers Dataset

Contains borrower-level information such as:

* Personal attributes
* Financial background
* Account history

### 2. Loans Dataset

Contains loan-related attributes such as:

* Loan amount
* Loan type
* Repayment details
* Default status

### 3. Bureau Dataset

Contains external credit bureau information:

* Previous credit records
* Outstanding loans
* Credit history indicators

These datasets are combined and processed to create a **training dataset for predictive modeling**.

---

## Data Preprocessing

Key preprocessing steps include:

### 1. Data Cleaning

* Handling missing values
* Converting boolean fields to integers
* Standardizing column formats

### 2. Feature Preparation

* Combining information across multiple datasets
* Transforming categorical variables if necessary

### 3. Class Imbalance Handling

The dataset contains **class imbalance**:

* Only **~8.5% of records belong to the minority class (defaults)**.

Techniques such as:

* Resampling
* Balanced evaluation metrics
  are used to address this issue.

---

## Exploratory Data Analysis (EDA)

EDA includes:

* Distribution plots

* Correlation analysis

* Feature importance exploration

* Visualization using:

* **Matplotlib**

* **Seaborn**

EDA helps identify:

* Risk-related patterns
* Relationships between financial variables and default behavior

---

## Machine Learning Pipeline

The modeling pipeline consists of:

### 1. Train-Test Split

The dataset is split into:

* Training set
* Testing set

Using:

```python
train_test_split
```

### 2. Model Training

Supervised classification models are trained to predict default probability.

Typical models for this task include:

* Logistic Regression
* Random Forest
* Gradient Boosting
* XGBoost

*(Model choice can be extended depending on experimentation.)*

### 3. Model Evaluation

Performance is evaluated using classification metrics such as:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix
* ROC-AUC

These metrics help determine how well the model identifies risky borrowers.

---

## Technologies Used

* **Python**
* **Pandas** – Data manipulation
* **NumPy** – Numerical computing
* **Matplotlib** – Visualization
* **Seaborn** – Statistical plotting
* **Scikit-learn** – Machine learning models and evaluation
* **Jupyter Notebook** – Development environment

---

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/shubhammjha/Credit_Risk_Modelling.git
cd Credit_Risk_Modelling
```

### 2. Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

### 3. Run the Notebook

```bash
jupyter notebook
```

Open:

```
credit_risk_model.ipynb
```

Run all cells to reproduce the analysis and model training.

---

## Future Improvements

Potential improvements include:

* Feature engineering for better predictive power
* Hyperparameter tuning
* Advanced ensemble models
* Model explainability (SHAP / LIME)
* Deployment as an API or web service

---

## Applications

This project demonstrates how machine learning can be applied in:

* **Credit risk modeling**
* **FinTech applications**
* **Automated credit scoring systems**
* **Financial fraud and risk analysis**

---

## License

This project is open-source and available under the **MIT License**.
