# import pandas as pd
# from .utils import read_dataset, save_dataset
# from .profiler import generate_profile
# from .imputer import AutoImputer
# from .outlier import detect_outliers_isolation, cap_outliers_iqr
# from .dedupe import deduplicate
# from .validator import validate_with_ge
#
# # Main data cleaning pipeline
# class CleaningPipeline:
#     def __init__(self):
#         self.imputer = AutoImputer()
#
#     # Run full cleaning
#     def run(self, df: pd.DataFrame) -> dict:
#         report = {}
#
#         # ---------------- 1. Save input shape ----------------
#         report['input_shape'] = df.shape
#
#         # ---------------- 2. Dataset profiling ----------------
#         report['profile'] = generate_profile(df)
#
#         # ---------------- 3. Remove duplicates ----------------
#         if df.shape[1] > 0:
#             df = deduplicate(df, subset_cols=[df.columns[0]])
#         report['after_dedupe_shape'] = df.shape
#
#         # ---------------- 4. Impute missing values ----------------
#         df = self.imputer.fit_predict(df)
#         report['after_impute_nulls'] = int(df.isna().sum().sum())
#
#         # ---------------- 5. Detect & fix outliers ----------------
#         outliers = detect_outliers_isolation(df)
#         report['n_outliers_detected'] = len(outliers)
#
#         if len(outliers) > 0:
#             df = cap_outliers_iqr(df)
#
#         # ---------------- 6. Validate final dataset ----------------
#         report['validation'] = validate_with_ge(df)
#
#         # ---------------- 7. Output summary ----------------
#         report['output_shape'] = df.shape
#         report['cleaned_sample'] = df.head(5).to_dict(orient='records')
#
#         return {"report": report, "cleaned_df": df}









import pandas as pd
from .imputer import AutoImputer
from .dedupe import deduplicate
from .validator import validate_with_ge
from .profiler import generate_profile

from .outlier import (
    detect_outliers_isolation,
    cap_outliers_iqr,
    count_iqr_outliers
)


class CleaningPipeline:
    def __init__(self):
        self.imputer = AutoImputer()

    def run(self, df: pd.DataFrame) -> dict:

        report = {}

        # ---------------------------------------------------
        # BEFORE CLEANING
        # ---------------------------------------------------
        report["before_missing"] = int(df.isna().sum().sum())
        report["before_duplicates"] = df.duplicated().sum()

        before_outliers = detect_outliers_isolation(df)
        report["before_outliers"] = len(before_outliers)

        # ---------------------------------------------------
        # PROFILE GENERATION
        # ---------------------------------------------------
        try:
            report["profile"] = generate_profile(df)
        except:
            report["profile"] = "Profile generation failed"

        # ---------------------------------------------------
        # REMOVE DUPLICATES
        # ---------------------------------------------------
        try:
            df = deduplicate(df, subset_cols=df.columns.tolist())
        except:
            pass

        # ---------------------------------------------------
        # IMPUTE MISSING VALUES
        # ---------------------------------------------------
        try:
            df = self.imputer.fit_predict(df)
        except:
            pass

        # ---------------------------------------------------
        # OUTLIER CLEANING (IQR Winsorization)
        # ---------------------------------------------------
        try:
            df = cap_outliers_iqr(df)
        except:
            pass

        # ---------------------------------------------------
        # AFTER CLEANING
        # ---------------------------------------------------
        report["after_missing"] = int(df.isna().sum().sum())
        report["after_duplicates"] = df.duplicated().sum()
        report["after_outliers"] = count_iqr_outliers(df)

        # ---------------------------------------------------
        # VALIDATION SUMMARY
        # ---------------------------------------------------
        try:
            report["validation"] = validate_with_ge(df)
        except:
            report["validation"] = {}

        return {"report": report, "cleaned_df": df}
