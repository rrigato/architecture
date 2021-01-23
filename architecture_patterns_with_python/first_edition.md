- [chapter_3](#chapter_3)
- [chapter_4](#chapter_4)
- [chapter_5](#chapter_5)
- [chapter_6](#chapter_6)
- [chapter_7](#chapter_7)
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


- structure the interface to your repository layer so that CRUD is an atomic transaction (happens all at once or not at all)

  - make the default for the transaction to rollback and a commit is explict declared in code and only occurs on total success

- How can we keep the details of the connection/session away from our business logic if the connection is being reused

# chapter_7
- optimistic concurrency = client needs to handle errors if updating the same rows as another client on a database
- pessimistic concurrency = server proactively locks rows to prevent multiple clients attempting an update at the same time

- simulate a concurrency error:
  - use time.sleep
  - set a new random version number and call with that same version number twice
- SELECT FOR UPDATE = locks the row you are attempting to update in SQL, other clients will waitin until you update before being able to read
- The key to growable systems depends much more on how the modules communicate as opposed to whether the modules are comprised of classes or functions