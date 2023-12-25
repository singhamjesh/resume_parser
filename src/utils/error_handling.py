import traceback
from fastapi import HTTPException


# @timing_decorator
# @log_io_decorator
def error_handler(error, status_code):
    # This function is handle error/exception
    if isinstance(error, Exception):
        errorMsg = traceback.format_exc()
    elif isinstance(error, str):
        errorMsg = error
    else:
        error = "Something went wrong! Please try again."

    raise HTTPException(
        status_code=status_code, detail=errorMsg)
