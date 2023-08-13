## test_driven_development
- TDD forces you to clearly define a goal for your function before coding it

- The business requirements are used to write the tests
    - The tests are used to write the code
- Write tests that check the boundaries of your algorithm
- no more than one test case should fail at a time

- Variadic = fancy word the author uses for passing an unknown number of arguements to a function such as *args and **kwargs in python

- A test should fail the first time you run it otherwise there is no point in having to maintain it.

- Test cases should be written such that if any refactoring is done for the project and the test cases still pass, the original business requirements are still met
  

## unit_testing
- Tests should be idempotent (fancy word textbooks use for the same test should have the same result each time)
- 
- You shouldn't test that the external system provides the correct output when given a set of inputs, only that you are calling the external api correctly

- Assume that external systems have followed the same best practices for their internal development for the external api your code depends on
  - Critical to make sure the libraries you use are well maintained since you will not be testing them
  
- CQRS (Command Query Responsibility Segregation) = Differentiation for processes that only consume information data (querying) versus changing the underlying objects (command)

- Do not write tests for private methods used within objects, only write them for their public interfaces/apis
  

- The goal of TDD is to create a "test suite that is capable of detecting regressions or the removal of important features in the future"