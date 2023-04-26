import pickle
import os
import sys
from src.logger import logging
from src.exception import CustomException


def save_object(filepath, object):
    try:
        logging.info("Saving the object in pickle file")
        dir_path = os.path.dirname(filepath)
        os.makedirs(dir_path,exist_ok=True)

        with open(filepath,'wb') as f:
            pickle.dump(object,f)
        logging.info("Object has been saved in pickle file")

    except Exception as e:
        logging.info("Exception has occured while saving a file")
        raise CustomException(e)
    