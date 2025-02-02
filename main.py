import os
import uvicorn
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

# Load CSV file
df = pd.read_csv("students.csv")

app = FastAPI()

# Enable CORS to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api")
def get_students(class_: list[str] = Query(None, alias="class")):
    """Return students as JSON, optionally filtered by class."""
    if class_:
        filtered_df = df[df["class"].isin(class_)]
    else:
        filtered_df = df

    return {"students": filtered_df.to_dict(orient="records")}

# Automatically get PORT from Railway
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Use Railway-assigned port, default to 8000
    uvicorn.run(app, host="0.0.0.0", port=port)
