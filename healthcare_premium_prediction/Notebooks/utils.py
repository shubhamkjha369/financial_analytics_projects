import os

ARTIFACT_DIR = "artifacts"
os.makedirs(ARTIFACT_DIR, exist_ok=True)

class HybridModel:
    def __init__(self, lr_int, xgb_res):
        self.lr_int = lr_int
        self.xgb_res = xgb_res

    def predict(self, X):
        base_pred = self.lr_int.predict(X)
        residual_pred = self.xgb_res.predict(X)
        return base_pred + residual_pred

import pandas as pd

def build_interaction_features(X: pd.DataFrame) -> pd.DataFrame:
    

    X_int = X.copy()

    # -----------------------------
    # Income × Age
    # -----------------------------
    X_int["income_x_age"] = X_int["income_lakhs"] * X_int["age"]

    # ----------------------------------
    # Income × Medical History (OHE)
    # ----------------------------------
    medical_cols = [c for c in X_int.columns if c.startswith("medical_history_")]
    for col in medical_cols:
        X_int[f"{col}_x_income"] = X_int[col] * X_int["income_lakhs"]

    # ----------------------------------
    # Income × Insurance Plan (OHE)
    # ----------------------------------
    insurance_cols = [c for c in X_int.columns if c.startswith("insurance_plan_")]
    for col in insurance_cols:
        X_int[f"{col}_x_income"] = X_int[col] * X_int["income_lakhs"]

    # ----------------------------------
    # Income × Income Level (OHE)
    # ----------------------------------
    income_level_cols = [c for c in X_int.columns if c.startswith("income_level_")]
    for col in income_level_cols:
        X_int[f"{col}_x_income"] = X_int[col] * X_int["income_lakhs"]

    return X_int
