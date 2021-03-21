from externals.request_object_api import ApiRequest
from externals.request_network_failure import NetworkFailure

if __name__ == "__main__":
    valid_input = ApiRequest()
    print(NetworkFailure(error_message="Network timeout").get_error_message())
    #invalid input example
    #print(NetworkFailure(error_message=12).get_error_message())
