import sys
import os
import pytest
from fastapi.testclient import TestClient

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import app

client = TestClient(app)

def test_create_accommodation():
    response = client.post("/accomodation", json={"id": 1, "name": "Hotel", "location": "Paris", "check_in": "2021-10-01", "check_out": "2021-10-05", "cost": 100.0})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Hotel", "location": "Paris", "check_in": "2021-10-01", "check_out": "2021-10-05", "cost": 100.0}

def test_create_trip():
    response = client.post("/trip", json={"id": 1, "name": "Paris Trip", "destinations": ["Paris"], "accommodations": [{"id": 1, "name": "Hotel", "location": "Paris", "check_in": "2021-10-01", "check_out": "2021-10-05", "cost": 100.0}], "start_date": "2021-10-01", "end_date": "2021-10-05"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Paris Trip", "destinations": ["Paris"], "accommodations": [{"id": 1, "name": "Hotel", "location": "Paris", "check_in": "2021-10-01", "check_out": "2021-10-05", "cost": 100.0}], "start_date": "2021-10-01", "end_date": "2021-10-05"}

def test_create_trip_multiple_destinations():
    response = client.post("/trip", json={"id": 1, "name": "Euro Trip", "destinations": ["Paris", "London"], "accommodations": [{"id": 1, "name": "Hotel", "location": "Paris", "check_in": "2021-10-01", "check_out": "2021-10-05", "cost": 100.0}], "start_date": "2021-10-01", "end_date": "2021-10-05"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Euro Trip", "destinations": ["Paris", "London"], "accommodations": [{"id": 1, "name": "Hotel", "location": "Paris", "check_in": "2021-10-01", "check_out": "2021-10-05", "cost": 100.0}], "start_date": "2021-10-01", "end_date": "2021-10-05"}

def test_get_accommodation():
        accommodation_data = {
            "id": 1,
            "name": "Hotel",
            "location": "Paris",
            "check_in": "2021-10-01",
            "check_out": "2021-10-05",
            "cost": 100.0
        }
        response = client.post("/accommodation", json=accommodation_data)
        accommodation_id = accommodation_data["id"]
        response = client.get(f"/accommodation/{accommodation_id}")
        assert response.status_code == 200
        assert response.json() == accommodation_data.copy()

# def test_get_trip():
#     trip_data = {
#         "id": 1,
#         "name": "Paris Trip",
#         "destinations": ["Paris"],
#         "accommodations": [{
#             "name": "Hotel",
#             "location": "Paris",
#             "check_in": "2021-10-01",
#             "check_out": "2021-10-05",
#             "cost": 100.0
#         }],
#         "start_date": "2021-10-01",
#         "end_date": "2021-10-05"
#     }
#     trip_id = post_and_get_id("/trip", trip_data)
#     assert trip_id is not None, "Trip ID not found in the response"
#     get_and_assert(f"/trip/{trip_id}", trip_data)
