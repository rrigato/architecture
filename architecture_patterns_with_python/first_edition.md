- [chapter_3](#chapter_3)
- [chapter_4](#chapter_4)
- [chapter_5](#chapter_5)
- [chapter_6](#chapter_6)
- [chapter_7](#chapter_7)
- [ch10_events](#ch10_events)
- [ch11_microservices](#ch11_microservices)
- [ch12_cqrs](#ch12_cqrs)
- [ch13_testing](#ch13_testing)
- [epilogue](#epilogue)
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

# ch10_events
- if you can't describe what your function does without using "then" or "and" then you might be violating the single responsibility principle

- commands = sent by one actor to another specific actor with the intent to accomplish something in the system
- events = capture facts about something that happened and sent to all actors

- commands stop processing and raise errors, while events log errors but continue processing other events

- In an event driven system, business logic that must be implemented by the system (or fail automatically) should be issued as a command
  - Cleanup/notification should be completed via events

- There will always be a level of transient background failure from network hiccups, table deadlocks and breif downtime
  - "If at first you don't succeed, retry the operation with an exponentially increasing backoff period"

- Retrying operations that might fail is a good way to improve the resiliency of the system


# ch11_microservices
- You can never completely avoid coupling, what we want to avoid is inappropriate coupling
- microservices are consistency boundaries that should be eventually consistent and allow for the call order of the microservices to be changed easily
- Having microservices communicate via an event bus makes the flow of the application difficult to see and introduces message consistency issues (at-least-once delivery versus at-most-once)

# ch12_cqrs
- reads are cachable and can be stale
- writes are uncachable and must be consistent

- post/redirect/get pattern = post to update a resource and then make an http get to a redirect page

- SELECT N+1 problem = ORM's will query a table once to get all the ID's of the objects it needs and then issue individual queries to return each object

# ch13_testing
```python
#using mock.patch tightly couples you to your implementation
#couples you to import json; json.loads()
@patch("json.loads")

#going to to from json import loads
#is a simple code change but you need to change all of your tests
@patch("loads")
```

- mailhog as a test email server
- every import creates coupling, so think through before doing so

# epilogue
- link cleanup work/refactoring to new feature releases
- each use case should succeed or fail as an atomic unit
- its better to duplicate some code than to have use cases call each other in a long chain

- Avoid having the business domain knowledge become out of step with the technical implmentation of the system by having the business and technical implementation team use the same terminology

- A use case should not call multiple repository interfaces because then it is not making a single atomic transaction
  - ex: first repo interface call suceeds, the second call fails

- idempotency is the key to reliability, because it enables enables retry safe retry of logic

- Inside docker, containers are accessible via their hostname defined as a service name in the docker file, outside docker you need to access via a port specified on localhost

- validate at the edge, the usecase and entities should only be passed valid requests