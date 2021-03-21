from copy import deepcopy
from usecase.request_object_contract import InvalidRequest
from usecase.request_object_contract import ValidRequest

class CustomerInfo(ValidRequest):
    """Gets File information about an entity
    """

    def input_validation(self, input_parameters):
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
            return(InvalidRequest(error_message="input_validation - key entity_name is required"))

        if type(input_parameters["entity_name"]) != str:
            return(InvalidRequest(error_message="input_validation - entity_name must be type str"))

        if len(input_parameters.keys()) != 1:
            return(InvalidRequest(error_message="input_validation - too many keys"))

        self._set_input_filters(input_filters=input_parameters)

        return(self)


    def _set_input_filters(self, input_filters):
        """input_parameters for a get_file_info usecase call

        Parameters
        ----------
        input_filters : dict
            {
                entity_name: str
            }
        """
        self._input_filters = input_filters


    def get_filters(self):
        """Returns filters for request object

        Parameters
        ----------

        Returns
        -------
        input_filters : dict
            dict that represents all input needed to invoke a usecase

        """
        return(deepcopy(self._input_filters))