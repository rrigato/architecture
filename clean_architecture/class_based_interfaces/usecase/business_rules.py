from repo.repo_implementation import HardDriveStorage

def get_file_size():
    """Initializes client

        Parameters
        ----------

        Returns
        -------
        Raises
        ------
    """
    file_client = HardDriveStorage()
    loaded_data = file_client.load_data("mock_entity")

    return("File size is " + str(len(loaded_data.keys())))

