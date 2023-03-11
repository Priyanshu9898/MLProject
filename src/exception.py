import sys
import logging
import pandas as pd

from src.logger import logging

def error_message_detail(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occured in Python Script name [{0}] Line No. [{1}] Error Message [{2}]".format(file_name, exc_tb.tb_lineno, str(error))

    return error_message

class customException(Exception):

    # Constructor or Initializer
    def __init__(self, error_message, error_detail:sys):
        super().__init__(self, error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
    
    # __str__ is to print() the value
    def __str__(self):
        return self.error_message


def load_dataset(file_name):
    try:
        # load the dataset from file_name
        df = pd.read_csv(file_name)
    except FileNotFoundError as e:
        logging.info("File Not Found: %s" % file_name)
        raise customException('File not found', error_detail=sys)
    except ValueError as e:
        logging.info("Invalid File format: %s" % file_name)
        raise customException('Invalid file format', error_detail=sys)

if __name__ == "__main__":

    try:
        load_dataset('dataset.csv')
    except customException as e:
        print(e)


