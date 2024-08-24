from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

trips = {}
expenses = {}


class Accomodation(BaseModel):
    name: str
    location: str
    check_in: str
    check_out: str
    cost: float
class Trip(BaseModel):
    name: str
    destinations: List[str]
    accomodations: List[Accomodation]
    start_date: str
    end_date: str

class Expense(BaseModel):
    description: str
    amount: float
    date: str

@app.get("/")
async def root():
    return {"message": "Hello World"}