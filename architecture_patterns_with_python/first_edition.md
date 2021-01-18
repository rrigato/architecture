- [chapter_3](#chapter_3)
- [chapter_4](#chapter_4)
- [chapter_5](#chapter_5)
- [chapter_6](#chapter_6)
# chapter_3

- write your use case business logic so that it does not contain any state or I/O
- write tests that invoke the whole system but fake the I/O
- Makes the arguement that patches couples your test code to your implementation details
- Makes the arugement that overuse of patchesmocks makes the tests much mroe complicated and difficult for explaining the code


- fakes (stubs) = working implementation of the thing you are replacing but only used for the tests
  - Make assertions about the end state of the system instead of testing the behaviors along the way
- spies/mocks test how something was used
- fakes/stubs = allow state to be gathered in tests and validate that state in assertions

- you can make systems easier to maintain if you have an interface between your business logic and I/O

# chapter_4
- dependency inversion principle = the usecase layer depends on the repository abstraction and the implementation details in the repository also depend on that abstraction
- test web stuff as E2E tests

# chapter_5
- if you extend the existing functionality while keeping your existing code closed for modification, you will not need to modify each existing test

- aim for 1 e2e test per feature where error handling counts as a feature
- test the happy path for each feature and 1 e2e test that covers all the unhappy paths (with many unhappy path unit tests)

# chapter_6
- Unsure if I agree with the rule of thumb "dont mock what you dont own" when it comes to third party libraries such as pyodbc/request?
  - Idea is you should only mock the interface so each component has exactly what it needs and nothing more

- make the default for a database transaction to rollback and a commit is explict declared in code and  only occurs on total success
