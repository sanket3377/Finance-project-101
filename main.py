from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


class DataRequest(BaseModel):
    company: str
    data_items: List[str]
    timelines: List[str]


@app.post("/fetch")
async def fetch_data(request: DataRequest):

    print("Company:", request.company)
    print("Data Items:", request.data_items)
    print("Timelines:", request.timelines)

    return {
        "status": "received",
        "company": request.company,
        "data_items": request.data_items,
        "timelines": request.timelines
    }
