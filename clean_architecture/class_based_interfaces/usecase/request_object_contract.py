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

    @property 
    def error_message(self):
        return(self._error_message)

    @error_message.setter     
    def error_message(self, error_message):
        """
        """
        assert type(error_message) == str, "InvalidRequest - error_message must be type str" 
        self._error_message = error_message