import logging 
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_file_path=os.path.join(os.getcwd(),"logs")
os.makedirs(logs_file_path,exist_ok=True)

current_log_file=os.path.join(logs_file_path,LOG_FILE)

logging.basicConfig(
    filename=current_log_file,
    format="%(asctime)s --- %(message)s-- %(lineno)d %(name)s - %(levelname)s ",
    level=logging.INFO
)