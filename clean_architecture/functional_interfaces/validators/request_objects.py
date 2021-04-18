class ValidRequest():
    """
    """
    def __bool__(self):
        return(True)

    def __init__(request_filters):
        self._request_filters = request_filters


class InvalidRequest():
    """Value object that returns an invalid request to 
    client with error_message
    """
    def __bool__(self):
        return(True)

    def __init__(error_message):
        self._error_message = error_message