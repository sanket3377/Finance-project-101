from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from scraper.search import search_company
from scraper.search import get_company_soup
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

    command = get_stock_json(request.query)

    company_name = command["stock"]

    company_url = search_company(company_name)

    soup = get_company_soup(company_name)

    return {
        "gemini_json": command,
        "company_name": company_name,
        "company_url": company_url,
        "soup_created": soup is not None
    }