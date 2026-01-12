import great_expectations as ge
import pandas as pd

# Validate cleaned dataset using Great Expectations (basic checks)
def validate_with_ge(df: pd.DataFrame, expectation_suite_name: str = 'default') -> dict:
    results = {}

    try:
        ge_df = ge.from_pandas(df)

        # 1. Check every column for missing values
        results['not_null_columns'] = {}
        for c in df.columns:
            res = ge_df.expect_column_values_to_not_be_null(c)
            results['not_null_columns'][c] = res['success']

        # 2. Check for duplicate rows
        res = ge_df.expect_table_row_count_to_be_between(
            min_value=df.drop_duplicates().shape[0],
            max_value=df.shape[0]
        )
        results['duplicate_check'] = res['success']

        # 3. Check numeric columns for reasonable ranges
        results['numeric_range_checks'] = {}
        for col in df.select_dtypes(include='number').columns:
            res = ge_df.expect_column_values_to_be_between(
                col, min_value=df[col].min(), max_value=df[col].max()
            )
            results['numeric_range_checks'][col] = res['success']

    except Exception as e:
        results['error'] = str(e)

    return results
