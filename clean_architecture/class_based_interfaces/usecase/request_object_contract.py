from abc import ABC
from abc import abstractmethod

class ValidRequest(ABC):
    """All input validation is successfull. 
    The request can be passed to the usecase layer
    """
    def __bool__(self):
        """Returns True"""
        return(True)

    '''
        TODO 
        - how to enforce all objects go through input_validation
        - ex: CustomerInfo() creates a valid CustomerInfo, but you would not be able to call
            your usecase with that
        - make _input_filters a property?
        
    '''
    @abstractmethod
    def input_validation(self, input_parameters):
        """Define all input_parameters data types when inheriting

        Parameters
        ----------
        input_parameters : dict
            dict that represents all input needed to invoke a usecase

        Returns
        -------
        request_object : ValidRequest or InvalidRequest
            Depending on if input_parameters meets validation requirements

        """
        pass

    '''
        strongly preference returning immutable copy of filters
    '''
    @abstractmethod
    def get_filters(self):
        """Returns filters for request object

        Parameters
        ----------

        Returns
        -------
        input_filters : dict
            dict that represents all input needed to invoke a usecase

        """
        pass


class InvalidRequest:
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