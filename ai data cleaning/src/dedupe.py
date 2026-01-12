import pandas as pd
from rapidfuzz import fuzz, process

# Remove exact & fuzzy duplicates
def deduplicate(df: pd.DataFrame, subset_cols: list) -> pd.DataFrame:
    # ----------- 1. REMOVE EXACT DUPLICATES -----------
    df = df.drop_duplicates()

    # ----------- 2. REMOVE FUZZY DUPLICATES -----------
    # Create a combined key column from the subset columns (e.g. name + city)
    key = df[subset_cols].astype(str).agg(' '.join, axis=1)

    seen = {}         # stores unique keys
    keep_idx = []     # stores indexes to keep
    indices = list(df.index)

    for i, val in zip(indices, key):

        # If no rows stored yet → keep first row
        if not seen:
            seen[val] = i
            keep_idx.append(i)
            continue

        # Compare with all previously accepted keys
        choices = list(seen.keys())

        # Find closest match from previous entries
        match, score, _ = process.extractOne(val, choices, scorer=fuzz.ratio)

        # If similarity is high (>90%), treat as a fuzzy duplicate → DON'T keep
        if score > 90:
            continue

        # Else this is a new unique value → keep it
        seen[val] = i
        keep_idx.append(i)

    # Return final cleaned dataframe
    return df.loc[keep_idx].reset_index(drop=True)
