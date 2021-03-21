from usecase.request_object_contract import InvalidRequest
from usecase.request_object_contract import ValidRequest

class FileInfo(ValidRequest):
    """Gets File information about an entity
    """

    '''
        TODO - how to enforce all objects go through request_wfilters
    '''
    def request_wfilters(self, input_parameters):
        """input_parameters for a get_file_info usecase call

        Parameters
        ----------
        input_parameters : dict
            {
                entity_name: str
            }

        Returns
        -------
        request_object : ValidRequest or InvalidRequest
            Depending on if input_parameters meets validation requirements

        """
        if "entity_name" not in input_parameters.keys():
            return(InvalidRequest(error_message="request_wfilters - key entity_name is required"))

        if type(input_parameters["entity_name"]) != str:
            return(InvalidRequest(error_message="request_wfilters - entity_name must be type str"))

        return(self)