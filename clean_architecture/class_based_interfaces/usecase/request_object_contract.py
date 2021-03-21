from abc import ABC
from abc import abstractmethod

class ValidRequest(ABC):
    """All input validation is successfull. 
    The request can be passed to the usecase layer
    """
    def __bool__(self):
        """Returns True"""
        return(True)


class InvalidRequest(ABC):
    """Input/security requirements did not pass validation.
    Do not call usecase and return error to client
    """
    def __bool__(self):
        """Returns False"""
        return(False)

    def __init__(self, error_message):
        self._set_error_message(error_message=error_message)

    def get_error_message(self):
        return(self._error_message)
     
    def _set_error_message(self, error_message):
        """Private to ensure error_message is immutable, error_message is set once for the
        value object and never changed
        """
        if type(error_message) != str:
            raise TypeError("InvalidRequest - error_message must be type str")
        self._error_message = error_message