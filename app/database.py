from app.models import Classes, Booking
from typing import List


# creating two in-memory databases to store fitness-classes and booking data
class_db : List[dict] = []
booking_db : List[dict] = []