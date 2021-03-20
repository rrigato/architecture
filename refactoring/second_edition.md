- [introduction](#introduction)
- [chapter_1](#chapter_1)
- [chapter_2](#chapter_2)
- [ch3_when_to_refactor](#ch3_when_to_refactor)
- [ch4_testing_best_practices](#ch4_testing_best_practices)
- [refactoring_fundamentals_ch6](#refactoring_fundamentals_ch6)
# introduction

# chapter_1

> Any Fool can write code that a computer can understand, good programmers write code that humans can understand

- refactoring does not change a systems external structure, but focuses on incremental improvements to the system design during the development process
  
- first refactor the code to make adding the feature easy, then add the new feature

- local temporary variables make refactoring more difficult as they encourage large functions, replace them with a function lookup call if possible
- Bias towards immutable data
  - mutable state makes it difficult to determine what client made the change to the data

- Always leave the code base healthier than you found it
- The key to refactoring is to take small enough steps to where your unit tests are never failing
  
# chapter_2

- refactoring is a series of small steps that reduce the total debugging time because each step is followed by running your test suite
- Choose one of adding functionality or restructuring current code at a time
  - iterate between adding new capabilities and refactoring existing code to make addding new features easier

- Make sure your code has everything the developer needs to remember so you do not have to remember it manually

> I am not a good programmer, I am just an average guy with a methodological approach

- Good modularity results in you only having to understand a small subset of the code base to make a change
- Refactoring is a continual part of the development process, not something you set time for

- Refactor to add new features faster, fix bugs faster, and understand code faster, not to have "good engineering practices"
- Integrate with the mainline branch at least once a day and do not have any long lived feature branches
- Refactoring makes your code more modular for performance tuning
  - do not assume you know the bottleneck of your performance issues, use a profiler
  
# ch3_when_to_refactor
- unclear function/variable name
- long functions
- duplicated code
- dicts/objects that are mutated in multiple places
  - encapsulate global data mutation behind functions, all other dicts are passed by value to client
  - limit the scope of where variables can be mutated
- comments explaining bad code
- comments should be used when you need to explain something
- extract a loop/if statement into a function
- mimize the interactions a function has with data/functions outside of its module/architectural layer

# ch4_testing_best_practices
- Writing the test case first enables you to focus on the interface instead of the implementation
- There is a law of diminishing returns with tests, tests should be risk driven

- mutable shared fixtures produce the most difficult to debug errors

> setup -> invoke -> assert -> teardown

  - General test case flow

- Do not let the reality that testing can not catch all bugs stop you from writing tests that catch most bugs
- Before fixing a bug, first write a test that clearly reveals the bug
- Test case creation is an iterative activity that is a first class concern of any software engineer

- test coverage reports are only good for identifying untested areas of code, not for assessing the quality of a test suite

- How confident are you that if someone else introduces a bug into your code it will cause your test suite to fail?



# refactoring_fundamentals_ch6
- change a function name and its parameter names with separate steps of testing in between
- When changing a heavily used interface, create a duplicate function with a different name and migrate clients to the new function name

- add an assert statement when adding a new parameter to make sure all clients are passing in the new arguement

- encapsulating data mutation in a setter function interface helps avoid the problem of needing to simultaneously update clients and your repository to keep everything working

- Return a copy of data for getters

- const prevents that variables data type from changing, but it will not prevent you from mutating attribute values in a JS object

- split phase = when you have two independent calculations populating the same object, turn them into separate functions so you can easily modify the independent calculations without side effects

