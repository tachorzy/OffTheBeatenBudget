from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict

class Accommodation(BaseModel):
    name: str
    location: str
    check_in: str
    check_out: str
    cost: float
class Trip(BaseModel):
    name: str
    destinations: List[str]
    accommodations: List[Accommodation]
    start_date: str
    end_date: str

class Expense(BaseModel):
    description: str
    amount: float
    date: str

app = FastAPI()

trips: Dict[int, Trip] = {}
accommodations: Dict[int, Accommodation] = {}
expenses: Dict[int, Expense] = {}


@app.post("/accomodation")
async def create_accomodation(accommodation: Accommodation):
    accommodation_id = len(accommodations) + 1
    accommodations[accommodation_id] = accommodation
    return accommodation

@app.post("/trip")
async def create_trip(trip: Trip):
    trip_id = len(trips) + 1
    trips[trip_id] = trip
    return trip

@app.get("/")
async def root():
    return {"message": "Hello World"}