class ValidRequest():
    """Value object that can be used to invoke a usecase
    """
    def __bool__(self):
        return(True)

    def __init__(self, request_filters):
        self._request_filters = request_filters

    @property
    def request_filters(self):
        return(self._request_filters)



class InvalidRequest():
    """Value object that returns an invalid request to 
    client with error_message
    """
    def __bool__(self):
        return(False)

    def __init__(self, error_message):
        self._error_message = error_message

    @property
    def error_message(self):
        return(self._error_message)
