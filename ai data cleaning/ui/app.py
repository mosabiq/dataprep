# # import streamlit as st
# # import pandas as pd
# # import sys
# # import os
# # sys.path.append(os.path.dirname(os.path.dirname(__file__)))
# #
# # from src.pipeline import CleaningPipeline
# #
# # st.set_page_config(page_title="AI Data Cleaning App", layout="wide")
# #
# # # Title
# # st.title("🧹 Autonomous AI Data Cleaning Pipeline")
# # st.write("Upload your raw CSV file and the system will automatically clean it using AI.")
# #
# # # File upload
# # uploaded = st.file_uploader("Upload a CSV file", type=["csv"])
# #
# # if uploaded is not None:
# #     df = pd.read_csv(uploaded)
# #
# #     st.subheader("📌 Raw Data Preview")
# #     st.dataframe(df.head())
# #
# #     # Run pipeline button
# #     if st.button("Run Cleaning"):
# #         pipeline = CleaningPipeline()
# #
# #         with st.spinner("Cleaning your dataset... Please wait ⏳"):
# #             result = pipeline.run(df)
# #
# #         cleaned_df = result["cleaned_df"]
# #         report = result["report"]
# #
# #         st.subheader("✔️ Cleaning Report")
# #         st.json(report)
# #
# #         st.subheader("✔️ Cleaned Data Preview")
# #         st.dataframe(cleaned_df.head())
# #
# #         # Download button
# #         csv = cleaned_df.to_csv(index=False).encode("utf-8")
# #         st.download_button(
# #             "Download Cleaned CSV",
# #             data=csv,
# #             file_name="cleaned_dataset.csv",
# #             mime="text/csv"
# #         )
#
#
#
#
#
#
#
#
# # import sys
# # import sys
# # import os
# #
# # ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# # sys.path.append(ROOT_DIR)
# #
# #
# #
#
# #
# # import sys
# # import os
# #
# # # ---- FIX IMPORT PATH ----
# # ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# # if ROOT_DIR not in sys.path:
# #     sys.path.append(ROOT_DIR)
# #
# # import streamlit as st
# # import pandas as pd
# #
# # from src.pipeline import CleaningPipeline
# #
# # # ---------------- APP CONFIG ----------------
# # st.set_page_config(page_title="AI Data Cleaning App", layout="wide")
# #
# # st.title("🧹 AI Data Cleaning Pipeline")
# # st.write("Upload a CSV file to view dataset summary and clean it using AI.")
# #
# #
# # # ---------------- FILE UPLOADER ----------------
# # uploaded = st.file_uploader("Upload CSV File", type=["csv"])
# #
# # if uploaded is not None:
# #     df = pd.read_csv(uploaded)
# #
# #     # =====================================================
# #     # 📊 DATASET SUMMARY DASHBOARD
# #     # =====================================================
# #     st.header("📊 Dataset Summary Dashboard")
# #
# #     # ----- BASIC INFO -----
# #     col1, col2, col3 = st.columns(3)
# #     col1.metric("Rows", df.shape[0])
# #     col2.metric("Columns", df.shape[1])
# #     col3.metric("Memory (KB)", round(df.memory_usage(deep=True).sum() / 1024, 2))
# #
# #     # ----- COLUMN TYPES -----
# #     st.subheader("🔠 Column Types")
# #     type_df = pd.DataFrame(df.dtypes, columns=["Data Type"])
# #     st.dataframe(type_df, hide_index=False)
# #
# #     # ----- MISSING VALUES -----
# #     st.subheader("🕳 Missing Values Per Column")
# #     missing_df = df.isna().sum().reset_index()
# #     missing_df.columns = ["Column", "Missing Values"]
# #     st.dataframe(missing_df, hide_index=False)
# #
# #     # ----- UNIQUE VALUES -----
# #     st.subheader("🔢 Unique Values Per Column")
# #     unique_df = df.nunique().reset_index()
# #     unique_df.columns = ["Column", "Unique Values"]
# #     st.dataframe(unique_df, hide_index=False)
# #
# #     # ----- NUMERICAL SUMMARY -----
# #     st.subheader("📐 Numerical Summary")
# #     try:
# #         st.dataframe(df.describe().T, hide_index=False)
# #     except:
# #         st.info("No numeric columns found.")
# #
# #     # ----- CATEGORICAL SAMPLE -----
# #     st.subheader("🧩 Categorical Sample")
# #     cat_cols = df.select_dtypes(include=["object"]).columns
# #     if len(cat_cols) > 0:
# #         st.dataframe(df[cat_cols].head(), hide_index=False)
# #     else:
# #         st.info("No categorical columns found.")
# #
# #     # ----- RAW DATA PREVIEW -----
# #     st.subheader("👀 Raw Data Preview")
# #     st.dataframe(df.head(), hide_index=False)
# #
# #     st.write("---")
# #
# #     # =====================================================
# #     # 🧼 CLEANING PIPELINE
# #     # =====================================================
# #     st.header("🧼 Run Cleaning Pipeline")
# #
# #     if st.button("Run Cleaning"):
# #         pipeline = CleaningPipeline()
# #
# #         with st.spinner("Cleaning your dataset..."):
# #             result = pipeline.run(df)
# #
# #         cleaned_df = result["cleaned_df"]
# #         report = result["report"]
# #
# #         # ---------------- BEFORE vs AFTER ----------------
# #         st.subheader("📉 Before vs After Cleaning")
# #
# #         colA, colB = st.columns(2)
# #
# #         with colA:
# #             st.write("### 🟥 Before Cleaning")
# #             st.write("Missing Values:", report.get("before_missing"))
# #             st.write("Duplicates:", report.get("before_duplicates"))
# #             st.write("Outliers:", report.get("before_outliers"))
# #             st.dataframe(df.head(), hide_index=False)
# #
# #         with colB:
# #             st.write("### 🟩 After Cleaning")
# #             st.write("Missing Values:", report.get("after_missing"))
# #             st.write("Duplicates:", report.get("after_duplicates"))
# #             st.write("Outliers:", report.get("after_outliers"))
# #             st.dataframe(cleaned_df.head(), hide_index=False)
# #
# #         # ---------------- CLEANING REPORT ----------------
# #         st.subheader("📑 Cleaning Report")
# #         st.json(report)
# #
# #         # ---------------- DOWNLOAD CLEANED CSV ----------------
# #         cleaned_csv = cleaned_df.to_csv(index=False).encode("utf-8")
# #         st.download_button(
# #             "⬇️ Download Cleaned CSV",
# #             data=cleaned_csv,
# #             file_name="cleaned_dataset.csv",
# #             mime="text/csv"
# #         )
#
#
#
#
#
#
# # import sys
# # import os
# #
# # # ---- FIX IMPORT PATH ----
# # ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# # if ROOT_DIR not in sys.path:
# #     sys.path.append(ROOT_DIR)
# #
# # import streamlit as st
# # import pandas as pd
# # import seaborn as sns
# # import matplotlib.pyplot as plt
# #
# # from src.pipeline import CleaningPipeline
# #
# #
# # # =========================================================
# # # 📊 EDA FUNCTION
# # # =========================================================
# # def run_eda(df):
# #     st.header("📊 Exploratory Data Analysis (EDA)")
# #
# #     # 1. DATA PREVIEW
# #     st.subheader("👀 Dataset Preview")
# #     st.dataframe(df.head())
# #
# #     # 2. SUMMARY STATISTICS
# #     st.subheader("📐 Summary Statistics")
# #     st.dataframe(df.describe(include="all").T)
# #
# #     # 3. MISSING VALUE HEATMAP
# #     st.subheader("🕳 Missing Values Heatmap")
# #     fig, ax = plt.subplots(figsize=(10, 4))
# #     sns.heatmap(df.isna(), cbar=False, cmap="viridis", ax=ax)
# #     st.pyplot(fig)
# #
# #     # 4. CORRELATION HEATMAP
# #     st.subheader("🔥 Correlation Heatmap (Numerical Columns Only)")
# #     num_df = df.select_dtypes(include=["int64", "float64"])
# #
# #     if num_df.shape[1] > 0:
# #         fig, ax = plt.subplots(figsize=(10, 6))
# #         sns.heatmap(num_df.corr(), annot=True, cmap="coolwarm", ax=ax)
# #         st.pyplot(fig)
# #     else:
# #         st.info("No numerical columns found for correlation heatmap.")
# #
# #     # 5. NUMERIC DISTRIBUTIONS
# #     st.subheader("📊 Distribution Plots (Numeric Columns)")
# #     for col in num_df.columns:
# #         st.write(f"### Distribution of {col}")
# #         fig, ax = plt.subplots(figsize=(8, 4))
# #         sns.histplot(df[col], kde=True, ax=ax)
# #         st.pyplot(fig)
# #
# #     # 6. BOXPLOTS
# #     st.subheader("📦 Outlier Boxplots (Numeric Columns)")
# #     for col in num_df.columns:
# #         st.write(f"### Boxplot of {col}")
# #         fig, ax = plt.subplots(figsize=(8, 2))
# #         sns.boxplot(x=df[col], ax=ax)
# #         st.pyplot(fig)
# #
# #     # 7. CATEGORICAL ANALYSIS
# #     st.subheader("🧩 Categorical Value Counts")
# #     cat_cols = df.select_dtypes(include=["object"]).columns
# #
# #     if len(cat_cols) > 0:
# #         for col in cat_cols:
# #             st.write(f"### Value Counts → {col}")
# #             st.bar_chart(df[col].value_counts())
# #     else:
# #         st.info("No categorical columns found.")
# #
# #
# # # =========================================================
# # # STREAMLIT UI START
# # # =========================================================
# # st.set_page_config(page_title="AI Data Cleaning App", layout="wide")
# #
# # st.title("🧹 AI Data Cleaning Pipeline with EDA")
# # st.write("Upload your dataset to view summary, run EDA, and clean your data using AI.")
# #
# #
# # # ---------------- FILE UPLOADER ----------------
# # uploaded = st.file_uploader("Upload CSV File", type=["csv"])
# #
# #
# # if uploaded is not None:
# #     df = pd.read_csv(uploaded)
# #
# #     # =====================================================
# #     # 📊 DATASET SUMMARY DASHBOARD
# #     # =====================================================
# #     st.header("📊 Dataset Summary Dashboard")
# #
# #     col1, col2, col3 = st.columns(3)
# #     col1.metric("Rows", df.shape[0])
# #     col2.metric("Columns", df.shape[1])
# #     col3.metric("Memory (KB)", round(df.memory_usage(deep=True).sum() / 1024, 2))
# #
# #     st.subheader("🔠 Column Types")
# #     st.dataframe(pd.DataFrame(df.dtypes, columns=["Data Type"]))
# #
# #     st.subheader("🕳 Missing Values Per Column")
# #     missing_df = df.isna().sum().reset_index()
# #     missing_df.columns = ["Column", "Missing Values"]
# #     st.dataframe(missing_df)
# #
# #     st.subheader("🔢 Unique Values Per Column")
# #     unique_df = df.nunique().reset_index()
# #     unique_df.columns = ["Column", "Unique Values"]
# #     st.dataframe(unique_df)
# #
# #     st.subheader("📐 Numerical Summary")
# #     try:
# #         st.dataframe(df.describe().T)
# #     except:
# #         st.info("No numeric columns available.")
# #
# #     st.subheader("🧩 Categorical Sample")
# #     cat_cols = df.select_dtypes(include=["object"]).columns
# #     if len(cat_cols) > 0:
# #         st.dataframe(df[cat_cols].head())
# #     else:
# #         st.info("No categorical columns found.")
# #
# #     st.subheader("👀 Raw Data Preview")
# #     st.dataframe(df.head())
# #
# #     st.write("---")
# #
# #     # =====================================================
# #     # 📊 RUN EDA
# #     # =====================================================
# #     st.header("📊 Full EDA Report")
# #     run_eda(df)
# #
# #     st.write("---")
# #
# #     # =====================================================
# #     # 🧼 CLEANING PIPELINE
# #     # =====================================================
# #     st.header("🧼 Run Cleaning Pipeline")
# #
# #     if st.button("Run Cleaning"):
# #         pipeline = CleaningPipeline()
# #
# #         with st.spinner("Cleaning your dataset..."):
# #             result = pipeline.run(df)
# #
# #         cleaned_df = result["cleaned_df"]
# #         report = result["report"]
# #
# #         # ---------------- BEFORE vs AFTER ----------------
# #         st.subheader("📉 Before vs After Cleaning")
# #
# #         colA, colB = st.columns(2)
# #
# #         with colA:
# #             st.write("### 🟥 Before Cleaning")
# #             st.write("Missing Values:", report.get("before_missing"))
# #             st.write("Duplicates:", report.get("before_duplicates"))
# #             st.write("Outliers:", report.get("before_outliers"))
# #             st.dataframe(df.head())
# #
# #         with colB:
# #             st.write("### 🟩 After Cleaning")
# #             st.write("Missing Values:", report.get("after_missing"))
# #             st.write("Duplicates:", report.get("after_duplicates"))
# #             st.write("Outliers:", report.get("after_outliers"))
# #             st.dataframe(cleaned_df.head())
# #
# #         # ---------------- CLEANING REPORT ----------------
# #         st.subheader("📑 Cleaning Report")
# #         st.json(report)
# #
# #         # ---------------- DOWNLOAD CLEANED CSV ----------------
# #         cleaned_csv = cleaned_df.to_csv(index=False).encode("utf-8")
# #         st.download_button(
# #             "⬇️ Download Cleaned CSV",
# #             data=cleaned_csv,
# #             file_name="cleaned_dataset.csv",
# #             mime="text/csv"
# #         )
#
#
#
#
#
#
#
#
#
#
#
#
#
# #
# # import sys
# # import os
# #
# # # -------- FIX IMPORT PATH --------
# # ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# # if ROOT_DIR not in sys.path:
# #     sys.path.append(ROOT_DIR)
# #
# # import streamlit as st
# # import pandas as pd
# # import seaborn as sns
# # import matplotlib.pyplot as plt
# #
# # from src.pipeline import CleaningPipeline
# #
# #
# # # =========================================================
# # # 📊 COMPACT EDA FUNCTION
# # # =========================================================
# # def run_eda(df):
# #     st.subheader("📊 Compact EDA Report")
# #
# #     # ---- Missing Heatmap ----
# #     st.write("🕳 Missing Values Heatmap")
# #     fig, ax = plt.subplots(figsize=(5, 2))
# #     sns.heatmap(df.isna(), cbar=False, cmap="viridis", ax=ax)
# #     st.pyplot(fig)
# #
# #     # ---- Correlation Heatmap ----
# #     st.write("🔥 Correlation Heatmap")
# #     num_df = df.select_dtypes(include=["int64", "float64"])
# #     if num_df.shape[1] > 1:
# #         fig, ax = plt.subplots(figsize=(5, 3))
# #         sns.heatmap(num_df.corr(), annot=False, cmap="coolwarm", ax=ax)
# #         st.pyplot(fig)
# #     else:
# #         st.info("Not enough numeric columns for correlation.")
# #
# #     # ---- Distribution Plot ----
# #     st.write("📊 Distribution Plot")
# #     if len(num_df.columns) > 0:
# #         col = st.selectbox("Choose Column:", num_df.columns, key="dist")
# #         fig, ax = plt.subplots(figsize=(6, 2.5))
# #         sns.histplot(df[col], kde=True, ax=ax)
# #         st.pyplot(fig)
# #
# #     # ---- Boxplot ----
# #     st.write("📦 Boxplot")
# #     if len(num_df.columns) > 0:
# #         col = st.selectbox("Choose Column for Boxplot:", num_df.columns, key="box")
# #         fig, ax = plt.subplots(figsize=(6, 2))
# #         sns.boxplot(x=df[col], ax=ax)
# #         st.pyplot(fig)
# #
# #
# # # =========================================================
# # # STREAMLIT APP START
# # # =========================================================
# # st.set_page_config(page_title="AI Data Cleaning App", layout="wide")
# #
# # st.title("🧹 AI Data Cleaning Pipeline with Summary + EDA")
# # st.write("Upload a CSV file to view summaries, explore data, and clean it using AI.")
# #
# #
# # # ---------------- FILE UPLOADER ----------------
# # uploaded = st.file_uploader("Upload CSV File", type=["csv"])
# #
# #
# # # ===========================
# # # MAIN LOGIC
# # # ===========================
# # if uploaded is not None:
# #     df = pd.read_csv(uploaded)
# #
# #     # -------- TABS --------
# #     tab1, tab2, tab3 = st.tabs(["📊 Summary", "📈 EDA", "🧼 Cleaning Pipeline"])
# #
# #     # ===========================
# #     # TAB 1 — SUMMARY DASHBOARD
# #     # ===========================
# #     with tab1:
# #         st.header("📊 Dataset Summary Dashboard")
# #
# #         col1, col2, col3 = st.columns(3)
# #         col1.metric("Rows", df.shape[0])
# #         col2.metric("Columns", df.shape[1])
# #         col3.metric("Memory (KB)", round(df.memory_usage(deep=True).sum() / 1024, 2))
# #
# #         st.subheader("🔠 Column Types")
# #         st.dataframe(pd.DataFrame(df.dtypes, columns=["Data Type"]))
# #
# #         st.subheader("🕳 Missing Values Per Column")
# #         missing_df = df.isna().sum().reset_index()
# #         missing_df.columns = ["Column", "Missing Values"]
# #         st.dataframe(missing_df)
# #
# #         st.subheader("🔢 Unique Values Per Column")
# #         unique_df = df.nunique().reset_index()
# #         unique_df.columns = ["Column", "Unique Values"]
# #         st.dataframe(unique_df)
# #
# #         st.subheader("📐 Numerical Summary")
# #         try:
# #             st.dataframe(df.describe().T)
# #         except:
# #             st.info("No numeric columns available.")
# #
# #         st.subheader("🧩 Categorical Sample")
# #         cat_cols = df.select_dtypes(include=["object"]).columns
# #         if len(cat_cols) > 0:
# #             st.dataframe(df[cat_cols].head())
# #         else:
# #             st.info("No categorical columns found.")
# #
# #         st.subheader("👀 Raw Data Preview")
# #         st.dataframe(df.head())
# #
# #     # ===========================
# #     # TAB 2 — COMPACT EDA
# #     # ===========================
# #     with tab2:
# #         st.header("📈 Exploratory Data Analysis (Compact View)")
# #         run_eda(df)
# #
# #     # ===========================
# #     # TAB 3 — CLEANING PIPELINE
# #     # ===========================
# #     with tab3:
# #         st.header("🧼 Run Cleaning Pipeline")
# #
# #         if st.button("Run Cleaning"):
# #             pipeline = CleaningPipeline()
# #
# #             with st.spinner("Cleaning your dataset..."):
# #                 result = pipeline.run(df)
# #
# #             cleaned_df = result["cleaned_df"]
# #             report = result["report"]
# #
# #             colA, colB = st.columns(2)
# #
# #             with colA:
# #                 st.write("### 🟥 Before Cleaning")
# #                 st.write("Missing Values:", report.get("before_missing"))
# #                 st.write("Duplicates:", report.get("before_duplicates"))
# #                 st.write("Outliers:", report.get("before_outliers"))
# #                 st.dataframe(df.head())
# #
# #             with colB:
# #                 st.write("### 🟩 After Cleaning")
# #                 st.write("Missing Values:", report.get("after_missing"))
# #                 st.write("Duplicates:", report.get("after_duplicates"))
# #                 st.write("Outliers:", report.get("after_outliers"))
# #                 st.dataframe(cleaned_df.head())
# #
# #             st.subheader("📑 Cleaning Report")
# #             st.json(report)
# #
# #             cleaned_csv = cleaned_df.to_csv(index=False).encode("utf-8")
# #             st.download_button(
# #                 "⬇️ Download Cleaned CSV",
# #                 data=cleaned_csv,
# #                 file_name="cleaned_dataset.csv",
# #                 mime="text/csv"
# #             )
#
#
#
#
# #
# # import sys
# # import os
# #
# # # -----------------------------------------------------
# # # FIX IMPORT PATH FOR STREAMLIT
# # # -----------------------------------------------------
# # ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# # if ROOT_DIR not in sys.path:
# #     sys.path.append(ROOT_DIR)
# #
# # import streamlit as st
# # import pandas as pd
# # import seaborn as sns
# # import matplotlib.pyplot as plt
# # from src.pipeline import CleaningPipeline
# #
# #
# # # -----------------------------------------------------
# # # ADVANCED BEAUTIFUL UI CSS
# # # -----------------------------------------------------
# # st.markdown("""
# #     <style>
# #
# #     /* Main Header */
# #     .main-title {
# #         font-size: 38px;
# #         font-weight: 900;
# #         color: white;
# #         padding: 20px;
# #         text-align: center;
# #         border-radius: 14px;
# #         background: linear-gradient(90deg, #4b79ff, #4cc9f0);
# #         box-shadow: 0px 6px 18px rgba(0,0,0,0.2);
# #         margin-bottom: 25px;
# #     }
# #
# #     /* Metric Cards */
# #     .metric-card {
# #         background: #ffffffcc;
# #         backdrop-filter: blur(10px);
# #         padding: 20px;
# #         border-radius: 14px;
# #         border: 1px solid #e3e6ee;
# #         text-align: center;
# #         box-shadow: 0px 3px 10px rgba(0,0,0,0.1);
# #         transition: 0.3s ease-in-out;
# #     }
# #
# #     .metric-card:hover {
# #         transform: translateY(-4px);
# #         box-shadow: 0px 5px 16px rgba(0,0,0,0.18);
# #     }
# #
# #     /* Section Titles */
# #     .section-title {
# #         font-size: 22px;
# #         font-weight: 700;
# #         color: #333;
# #         margin-top: 20px;
# #         margin-bottom: 8px;
# #         padding-left: 12px;
# #         border-left: 5px solid #4cc9f0;
# #     }
# #
# #     /* Dataframe Shadow */
# #     div[data-testid="stDataFrame"] {
# #         border-radius: 12px;
# #         box-shadow: 0px 3px 12px rgba(0,0,0,0.06);
# #     }
# #
# #     /* Tabs */
# #     .stTabs [role="tablist"] button {
# #         font-size: 18px !important;
# #         padding: 10px 16px !important;
# #         font-weight: 600 !important;
# #     }
# #
# #     </style>
# # """, unsafe_allow_html=True)
# #
# #
# #
# # # -----------------------------------------------------
# # # COMPACT BEAUTIFUL EDA FUNCTION
# # # -----------------------------------------------------
# # def run_eda(df):
# #     st.markdown("<div class='section-title'>📈 Compact EDA Report</div>", unsafe_allow_html=True)
# #
# #     num_df = df.select_dtypes(include=["int64", "float64"])
# #
# #     # Missing heatmap
# #     st.write("🕳 Missing Value Heatmap")
# #     fig, ax = plt.subplots(figsize=(6, 2.5))
# #     sns.heatmap(df.isna(), cbar=False, cmap="Blues", ax=ax)
# #     st.pyplot(fig)
# #
# #     # Correlation Heatmap
# #     st.write("🔥 Correlation Heatmap")
# #     if num_df.shape[1] > 1:
# #         fig, ax = plt.subplots(figsize=(6, 3))
# #         sns.heatmap(num_df.corr(), annot=False, cmap="coolwarm", ax=ax)
# #         st.pyplot(fig)
# #     else:
# #         st.info("Not enough numeric columns.")
# #
# #     # Distribution Plot
# #     st.write("📊 Distribution Plot")
# #     if len(num_df.columns) > 0:
# #         col = st.selectbox("Choose Numeric Column", num_df.columns, key="dist")
# #         fig, ax = plt.subplots(figsize=(6, 2.8))
# #         sns.histplot(df[col], kde=True, color="#4b79ff", ax=ax)
# #         st.pyplot(fig)
# #
# #     # Boxplot
# #     st.write("📦 Boxplot")
# #     if len(num_df.columns) > 0:
# #         col = st.selectbox("Choose Column for Boxplot", num_df.columns, key="box")
# #         fig, ax = plt.subplots(figsize=(6, 2.5))
# #         sns.boxplot(x=df[col], color="#4cc9f0", ax=ax)
# #         st.pyplot(fig)
# #
# #
# #
# # # -----------------------------------------------------
# # # STREAMLIT APP
# # # -----------------------------------------------------
# # st.set_page_config(page_title="Advanced AI Cleaning App", layout="wide")
# #
# # st.markdown("<div class='main-title'>✨ AI Data Cleaner & EDA Dashboard ✨</div>", unsafe_allow_html=True)
# #
# # uploaded = st.file_uploader("📁 Upload CSV File", type=["csv"])
# #
# #
# #
# # # -----------------------------------------------------
# # # MAIN APP LOGIC
# # # -----------------------------------------------------
# # if uploaded is not None:
# #     df = pd.read_csv(uploaded)
# #
# #     tab1, tab2, tab3 = st.tabs(["📊 Summary", "📈 EDA", "🧼 Cleaning Pipeline"])
# #
# #
# #
# #     # -------------------------------------------------
# #     # TAB 1 — SUMMARY
# #     # -------------------------------------------------
# #     with tab1:
# #         st.markdown("<div class='section-title'>📊 Dataset Summary Dashboard</div>", unsafe_allow_html=True)
# #
# #         # Metric Cards
# #         col1, col2, col3 = st.columns(3)
# #         with col1:
# #             st.markdown(f"<div class='metric-card'><h4>Rows</h4><h2>{df.shape[0]}</h2></div>", unsafe_allow_html=True)
# #         with col2:
# #             st.markdown(f"<div class='metric-card'><h4>Columns</h4><h2>{df.shape[1]}</h2></div>", unsafe_allow_html=True)
# #         with col3:
# #             memory = round(df.memory_usage(deep=True).sum() / 1024, 2)
# #             st.markdown(f"<div class='metric-card'><h4>Memory (KB)</h4><h2>{memory}</h2></div>", unsafe_allow_html=True)
# #
# #         # Column Types
# #         st.markdown("<div class='section-title'>🔠 Column Types</div>", unsafe_allow_html=True)
# #         st.dataframe(pd.DataFrame(df.dtypes, columns=["Type"]))
# #
# #         # Missing Values
# #         st.markdown("<div class='section-title'>🕳 Missing Values</div>", unsafe_allow_html=True)
# #         missing_df = df.isna().sum().reset_index()
# #         missing_df.columns = ["Column", "Missing Values"]
# #         st.dataframe(missing_df)
# #
# #         # Unique Values
# #         st.markdown("<div class='section-title'>🔢 Unique Values</div>", unsafe_allow_html=True)
# #         unique_df = df.nunique().reset_index()
# #         unique_df.columns = ["Column", "Unique Values"]
# #         st.dataframe(unique_df)
# #
# #         # Numerical Summary
# #         st.markdown("<div class='section-title'>📐 Numerical Summary</div>", unsafe_allow_html=True)
# #         st.dataframe(df.describe().T)
# #
# #         # Preview
# #         st.markdown("<div class='section-title'>👀 Data Preview</div>", unsafe_allow_html=True)
# #         st.dataframe(df.head())
# #
# #
# #
# #     # -------------------------------------------------
# #     # TAB 2 — EDA
# #     # -------------------------------------------------
# #     with tab2:
# #         run_eda(df)
# #
# #
# #
# #     # -------------------------------------------------
# #     # TAB 3 — CLEANING PIPELINE
# #     # -------------------------------------------------
# #     with tab3:
# #         st.markdown("<div class='section-title'>🧼 AI Cleaning Pipeline</div>", unsafe_allow_html=True)
# #
# #         if st.button("✨ Run Cleaning", use_container_width=True):
# #             pipeline = CleaningPipeline()
# #
# #             with st.spinner("Running AI cleaning pipeline..."):
# #                 result = pipeline.run(df)
# #
# #             cleaned_df = result["cleaned_df"]
# #             report = result["report"]
# #
# #             colA, colB = st.columns(2)
# #
# #             # Before
# #             with colA:
# #                 st.markdown("<h4>🟥 Before Cleaning</h4>", unsafe_allow_html=True)
# #                 st.write("Missing:", report.get("before_missing"))
# #                 st.write("Duplicates:", report.get("before_duplicates"))
# #                 st.write("Outliers:", report.get("before_outliers"))
# #                 st.dataframe(df.head())
# #
# #             # After
# #             with colB:
# #                 st.markdown("<h4>🟩 After Cleaning</h4>", unsafe_allow_html=True)
# #                 st.write("Missing:", report.get("after_missing"))
# #                 st.write("Duplicates:", report.get("after_duplicates"))
# #                 st.write("Outliers:", report.get("after_outliers"))
# #                 st.dataframe(cleaned_df.head())
# #
# #             # Report
# #             st.markdown("<div class='section-title'>📑 Cleaning Report</div>", unsafe_allow_html=True)
# #             st.json(report)
# #
# #             # Download
# #             cleaned_csv = cleaned_df.to_csv(index=False).encode("utf-8")
# #             st.download_button(
# #                 "⬇️ Download Cleaned CSV",
# #                 cleaned_csv,
# #                 "cleaned_dataset.csv",
# #                 "text/csv"
# #             )
#
#
#
#
# #
# # import sys
# # import os
# #
# # # ---------------------------------------------------------
# # # FIX import path so src.pipeline works
# # # ---------------------------------------------------------
# # ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# # if ROOT_DIR not in sys.path:
# #     sys.path.append(ROOT_DIR)
# #
# # import streamlit as st
# # import pandas as pd
# # import seaborn as sns
# # import matplotlib.pyplot as plt
# #
# # from src.pipeline import CleaningPipeline
# #
# #
# # # ---------------------------------------------------------
# # # PAGE SETTINGS
# # # ---------------------------------------------------------
# # st.set_page_config(page_title="AI Data Cleaning App", layout="wide")
# #
# # # ---------------------------------------------------------
# # # LEFT NAVIGATION BAR
# # # ---------------------------------------------------------
# # st.sidebar.title("📌 Navigation")
# #
# # page = st.sidebar.radio(
# #     "Go to:",
# #     ["Dataset Summary", "EDA", "Cleaning Pipeline"]
# # )
# #
# # st.sidebar.info("Upload your CSV at the top of the screen.")
# #
# #
# # # ---------------------------------------------------------
# # # FILE UPLOADER (GLOBAL)
# # # ---------------------------------------------------------
# # uploaded = st.file_uploader("📁 Upload CSV File", type=["csv"])
# #
# #
# # # ---------------------------------------------------------
# # # SUMMARY PAGE FUNCTION
# # # ---------------------------------------------------------
# # def show_summary(df: pd.DataFrame):
# #     st.title("📊 Dataset Summary Dashboard")
# #
# #     # Metrics Row
# #     c1, c2, c3 = st.columns(3)
# #     c1.metric("Rows", df.shape[0])
# #     c2.metric("Columns", df.shape[1])
# #     mem = round(df.memory_usage(deep=True).sum() / 1024, 2)
# #     c3.metric("Memory (KB)", mem)
# #
# #     st.markdown("---")
# #     st.subheader("🔠 Column Types")
# #
# #     type_df = pd.DataFrame(df.dtypes, columns=["Data Type"]).reset_index()
# #     type_df.columns = ["Column", "Data Type"]
# #     st.dataframe(type_df, use_container_width=True)
# #
# #     st.markdown("---")
# #     st.subheader("🕳 Missing Values per Column")
# #     missing_df = df.isna().sum().reset_index()
# #     missing_df.columns = ["Column", "Missing Values"]
# #     st.dataframe(missing_df, use_container_width=True)
# #
# #     st.markdown("---")
# #     st.subheader("🔢 Unique Values per Column")
# #     uniq = df.nunique().reset_index()
# #     uniq.columns = ["Column", "Unique Values"]
# #     st.dataframe(uniq, use_container_width=True)
# #
# #     st.markdown("---")
# #     st.subheader("📐 Numerical Summary")
# #     try:
# #         desc = df.describe().T.reset_index()
# #         desc.columns = ["Column"] + list(desc.columns[1:])
# #         st.dataframe(desc, use_container_width=True)
# #     except:
# #         st.info("No numeric columns found.")
# #
# #     st.markdown("---")
# #     st.subheader("👀 Data Preview")
# #     st.dataframe(df.head(), use_container_width=True)
# #
# #
# # # ---------------------------------------------------------
# # # EDA PAGE FUNCTION — Compact & Side-by-Side Charts
# # # ---------------------------------------------------------
# # def run_eda(df: pd.DataFrame):
# #     st.title("📈 Exploratory Data Analysis (EDA)")
# #
# #     num_df = df.select_dtypes(include=["int64", "float64"])
# #
# #     # ------------------------------
# #     # ROW 1 — Missing heatmap + Correlation heatmap
# #     # ------------------------------
# #     col1, col2 = st.columns(2)
# #
# #     with col1:
# #         st.subheader("🕳 Missing Values Heatmap")
# #         fig, ax = plt.subplots(figsize=(4, 2))
# #         sns.heatmap(df.isna(), cbar=False, cmap="Blues", ax=ax)
# #         ax.set_xlabel("")
# #         ax.set_ylabel("")
# #         st.pyplot(fig)
# #
# #     with col2:
# #         st.subheader("🔥 Correlation Heatmap")
# #         if num_df.shape[1] > 1:
# #             fig, ax = plt.subplots(figsize=(4, 2))
# #             sns.heatmap(num_df.corr(), cmap="coolwarm", ax=ax)
# #             ax.set_xlabel("")
# #             ax.set_ylabel("")
# #             st.pyplot(fig)
# #         else:
# #             st.info("Not enough numerical columns.")
# #
# #     # ------------------------------
# #     # ROW 2 — Distribution + Boxplot
# #     # ------------------------------
# #     st.markdown("---")
# #     st.subheader("📊 Distribution & Outlier View")
# #
# #     if len(num_df.columns) > 0:
# #         col3, col4 = st.columns(2)
# #
# #         with col3:
# #             col_selected = st.selectbox("Choose numeric column for distribution:", num_df.columns)
# #             fig, ax = plt.subplots(figsize=(4, 2))
# #             sns.histplot(df[col_selected], kde=True, ax=ax)
# #             st.pyplot(fig)
# #
# #         with col4:
# #             col_box = st.selectbox("Choose numeric column for boxplot:", num_df.columns, key="box_key")
# #             fig, ax = plt.subplots(figsize=(4, 2))
# #             sns.boxplot(x=df[col_box], ax=ax)
# #             st.pyplot(fig)
# #
# #     else:
# #         st.info("No numeric columns available.")
# #
# #     # ------------------------------
# #     # Categorical Summary
# #     # ------------------------------
# #     st.markdown("---")
# #     st.subheader("🧩 Categorical Columns Overview")
# #
# #     cat_cols = df.select_dtypes(include=["object"]).columns
# #     if len(cat_cols) > 0:
# #         for col in cat_cols[:3]:  # limit to top 3 to avoid clutter
# #             st.write(f"**{col} – Top Values:**")
# #             st.write(df[col].value_counts().head(5))
# #     else:
# #         st.info("No categorical columns found.")
# #
# #
# # # ---------------------------------------------------------
# # # CLEANING PIPELINE PAGE FUNCTION
# # # ---------------------------------------------------------
# # def run_cleaning(df: pd.DataFrame):
# #     st.title("🧼 Cleaning Pipeline")
# #
# #     if st.button("Run Cleaning"):
# #         pipeline = CleaningPipeline()
# #
# #         with st.spinner("Cleaning dataset..."):
# #             result = pipeline.run(df)
# #
# #         cleaned_df = result["cleaned_df"]
# #         report = result["report"]
# #
# #         cA, cB = st.columns(2)
# #
# #         with cA:
# #             st.subheader("🟥 Before Cleaning")
# #             st.json({
# #                 "Missing": report.get("before_missing"),
# #                 "Duplicates": report.get("before_duplicates"),
# #                 "Outliers": report.get("before_outliers")
# #             })
# #             st.dataframe(df.head(), use_container_width=True)
# #
# #         with cB:
# #             st.subheader("🟩 After Cleaning")
# #             st.json({
# #                 "Missing": report.get("after_missing"),
# #                 "Duplicates": report.get("after_duplicates"),
# #                 "Outliers": report.get("after_outliers")
# #             })
# #             st.dataframe(cleaned_df.head(), use_container_width=True)
# #
# #         st.markdown("---")
# #         st.subheader("📑 Full Cleaning Report")
# #         st.json(report)
# #
# #         # Download cleaned data
# #         st.download_button(
# #             "⬇️ Download Cleaned CSV",
# #             cleaned_df.to_csv(index=False).encode("utf-8"),
# #             "cleaned_dataset.csv",
# #             "text/csv"
# #         )
# #     else:
# #         st.info("Click 'Run Cleaning' to execute the pipeline.")
# #
# #
# # # ---------------------------------------------------------
# # # MAIN PAGE LOGIC
# # # ---------------------------------------------------------
# # if uploaded is None:
# #     st.info("Upload a CSV file to begin.")
# # else:
# #     df = pd.read_csv(uploaded)
# #
# #     if page == "Dataset Summary":
# #         show_summary(df)
# #
# #     elif page == "EDA":
# #         run_eda(df)
# #
# #     elif page == "Cleaning Pipeline":
# #         run_cleaning(df)
#
#
#
#
#
# # ui/app.py
# # """
# # Full UI for DataPrep with:
# # - Gradient dark-blue top navbar (interactive)
# # - Sidebar with logo + MAIN MENU + FEATURES
# # - Hero welcome card
# # - Summary / EDA / Cleaning pages (functions unchanged in logic)
# # - Download selector (CSV / Pickle)
# # - No backend changes (uses src.pipeline.CleaningPipeline)
# # """
# # #
# # import sys
# # import os
# # import streamlit as st
# # import pandas as pd
# # import seaborn as sns
# # import matplotlib.pyplot as plt
# #
# # # Ensure project root on path so src imports work
# # ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# # if ROOT_DIR not in sys.path:
# #     sys.path.append(ROOT_DIR)
# #
# # from src.pipeline import CleaningPipeline
# #
# # # -------------------------
# # # Page config
# # # -------------------------
# # st.set_page_config(page_title="DataPrep – AI Cleaner", layout="wide")
# #
# # # -------------------------
# # # CSS (Gradient navbar, sidebar, cards, hero)
# # # -------------------------
# # st.markdown(
# #     """
# #     <style>
# #     :root{
# #       --primary: #0b6ef6;
# #       --accent: #095fc1;
# #       --muted: #64748b;
# #       --card-bg: #ffffff;
# #       --surface: #f6f8fb;
# #       --border: #e6eefc;
# #       --shadow: 0 10px 30px rgba(11,110,246,0.07);
# #     }
# #
# #     /* App background */
# #     .stApp {
# #       background: var(--surface);
# #       color: #0b1a2b;
# #       font-family: "Segoe UI", Roboto, "Helvetica Neue", Arial;
# #     }
# #
# #     /* ========== TOP NAV BAR (gradient dark-blue card) ========== */
# #     .topnav {
# #         width: 100%;
# #         background: linear-gradient(135deg, #001f4d, #004b99);
# #         padding: 12px 18px;
# #         border-radius: 14px;
# #         border: 1px solid rgba(255,255,255,0.06);
# #         box-shadow: 0 10px 30px rgba(0, 40, 120, 0.40);
# #         display: flex;
# #         align-items: center;
# #         justify-content: space-between;
# #         margin-bottom: 16px;
# #     }
# #     .topnav-left { display:flex; align-items:center; gap:14px; }
# #     .topnav-title { font-size:20px; font-weight:800; color:#fff; margin:0; }
# #     .nav-menu { display:flex; gap:18px; align-items:center; }
# #     .nav-item {
# #         color: rgba(219,234,254,0.92);
# #         font-size:14px;
# #         font-weight:700;
# #         padding:6px 10px;
# #         border-radius:8px;
# #     }
# #     .nav-item-active {
# #         color: white;
# #         background: rgba(255,255,255,0.08);
# #         box-shadow: 0 6px 18px rgba(0,0,0,0.08);
# #     }
# #
# #     /* search input styled for dark background */
# #     .search-box {
# #         width: 260px;
# #         padding: 8px 12px;
# #         border-radius: 12px;
# #         border: 1px solid rgba(255,255,255,0.18);
# #         background: rgba(255,255,255,0.06);
# #         font-size: 14px;
# #         color: #e8f4ff;
# #     }
# #     .search-box::placeholder { color: #c7ddff; }
# #     .search-box:focus { outline: none; background: rgba(255,255,255,0.09); }
# #
# #     .notify-btn {
# #         background: rgba(255,255,255,0.08);
# #         border: 1px solid rgba(255,255,255,0.14);
# #         padding: 8px 10px;
# #         border-radius: 10px;
# #         color: #fff;
# #         cursor: pointer;
# #     }
# #     .notify-btn:hover { background: rgba(255,255,255,0.12); }
# #
# #     /* ========== SIDEBAR ========== */
# #     [data-testid="stSidebar"] {
# #       background: #ffffff;
# #       padding: 20px;
# #       width: 300px !important;
# #       border-right: 1px solid var(--border);
# #     }
# #     .brand-wrapper {
# #       display:flex;
# #       align-items:center;
# #       gap:12px;
# #       padding:10px;
# #       background:#fff;
# #       border-radius:12px;
# #       border:1px solid #e6eefc;
# #       margin-bottom:12px;
# #       box-shadow:0 8px 20px rgba(11,110,246,0.03);
# #     }
# #     .brand-logo {
# #       width:40px;
# #       height:40px;
# #       border-radius:8px;
# #       object-fit:contain;
# #       background:#eef6ff;
# #       padding:6px;
# #     }
# #     .brand-name { font-weight:800; color:#073763; font-size:18px; margin:0; }
# #     .brand-sub { color:var(--muted); font-size:12px; margin-top:2px; }
# #
# #     .sidebar-section {
# #       font-size:12px;
# #       color:#94a3b8;
# #       margin-top:18px;
# #       margin-bottom:8px;
# #       font-weight:700;
# #       letter-spacing:0.6px;
# #     }
# #
# #     /* Off-white menu cards */
# #     .menu-card {
# #       background: #fafafa;
# #       border-radius: 12px;
# #       padding: 10px 12px;
# #       border: 1px solid #f0f1f5;
# #       width:100%;
# #       margin-bottom:8px;
# #       font-size:15px;
# #       color:#243447;
# #       cursor:pointer;
# #     }
# #     .menu-card:hover { background:#f0f4f9; border-color:#e5e9f6; }
# #
# #     .feature-item {
# #       background: #ffffff;
# #       border-radius:10px;
# #       padding:8px 12px;
# #       margin-bottom:8px;
# #       border:1px solid var(--border);
# #       display:flex;
# #       align-items:center;
# #       gap:10px;
# #       color:#334155;
# #     }
# #
# #     .circle-dot { width:10px; height:10px; border-radius:50%; display:inline-block; margin-right:8px; }
# #     .dot-blue { background:#1d4ed8; }
# #     .dot-green { background:#059669; }
# #     .dot-yellow { background:#f59e0b; }
# #     .dot-purple { background:#7c3aed; }
# #     .dot-dark { background:#0f172a; }
# #
# #     /* Content cards */
# #     .card {
# #       background: var(--card-bg);
# #       border-radius:12px;
# #       padding:14px;
# #       border:1px solid var(--border);
# #       box-shadow:var(--shadow);
# #       margin-bottom:12px;
# #     }
# #
# #     .kpi-title { color:var(--muted); font-weight:700; margin:0; font-size:13px; }
# #     .kpi-value { color:#073763; font-weight:800; font-size:28px; margin-top:6px; }
# #
# #     /* Dataframe card look */
# #     div[data-testid="stDataFrame"] { border-radius:10px; border:1px solid var(--border); box-shadow: 0 8px 24px rgba(11,110,246,0.03); }
# #
# #     /* Buttons */
# #     .stButton>button { background:var(--primary); color:white; border-radius:10px; padding:8px 12px; border:none; }
# #     .stButton>button:hover { background:var(--accent); }
# #
# #     /* Hero card (futuristic neon blue) */
# #     .hero {
# #       background: linear-gradient(135deg, rgba(0,132,255,0.95), rgba(0,76,255,0.95));
# #       border-radius: 16px;
# #       padding: 26px;
# #       color: white;
# #       margin-bottom: 18px;
# #       box-shadow: 0 16px 40px rgba(0,76,255,0.14);
# #       position: relative;
# #       overflow: hidden;
# #     }
# #     .hero h1 { margin: 0; font-size: 30px; font-weight:800; text-shadow: 0 6px 18px rgba(0,0,0,0.18); }
# #     .hero p { margin:6px 0 0 0; opacity:0.95; font-size:14px; }
# #
# #     .hero::before {
# #       content: "";
# #       position: absolute;
# #       right: -80px;
# #       top: -60px;
# #       width: 360px;
# #       height: 360px;
# #       background: radial-gradient(circle at 30% 30%, rgba(255,255,255,0.12), rgba(255,255,255,0) 36%);
# #       transform: rotate(20deg);
# #       opacity: 0.6;
# #     }
# #
# #     </style>
# #     """,
# #     unsafe_allow_html=True,
# # )
# #
# # # -------------------------
# # # TOP NAVBAR (visual) + interactive buttons underneath for routing
# # # -------------------------
# # # Visual navbar (HTML)
# # st.markdown(
# #     """
# #     <div class="topnav">
# #       <div class="topnav-left">
# #         <div class="topnav-title">DataPrep</div>
# #       </div>
# #
# #       <!-- visual menu (decorative; real buttons below handle routing) -->
# #       <div class="nav-menu" style="display:flex;align-items:center;">
# #         <div class="nav-item">Home</div>
# #         <div class="nav-item">Summary</div>
# #         <div class="nav-item">EDA</div>
# #         <div class="nav-item">Cleaning</div>
# #       </div>
# #
# #       <!-- search + notify -->
# #       <div style="display:flex;align-items:center;gap:12px;">
# #         <input class="search-box" placeholder="Search..." />
# #         <div class="notify-btn">🔔</div>
# #       </div>
# #     </div>
# #     """,
# #     unsafe_allow_html=True,
# # )
# #
# # # To make the navbar interactive (clicks change pages), create invisible 1-row buttons aligned under navbar.
# # # We put them in columns to roughly align with visual menu; clicking these sets the page.
# # nav_col_left, nav_col_center, nav_col_right = st.columns([1, 2, 1])
# # with nav_col_left:
# #     # empty to keep layout
# #     st.write("")
# # with nav_col_center:
# #     # place actual buttons for navigation (styled by global button CSS)
# #     b_home = st.button("Home", key="nav_home_small")
# #     b_summary = st.button("Summary", key="nav_summary_small")
# #     b_eda = st.button("EDA", key="nav_eda_small")
# #     b_clean = st.button("Cleaning", key="nav_clean_small")
# # with nav_col_right:
# #     st.write("")
# #
# # # -------------------------
# # # SIDEBAR content (logo + MAIN MENU + FEATURES)
# # # -------------------------
# # # Logo file path (optional): ui/assets/logo.png
# # logo_path = "ui/assets/logo.png"  # adjust if your assets path differs
# # # Brand block
# # st.sidebar.markdown(
# #     f"""
# #     <div class="brand-wrapper">
# #       <img src="{logo_path}" class="brand-logo" alt="logo" />
# #       <div>
# #         <div class="brand-name">DataPrep</div>
# #         <div class="brand-sub">Prepare, clean & inspect data</div>
# #       </div>
# #     </div>
# #     """,
# #     unsafe_allow_html=True,
# # )
# #
# # # Sidebar MAIN MENU rendered as off-white menu cards (clickable using st.button)
# # st.sidebar.markdown('<div class="sidebar-section">MAIN MENU</div>', unsafe_allow_html=True)
# #
# # # We'll render menu cards as markdown for look, and use st.button underneath for click handling.
# # st.sidebar.markdown('<div class="menu-card">Summary</div>', unsafe_allow_html=True)
# # sidebar_summary = st.sidebar.button("Go to Summary", key="sb_summary")
# #
# # st.sidebar.markdown('<div class="menu-card">EDA</div>', unsafe_allow_html=True)
# # sidebar_eda = st.sidebar.button("Go to EDA", key="sb_eda")
# #
# # st.sidebar.markdown('<div class="menu-card">Cleaning</div>', unsafe_allow_html=True)
# # sidebar_clean = st.sidebar.button("Go to Cleaning", key="sb_clean")
# #
# # # FEATURES section
# # st.sidebar.markdown('<div class="sidebar-section">FEATURES</div>', unsafe_allow_html=True)
# # st.sidebar.markdown('<div class="feature-item"><span class="circle-dot dot-blue"></span> Data Analysis</div>', unsafe_allow_html=True)
# # st.sidebar.markdown('<div class="feature-item"><span class="circle-dot dot-green"></span> ML Preparation</div>', unsafe_allow_html=True)
# # st.sidebar.markdown('<div class="feature-item"><span class="circle-dot dot-yellow"></span> Outlier Report</div>', unsafe_allow_html=True)
# # st.sidebar.markdown('<div class="feature-item"><span class="circle-dot dot-purple"></span> Profiling</div>', unsafe_allow_html=True)
# # st.sidebar.markdown('<div class="feature-item"><span class="circle-dot dot-dark"></span> Storage</div>', unsafe_allow_html=True)
# #
# # # small footer spacing
# # st.sidebar.markdown("<br><br>", unsafe_allow_html=True)
# #
# # # -------------------------
# # # Page routing state
# # # -------------------------
# # if "page" not in st.session_state:
# #     st.session_state.page = "Summary"
# #
# # # Buttons from navbar (center) or sidebar update the page
# # if b_home:
# #     st.session_state.page = "Summary"
# # if b_summary:
# #     st.session_state.page = "Summary"
# # if b_eda:
# #     st.session_state.page = "EDA"
# # if b_clean:
# #     st.session_state.page = "Cleaning"
# #
# # if sidebar_summary:
# #     st.session_state.page = "Summary"
# # if sidebar_eda:
# #     st.session_state.page = "EDA"
# # if sidebar_clean:
# #     st.session_state.page = "Cleaning"
# #
# # page = st.session_state.page
# #
# # # -------------------------
# # # HERO welcome card (futuristic neon-blue)
# # # -------------------------
# # st.markdown(
# #     """
# #     <div class="hero">
# #       <h1>Welcome to DataPrep</h1>
# #       <p>Your futuristic AI-powered data cleaning and exploratory analysis hub.</p>
# #     </div>
# #     """,
# #     unsafe_allow_html=True,
# # )
# #
# # # -------------------------
# # # Uploader (global)
# # # -------------------------
# # uploaded = st.file_uploader("Upload CSV file", type=["csv"])
# #
# # # -------------------------
# # # ---------- USER FUNCTIONS (unchanged backend logic) ----------
# # # Summary, EDA and Cleaning implementations are kept functionally the same
# # # as requested: only UI wrapper changed.
# # # -------------------------
# #
# # def show_summary(df: pd.DataFrame):
# #     st.markdown('<div class="card"><div style="display:flex;justify-content:space-between;align-items:center;"><div>'
# #                 '<div class="kpi-title">Dataset Summary</div>'
# #                 '<div style="font-size:12px;color:var(--muted);">Quick overview</div></div>'
# #                 '<div style="font-weight:700;color:#e6f2ff;border-radius:50%;padding:8px;background:rgba(255,255,255,0.04)">🔷</div>'
# #                 '</div></div>', unsafe_allow_html=True)
# #
# #     # KPI row
# #     k1, k2, k3, k4 = st.columns([2,1,1,1])
# #     with k1:
# #         st.markdown(f'<div class="card"><div class="kpi-title">Rows</div><div class="kpi-value">{df.shape[0]}</div></div>', unsafe_allow_html=True)
# #     with k2:
# #         st.markdown(f'<div class="card"><div class="kpi-title">Columns</div><div class="kpi-value">{df.shape[1]}</div></div>', unsafe_allow_html=True)
# #     with k3:
# #         mem_kb = round(df.memory_usage(deep=True).sum() / 1024, 2)
# #         st.markdown(f'<div class="card"><div class="kpi-title">Memory (KB)</div><div class="kpi-value">{mem_kb}</div></div>', unsafe_allow_html=True)
# #     with k4:
# #         missing_total = int(df.isna().sum().sum())
# #         st.markdown(f'<div class="card"><div class="kpi-title">Missing</div><div class="kpi-value">{missing_total}</div></div>', unsafe_allow_html=True)
# #
# #     st.markdown("---")
# #     c1, c2 = st.columns([2,1])
# #     with c1:
# #         st.markdown('<div class="card"><h4 style="margin:0;color:#073763">Column Types</h4>', unsafe_allow_html=True)
# #         type_df = pd.DataFrame(df.dtypes, columns=["Type"]).reset_index().rename(columns={"index":"Column"})
# #         st.dataframe(type_df, use_container_width=True)
# #         st.markdown('</div>', unsafe_allow_html=True)
# #     with c2:
# #         st.markdown('<div class="card"><h4 style="margin:0;color:#073763">Top Missing</h4>', unsafe_allow_html=True)
# #         miss_df = df.isna().sum().sort_values(ascending=False).reset_index()
# #         miss_df.columns = ["Column", "Missing"]
# #         st.dataframe(miss_df.head(8), use_container_width=True)
# #         st.markdown('</div>', unsafe_allow_html=True)
# #
# #     st.markdown("---")
# #     r1, r2 = st.columns([2,1])
# #     with r1:
# #         st.markdown('<div class="card"><h4 style="margin:0;color:#073763">Unique Values</h4>', unsafe_allow_html=True)
# #         uniq = df.nunique().reset_index()
# #         uniq.columns = ["Column", "Unique"]
# #         st.dataframe(uniq.head(12), use_container_width=True)
# #         st.markdown('</div>', unsafe_allow_html=True)
# #     with r2:
# #         st.markdown('<div class="card"><h4 style="margin:0;color:#073763">Preview</h4>', unsafe_allow_html=True)
# #         st.dataframe(df.head(6), use_container_width=True)
# #         st.markdown('</div>', unsafe_allow_html=True)
# #
# #
# # def run_eda(df: pd.DataFrame):
# #     st.markdown('<div class="card"><h4 style="margin:0;color:#073763">Exploratory Data Analysis</h4>', unsafe_allow_html=True)
# #     num_df = df.select_dtypes(include=["int64", "float64"])
# #
# #     # row 1
# #     c1, c2 = st.columns(2)
# #     with c1:
# #         st.markdown('<div style="margin-bottom:8px"><strong>Missing Values</strong></div>', unsafe_allow_html=True)
# #         fig, ax = plt.subplots(figsize=(5,2.2))
# #         sns.heatmap(df.isna(), cbar=False, cmap="Blues", ax=ax)
# #         ax.set_xlabel(""); ax.set_ylabel("")
# #         st.pyplot(fig)
# #     with c2:
# #         st.markdown('<div style="margin-bottom:8px"><strong>Correlation</strong></div>', unsafe_allow_html=True)
# #         if num_df.shape[1] > 1:
# #             fig, ax = plt.subplots(figsize=(5,2.2))
# #             sns.heatmap(num_df.corr(), cmap="coolwarm", ax=ax)
# #             ax.set_xlabel(""); ax.set_ylabel("")
# #             st.pyplot(fig)
# #         else:
# #             st.info("Not enough numeric columns for correlation.")
# #     st.markdown('</div>', unsafe_allow_html=True)
# #
# #     st.markdown('---')
# #     st.markdown('<div class="card"><h4 style="margin:0;color:#073763">Distribution & Outliers</h4>', unsafe_allow_html=True)
# #     if len(num_df.columns) > 0:
# #         d1, d2 = st.columns(2)
# #         with d1:
# #             col_sel = st.selectbox("Distribution column", num_df.columns, key="eda_dist")
# #             fig, ax = plt.subplots(figsize=(5,2))
# #             sns.histplot(df[col_sel].dropna(), kde=True, ax=ax)
# #             st.pyplot(fig)
# #         with d2:
# #             col_box = st.selectbox("Boxplot column", num_df.columns, key="eda_box")
# #             fig, ax = plt.subplots(figsize=(5,2))
# #             sns.boxplot(x=df[col_box].dropna(), ax=ax)
# #             st.pyplot(fig)
# #     else:
# #         st.info("No numeric columns available.")
# #     st.markdown('</div>', unsafe_allow_html=True)
# #
# #
# # def run_cleaning(df: pd.DataFrame):
# #     st.markdown('<div class="section-title">Cleaning Pipeline</div>', unsafe_allow_html=True)
# #
# #     prog = st.progress(0)
# #     status = st.empty()
# #
# #     # Step 1: missing
# #     status.write("🔍 Step 1: Checking missing values...")
# #     missing_count = int(df.isna().sum().sum())
# #     st.info(f"Missing values: {missing_count}")
# #     prog.progress(20)
# #
# #     # Step 2: duplicates
# #     status.write("🔍 Step 2: Checking duplicates...")
# #     duplicates = int(df.duplicated().sum())
# #     st.info(f"Duplicate rows: {duplicates}")
# #     prog.progress(40)
# #
# #     # Step 3: outliers
# #     status.write("🔍 Step 3: Detecting outliers (z-score)...")
# #     num_df = df.select_dtypes(include=["int64", "float64"])
# #     outlier_total = 0
# #     try:
# #         if len(num_df.columns) > 0:
# #             from scipy import stats
# #             z = stats.zscore(num_df.fillna(num_df.mean()))
# #             outlier_total = int((abs(z) > 3).sum().sum())
# #             st.info(f"Outliers detected (|z|>3): {outlier_total}")
# #         else:
# #             st.warning("No numeric columns for outlier detection.")
# #     except Exception:
# #         st.warning("scipy not installed — skipping zscore outlier detection.")
# #     prog.progress(60)
# #
# #     st.markdown('---')
# #     st.subheader("Execute Full Cleaning")
# #
# #     if st.button("Run Full Cleaning", key="run_full_clean"):
# #         status.write("⚙️ Running cleaning pipeline...")
# #         pipeline = CleaningPipeline()
# #         with st.spinner("Cleaning dataset..."):
# #             result = pipeline.run(df)
# #
# #         cleaned_df = result["cleaned_df"]
# #         report = result["report"]
# #
# #         # safe casting helper
# #         def to_int_safe(x):
# #             try:
# #                 return int(x)
# #             except Exception:
# #                 try:
# #                     return int(float(x))
# #                 except Exception:
# #                     return 0
# #
# #         before_missing = to_int_safe(report.get("before_missing", 0))
# #         before_dup = to_int_safe(report.get("before_duplicates", 0))
# #         before_out = to_int_safe(report.get("before_outliers", 0))
# #
# #         after_missing = to_int_safe(report.get("after_missing", 0))
# #         after_dup = to_int_safe(report.get("after_duplicates", 0))
# #         after_out = to_int_safe(report.get("after_outliers", 0))
# #
# #         prog.progress(100)
# #         status.write("✅ Cleaning Completed")
# #         st.success("Dataset cleaned successfully!")
# #
# #         st.markdown('<div class="card"><h4 style="margin:0;color:#073763">Cleaning Results Overview</h4>', unsafe_allow_html=True)
# #         left, right = st.columns(2)
# #         with left:
# #             st.markdown('<div style="margin-bottom:8px"><strong>Before</strong></div>', unsafe_allow_html=True)
# #             a1, a2, a3 = st.columns(3)
# #             a1.markdown(f'<div class="card"><div class="kpi-title">Missing</div><div class="kpi-value">{before_missing}</div></div>', unsafe_allow_html=True)
# #             a2.markdown(f'<div class="card"><div class="kpi-title">Duplicates</div><div class="kpi-value">{before_dup}</div></div>', unsafe_allow_html=True)
# #             a3.markdown(f'<div class="card"><div class="kpi-title">Outliers</div><div class="kpi-value">{before_out}</div></div>', unsafe_allow_html=True)
# #             st.markdown("<div style='margin-top:8px'><strong>Preview (Before)</strong></div>", unsafe_allow_html=True)
# #             st.dataframe(df.head(), use_container_width=True)
# #         with right:
# #             st.markdown('<div style="margin-bottom:8px"><strong>After</strong></div>', unsafe_allow_html=True)
# #             b1, b2, b3 = st.columns(3)
# #             b1.markdown(f'<div class="card"><div class="kpi-title">Missing</div><div class="kpi-value">{after_missing}</div></div>', unsafe_allow_html=True)
# #             b2.markdown(f'<div class="card"><div class="kpi-title">Duplicates</div><div class="kpi-value">{after_dup}</div></div>', unsafe_allow_html=True)
# #             b3.markdown(f'<div class="card"><div class="kpi-title">Outliers</div><div class="kpi-value">{after_out}</div></div>', unsafe_allow_html=True)
# #             st.markdown("<div style='margin-top:8px'><strong>Preview (After)</strong></div>", unsafe_allow_html=True)
# #             st.dataframe(cleaned_df.head(), use_container_width=True)
# #         st.markdown('</div>', unsafe_allow_html=True)
# #
# #         # Download selector (CSV / Pickle)
# #         st.markdown('---')
# #         st.markdown("### 📥 Download Cleaned File")
# #         file_format = st.selectbox("Select file format", ("CSV", "Pickle (.pkl)"), key="download_choice_final")
# #
# #         if file_format == "CSV":
# #             st.download_button(
# #                 label="⬇️ Download as CSV",
# #                 data=cleaned_df.to_csv(index=False).encode("utf-8"),
# #                 file_name="cleaned_dataset.csv",
# #                 mime="text/csv",
# #                 key="download_csv_final"
# #             )
# #         else:
# #             import pickle
# #             pickle_bytes = pickle.dumps(cleaned_df)
# #             st.download_button(
# #                 label="⬇️ Download as Pickle (.pkl)",
# #                 data=pickle_bytes,
# #                 file_name="cleaned_dataset.pkl",
# #                 mime="application/octet-stream",
# #                 key="download_pkl_final"
# #             )
# #     else:
# #         st.info("Click 'Run Full Cleaning' to execute the pipeline.")
# #
# # # -------------------------
# # # Main router: load uploaded and route to selected page
# # # -------------------------
# # if uploaded is None:
# #     st.info("Upload a CSV file to start (use the uploader above).")
# # else:
# #     try:
# #         df = pd.read_csv(uploaded)
# #     except Exception as e:
# #         st.error(f"Failed to read uploaded CSV: {e}")
# #     else:
# #         if page == "Summary":
# #             show_summary(df)
# #         elif page == "EDA":
# #             run_eda(df)
# #         elif page == "Cleaning":
# #             run_cleaning(df)
# #
#
#
#
#
#
#
#
#
#
#
# import sys
# import os
# import streamlit as st
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
#
# # Ensure project root on path so src imports work
# ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# if ROOT_DIR not in sys.path:
#     sys.path.append(ROOT_DIR)
#
# from src.pipeline import CleaningPipeline
#
# # -------------------------
# # Page config
# # -------------------------
# st.set_page_config(page_title="DataPrep – AI Cleaner", layout="wide")
#
# # -------------------------
# # CSS (Soft shadows + Gradient navbar + Sidebar + Cards)
# # -------------------------
# st.markdown(
#     """
#     <style>
#     :root{
#       --primary: #0b6ef6;
#       --accent: #095fc1;
#       --muted: #64748b;
#       --card-bg: #ffffff;
#       --surface: #f6f8fb;
#       --border: #e8eef6;
#       --soft-shadow: 0 8px 22px rgba(0,0,0,0.08);
#     }
#
#     .stApp {
#       background: var(--surface);
#       font-family: "Segoe UI", Roboto, sans-serif;
#     }
#
#     /* ---------- TOP NAV BAR ---------- */
#     .topnav {
#         width: 100%;
#         background: linear-gradient(135deg, #003366, #0b6ef6);
#         padding: 14px 22px;
#         border-radius: 14px;
#         border: 1px solid rgba(255,255,255,0.10);
#         box-shadow: var(--soft-shadow);
#         display: flex;
#         align-items: center;
#         justify-content: space-between;
#         margin-bottom: 18px;
#         margin-top: 10px;
#     }
#
#     .topnav-title {
#         color: white;
#         font-size: 22px;
#         font-weight: 800;
#         letter-spacing: 0.5px;
#     }
#
#     .nav-menu {
#         display: flex;
#         gap: 20px;
#     }
#
#     .nav-link {
#         padding: 6px 12px;
#         color: #e9f3ff;
#         font-weight: 600;
#         font-size: 15px;
#         border-radius: 8px;
#     }
#     .nav-link:hover {
#         background: rgba(255,255,255,0.10);
#     }
#     .nav-active {
#         background: rgba(255,255,255,0.20);
#         color: white;
#         box-shadow: var(--soft-shadow);
#     }
#
#     .search-box {
#         width: 260px;
#         background: rgba(255,255,255,0.15);
#         border: 1px solid rgba(255,255,255,0.25);
#         padding: 8px 12px;
#         border-radius: 10px;
#         color: white;
#     }
#     .search-box::placeholder {
#         color: #d0e4ff;
#     }
#     .notify-btn {
#         background: rgba(255,255,255,0.15);
#         padding: 8px 10px;
#         border-radius: 10px;
#         border: 1px solid rgba(255,255,255,0.25);
#         cursor: pointer;
#         color: white;
#     }
#
#     /* ---------- SIDEBAR ---------- */
#     [data-testid="stSidebar"] {
#       background: #ffffff;
#       padding: 20px;
#       border-right: 1px solid var(--border);
#     }
#
#     .menu-card {
#       background: #f9fbff;
#       padding: 12px;
#       border: 1px solid var(--border);
#       border-radius: 12px;
#       margin-bottom: 10px;
#       font-weight: 600;
#       cursor: pointer;
#       box-shadow: var(--soft-shadow);
#     }
#     .menu-card:hover {
#       background: #eef4ff;
#     }
#
#     .sidebar-section {
#       margin-top: 22px;
#       margin-bottom: 6px;
#       font-size: 12px;
#       font-weight: 700;
#       color: #94a3b8;
#       letter-spacing: 0.5px;
#     }
#
#     /* ---------- CONTENT CARDS ---------- */
#     .card {
#       background: white;
#       border-radius: 14px;
#       padding: 18px;
#       border: 1px solid var(--border);
#       box-shadow: var(--soft-shadow);
#       margin-bottom: 16px;
#     }
#
#     .kpi-title {
#         color: var(--muted);
#         font-size: 13px;
#         font-weight: 700;
#     }
#     .kpi-value {
#         font-size: 26px;
#         font-weight: 800;
#         margin-top: 4px;
#         color: #003366;
#     }
#
#     /* ---------- HERO CARD ---------- */
#     .hero {
#       background: linear-gradient(135deg, #0b6ef6, #003f88);
#       color: white;
#       padding: 26px;
#       border-radius: 18px;
#       box-shadow: var(--soft-shadow);
#       margin-bottom: 20px;
#       position: relative;
#       overflow: hidden;
#     }
#     .hero::before {
#       content: "";
#       position: absolute;
#       right: -80px; top: -80px;
#       width: 260px; height: 260px;
#       background: radial-gradient(circle, rgba(255,255,255,0.25), transparent 70%);
#       border-radius: 50%;
#       opacity: 0.35;
#     }
#     .hero h1 {
#       margin:0;
#       font-size: 32px;
#       font-weight: 800;
#     }
#     .hero p {
#       margin-top: 6px;
#       opacity: 0.85;
#     }
#
#     </style>
#     """,
#     unsafe_allow_html=True,
# )
#
# # -------------------------
# # TOP NAVBAR (visual only)
# # -------------------------
# st.markdown(
#     """
#     <div class="topnav">
#         <div class="topnav-title">DataPrep</div>
#
#         <div class="nav-menu">
#             <span class="nav-link nav-active">Summary</span>
#             <span class="nav-link">EDA</span>
#             <span class="nav-link">Cleaning</span>
#         </div>
#
#         <div style="display:flex;gap:12px;">
#             <input class="search-box" placeholder="Search..." />
#             <div class="notify-btn">🔔</div>
#         </div>
#     </div>
#     """,
#     unsafe_allow_html=True,
# )
#
# # NAV BUTTONS (Actual routing buttons)
# nav1, nav2, nav3 = st.columns([1,1,1])
# with nav1:
#     b_summary = st.button("Summary")
# with nav2:
#     b_eda = st.button("EDA")
# with nav3:
#     b_clean = st.button("Cleaning")
#
# # Sidebar
# st.sidebar.markdown('<div class="sidebar-section">MAIN MENU</div>', unsafe_allow_html=True)
#
# sidebar_summary = st.sidebar.button("Summary")
# sidebar_eda = st.sidebar.button("EDA")
# sidebar_clean = st.sidebar.button("Cleaning")
#
# # Routing state
# if "page" not in st.session_state:
#     st.session_state.page = "Summary"
#
# if b_summary or sidebar_summary:
#     st.session_state.page = "Summary"
# if b_eda or sidebar_eda:
#     st.session_state.page = "EDA"
# if b_clean or sidebar_clean:
#     st.session_state.page = "Cleaning"
#
# page = st.session_state.page
#
# # -------------------------
# # HERO
# # -------------------------
# st.markdown(
#     """
#     <div class="hero">
#         <h1>Welcome to DataPrep</h1>
#         <p>Your AI-powered hub for data cleaning and exploration.</p>
#     </div>
#     """,
#     unsafe_allow_html=True,
# )
#
# # -------------------------
# # Upload
# # -------------------------
# uploaded = st.file_uploader("Upload CSV file", type=["csv"])
#
#
# # ============================
# # SUMMARY
# # ============================
# def show_summary(df):
#
#     st.markdown('<div class="card"><h3>Dataset Summary</h3></div>', unsafe_allow_html=True)
#
#     c1, c2, c3, c4 = st.columns(4)
#     c1.markdown(f'<div class="card"><div class="kpi-title">Rows</div><div class="kpi-value">{df.shape[0]}</div></div>', unsafe_allow_html=True)
#     c2.markdown(f'<div class="card"><div class="kpi-title">Columns</div><div class="kpi-value">{df.shape[1]}</div></div>', unsafe_allow_html=True)
#     c3.markdown(f'<div class="card"><div class="kpi-title">Memory KB</div><div class="kpi-value">{round(df.memory_usage().sum()/1024,2)}</div></div>', unsafe_allow_html=True)
#     c4.markdown(f'<div class="card"><div class="kpi-title">Missing</div><div class="kpi-value">{df.isna().sum().sum()}</div></div>', unsafe_allow_html=True)
#
#     st.markdown("---")
#
#     left, right = st.columns([2,1])
#
#     with left:
#         st.markdown('<div class="card"><h4>Column Types</h4>', unsafe_allow_html=True)
#         dtype_df = pd.DataFrame(df.dtypes, columns=["Type"]).reset_index().rename(columns={"index":"Column"})
#         st.dataframe(dtype_df, use_container_width=True)
#         st.markdown('</div>', unsafe_allow_html=True)
#
#     with right:
#         st.markdown('<div class="card"><h4>Missing Values</h4>', unsafe_allow_html=True)
#         miss = df.isna().sum().reset_index()
#         miss.columns = ["Column", "Missing"]
#         st.dataframe(miss, use_container_width=True)
#         st.markdown('</div>', unsafe_allow_html=True)
#
#
# # ============================
# # EDA
# # ============================
# def run_eda(df):
#     st.markdown('<div class="card"><h3>Exploratory Data Analysis</h3></div>', unsafe_allow_html=True)
#
#     num_df = df.select_dtypes(include=["int64","float64"])
#
#     c1, c2 = st.columns(2)
#
#     with c1:
#         st.markdown('<div class="card"><h4>Missing Heatmap</h4>', unsafe_allow_html=True)
#         fig, ax = plt.subplots(figsize=(5,2.4))
#         sns.heatmap(df.isna(), cbar=False, ax=ax)
#         st.pyplot(fig)
#
#     with c2:
#         st.markdown('<div class="card"><h4>Correlation</h4>', unsafe_allow_html=True)
#         if len(num_df.columns) > 1:
#             fig, ax = plt.subplots(figsize=(5,2.4))
#             sns.heatmap(num_df.corr(), cmap="coolwarm", ax=ax)
#             st.pyplot(fig)
#         else:
#             st.info("Not enough numeric columns.")
#
#     st.markdown("---")
#
#     if len(num_df.columns):
#         d1, d2 = st.columns(2)
#         with d1:
#             st.markdown('<div class="card"><h4>Distribution</h4>', unsafe_allow_html=True)
#             col = st.selectbox("Column", num_df.columns)
#             fig, ax = plt.subplots(figsize=(5,2.4))
#             sns.histplot(df[col], kde=True, ax=ax)
#             st.pyplot(fig)
#
#         with d2:
#             st.markdown('<div class="card"><h4>Boxplot</h4>', unsafe_allow_html=True)
#             col2 = st.selectbox("Box Column", num_df.columns)
#             fig, ax = plt.subplots(figsize=(5,2.4))
#             sns.boxplot(x=df[col2], ax=ax)
#             st.pyplot(fig)
#
#
# # ============================
# # CLEANING
# # ============================
# def run_cleaning(df):
#     st.markdown('<div class="card"><h3>Cleaning Pipeline</h3></div>', unsafe_allow_html=True)
#
#     prog = st.progress(0)
#     status = st.empty()
#
#     # missing
#     status.write("Checking missing values...")
#     missing = df.isna().sum().sum()
#     prog.progress(20)
#
#     # duplicates
#     status.write("Checking duplicates...")
#     duplicates = df.duplicated().sum()
#     prog.progress(40)
#
#     # outliers
#     status.write("Detecting outliers...")
#     num_df = df.select_dtypes(include=["int64","float64"])
#     outliers = 0
#     prog.progress(60)
#
#     st.write("Missing:", missing)
#     st.write("Duplicates:", duplicates)
#     st.write("Outliers:", outliers)
#
#     st.markdown("---")
#
#     if st.button("Run Full Cleaning"):
#         pipeline = CleaningPipeline()
#         result = pipeline.run(df)
#
#         cleaned_df = result["cleaned_df"]
#         report = result["report"]
#
#         before_m = int(report.get("before_missing",0))
#         after_m = int(report.get("after_missing",0))
#
#         before_d = int(report.get("before_duplicates",0))
#         after_d = int(report.get("after_duplicates",0))
#
#         before_o = int(report.get("before_outliers",0))
#         after_o = int(report.get("after_outliers",0))
#
#         prog.progress(100)
#         st.success("Cleaning Completed!")
#
#         left, right = st.columns(2)
#
#         with left:
#             st.markdown('<div class="card"><h4>Before Cleaning</h4>', unsafe_allow_html=True)
#             st.write("Missing:", before_m)
#             st.write("Duplicates:", before_d)
#             st.write("Outliers:", before_o)
#             st.dataframe(df.head())
#             st.markdown('</div>', unsafe_allow_html=True)
#
#         with right:
#             st.markdown('<div class="card"><h4>After Cleaning</h4>', unsafe_allow_html=True)
#             st.write("Missing:", after_m)
#             st.write("Duplicates:", after_d)
#             st.write("Outliers:", after_o)
#             st.dataframe(cleaned_df.head())
#             st.markdown('</div>', unsafe_allow_html=True)
#
#         # Download
#         st.markdown("---")
#         st.subheader("Download Cleaned File")
#
#         fmt = st.selectbox("Format", ["CSV","Pickle"])
#
#         if fmt == "CSV":
#             st.download_button("Download CSV",
#                 cleaned_df.to_csv(index=False).encode("utf-8"),
#                 "cleaned.csv",
#                 "text/csv")
#         else:
#             import pickle
#             st.download_button("Download PKL",
#                 pickle.dumps(cleaned_df),
#                 "cleaned.pkl",
#                 "application/octet-stream")
#
#
# # -------------------------
# # MAIN ROUTING
# # -------------------------
# if uploaded is None:
#     st.info("Upload a CSV to begin.")
# else:
#     df = pd.read_csv(uploaded)
#
#     if page == "Summary":
#         show_summary(df)
#     elif page == "EDA":
#         run_eda(df)
#     elif page == "Cleaning":
#         run_cleaning(df)
#
#
#
#
#
#
#
#
#
#





