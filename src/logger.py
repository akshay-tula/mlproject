import logging
import os
from datetime import datetime
import sys

# 1. Define the log file NAME
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

LOGS_PATH = os.path.join(os.getcwd(), "logs")

# 3. Create the log folder if it doesn't exist
os.makedirs(LOGS_PATH, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOGS_PATH, LOG_FILE)

LOG_FORMAT = "[%(asctime)s] %(lineno)d: %(name)s - %(levelname)s - %(message)s"

logging.basicConfig(
    handlers=[logging.FileHandler(LOG_FILE_PATH),
              logging.StreamHandler(sys.stdout)
              ],
    format=LOG_FORMAT, 
    level=logging.INFO
)
logging = logging.getLogger("MLPROJECT_LOGGER")

if __name__ == "__main__":
    logging.info("Logging has started successfully.")