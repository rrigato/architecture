from externals.request_object_api import CustomerInfo
from externals.request_network_failure import NetworkFailure
from usecase.business_rules import customer_count

if __name__ == "__main__":
    valid_input = CustomerInfo().input_validation({"entity_name": "HighLevelObject"})
    print(valid_input.get_filters())
    print(NetworkFailure(error_message="Network timeout").get_error_message())
    if bool(valid_input) == True:
        print(customer_count()) 
    #invalid input example
    #print(NetworkFailure(error_message=12).get_error_message())
