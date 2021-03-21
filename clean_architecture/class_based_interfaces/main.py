from externals.request_object_api import CustomerInfo
from usecase.business_rules import customer_count

def invalid_customer_example():
    invalid_customer_request = CustomerInfo().input_validation({"not_a_valid_key": 1234})

    if bool(invalid_customer_request) == False:
        print(invalid_customer_request.get_error_message())


def valid_customer_example():
    valid_customer_request = CustomerInfo().input_validation({"entity_name": "HighLevelObject"})
    
    print(valid_customer_request.get_filters())

    if bool(valid_customer_request) == True:
        print(customer_count()) 


if __name__ == "__main__":
    invalid_customer_example()
    valid_customer_example()

