class ResponseSuccess():
    """usecase executed sucessfully, returning output 
    of business logic
    """
    def __bool__(self):
        return(True)

    def __init__(self, response_value):
        self._response_value = response_value

    @property
    def response_value(self):
        return(self._response_value)




class ResponseFailure():
    """Error occurred when processing the usecase
    """
    def __bool__(self):
        return(False)

    def __init__(error_message):
        self._error_message = error_message

    @property
    def error_message(self):
        return(self._error_message)
