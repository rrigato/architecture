from abc import ABC
from abc import abstractmethod

class ValidRequest(ABC):

    def __bool__(self):
        """Interface specification to retrieve dict
        """
        return(True)


class InvalidRequest(ABC):
    def __bool__(self):
        """Interface specification to retrieve dict
        """
        return(False)