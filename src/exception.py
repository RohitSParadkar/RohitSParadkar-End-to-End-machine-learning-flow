import sys

def custom_error_message(error,error_details:sys):
    _,_,exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = "Error is occured at Script Name{0} and line number {1} error message is {2}".format(file_name,line_number,str(error))
    return error_message

class customException(Exception):
    def __init__(self,error_message,error_deatils:sys):
        super().__init__(error_message)
        self.error_message = custom_error_message(error_message,error_details=error_deatils)
    
    def __str__(self):
        return self.error_message