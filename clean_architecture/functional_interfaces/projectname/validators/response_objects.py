class ResponseSuccess():
    """usecase executed sucessfully, returning output 
    of business logic
    """
    def __bool__(self):
        return(True)

    def __init__(response_value):
        self._response_value = response_value


class ResponseFailure():
    """Error occurred when processing the usecase
    """
    def __bool__(self):
        return(False)

    def __init__(error_message):
        self._error_message = error_message