from ydata_profiling import ProfileReport
import pandas as pd
from .utils import profile_basic

# Generates two types of dataset profiles:
# 1. A quick JSON-style summary (basic)
# 2. A detailed HTML report (advanced)

def generate_profile(df: pd.DataFrame, output_html: str = 'profile.html') -> dict:
    # ------------- BASIC PROFILE (FAST) -------------
    # Uses our own function from utils.py
    basic = profile_basic(df)

    # ------------- ADVANCED PROFILE (DETAILED) -------------
    try:
        profile = ProfileReport(df, minimal=True)
        profile.to_file(output_html)        # saves HTML file
    except Exception:
        # If ydata_profiling fails (common on Windows with big datasets)
        pass

    return basic
