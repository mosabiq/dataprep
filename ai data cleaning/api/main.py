from fastapi import FastAPI, UploadFile, File
import pandas as pd
from io import StringIO
from src.pipeline import CleaningPipeline

# Create FastAPI app
app = FastAPI()

# Initialize pipeline
pipeline = CleaningPipeline()

# API endpoint: /clean
@app.post("/clean")
async def clean(file: UploadFile = File(...)):
    # Read uploaded CSV file
    content = await file.read()
    s = content.decode("utf-8")

    # Convert file → pandas dataframe
    df = pd.read_csv(StringIO(s))

    # Run the cleaning pipeline
    res = pipeline.run(df)

    # Convert cleaned dataframe to CSV string
    out_csv = res["cleaned_df"].to_csv(index=False)

    # Return report and cleaned CSV
    return {
        "report": res["report"],
        "cleaned_csv": out_csv
    }
