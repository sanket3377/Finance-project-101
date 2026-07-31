from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from scraper.search import search_company
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # For development. Later we'll restrict this.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DataRequest(BaseModel):
    company: str
    data_items: List[str]
    timelines: List[str]

@app.get("/")
async def home():
    return {"message": "Backend is running successfully!"}

@app.post("/fetch")


@app.post("/fetch")
async def fetch_data(request: DataRequest):

    result = search_company(request.company)

    return result
