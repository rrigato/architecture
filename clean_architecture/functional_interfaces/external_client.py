from projectname.validators.create_usecase_name_request import validate_usecase_name

if __name__ == "__main__":
    invalid_request_example = validate_usecase_name(arg1=-5)
    valid_request = validate_usecase_name(arg1=25)

    print("----------Invalid request message----------")
    print(invalid_request_example.error_message)

    print("\n----------valid request filters----------")
    print(valid_request.request_filters)