#
# # ui/app.py
# """
# DataPrep — Dashboard-style UI with:
# - JavaScript clickable top navbar (Summary / EDA / Cleaning)
#   (JS sets window.location.search='?page=summary' which reloads the app;
#    Python reads st.query_params to route)
# - Left sidebar styled as an off-white rectangular card
# - Soft shadows on all cards
# - Backend logic (CleaningPipeline) unchanged
# - Download cleaned dataset as CSV / Pickle
# """
#
# import os
# import sys
# import streamlit as st
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
#
# # Ensure project root so src imports work
# ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# if ROOT_DIR not in sys.path:
#     sys.path.append(ROOT_DIR)
#
# from src.pipeline import CleaningPipeline
#
# # Page config
# st.set_page_config(page_title="DataPrep – AI Cleaner", layout="wide", initial_sidebar_state="expanded")
#
# # -------------------------
# # CSS (soft shadow + off-white sidebar card)
# # -------------------------
# st.markdown(
#     """
#     <style>
#     :root{
#       --primary: #0b6ef6;
#       --accent: #095fc1;
#       --muted: #64748b;
#       --card-bg: #ffffff;
#       --surface: #f6f8fb;
#       --border: #e8eef6;
#       --soft-shadow: 0 8px 26px rgba(11,110,246,0.08);
#       --sidebar-bg: #fbfdff;
#     }
#
#     /* Hide default Streamlit header (top black bar) */
#     header[data-testid="stHeader"] { display: none; }
#
#     .stApp{
#       background: var(--surface);
#       font-family: "Inter", "Segoe UI", Roboto, "Helvetica Neue", Arial;
#       color: #0f172a;
#     }
#
#     /* Top navbar */
#     .topnav {
#         width: 100%;
#         background: linear-gradient(135deg,#002c6d,#0056c9);
#         padding: 8px 16px;
#         border-radius: 12px;
#         border: 1px solid rgba(255,255,255,0.06);
#         box-shadow: var(--soft-shadow);
#         display: flex;
#         align-items: center;
#         justify-content: space-between;
#         margin-bottom: 18px;
#     }
#     .brand-title { color:#fff; font-weight:800; font-size:18px; margin:0; padding-left:8px; }
#     .nav-links { display:flex; gap:12px; align-items:center; }
#     .nav-link {
#         color: rgba(235,245,255,0.95);
#         font-weight:700;
#         padding:6px 12px;
#         border-radius:8px;
#         cursor:pointer;
#         user-select:none;
#     }
#     .nav-link.active { background: rgba(255,255,255,0.12); color:#fff; box-shadow: var(--soft-shadow); }
#
#     .search-box { width:260px; padding:6px 10px; border-radius:10px; border:1px solid rgba(255,255,255,0.12); background: rgba(255,255,255,0.06); color:#eaf6ff; }
#     .notify { padding:6px 8px; border-radius:8px; background: rgba(255,255,255,0.12); color:white; }
#
#     /* Sidebar off-white card look */
#     [data-testid="stSidebar"] {
#       background: var(--sidebar-bg);
#       padding: 22px;
#       border-right: 1px solid var(--border);
#       width: 300px !important;
#     }
#     .sidebar-card {
#       background: #ffffff;
#       border-radius: 14px;
#       padding: 14px;
#       border: 1px solid var(--border);
#       box-shadow: var(--soft-shadow);
#       margin-bottom: 14px;
#       display:flex; gap:12px; align-items:center;
#     }
#     .brand-square { width:56px; height:56px; border-radius:10px; background:#eef6ff; flex-shrink:0; }
#     .brand-name { font-weight:800; color:#073763; font-size:18px; margin:0; }
#     .brand-sub { font-size:12px; color:var(--muted); margin:0; }
#
#     .sidebar-section { font-size:12px; color:#94a3b8; margin-top:16px; margin-bottom:8px; font-weight:700; }
#
#     /* Make sidebar menu buttons look like off-white cards */
#     [data-testid="stSidebar"] .stButton > button {
#       width: 100%;
#       text-align: left;
#       padding: 10px 12px;
#       border-radius: 12px;
#       border: 1px solid var(--border);
#       background: #fbfdff;
#       color: #0b2233;
#       font-weight:700;
#       box-shadow: var(--soft-shadow);
#       margin-bottom: 8px;
#     }
#     [data-testid="stSidebar"] .stButton > button:hover { background:#eef4ff; }
#
#     .feature-item {
#       display:flex; align-items:center; gap:10px;
#       padding:9px 12px; border-radius:12px; border:1px solid var(--border);
#       margin-bottom:8px; background:#fff; box-shadow:var(--soft-shadow);
#       color:#374151;
#     }
#
#     /* Card style for content */
#     .card {
#       background: var(--card-bg);
#       border-radius:12px;
#       padding:16px;
#       border:1px solid var(--border);
#       box-shadow: var(--soft-shadow);
#       margin-bottom:16px;
#     }
#     .kpi-title { color:var(--muted); font-weight:700; font-size:13px; }
#     .kpi-value { color:#073763; font-weight:800; font-size:26px; margin-top:6px; }
#
#     /* Hero */
#     .hero {
#       background: linear-gradient(135deg,#0b6ef6,#003f88);
#       color:white;
#       padding:22px;
#       border-radius:14px;
#       box-shadow: var(--soft-shadow);
#       margin-bottom:20px;
#     }
#     .hero h1 { margin:0; font-size:28px; font-weight:800; }
#     .hero p { margin-top:8px; opacity:0.95; }
#
#     /* smaller dataframe radius */
#     .stDataFrame > div:first-child { border-radius:10px; }
#
#     </style>
#     """,
#     unsafe_allow_html=True,
# )
#
# # -------------------------
# # Read page from query params (if present)
# # -------------------------
# params = st.query_params
# page_param = params.get("page", [""])[0].lower() if params.get("page") else ""
# if page_param in ("summary", "eda", "cleaning", "home"):
#     # store as TitleCase
#     st.session_state.page = "Summary" if page_param in ("", "home", "summary") else page_param.capitalize()
# else:
#     if "page" not in st.session_state:
#         st.session_state.page = "Summary"
#
# # -------------------------
# # Top navbar HTML (JS clickable)
# # -------------------------
# # JS sets window.location.search to '?page=summary' which reloads the page and lets st.query_params pick it up.
# st.markdown(
#     f"""
#     <div class="topnav">
#       <div style="display:flex;align-items:center;gap:18px;">
#         <div class="brand-title">DataPrep</div>
#         <div class="nav-links">
#           <div class="nav-link {'active' if st.session_state.page=='Summary' else ''}" onclick="window.location.search='?page=summary'">Summary</div>
#           <div class="nav-link {'active' if st.session_state.page=='EDA' else ''}" onclick="window.location.search='?page=eda'">EDA</div>
#           <div class="nav-link {'active' if st.session_state.page=='Cleaning' else ''}" onclick="window.location.search='?page=cleaning'">Cleaning</div>
#         </div>
#       </div>
#
#       <div style="display:flex;align-items:center;gap:12px;">
#         <input class="search-box" placeholder="Search..." />
#         <div class="notify">🔔</div>
#       </div>
#     </div>
#     """,
#     unsafe_allow_html=True,
# )
#
# # -------------------------
# # Actual smaller invisible controls (left as backup)
# # -------------------------
# # We no longer display duplicate black buttons — navigation is via JS + query param.
# # But keep small Streamlit buttons in the layout for keyboard navigation (optional)
# # placed in a collapsed column so they are not visually prominent.
# c1, c2 = st.columns([1, 9])
# with c1:
#     st.write("")  # spacer
# with c2:
#     st.write("")  # main canvas spacer
#
# # -------------------------
# # Sidebar content (off-white rectangular card + menu)
# # -------------------------
# with st.sidebar:
#     # Top collapse toggle and info (we keep small toggle)
#     cols = st.columns([1, 9])
#     with cols[0]:
#         if st.button("☰", key="toggle_sidebar_small"):
#             # small visual toggle - we won't implement collapse full behavior here
#             st.session_state["sidebar_toggled"] = not st.session_state.get("sidebar_toggled", False)
#     with cols[1]:
#         st.write("")
#
#     # Off-white rectangular brand card
#     st.markdown(
#         """
#         <div class="sidebar-card">
#           <div class="brand-square"></div>
#           <div>
#             <div class="brand-name">DataPrep</div>
#             <div class="brand-sub">Prepare, clean & inspect data</div>
#           </div>
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )
#
#     st.markdown('<div class="sidebar-section">MAIN MENU</div>', unsafe_allow_html=True)
#
#     # Sidebar menu buttons (styled as off-white card-buttons)
#     if st.button("Summary", key="sb_summary"):
#         # update URL to keep navigation consistent (this reloads the page)
#         st.experimental_set_query_params(page="summary")
#     if st.button("EDA", key="sb_eda"):
#         st.experimental_set_query_params(page="eda")
#     if st.button("Cleaning", key="sb_clean"):
#         st.experimental_set_query_params(page="cleaning")
#
#     st.markdown('<div class="sidebar-section">FEATURES</div>', unsafe_allow_html=True)
#     st.markdown('<div class="feature-item"><div style="width:10px;height:10px;border-radius:50%;background:#1d4ed8"></div> Data Analysis</div>', unsafe_allow_html=True)
#     st.markdown('<div class="feature-item"><div style="width:10px;height:10px;border-radius:50%;background:#059669"></div> ML Preparation</div>', unsafe_allow_html=True)
#     st.markdown('<div class="feature-item"><div style="width:10px;height:10px;border-radius:50%;background:#f59e0b"></div> Outlier Report</div>', unsafe_allow_html=True)
#     st.markdown('<div class="feature-item"><div style="width:10px;height:10px;border-radius:50%;background:#7c3aed"></div> Profiling</div>', unsafe_allow_html=True)
#
# # -------------------------
# # Hero and uploader
# # -------------------------
# st.markdown(
#     """
#     <div class="hero">
#       <h1>Welcome to DataPrep</h1>
#       <p>Your AI-powered hub for data cleaning and exploratory analysis.</p>
#     </div>
#     """,
#     unsafe_allow_html=True,
# )
#
# uploaded = st.file_uploader("Upload CSV file", type=["csv"])
#
# # -------------------------
# # ---------- FUNCTIONAL PAGES (backend logic preserved) ----------
# # -------------------------
# def show_summary(df: pd.DataFrame):
#     st.markdown('<div class="card"><h3>Dataset Summary</h3></div>', unsafe_allow_html=True)
#
#     # KPI row
#     k1, k2, k3, k4 = st.columns(4)
#     k1.markdown(f'<div class="card"><div class="kpi-title">Rows</div><div class="kpi-value">{df.shape[0]}</div></div>', unsafe_allow_html=True)
#     k2.markdown(f'<div class="card"><div class="kpi-title">Columns</div><div class="kpi-value">{df.shape[1]}</div></div>', unsafe_allow_html=True)
#     mem_kb = round(df.memory_usage(deep=True).sum() / 1024, 2)
#     k3.markdown(f'<div class="card"><div class="kpi-title">Memory (KB)</div><div class="kpi-value">{mem_kb}</div></div>', unsafe_allow_html=True)
#     miss_total = int(df.isna().sum().sum())
#     k4.markdown(f'<div class="card"><div class="kpi-title">Missing</div><div class="kpi-value">{miss_total}</div></div>', unsafe_allow_html=True)
#
#     st.markdown('---')
#     left, right = st.columns([2,1])
#     with left:
#         st.markdown('<div class="card"><h4>Column Types</h4>', unsafe_allow_html=True)
#         dtype_df = pd.DataFrame(df.dtypes, columns=["Type"]).reset_index().rename(columns={"index":"Column"})
#         st.dataframe(dtype_df, use_container_width=True)
#         st.markdown('</div>', unsafe_allow_html=True)
#     with right:
#         st.markdown('<div class="card"><h4>Top Missing</h4>', unsafe_allow_html=True)
#         miss_df = df.isna().sum().sort_values(ascending=False).reset_index()
#         miss_df.columns = ["Column", "Missing"]
#         st.dataframe(miss_df.head(8), use_container_width=True)
#         st.markdown('</div>', unsafe_allow_html=True)
#
#     st.markdown('---')
#     r1, r2 = st.columns([2,1])
#     with r1:
#         st.markdown('<div class="card"><h4>Unique Values</h4>', unsafe_allow_html=True)
#         uniq = df.nunique().reset_index()
#         uniq.columns = ["Column", "Unique"]
#         st.dataframe(uniq.head(12), use_container_width=True)
#         st.markdown('</div>', unsafe_allow_html=True)
#     with r2:
#         st.markdown('<div class="card"><h4>Preview</h4>', unsafe_allow_html=True)
#         st.dataframe(df.head(6), use_container_width=True)
#         st.markdown('</div>', unsafe_allow_html=True)
#
#
# def run_eda(df: pd.DataFrame):
#     st.markdown('<div class="card"><h3>Exploratory Data Analysis</h3></div>', unsafe_allow_html=True)
#
#     num_df = df.select_dtypes(include=["int64", "float64"])
#
#     c1, c2 = st.columns(2)
#     with c1:
#         st.markdown('<div class="card"><h4>Missing Heatmap</h4>', unsafe_allow_html=True)
#         fig, ax = plt.subplots(figsize=(6, 3))
#         sns.heatmap(df.isna(), cbar=False, ax=ax)
#         ax.set_xlabel(""); ax.set_ylabel("")
#         st.pyplot(fig)
#         st.markdown('</div>', unsafe_allow_html=True)
#     with c2:
#         st.markdown('<div class="card"><h4>Correlation</h4>', unsafe_allow_html=True)
#         if num_df.shape[1] > 1:
#             fig, ax = plt.subplots(figsize=(6, 3))
#             sns.heatmap(num_df.corr(), cmap="coolwarm", ax=ax)
#             st.pyplot(fig)
#         else:
#             st.info("Not enough numeric columns for correlation.")
#         st.markdown('</div>', unsafe_allow_html=True)
#
#     st.markdown('---')
#     if len(num_df.columns) > 0:
#         d1, d2 = st.columns(2)
#         with d1:
#             st.markdown('<div class="card"><h4>Distribution</h4>', unsafe_allow_html=True)
#             col_sel = st.selectbox("Distribution column", num_df.columns, key="eda_dist")
#             fig, ax = plt.subplots(figsize=(6, 3))
#             sns.histplot(df[col_sel].dropna(), kde=True, ax=ax)
#             st.pyplot(fig)
#             st.markdown('</div>', unsafe_allow_html=True)
#         with d2:
#             st.markdown('<div class="card"><h4>Boxplot</h4>', unsafe_allow_html=True)
#             col_box = st.selectbox("Boxplot column", num_df.columns, key="eda_box")
#             fig, ax = plt.subplots(figsize=(6, 3))
#             sns.boxplot(x=df[col_box].dropna(), ax=ax)
#             st.pyplot(fig)
#             st.markdown('</div>', unsafe_allow_html=True)
#     else:
#         st.info("No numeric columns available.")
#
#
# def run_cleaning(df: pd.DataFrame):
#     st.markdown('<div class="card"><h3>Cleaning Pipeline</h3></div>', unsafe_allow_html=True)
#
#     prog = st.progress(0)
#     status = st.empty()
#
#     # Step 1
#     status.write("🔍 Step 1: Checking missing values...")
#     missing_count = int(df.isna().sum().sum())
#     st.info(f"Missing values: {missing_count}")
#     prog.progress(20)
#
#     # Step 2
#     status.write("🔍 Step 2: Checking duplicates...")
#     duplicates = int(df.duplicated().sum())
#     st.info(f"Duplicate rows: {duplicates}")
#     prog.progress(40)
#
#     # Step 3
#     status.write("🔍 Step 3: Detecting outliers (z-score)...")
#     num_df = df.select_dtypes(include=["int64", "float64"])
#     outlier_total = 0
#     try:
#         if len(num_df.columns) > 0:
#             from scipy import stats
#             z = stats.zscore(num_df.fillna(num_df.mean()))
#             outlier_total = int((abs(z) > 3).sum().sum())
#             st.info(f"Outliers detected (|z|>3): {outlier_total}")
#         else:
#             st.warning("No numeric columns for outlier detection.")
#     except Exception:
#         st.warning("scipy not installed — skipping zscore outlier detection.")
#     prog.progress(60)
#
#     st.markdown('---')
#     st.subheader("Execute Full Cleaning")
#
#     if st.button("Run Full Cleaning", key="run_full_clean"):
#         status.write("⚙️ Running cleaning pipeline...")
#         pipeline = CleaningPipeline()
#         with st.spinner("Cleaning dataset..."):
#             result = pipeline.run(df)
#
#         cleaned_df = result.get("cleaned_df", df.copy())
#         report = result.get("report", {})
#
#         def to_int_safe(x):
#             try:
#                 return int(x)
#             except Exception:
#                 try:
#                     return int(float(x))
#                 except Exception:
#                     return 0
#
#         before_missing = to_int_safe(report.get("before_missing", 0))
#         before_dup = to_int_safe(report.get("before_duplicates", 0))
#         before_out = to_int_safe(report.get("before_outliers", 0))
#
#         after_missing = to_int_safe(report.get("after_missing", 0))
#         after_dup = to_int_safe(report.get("after_duplicates", 0))
#         after_out = to_int_safe(report.get("after_outliers", 0))
#
#         prog.progress(100)
#         status.write("✅ Cleaning Completed")
#         st.success("Dataset cleaned successfully!")
#
#         st.markdown('<div class="card"><h4>Cleaning Results Overview</h4></div>', unsafe_allow_html=True)
#
#         left, right = st.columns(2)
#         with left:
#             st.markdown('<div class="card"><strong>Before</strong></div>', unsafe_allow_html=True)
#             a1, a2, a3 = st.columns(3)
#             a1.markdown(f'<div class="card"><div class="kpi-title">Missing</div><div class="kpi-value">{before_missing}</div></div>', unsafe_allow_html=True)
#             a2.markdown(f'<div class="card"><div class="kpi-title">Duplicates</div><div class="kpi-value">{before_dup}</div></div>', unsafe_allow_html=True)
#             a3.markdown(f'<div class="card"><div class="kpi-title">Outliers</div><div class="kpi-value">{before_out}</div></div>', unsafe_allow_html=True)
#             st.markdown("<div style='margin-top:8px'><strong>Preview (Before)</strong></div>", unsafe_allow_html=True)
#             st.dataframe(df.head(), use_container_width=True)
#         with right:
#             st.markdown('<div class="card"><strong>After</strong></div>', unsafe_allow_html=True)
#             b1, b2, b3 = st.columns(3)
#             b1.markdown(f'<div class="card"><div class="kpi-title">Missing</div><div class="kpi-value">{after_missing}</div></div>', unsafe_allow_html=True)
#             b2.markdown(f'<div class="card"><div class="kpi-title">Duplicates</div><div class="kpi-value">{after_dup}</div></div>', unsafe_allow_html=True)
#             b3.markdown(f'<div class="card"><div class="kpi-title">Outliers</div><div class="kpi-value">{after_out}</div></div>', unsafe_allow_html=True)
#             st.markdown("<div style='margin-top:8px'><strong>Preview (After)</strong></div>", unsafe_allow_html=True)
#             st.dataframe(cleaned_df.head(), use_container_width=True)
#
#         st.markdown('---')
#         st.markdown("### 📥 Download Cleaned File")
#         file_format = st.selectbox("Select file format", ("CSV", "Pickle (.pkl)"), key="download_choice_final")
#
#         if file_format == "CSV":
#             st.download_button(
#                 label="⬇️ Download as CSV",
#                 data=cleaned_df.to_csv(index=False).encode("utf-8"),
#                 file_name="cleaned_dataset.csv",
#                 mime="text/csv",
#                 key="download_csv_final"
#             )
#         else:
#             import pickle
#             pickle_bytes = pickle.dumps(cleaned_df)
#             st.download_button(
#                 label="⬇️ Download as Pickle (.pkl)",
#                 data=pickle_bytes,
#                 file_name="cleaned_dataset.pkl",
#                 mime="application/octet-stream",
#                 key="download_pkl_final"
#             )
#     else:
#         st.info("Click 'Run Full Cleaning' to execute the pipeline.")
#
# # -------------------------
# # Router: load uploaded CSV and show page
# # -------------------------
# if uploaded is None:
#     st.info("Upload a CSV file to start (use the uploader above).")
# else:
#     try:
#         df = pd.read_csv(uploaded)
#     except Exception as e:
#         st.error(f"Failed to read uploaded CSV: {e}")
#     else:
#         page = st.session_state.get("page", "Summary").lower()
#         if page in ("home", "summary"):
#             show_summary(df)
#         elif page == "eda":
#             run_eda(df)
#         elif page == "cleaning":
#             run_cleaning(df)
#         else:
#             show_summary(df)



