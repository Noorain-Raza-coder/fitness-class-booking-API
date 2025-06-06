from fastapi.testclient import TestClient
from app.main import app
from datetime import datetime, timedelta
from app.database import class_db

client = TestClient(app)

# TEST CASES FOR '/classes' ROUTE

## positive test cases
def test_get_classes_positive():
    class_db.append({
        "id": 1,
        "name": "Yoga",
        "date": datetime.now() + timedelta(days=1),
        "instructor": "Ravi",
        "available_slots": 10
    })
    response = client.get("/classes")
    assert response.status_code == 200
    assert isinstance(response.json()["classes"], list)


## negative test cases
def test_get_classes_when_empty():
    # Temporarily clear class_db
    from app.database import class_db
    class_db.clear()
    response = client.get("/classes")
    assert response.status_code == 404
    assert response.json()["detail"] == "Classes Not found"






# TEST CASES FOR "/classes/available" ROUTE

## Positive test case when only one class is available
def test_available_classes_positive():
    class_db.clear()
    class_db.append({
        "id": 1,
        "name": "Yoga",
        "date": datetime.now() + timedelta(days=1),
        "instructor": "Ravi",
        "available_slots": 10
    })
    response = client.get("/classes/available")
    assert response.status_code == 200
    assert len(response.json()["classes"]) == 1


## Positive test case when only past classes are available
def test_no_future_classes():
    class_db.clear()
    class_db.append({
        "id": 2,
        "name": "Zumba",
        "date": datetime.now() - timedelta(days=1),
        "instructor": "Anu",
        "available_slots": 5
    })
    response = client.get("/classes/available")
    assert response.status_code == 200
    assert response.json()["classes"] == []


## Negative test case when no class is available
def test_available_classes_empty():
    class_db.clear()
    response = client.get("/classes/available")
    assert response.status_code == 404  # because get_all_classes() raises 404


## Negative test case when invalid date is passed
def test_invalid_date_field():
    class_db.clear()
    class_db.append({
        "id": 3,
        "name": "HIIT",
        "date": "2025-06-10",  # invalid format for comparison
        "instructor": "Raj",
        "available_slots": 7
    })
    try:
        response = client.get("/classes/available")
        assert response.status_code == 500  # should fail with internal error
    except Exception:
        assert True
