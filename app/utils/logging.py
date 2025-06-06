import logging as logger
from datetime import datetime
import os


FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
FILE_DIR = os.path.join(os.getcwd(), "logs")

FULL_FILE_PATH = os.path.join(FILE_DIR, FILE_NAME)


logger.basicConfig(
                filename=FULL_FILE_PATH, 
                level=logger.INFO,
                format='[%(asctime)s] - %(lineno)s - %(name)s - %(levelname)s - %(message)s'
                )