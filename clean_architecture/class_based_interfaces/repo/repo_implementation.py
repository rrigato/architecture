from usecase.interface_spec import IoPlugin
'''
    TODO - determine limit on how many interfaces can be inherited?
'''
class HardDriveStorage(IoPlugin):
    def load_data(self, file_name):
        """implementation of interface

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
        return(
            {
                "entity_count": 5,
                "entity_description": "trivial example that will run into unexpected problems in prod"
            }
        )