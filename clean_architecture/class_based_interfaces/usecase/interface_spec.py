from abc import ABC
from abc import abstractmethod

class IoPlugin(ABC):
    @abstractmethod
    def load_data(self, file_name):
        """Initializes client

            Parameters
            ----------

            Returns
            -------
            loaded_json_file : dict
                deserialized dict with the following schema
                {
                    "hello": int,
                    "world": str
                }
            Raises
            ------
        """
        pass
