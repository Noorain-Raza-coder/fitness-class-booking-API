from fastapi import APIRouter, HTTPException
from app.models import Booking
from app.database import class_db, booking_db
from app.seeds import seed_booking
from app.utils.logging import logger


# router for booking endpoints
booking_rt = APIRouter(tags=["Booking"])



@booking_rt.post('/booking')
def book_slot(request : Booking):
    """
        Book a Fitness-Class Slot.

        This endpoint allows a client to book a slot for fitness-classes if slot is available.

        - Args:
            - id (int) : Booking ID
            - class_id (int) : Fitness-Class ID
            - client_name (str) : Client name
            - client_email (str) : client email ID

        - Returns:
            - dict : returns successfull slot booking message along with client details.

        - Raise:
            - HTTPException 404 : if fitness-class id is not available
    """

    request = request.dict()
    logger.info(f"Request is received : {request}")

    for cls in class_db:
        if cls["id"] == request["class_id"]:
            if cls["available_slots"] > 0:

                # calling seed_booking fucntion to insert the booking details
                seed_booking(request)

                cls["available_slots"] = cls["available_slots"] - 1
                logger.info(f"Slot is booked for a class ID : {cls['id']}")
                return {"msg":"slot is booked successfully","details":request}
            else:
                logger.warning(f"Slots are not available for class ID : {cls['id']}")
                return {"msg":"Slots are not available"}    
    
    logger.error(f"Class not found for class id : {request['class_id']}")
    raise HTTPException(status_code=404, detail="Class Not Found")
        




@booking_rt.get('/booking/all')
def get_all_bookings():
    """
        Get all clients bookings.

        This endpoint returns a list of bookings made by clients.

        - Returns:
            - List : returns a list of dictionaries containing booking details.
    """
    logger.info("Request is made to get all bookings.")
    if booking_db :
        logger.info(f"a list of {len(booking_db)} bookings is returned.")
        return {"bookings":booking_db}
    else:
        logger.warning("No booking is found.")
        return {"msg":"No Booking Found"}





@booking_rt.get('/booking')
def get_bookings_by_email(email:str):
    """
        Get all the bookings made by a specific client.

        This endpoint returns a list of bookings made by a specific client.

        - Args :
            - email (str) : Client email ID.

        - Returns:
            - List : returns a list of dictionaries containing booking details.
        
        - Raises:
            - HTTPException 404 : if no booking found for a specific client.
    """
    logger.info(f"Request is made to get booking details for email id : {email}")
    user_bookings = [b for b in booking_db if b["client_email"] == email]
    if not user_bookings:
        logger.error(f"No booking found for client email : {email}")
        raise HTTPException(status_code=404, detail="No Booking Found")
    logger.info(f"a list of {len(user_bookings)} bookings is returned.")
    return {"bookings":user_bookings}