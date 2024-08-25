from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

class Accommodation(BaseModel):
    id: int
    name: str
    location: str
    check_in: str
    check_out: str
    cost: float
class Trip(BaseModel):
    id: int
    name: str
    destinations: List[str]
    accommodations: List[Accommodation]
    start_date: str
    end_date: str

class Expense(BaseModel):
    id: int
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

@app.get("/accommodation/{accommodation_id}")
async def get_accommodation(accommodation_id: int):
    if accommodation_id in accommodations:
        return accommodations[accommodation_id]
    else:
        raise HTTPException(status_code=404, detail="Accommodation not found")

@app.get("/trip/{trip_id}")
async def get_trip(trip_id: int):
    if trip_id in trips:
        return trips[trip_id]
    else:
        raise HTTPException(status_code=404, detail="Trip not found")

@app.get("/")
async def root():
    return {"message": "Hello World"}