# ui/app.py
"""
DataPrep — Dashboard-style UI with:
- JavaScript clickable top navbar (Summary / EDA / Cleaning)
- Left sidebar styled as an off-white rectangular card
- Soft shadows on all cards
- Backend logic (CleaningPipeline) unchanged
- Download cleaned dataset as CSV / Pickle
"""

import os
import sys
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Ensure project root so src imports work
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from src.pipeline import CleaningPipeline

# Page config
st.set_page_config(page_title="DataPrep – AI Cleaner", layout="wide", initial_sidebar_state="expanded")

# -------------------------
# CSS (soft shadow + off-white sidebar card)
# -------------------------
st.markdown(
    """
    <style>
    :root{
      --primary: #0b6ef6;
      --accent: #095fc1;
      --muted: #64748b;
      --card-bg: #ffffff;
      --surface: #f6f8fb;
      --border: #e8eef6;
      --soft-shadow: 0 8px 26px rgba(11,110,246,0.08);
      --sidebar-bg: #fbfdff;
    }

    /* Hide default Streamlit header (top black bar) */
    header[data-testid="stHeader"] { display: none; }

    .stApp{
      background: var(--surface);
      font-family: "Inter", "Segoe UI", Roboto, "Helvetica Neue", Arial;
      color: #0f172a;
    }

    /* Top navbar */
    .topnav {
        width: 100%;
        background: linear-gradient(135deg,#002c6d,#0056c9);
        padding: 8px 16px;
        border-radius: 12px;
        border: 1px solid rgba(255,255,255,0.06);
        box-shadow: var(--soft-shadow);
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 18px;
    }
    .brand-title { color:#fff; font-weight:800; font-size:18px; margin:0; padding-left:8px; }
    .nav-links { display:flex; gap:12px; align-items:center; }
    .nav-link {
        color: rgba(235,245,255,0.95);
        font-weight:700;
        padding:6px 12px;
        border-radius:8px;
        cursor:pointer;
        user-select:none;
    }
    .nav-link.active { background: rgba(255,255,255,0.12); color:#fff; box-shadow: var(--soft-shadow); }

    .search-box { width:260px; padding:6px 10px; border-radius:10px; border:1px solid rgba(255,255,255,0.12); background: rgba(255,255,255,0.06); color:#eaf6ff; }
    .notify { padding:6px 8px; border-radius:8px; background: rgba(255,255,255,0.12); color:white; }

    /* Sidebar off-white card look */
    [data-testid="stSidebar"] {
      background: var(--sidebar-bg);
      padding: 22px;
      border-right: 1px solid var(--border);
      width: 300px !important;
    }
    .sidebar-card {
      background: #ffffff;
      border-radius: 14px;
      padding: 14px;
      border: 1px solid var(--border);
      box-shadow: var(--soft-shadow);
      margin-bottom: 14px;
      display:flex; gap:12px; align-items:center;
    }
    .brand-square { width:56px; height:56px; border-radius:10px; background:#eef6ff; flex-shrink:0; }
    .brand-name { font-weight:800; color:#073763; font-size:18px; margin:0; }
    .brand-sub { font-size:12px; color:var(--muted); margin:0; }

    .sidebar-section { font-size:12px; color:#94a3b8; margin-top:16px; margin-bottom:8px; font-weight:700; }

    /* Make sidebar menu buttons look like off-white cards */
    [data-testid="stSidebar"] .stButton > button {
      width: 100%;
      text-align: left;
      padding: 10px 12px;
      border-radius: 12px;
      border: 1px solid var(--border);
      background: #fbfdff;
      color: #0b2233;
      font-weight:700;
      box-shadow: var(--soft-shadow);
      margin-bottom: 8px;
    }
    [data-testid="stSidebar"] .stButton > button:hover { background:#eef4ff; }

    .feature-item {
      display:flex; align-items:center; gap:10px;
      padding:9px 12px; border-radius:12px; border:1px solid var(--border);
      margin-bottom:8px; background:#fff; box-shadow:var(--soft-shadow);
      color:#374151;
    }

    /* Card style for content */
    .card {
      background: var(--card-bg);
      border-radius:12px;
      padding:16px;
      border:1px solid var(--border);
      box-shadow: var(--soft-shadow);
      margin-bottom:16px;
    }
    .kpi-title { color:var(--muted); font-weight:700; font-size:13px; }
    .kpi-value { color:#073763; font-weight:800; font-size:26px; margin-top:6px; }

    /* Hero */
    .hero {
      background: linear-gradient(135deg,#0b6ef6,#003f88);
      color:white;
      padding:22px;
      border-radius:14px;
      box-shadow: var(--soft-shadow);
      margin-bottom:20px;
    }
    .hero h1 { margin:0; font-size:28px; font-weight:800; }
    .hero p { margin-top:8px; opacity:0.95; }

    /* smaller dataframe radius */
    .stDataFrame > div:first-child { border-radius:10px; }

    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------------
# Read page from query params (if present)
# -------------------------
# Keep using st.query_params here (OK) but DO NOT use st.experimental_set_query_params anywhere.
params = st.query_params
page_param = params.get("page", [""])[0].lower() if params.get("page") else ""
if page_param in ("summary", "eda", "cleaning", "home"):
    # store as TitleCase
    # if page_param is empty or "home" -> default to Summary
    if page_param in ("", "home", "summary"):
        st.session_state.page = "Summary"
    elif page_param == "eda":
        st.session_state.page = "EDA"
    elif page_param == "cleaning":
        st.session_state.page = "Cleaning"
else:
    if "page" not in st.session_state:
        st.session_state.page = "Summary"

# -------------------------
# Top navbar HTML (JS clickable)
# -------------------------
# JS sets window.location.search to '?page=...' which reloads the page and lets st.query_params pick it up.
st.markdown(
    f"""
    <div class="topnav">
      <div style="display:flex;align-items:center;gap:18px;">
        <div class="brand-title">DataPrep</div>
        <div class="nav-links">
          <div class="nav-link {'active' if st.session_state.get('page','Summary')=='Summary' else ''}" onclick="window.location.search='?page=summary'">Summary</div>
          <div class="nav-link {'active' if st.session_state.get('page','Summary')=='EDA' else ''}" onclick="window.location.search='?page=eda'">EDA</div>
          <div class="nav-link {'active' if st.session_state.get('page','Summary')=='Cleaning' else ''}" onclick="window.location.search='?page=cleaning'">Cleaning</div>
        </div>
      </div>

      <div style="display:flex;align-items:center;gap:12px;">
        <input class="search-box" placeholder="Search..." />
        <div class="notify">🔔</div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# -------------------------
# Actual smaller invisible controls (left as backup)
# -------------------------
c1, c2 = st.columns([1, 9])
with c1:
    st.write("")  # spacer
with c2:
    st.write("")  # main canvas spacer

# -------------------------
# Sidebar content (off-white rectangular card + menu)
# -------------------------
with st.sidebar:
    # Top collapse toggle and info (we keep small toggle)
    cols = st.columns([1, 9])
    with cols[0]:
        if st.button("☰", key="toggle_sidebar_small"):
            st.session_state["sidebar_toggled"] = not st.session_state.get("sidebar_toggled", False)
    with cols[1]:
        st.write("")

    # Off-white rectangular brand card
    st.markdown(
        """
        <div class="sidebar-card">
          <div class="brand-square"></div>
          <div>
            <div class="brand-name">DataPrep</div>
            <div class="brand-sub">Prepare, clean & inspect data</div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="sidebar-section">MAIN MENU</div>', unsafe_allow_html=True)

    # Sidebar menu buttons (styled as off-white card-buttons)
    # --- important: DO NOT use experimental_set_query_params here (that caused errors).
    if st.button("Summary", key="sb_summary"):
        st.session_state.page = "Summary"
    if st.button("EDA", key="sb_eda"):
        st.session_state.page = "EDA"
    if st.button("Cleaning", key="sb_clean"):
        st.session_state.page = "Cleaning"

    st.markdown('<div class="sidebar-section">FEATURES</div>', unsafe_allow_html=True)
    st.markdown('<div class="feature-item"><div style="width:10px;height:10px;border-radius:50%;background:#1d4ed8"></div> Data Analysis</div>', unsafe_allow_html=True)
    st.markdown('<div class="feature-item"><div style="width:10px;height:10px;border-radius:50%;background:#059669"></div> ML Preparation</div>', unsafe_allow_html=True)
    st.markdown('<div class="feature-item"><div style="width:10px;height:10px;border-radius:50%;background:#f59e0b"></div> Outlier Report</div>', unsafe_allow_html=True)
    st.markdown('<div class="feature-item"><div style="width:10px;height:10px;border-radius:50%;background:#7c3aed"></div> Profiling</div>', unsafe_allow_html=True)

# -------------------------
# Hero and uploader
# -------------------------
st.markdown(
    """
    <div class="hero">
      <h1>Welcome to DataPrep</h1>
      <p>Your AI-powered hub for data cleaning and exploratory analysis.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

uploaded = st.file_uploader("Upload CSV file", type=["csv"])

# -------------------------
# ---------- FUNCTIONAL PAGES (backend logic preserved) ----------
# -------------------------
def show_summary(df: pd.DataFrame):
    st.markdown('<div class="card"><h3>Dataset Summary</h3></div>', unsafe_allow_html=True)

    # KPI row
    k1, k2, k3, k4 = st.columns(4)
    k1.markdown(f'<div class="card"><div class="kpi-title">Rows</div><div class="kpi-value">{df.shape[0]}</div></div>', unsafe_allow_html=True)
    k2.markdown(f'<div class="card"><div class="kpi-title">Columns</div><div class="kpi-value">{df.shape[1]}</div></div>', unsafe_allow_html=True)
    mem_kb = round(df.memory_usage(deep=True).sum() / 1024, 2)
    k3.markdown(f'<div class="card"><div class="kpi-title">Memory (KB)</div><div class="kpi-value">{mem_kb}</div></div>', unsafe_allow_html=True)
    miss_total = int(df.isna().sum().sum())
    k4.markdown(f'<div class="card"><div class="kpi-title">Missing</div><div class="kpi-value">{miss_total}</div></div>', unsafe_allow_html=True)

    st.markdown('---')
    left, right = st.columns([2,1])
    with left:
        st.markdown('<div class="card"><h4>Column Types</h4>', unsafe_allow_html=True)
        dtype_df = pd.DataFrame(df.dtypes, columns=["Type"]).reset_index().rename(columns={"index":"Column"})
        st.dataframe(dtype_df, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with right:
        st.markdown('<div class="card"><h4>Top Missing</h4>', unsafe_allow_html=True)
        miss_df = df.isna().sum().sort_values(ascending=False).reset_index()
        miss_df.columns = ["Column", "Missing"]
        st.dataframe(miss_df.head(8), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('---')
    r1, r2 = st.columns([2,1])
    with r1:
        st.markdown('<div class="card"><h4>Unique Values</h4>', unsafe_allow_html=True)
        uniq = df.nunique().reset_index()
        uniq.columns = ["Column", "Unique"]
        st.dataframe(uniq.head(12), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with r2:
        st.markdown('<div class="card"><h4>Preview</h4>', unsafe_allow_html=True)
        st.dataframe(df.head(6), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)


def run_eda(df: pd.DataFrame):
    st.markdown('<div class="card"><h3>Exploratory Data Analysis</h3></div>', unsafe_allow_html=True)

    num_df = df.select_dtypes(include=["int64", "float64"])

    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="card"><h4>Missing Heatmap</h4>', unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(6, 3))
        sns.heatmap(df.isna(), cbar=False, ax=ax)
        ax.set_xlabel(""); ax.set_ylabel("")
        st.pyplot(fig)
        st.markdown('</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="card"><h4>Correlation</h4>', unsafe_allow_html=True)
        if num_df.shape[1] > 1:
            fig, ax = plt.subplots(figsize=(6, 3))
            sns.heatmap(num_df.corr(), cmap="coolwarm", ax=ax)
            st.pyplot(fig)
        else:
            st.info("Not enough numeric columns for correlation.")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('---')
    if len(num_df.columns) > 0:
        d1, d2 = st.columns(2)
        with d1:
            st.markdown('<div class="card"><h4>Distribution</h4>', unsafe_allow_html=True)
            col_sel = st.selectbox("Distribution column", num_df.columns, key="eda_dist")
            fig, ax = plt.subplots(figsize=(6, 3))
            sns.histplot(df[col_sel].dropna(), kde=True, ax=ax)
            st.pyplot(fig)
            st.markdown('</div>', unsafe_allow_html=True)
        with d2:
            st.markdown('<div class="card"><h4>Boxplot</h4>', unsafe_allow_html=True)
            col_box = st.selectbox("Boxplot column", num_df.columns, key="eda_box")
            fig, ax = plt.subplots(figsize=(6, 3))
            sns.boxplot(x=df[col_box].dropna(), ax=ax)
            st.pyplot(fig)
            st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info("No numeric columns available.")


def run_cleaning(df: pd.DataFrame):
    st.markdown('<div class="card"><h3>Cleaning Pipeline</h3></div>', unsafe_allow_html=True)

    prog = st.progress(0)
    status = st.empty()

    # Step 1
    status.write("🔍 Step 1: Checking missing values...")
    missing_count = int(df.isna().sum().sum())
    st.info(f"Missing values: {missing_count}")
    prog.progress(20)

    # Step 2
    status.write("🔍 Step 2: Checking duplicates...")
    duplicates = int(df.duplicated().sum())
    st.info(f"Duplicate rows: {duplicates}")
    prog.progress(40)

    # Step 3
    status.write("🔍 Step 3: Detecting outliers (z-score)...")
    num_df = df.select_dtypes(include=["int64", "float64"])
    outlier_total = 0
    try:
        if len(num_df.columns) > 0:
            from scipy import stats
            z = stats.zscore(num_df.fillna(num_df.mean()))
            outlier_total = int((abs(z) > 3).sum().sum())
            st.info(f"Outliers detected (|z|>3): {outlier_total}")
        else:
            st.warning("No numeric columns for outlier detection.")
    except Exception:
        st.warning("scipy not installed — skipping zscore outlier detection.")
    prog.progress(60)

    st.markdown('---')
    st.subheader("Execute Full Cleaning")

    if st.button("Run Full Cleaning", key="run_full_clean"):
        status.write("⚙️ Running cleaning pipeline...")
        pipeline = CleaningPipeline()
        with st.spinner("Cleaning dataset..."):
            result = pipeline.run(df)

        cleaned_df = result.get("cleaned_df", df.copy())
        report = result.get("report", {})

        def to_int_safe(x):
            try:
                return int(x)
            except Exception:
                try:
                    return int(float(x))
                except Exception:
                    return 0

        before_missing = to_int_safe(report.get("before_missing", 0))
        before_dup = to_int_safe(report.get("before_duplicates", 0))
        before_out = to_int_safe(report.get("before_outliers", 0))

        after_missing = to_int_safe(report.get("after_missing", 0))
        after_dup = to_int_safe(report.get("after_duplicates", 0))
        after_out = to_int_safe(report.get("after_outliers", 0))

        prog.progress(100)
        status.write("✅ Cleaning Completed")
        st.success("Dataset cleaned successfully!")

        st.markdown('<div class="card"><h4>Cleaning Results Overview</h4></div>', unsafe_allow_html=True)

        left, right = st.columns(2)
        with left:
            st.markdown('<div class="card"><strong>Before</strong></div>', unsafe_allow_html=True)
            a1, a2, a3 = st.columns(3)
            a1.markdown(f'<div class="card"><div class="kpi-title">Missing</div><div class="kpi-value">{before_missing}</div></div>', unsafe_allow_html=True)
            a2.markdown(f'<div class="card"><div class="kpi-title">Duplicates</div><div class="kpi-value">{before_dup}</div></div>', unsafe_allow_html=True)
            a3.markdown(f'<div class="card"><div class="kpi-title">Outliers</div><div class="kpi-value">{before_out}</div></div>', unsafe_allow_html=True)
            st.markdown("<div style='margin-top:8px'><strong>Preview (Before)</strong></div>", unsafe_allow_html=True)
            st.dataframe(df.head(), use_container_width=True)
        with right:
            st.markdown('<div class="card"><strong>After</strong></div>', unsafe_allow_html=True)
            b1, b2, b3 = st.columns(3)
            b1.markdown(f'<div class="card"><div class="kpi-title">Missing</div><div class="kpi-value">{after_missing}</div></div>', unsafe_allow_html=True)
            b2.markdown(f'<div class="card"><div class="kpi-title">Duplicates</div><div class="kpi-value">{after_dup}</div></div>', unsafe_allow_html=True)
            b3.markdown(f'<div class="card"><div class="kpi-title">Outliers</div><div class="kpi-value">{after_out}</div></div>', unsafe_allow_html=True)
            st.markdown("<div style='margin-top:8px'><strong>Preview (After)</strong></div>", unsafe_allow_html=True)
            st.dataframe(cleaned_df.head(), use_container_width=True)

        st.markdown('---')
        st.markdown("### 📥 Download Cleaned File")
        file_format = st.selectbox("Select file format", ("CSV", "Pickle (.pkl)"), key="download_choice_final")

        if file_format == "CSV":
            st.download_button(
                label="⬇️ Download as CSV",
                data=cleaned_df.to_csv(index=False).encode("utf-8"),
                file_name="cleaned_dataset.csv",
                mime="text/csv",
                key="download_csv_final"
            )
        else:
            import pickle
            pickle_bytes = pickle.dumps(cleaned_df)
            st.download_button(
                label="⬇️ Download as Pickle (.pkl)",
                data=pickle_bytes,
                file_name="cleaned_dataset.pkl",
                mime="application/octet-stream",
                key="download_pkl_final"
            )
    else:
        st.info("Click 'Run Full Cleaning' to execute the pipeline.")

# -------------------------
# Router: load uploaded CSV and show page
# -------------------------
if uploaded is None:
    st.info("Upload a CSV file to start (use the uploader above).")
else:
    try:
        df = pd.read_csv(uploaded)
    except Exception as e:
        st.error(f"Failed to read uploaded CSV: {e}")
    else:
        page = st.session_state.get("page", "Summary").lower()
        if page in ("home", "summary"):
            show_summary(df)
        elif page == "eda":
            run_eda(df)
        elif page == "cleaning":
            run_cleaning(df)
        else:
            show_summary(df)
