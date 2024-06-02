import logging
import os
from datetime import datetime

# Create logs directory if it doesn't exist
if not os.path.exists('logs'):
    os.makedirs('logs')

# Generate a unique log file name based on the current timestamp
log_filename = datetime.now().strftime("logs/app_%Y_%m_%d_%H_%M_%S.log")

# Configure logging
logging.basicConfig(
    filename=log_filename,
    filemode='a',  # Append mode
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO  # Change to logging.INFO or logging.ERROR to adjust logging level
)


