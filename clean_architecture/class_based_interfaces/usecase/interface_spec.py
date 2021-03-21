from abc import ABC
from abc import abstractmethod

class IoPlugin(ABC):
    @abstractmethod
    def load_data(self, entity_name):
        """Interface specification to retrieve dict

            Parameters
            ----------
            entity_name : str

            Returns
            -------
            loaded_json_file : dict
                deserialized dict with the following schema
                {
                    "entity_count": int,
                    "entity_description": str
                }
            Raises
            ------
        """
        pass
