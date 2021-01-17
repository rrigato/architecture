## introduction
The goal is to create a microservices based architecture that is as independent as possible

## environment_setup
One Virtual Environment for all projects or one virtual environment per project?

Cookie Cutter template for creating python packages

https://github.com/audreyfeldroy/cookiecutter-pypackage


## test_driven_development
- TDD forces you to clearly define a goal for your function before coding it

- The business requirements are used to write the tests
    - The tests are used to write the code
- Write tests that check the boundaries of your algorithm
- no more than one test case should fail at a time

- No premature optimization = write code that passes the test cases, then optimize later
- Variadic = fancy word the author uses for passing an unknown number of arguements to a function such as *args and **kwargs in python

- A test should fail the first time you run it otherwise there is no point in having to maintain it.

- Test cases should be written such that if any refactoring is done for the project and the test cases still pass, the original business requirements are still met

- Author uses pytest, but I lean towards the built in unittest package
  
- test case naming convention test_<function_name>_<requirement_being_tested> 

- TDD provides a check to ensure that you are not re-introducing bugs when adding new features/patches to an existing code base.

## unit_testing
- Tests should be idempotent (fancy word textbooks use for the same test should have the same result each time)
- 
- You shouldn't test that the external system provides the correct output when given a set of inputs, only that you are calling the external api correctly
  - Tradeoff with patching external libraries that tightly couples you to your implementation
  - Instead of passing in your external dependency as a function arguement and then using a fake as an injection for tests


- The theory is that external systems have followed the same best practices for their internal development for the external api your code depends on
  - Critical to make sure the libraries you use are well maintained since you will not be testing them
  
- CQRS (Command Query Responsibility Segregation) = Differentiation for processes that only consume information data (querying) versus changing the underlying objects (command)

## mocks
- Mocks = use for simulating an object external to your system

- python unittest mock library = callables that be a method or attribute, and you can define these methods/attributes dynamically

- mock library side_effect parameter = can pass callables, iterables, and exceptions that will be invoked when the method is called
- Use a mock object to assign a static return_value response for external systems
- Do not write tests for private methods used within objects, only write them for their public interfaces/apis
  
- Patching = replace globally reachable objects with a mock at runtime
- The goal of TDD is to create a "test suite that is capable of detecting regressions or the removal of important features in the future"