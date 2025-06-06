from fastapi import FastAPI
from app.routes import booking, classes
from app.seeds import seed_classes

# setting up the title and description of FastAPI's swagger UI
app = FastAPI(title="Omnify Fitness-Classes Booking API", description="These APIs allow a client to check the available fitness classes, book a slot and check booked slots.")



@app.on_event("startup")
def init_class_db():
    """
        Get Initialise the in-memory classes database.
        
        This endpoint initialise the database for fitness-classes with dummy data when
        FastAPI server is initialised.

        Returns:
                None
    """
    seed_classes()



app.include_router(classes.classes_rt)
app.include_router(booking.booking_rt)

