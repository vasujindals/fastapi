from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

# Load student data from CSV
df = pd.read_csv("students.csv")

# Initialize FastAPI app
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

