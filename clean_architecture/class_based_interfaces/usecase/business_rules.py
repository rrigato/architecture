from repo.repo_implementation import HardDriveStorage

def customer_count():
    """Gets number of customers

        Parameters
        ----------

        Returns
        -------
        file_size : float
            size of the file with custom business logic applied

        Raises
        ------
    """
    file_client = HardDriveStorage()
    loaded_data = file_client.load_data("mock_entity")

    '''
        This is a pretty good example of how random business rules are -_-
    '''
    return((((loaded_data["entity_count"] * 8) - 10)/10))

