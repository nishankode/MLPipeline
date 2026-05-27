# datascienceproject
import os
import sys 
import logging 

log_dir = 'logs'
log_file_path = os.path.join(log_dir, 'logger.log')
os.makedirs(log_dir, exist_ok=True)

logger_message = "%(asctime)s : %(levelname)s : %(message)s"
logging.basicConfig(
    level=logging.INFO,
    format=logger_message,
    handlers=[
        logging.FileHandler(filename=log_file_path),
        logging.StreamHandler(stream=sys.stdout)
    ]
)

logger = logging.getLogger(name=__name__)