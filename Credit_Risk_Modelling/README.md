# Credit Risk Modelling
# Streamlit app: https://mainpy-yf6kkeqh3akjx32xc9kely.streamlit.app/

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
Credit_Risk_Modelling/
│
├── app/
│   ├── artifacts/
│   │   └── model_data.joblib      # Saved Logistic Regression model, scaler, and features
│   ├── main.py                    # Streamlit web application interface
│   └── prediction_helper.py       # Helper script for preprocessing inputs and calculating credit score
│
├── dataset/
│   ├── customers.csv              # Customer demographic and financial information
│   ├── loans.csv                  # Loan-specific details
│   └── bureau_data.csv            # Credit bureau history and related financial records
│
├── notebooks/
│   └── credit_risk_model.ipynb    # Jupyter Notebook with full EDA, model training, and evaluation
│
├── requirements.txt               # Project dependencies
├── LICENSE                        # MIT License file
└── README.md                      # Project documentation
```

### Files

* **app/main.py** – Interactive Streamlit web interface for credit risk assessment.
* **app/prediction_helper.py** – Python script for processing input values, scaling numerical features, and running predictions using the trained model.
* **app/artifacts/model_data.joblib** – Saved model data containing the trained Logistic Regression model, MinMaxScaler, selected feature names, and list of columns scaled during preprocessing.
* **dataset/customers.csv** – Customer demographic and financial information.
* **dataset/loans.csv** – Loan-specific details.
* **dataset/bureau_data.csv** – Credit bureau history and related financial records.
* **notebooks/credit_risk_model.ipynb** – Full machine learning workflow (EDA, data preprocessing, handling class imbalance, and model training/evaluation) implemented in a Jupyter Notebook.
* **requirements.txt** – Package dependencies needed to run both the Jupyter Notebook and the Streamlit app.

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

Supervised classification models are trained to predict default probability. A **Logistic Regression** model is trained and deployed in this project due to its interpretability and robust performance on structured financial data.

The model is saved as a serialized joblib artifact (`app/artifacts/model_data.joblib`) alongside the MinMaxScaler and feature parameters to ensure consistent preprocessing during inference.

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
git clone https://github.com/shubhamkjha369/financial_analytics_projects.git
cd financial_analytics_projects/Credit_Risk_Modelling
```

### 2. Install Dependencies

You can install all required dependencies (including Streamlit, Scikit-learn, XGBoost, and Jupyter) using:

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit Web Application

To launch the interactive credit risk modeling dashboard:

```bash
streamlit run app/main.py
```

### 4. Run the Jupyter Notebook

To explore the EDA and model training pipeline:

```bash
jupyter notebook
```

Open and run all cells in `notebooks/credit_risk_model.ipynb` to reproduce the analysis.

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
