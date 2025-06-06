from app.models import Classes, GetBooking
from datetime import datetime, timedelta
from app.database import class_db, booking_db



def seed_classes():
    """
        Initialise the Fitness-Class in-memory database.

        This function populates the fitness-class database with pre-defined dummy classes.

        Returns:
            None
    """
    class_db.extend(
        [   Classes(id=1, name="YOGA", date=datetime.now() + timedelta(1), instructor="Noorain", available_slots=5).dict(),
            Classes(id=2, name="ZUMBA", date=datetime.now() + timedelta(2), instructor="Kavya", available_slots=10).dict(),
            Classes(id=3, name="NIIT", date=datetime.now() - timedelta(2), instructor="Zain", available_slots=3).dict(),
            Classes(id=4, name="GYM", date=datetime.now() + timedelta(3), instructor="Rocky", available_slots=0).dict()
        ])
    




def seed_booking(request):
    """
        Insert records into booking database.

        This function insert the booking details of a client into booking database.

        Args :
            id (int) : Booking ID
            class_id (int) : Fitness-Class ID
            client_name (str) : Client name
            client_email (str) : Client email ID
        
        Returns :
            None
    """
    booking_id = len(booking_db) + 1
    booking_db.append(
            GetBooking(id=booking_id, 
                      class_id=request["class_id"], 
                      client_name=request["client_name"],
                      client_email=request["client_email"]).dict()
                    )

