import sys

def error_message_details(error, error_detail:sys):

    _,_,exc_tb = error_detail.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occured in python script {file_name} at line number {exc_tb.tb_lineno} error message{str(error)}"
    return error_message


class CustomException(Exception     ):
    def __init__(self,error_name, error_details:sys):
        super().__init__(error_name)
        self.error_message = error_message_details(error_name,error_details)
    def __str__(self) -> str:
        return self.error_message