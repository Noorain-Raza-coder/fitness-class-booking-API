# 🏋️‍♀️ Fitness Class Booking API

A simple RESTful API built using **FastAPI** to manage bookings for a fictional fitness studio offering classes like Yoga, Zumba, and HIIT.

---

## 📌 Project Objective

The goal of this project is to build a backend system where:
- Users can view all available fitness classes
- Users can book a slot in a class
- Users can view their bookings using their email

This project demonstrates RESTful API design, clean architecture, validation, error handling, and basic testing.

---

## 🚀 Tech Stack

- **Language**: Python 3.10+
- **Framework**: FastAPI
- **Database**: In-memory using Python lists
- **Testing**: Pytest
- **Tools**: Uvicorn, Pydantic, Logging, Swagger UI (via FastAPI)

---

## 🧠 Approach

- Designed modular routers for classes and bookings.
- Used Pydantic models for schema validation.
- Stored data in memory (lists) to keep setup simple.
- Added validation and error handling.
- Logging enabled via a custom module.
- Unit tests included for all major routes.

---

## 📂 Project Structure

```
fitness-booking-api/
├── app/
│   ├── __init__.py
│   ├── main.py                  # Entry point for the FastAPI app
│   ├── models.py                # Pydantic models and data classes
│   ├── database.py              # SQLite setup and in-memory data
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── classes.py           # Endpoints for viewing classes
│   │   ├── bookings.py          # Endpoints for booking and viewing bookings
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── timezone_helper.py   # Timezone conversion helper
│   │   ├── validators.py        # Input validation logic
│   ├── seed_data.py             # File to populate sample data into the DB
│
├── tests/
│   ├── __init__.py
│   ├── test_classes.py          # Tests for /classes endpoints
│   ├── test_bookings.py         # Tests for /book and /bookings endpoints
│
├── requirements.txt             # Dependencies
├── README.md                    # Setup instructions and API documentation
├── run.sh                       # Bash script to run the app
├── .gitignore                   # Ignore __pycache__, .env, etc.

```


---

## 🔌 API Endpoints

### 🎓 Class Routes

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/classes` | Get all fitness classes |
| GET    | `/classes/available` | Get upcoming classes with available slots |

### 📅 Booking Routes

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   | `/booking` | Book a slot in a class |
| GET    | `/booking/all` | Get all bookings (for admin) |
| GET    | `/booking?email=<client_email>` | Get bookings for a specific client by email |

---

## ⚙️ Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/fitness-class-booking-api.git
cd fitness-class-booking-api
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```


### 3. Install Dependencies
```bash
pip install -r requirements.txt
```



## ▶️ Running the Project
```bash
uvicorn app.main:app --reload
```
This will start the server at:
http://127.0.0.1:8000

🧪 API Docs
- Swagger UI: http://127.0.0.1:8000/docs
- Redoc: http://127.0.0.1:8000/redoc


## ✅ Running Tests
Make sure you're in the root directory:
```bash
pytest app/tests
```


## 🙋‍♂️ Author
Built with ❤️ by Noorain Raza
