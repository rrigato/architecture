from externals.request_object_api import FileInfo
from externals.request_network_failure import NetworkFailure
from usecase.business_rules import get_file_size

if __name__ == "__main__":
    valid_input = FileInfo().request_wfilters({"entity_name": "HighLevelObject"})
    print(NetworkFailure(error_message="Network timeout").get_error_message())
    if bool(valid_input) == True:
        print(get_file_size()) 
    #invalid input example
    #print(NetworkFailure(error_message=12).get_error_message())
