import pandas as pd
import numpy as np
from typing import Tuple, Dict

# Read dataset from a CSV file
def read_dataset(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

# Save cleaned dataset to a CSV file
def save_dataset(df: pd.DataFrame, path: str):
    df.to_csv(path, index=False)

# Automatically detect the type of a column (numeric, datetime, categorical, boolean)
def detect_column_type(series: pd.Series) -> str:
    if pd.api.types.is_datetime64_any_dtype(series):
        return 'datetime'
    if pd.api.types.is_numeric_dtype(series):
        return 'numeric'
    if pd.api.types.is_bool_dtype(series):
        return 'boolean'
    return 'categorical'

# Create a basic profile summary for the dataset (missing values, unique values, etc.)
def profile_basic(df: pd.DataFrame) -> Dict:
    profile = {}
    for c in df.columns:
        s = df[c]
        profile[c] = {
            'dtype': str(s.dtype),                            # datatype of column
            'n_missing': int(s.isna().sum()),                 # number of missing values
            'n_unique': int(s.nunique(dropna=True)),          # number of unique values
            'sample_values': (
                s.dropna().sample(min(5, max(1, len(s.dropna()))))
                 .astype(str).tolist() if len(s.dropna()) > 0 else []
            )
        }
    return profile
