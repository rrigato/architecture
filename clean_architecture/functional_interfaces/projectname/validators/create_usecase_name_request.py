from projectname.validators.check_input import arg1_range
from projectname.validators.request_objects import InvalidRequest
from projectname.validators.request_objects import ValidRequest

def validate_usecase_name(arg1):
    """
        Parameters
        ----------
        arg1 : int
            in the interval (0,100]
            

        Returns
        -------
        request_object : ValidRequest or InvalidRequest
        ValidRequest if all preconditions to invoke usecase_name are met,
        otherwise an InvalidRequst. If ValidRequest, usecase_name
        has all input neceassary to invoke its interface and the only 
        thing that can result in a failure is if the usecase has an unexpected
        error
    """
    '''
        Performs the following:
            - data type checking of arguements
            - Prequisites for usecase design by contract
            - collects any business logic specific input domain
            validation
    '''
    if bool(arg1_range(arg1=arg1)) == False:
        return(InvalidRequest(error_message="arg1 is invalid"))

    return(ValidRequest())
