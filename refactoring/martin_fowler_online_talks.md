- [introduction](#introduction)
- [refactoring](#refactoring)
- [event_based_architectures](#event_based_architectures)
# introduction
General notes from online talks provided by Martin Fowler

# refactoring
- the way to get performance improvements is to have small, modular, well named code
  - Then it will be easy to run a profiler to determine where your code is experiencing performance bottlenecks and focus your effort on efficient performance tuning

- Do not change the external behavior of the program while you are refactoring, just make sure the tests pass
- Mean time to recovery (MTTR) is more important than mean time between failure (MTBF)
  - More important to quickly identify and fix failures
- team size = 2 pizza teams that have some customer facing responsibilities with autonomy
  - everything they need technically and access to users
- team should be technically led, trust is key
  - learning ismore important than blaming

# event_based_architectures
- benefits of adding events to an event bus/queue is that it decouples your dependencies from the system gathering the event
  - downside si you no longer have a single view of the entire system
- event sourcing = you can always recover the current state by running through the event logs (version control method of events)
  - take a snapshot to improve performance
  - Need to think through the versioning of events if you need to make a change historically

- Command Query Responsibility Segregation (CQRS) = separate write workload from the read workload 
