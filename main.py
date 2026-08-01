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

    gemini_output = parse_query(request.query)

    reply = search_company(gemini_output)

    soups = get_company_soup(reply)

    return {
"gemini_output":gemini_output,"url": reply, "soup": soups[:500]}