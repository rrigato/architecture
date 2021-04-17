# [ian cooper](https://youtube.com/watch?v=SxJPQ5qXisw)

- layered architecture = enables you to avoid acyclic dependencies
- 2 types of business logic:
  - domain logic (business rules)
  - orchestration tasks for application to implement business logic

- clean architecture is about abstracting away low level infrastructure, I/O and framework concerns

- ports and adapters:
  - adapters = low level I/O plugins
  - ports = converts adapters into representation that can be used by the application logic


- usecase and entities layers should have no I/O, be base python, be pure functions, and easy to test
- entities layer = enterprise business rules representing current state as data classes
- usecase layer = application specific business rules and orchestration

- request/response objects
  - validators that provide an abstraction from externals (lambda, frameworks, libraries, UI) trying to call business logic

