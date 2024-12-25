import logging
import os
import sys
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

os.makedirs(logs_path, exist_ok=True)
LOF_FILE_PATH = os.path.join(logs_path, LOG_FILE)



logging.basicConfig(
filename=LOF_FILE_PATH,
format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
level=logging.INFO,

)
