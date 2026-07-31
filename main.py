from fastapi import FastAPI
from pydantic import BaseModel

from gemini import parse_query
from search import search

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

    # Step 3: Send Gemini's output to the search module
    results = search(gemini_output)

    # Step 4: Return whatever the search module returns
    return results