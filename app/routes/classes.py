from fastapi import APIRouter, HTTPException
from app.database import class_db
from datetime import datetime
from app.utils.logging import logger


classes_rt = APIRouter(tags=["Classes"])



@classes_rt.get('/classes', status_code=200)
def get_all_classes():
    """
        Get all Fitness-Classes.

        This function returns a list of all fitness-classes i.e past and future classes.

        - Returns:
            - List : Returns a list of fitness-classes detials.

        - Raises:
            - HTTPException 404 : if classes are not found.
    """
    logger.info("Request is made to get all the classes.")
    if not class_db:
        logger.error("No Class is found.")
        raise HTTPException(status_code=404, detail="Classes Not found")
    
    logger.info(f"A list of {len(class_db)} classes is returned.")
    return {"classes":class_db} 



@classes_rt.get('/classes/available', status_code=200)
def get_available_classes():
    """
        Get available fitness-classes.

        This function returns a list of all available fitness-classes.

        - Returns:
            - List : List of detials of fitness-classes.

        - Raises:
            - HTTPException 404 : if classes are not available.  
    """
    logger.info("Request is made to get available classes.")
    cls = get_all_classes()
    available_classes = [c for c in cls["classes"] if c.get('date') >= datetime.now()]
    
    logger.info(f"a list of {len(available_classes)} is returned.")
    return {"classes":available_classes}



