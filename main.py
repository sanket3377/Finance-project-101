from fastapi import FastAPI
from pydantic import BaseModel

from scraper.gemini import parse_query
from scraper.search import search_company
from scraper.search import get_company_soup

app = FastAPI()


class UserRequest(BaseModel):
    query: str


@app.post("/search")
async def run_search(request: UserRequest):
    # Step 1: Send the user's query to Gemini
    gemini_output = parse_query(request.query)

    # Step 2: Store the Gemini output (optional)
    print("Gemini Output:")
    print(gemini_output)
    company = gemini_output["company"]

    url = search_company(company)
    soup = get_company_soup(url)

    # Step 4: Return whatever the search module returns
    return {
    "html": str(soup)
}