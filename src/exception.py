import sys
from src.logger import logging

def get_error_details(error):
    _,_,exc_tb=sys.exc_info() #this function return error type, error value ,error traceback
    filename=exc_tb.tb_frame.f_code.co_filename # by this way we can get the filename in which the error occurred

    error_msg=f"Error has occurred in {filename} at line {exc_tb.tb_lineno} -- {error}"

    return error_msg

class CustomException(Exception):

    def __init__(self,error):
        self.error=get_error_details(error)

    def __str__(self):
        return self.error
'''
if __name__=="__main__":
    logging.info("Logging has started")
    try:
        a=1/0
    except Exception as e:
        logging.info('Division by zero') 
        raise CustomException(e)
        '''
