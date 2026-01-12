import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from joblib import dump, load


# This class handles the automatic filling (imputation) of missing values.
class AutoImputer:
    def __init__(self):
        self.label_encoders = {}

    # Main function to clean missing values
    def fit_predict(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()

        # --------------------------
        # NUMERIC MISSING VALUES
        # --------------------------
        numeric_cols = df.select_dtypes(include='number').columns.tolist()
        cat_cols = df.select_dtypes(exclude='number').columns.tolist()

        # Simple numeric imputer (median)
        num_imp = SimpleImputer(strategy='median')
        if len(numeric_cols) > 0:
            df[numeric_cols] = num_imp.fit_transform(df[numeric_cols])

        # --------------------------
        # CATEGORICAL MISSING VALUES
        # --------------------------
        for c in cat_cols:
            if df[c].isna().sum() == 0:
                continue

            mode = df[c].mode(dropna=True)
            if len(mode) > 0:
                df[c] = df[c].fillna(mode[0])  # Fill with most common category
            else:
                df[c] = df[c].fillna('missing')

        # Optional: advanced ML imputers can be added here

        return df

    # Save imputer
    def save(self, path: str):
        dump(self, path)

    # Load imputer
    @staticmethod
    def load(path: str):
        return load(path)
