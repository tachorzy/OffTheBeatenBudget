import sys
import os
import pytest
from fastapi.testclient import TestClient

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import app

client = TestClient(app)

def test_create_accommodation():
    response = client.post("/accomodation", json={"name": "Hotel", "location": "Paris", "check_in": "2021-10-01", "check_out": "2021-10-05", "cost": 100.0})
    assert response.status_code == 200
    assert response.json() == {"name": "Hotel", "location": "Paris", "check_in": "2021-10-01", "check_out": "2021-10-05", "cost": 100.0}

def test_create_trip():
    response = client.post("/trip", json={"name": "Paris Trip", "destinations": ["Paris"], "accommodations": [{"name": "Hotel", "location": "Paris", "check_in": "2021-10-01", "check_out": "2021-10-05", "cost": 100.0}], "start_date": "2021-10-01", "end_date": "2021-10-05"})
    assert response.status_code == 200
    assert response.json() == {"name": "Paris Trip", "destinations": ["Paris"], "accommodations": [{"name": "Hotel", "location": "Paris", "check_in": "2021-10-01", "check_out": "2021-10-05", "cost": 100.0}], "start_date": "2021-10-01", "end_date": "2021-10-05"}

def test_create_trip_multiple_destinations():
    response = client.post("/trip", json={"name": "Euro Trip", "destinations": ["Paris", "London"], "accommodations": [{"name": "Hotel", "location": "Paris", "check_in": "2021-10-01", "check_out": "2021-10-05", "cost": 100.0}], "start_date": "2021-10-01", "end_date": "2021-10-05"})
    assert response.status_code == 200
    assert response.json() == {"name": "Euro Trip", "destinations": ["Paris", "London"], "accommodations": [{"name": "Hotel", "location": "Paris", "check_in": "2021-10-01", "check_out": "2021-10-05", "cost": 100.0}], "start_date": "2021-10-01", "end_date": "2021-10-05"}

def test_get_accommodation():
    response = client.post("/accomodation", json={"name": "Hotel", "location": "Paris", "check_in": "2021-10-01", "check_out": "2021-10-05", "cost": 100.0})
    accommodation_id = response.json()["id"]
    response = client.get(f"/accomodation/{accommodation_id}")
    assert response.status_code == 200
    assert response.json() == {"name": "Hotel", "location": "Paris", "check_in": "2021-10-01", "check_out": "2021-10-05", "cost": 100.0}

def test_get_trip():
    response = client.post("/trip", json={"name": "Paris Trip", "destinations": ["Paris"], "accommodations": [{"name": "Hotel", "location": "Paris", "check_in": "2021-10-01", "check_out": "2021-10-05", "cost": 100.0}], "start_date": "2021-10-01", "end_date": "2021-10-05"})
    trip_id = response.json()["id"]
    response = client.get(f"/trip/{trip_id}")
    assert response.status_code == 200
    assert response.json() == {"name": "Paris Trip", "destinations": ["Paris"], "accommodations": [{"name": "Hotel", "location": "Paris", "check_in": "2021-10-01", "check_out": "2021-10-05", "cost": 100.0}], "start_date": "2021-10-01", "end_date": "2021-10-05"}

