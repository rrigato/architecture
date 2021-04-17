
- usecase and entities layers should have no I/O, be base python, be pure functions, and easy to test

# entities
- entities layer = enterprise business rules representing current state as data classes

# repo
- I/O with persistant storage, apis, 3rd part libraries or frameworks
- returns (return_val1, None) is successful
- returns (None, string_representation_of_error) if there is an error
- Can return multiple values as long as the last value returned is either a string error or None

# usecase
- usecase layer = application specific business rules and orchestration

# validators
- request/response objects
  - validators that provide an abstraction from externals (lambda, frameworks, libraries, UI) trying to call business logic
