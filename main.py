from fastapi import FastAPI
from pydantic import BaseModel

from scraper.gemini import parse_query
from scraper.search import search_company
from scraper.search import get_company_soup

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For testing. Later, replace "*" with your frontend URL.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class UserRequest(BaseModel):
    query: str


@app.post("/search")
async def run_search(request: UserRequest):
    # Step 1: Send the user's query to Gemini
    gemini_output = str(parse_query(request.query))

    # Step 2: Store the Gemini output (optional)
    print("Gemini:", gemini_output)

    reply = search_company(gemini_output)
    print("URL:", url)

    soups = get_company_soup(url)
    print("Soup:", soup)

    return {
"gemini_output":gemini_output,"url": str(reply), "soup": str(soups)[:500]}