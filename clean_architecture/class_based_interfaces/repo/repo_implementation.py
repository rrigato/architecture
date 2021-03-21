from usecase.interface_spec import IoPlugin

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
                    "hello": int,
                    "world": str
                }
            Raises
            ------
        """
        return(
            {
                "hello": 5,
                "world": "trivial example that will run into unexpected problems in prod"
            }
        )