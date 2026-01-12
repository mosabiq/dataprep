# import pandas as pd
# import numpy as np
# from sklearn.ensemble import IsolationForest
#
# # Detect outliers using Isolation Forest (advanced ML method)
# def detect_outliers_isolation(df: pd.DataFrame, numeric_cols=None, contamination=0.01):
#     if numeric_cols is None:
#         numeric_cols = df.select_dtypes(include='number').columns.tolist()
#
#     if len(numeric_cols) == 0:
#         return []
#
#     iso = IsolationForest(contamination=contamination, random_state=42)
#
#     # Fit the model on numeric columns (handling NaN by filling with 0)
#     preds = iso.fit_predict(df[numeric_cols].fillna(0))
#
#     # Outliers are labeled as -1
#     outlier_idx = np.where(preds == -1)[0]
#
#     return outlier_idx.tolist()
#
# # Cap (limit) outliers using IQR method so they fall within normal range
# def cap_outliers_iqr(df: pd.DataFrame, cols=None, factor=1.5):
#     df = df.copy()
#
#     if cols is None:
#         cols = df.select_dtypes(include='number').columns.tolist()
#
#     for c in cols:
#         Q1 = df[c].quantile(0.25)
#         Q3 = df[c].quantile(0.75)
#         IQR = Q3 - Q1
#         lower = Q1 - factor * IQR
#         upper = Q3 + factor * IQR
#
#         # Cap values outside the range
#         df[c] = df[c].clip(lower, upper)
#
#     return df







#
# import numpy as np
# import pandas as pd
# from sklearn.ensemble import IsolationForest
#
# # ---------------------------------------------------
# # Detect outliers using Isolation Forest
# # ---------------------------------------------------
# def detect_outliers_isolation(df, contamination="auto"):
#     num_df = df.select_dtypes(include=["int64", "float64"])
#
#     if num_df.shape[1] == 0:
#         return []
#
#     try:
#         iso = IsolationForest(contamination=contamination, random_state=42)
#         preds = iso.fit_predict(num_df)
#         outlier_indices = np.where(preds == -1)[0].tolist()
#         return outlier_indices
#     except:
#         return []
#
#
# # ---------------------------------------------------
# # Cap outliers using IQR method (Winsorization)
# # ---------------------------------------------------
# def cap_outliers_iqr(df):
#     df = df.copy()
#     num_cols = df.select_dtypes(include=["int64", "float64"]).columns
#
#     for col in num_cols:
#         Q1 = df[col].quantile(0.25)
#         Q3 = df[col].quantile(0.75)
#         IQR = Q3 - Q1
#
#         lower = Q1 - 1.5 * IQR
#         upper = Q3 + 1.5 * IQR
#
#         # Clip values outside IQR limits
#         df[col] = df[col].clip(lower, upper)
#
#     return df






import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest

# ---------------------------------------------------
# Detect outliers using Isolation Forest (before cleaning)
# ---------------------------------------------------
def detect_outliers_isolation(df, contamination="auto"):
    num_df = df.select_dtypes(include=["int64", "float64"])

    if num_df.shape[1] == 0:
        return []

    try:
        iso = IsolationForest(contamination=contamination, random_state=42)
        preds = iso.fit_predict(num_df)
        outlier_indices = np.where(preds == -1)[0].tolist()
        return outlier_indices
    except:
        return []


# ---------------------------------------------------
# Cap outliers using IQR (winsorization)
# ---------------------------------------------------
def cap_outliers_iqr(df):
    df = df.copy()
    num_cols = df.select_dtypes(include=["int64", "float64"]).columns

    for col in num_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        df[col] = df[col].clip(lower, upper)

    return df


# ---------------------------------------------------
# Count outliers using IQR (AFTER cleaning)
# ---------------------------------------------------
def count_iqr_outliers(df):
    outlier_count = 0
    num_cols = df.select_dtypes(include=["int64", "float64"]).columns

    for col in num_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        outlier_count += df[(df[col] < lower) | (df[col] > upper)].shape[0]

    return outlier_count
