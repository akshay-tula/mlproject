import logging
import os
from datetime import datetime
import sys 

# 1. Define the log file NAME
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 2. Define the log folder PATH (relative to the script execution directory)
LOGS_PATH = os.path.join(os.getcwd(), "logs") 

# 3. Create the log folder if it doesn't exist
os.makedirs(LOGS_PATH, exist_ok=True)

# 4. Define the complete log file path
LOG_FILE_PATH = os.path.join(LOGS_PATH, LOG_FILE) # <--- Combine folder and file name

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s ] %(lineno)d: %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
