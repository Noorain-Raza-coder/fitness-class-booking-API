from pydantic import BaseModel, EmailStr
from datetime import datetime


# data validation class for fitness-classes
class Classes(BaseModel):
    id : int
    name : str
    date : datetime
    instructor : str
    available_slots : int


# data validation class for booking
class Booking(BaseModel):
    id : int
    class_id : int
    client_name : str
    client_email : EmailStr


# data validation class to get booking details for a specific client
class GetBooking(BaseModel):
    id : int
    class_id : int
    client_name : str
    client_email : EmailStr