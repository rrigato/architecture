from usecase.request_object_contract import InvalidRequest


class NetworkFailure(InvalidRequest):
    """Do not create a class like this that inherits 
        from anything that is not an interface
    """
    pass