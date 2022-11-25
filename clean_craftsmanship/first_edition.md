- Reaching a high percentage of unit test coverage to check a box results in flaky tests

![extreme programming circle of life](images/extreme_programming_circle_of_life.png)

- Test driven development creates a test suite you trust with your professional life

- A passing test suite should provide confidence that all the business rules are met and that your code is deployable to production


- TDD is not coupled to the code, has small cycle times and runs in seconds


**Laws of TDD**
1) write no production code until you have a test case that fails due to the lack of the production code

2) write only enough test code that is sufficient to make the test case fail

3) write no more production code than what is necessary to make the test case pass


- Tests are the safe source documentation for how to invoke/use an interface

- Red -> green -> refactor
- First focus on the functionality then focus on the design structure

- Every engineer on the team leaves the code in a better place than when they checked it out because they know a passing test suite meets the business requirements

- software engineering is breaking down large and complex systems into a set of small problems

- Delete a test case if it requires a large complicated implementation to pass
- Think of test case implementations as involving arrange, act and assert phases
- Behaviour-driven-development = Verify business requirements are met by the system under test by using a given, when, then (GWT) test creation methodology

## mock-types
- dummy = implements an interface to do nothing as the function under test does not require the interface to be implemented, simply passed
