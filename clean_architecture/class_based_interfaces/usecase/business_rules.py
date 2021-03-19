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
    file_client.load_data("mock_filename")

if __name__ == "__main__":
    get_file_size()