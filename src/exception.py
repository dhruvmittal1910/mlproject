# exception or error handling
import sys
from src.logger import logging

def error_message_details(error,error_detail:sys):
    # return type of sys gives me 
    _,_,exc_tb=error_detail.exec_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="error occured in py script name [{0}] line number [{1}] with error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_details(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
    

# above code is common for the error handling in all files