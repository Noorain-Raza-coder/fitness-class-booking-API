from fastapi.testclient import TestClient
from app.main import app
from datetime import datetime, timedelta
from app.database import class_db, booking_db

client = TestClient(app)

# helping function
def setup_class_data():
    class_db.clear()
    booking_db.clear()
    class_db.append({
        "id": 1,
        "name": "Yoga",
        "date": datetime.now() + timedelta(days=1),
        "instructor": "Ravi",
        "available_slots": 2
    })


# TEST CASES FOR "/booking" ROUTE
def test_successful_booking():
    setup_class_data()
    response = client.post("/booking", json={
        "id": 100,
        "class_id": 1,
        "client_name": "Alice",
        "client_email": "alice@example.com"
    })
    assert response.status_code == 200
    assert response.json()["msg"] == "slot is booked successfully"
    assert len(booking_db) == 1



def test_overbooking():
    setup_class_data()
    # Fill all slots
    for i in range(2):
        client.post("/booking", json={
            "id": i,
            "class_id": 1,
            "client_name": f"User{i}",
            "client_email": f"user{i}@example.com"
        })
    # Try one more booking
    response = client.post("/booking", json={
        "id": 3,
        "class_id": 1,
        "client_name": "LateUser",
        "client_email": "late@example.com"
    })
    assert response.status_code == 200
    assert response.json()["msg"] == "Slots are not available"



def test_invalid_class_id():
    setup_class_data()
    response = client.post("/booking", json={
        "id": 999,
        "class_id": 999,
        "client_name": "Ghost",
        "client_email": "ghost@example.com"
    })
    assert response.status_code == 404
    assert response.json()["detail"] == "Class Not Found"



def test_missing_fields():
    setup_class_data()
    response = client.post("/booking", json={
        "id": 102,
        "class_id": 1,
        "client_name": "Bob"
        # Missing client_email
    })
    assert response.status_code == 422  # FastAPI validation error





# TEST CASE FOR "/booking/all" ROUTE
def test_get_all_bookings():
    booking_db.clear()
    booking_db.append({
        "id": 200,
        "class_id": 1,
        "client_name": "Ria",
        "client_email": "ria@example.com"
    })
    response = client.get("/booking/all")
    assert response.status_code == 200
    assert "bookings" in response.json()
    assert len(response.json()["bookings"]) == 1



def test_no_bookings_found():
    booking_db.clear()
    response = client.get("/booking/all")
    assert response.status_code == 200
    assert response.json()["msg"] == "No Booking Found"






# TEST CASES FOR "/booking/?email=.." ROUTE
def test_bookings_by_email_found():
    booking_db.clear()
    booking_db.append({
        "id": 300,
        "class_id": 1,
        "client_name": "Sam",
        "client_email": "sam@example.com"
    })
    response = client.get("/booking", params={"email": "sam@example.com"})
    assert response.status_code == 200
    assert len(response.json()["bookings"]) == 1



def test_bookings_by_email_not_found():
    booking_db.clear()
    response = client.get("/booking", params={"email": "notfound@example.com"})
    assert response.status_code == 404
    assert response.json()["detail"] == "No Booking Found"



def test_missing_email_param():
    response = client.get("/booking")
    assert response.status_code == 422
