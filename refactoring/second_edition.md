- [introduction](#introduction)
- [chapter_1](#chapter_1)
- [chapter_2](#chapter_2)
- [ch3_when_to_refactor](#ch3_when_to_refactor)
- [ch4_testing_best_practices](#ch4_testing_best_practices)
- [refactoring_fundamentals_ch6](#refactoring_fundamentals_ch6)
- [encapsulation_ch7](#encapsulation_ch7)
- [moving_elements_ch8](#moving_elements_ch8)
- [organizing_data_ch9](#organizing_data_ch9)
- [simplify_conditional_logic_ch10](#simplify_conditional_logic_ch10)
- [refactoring_apis_ch11](#refactoring_apis_ch11)
- [inheritance_ch13](#inheritance_ch13)
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

# encapsulation_ch7
- making updates on dicts/JS object visible and gathered ina single place is key to encapsulation
- Bias towards providing unnecessary copys of collections as opposed to having to debug errors from unexpected dict/js object modifications

- extract calculation behavior into a function to make sure you are not duplicating across a code base

# moving_elements_ch8
- The key to modular design is grouping related components and clearly defining the links between different modules
- modularity = ability to make software design modifications while only understanding a small subset of the design

- apply assertions when refactoring shared data among multiple clients to validate behaviors output by client callers

- Breaking one loop that does multiple things at once into multiple loops each doing one thing makes the code easier to understand and easier to extract into its own functions

- preference using map (applies a function to transform each element in the input collection) and filter (uses a function to select a subset of the input collection) over looping

- remove unused code, not because it is a performance hit, but because it makes it more difficult for the developer to understand


# organizing_data_ch9
- Preference setting a variable only once, because if a variable is set more than once, it is a sign that it has more than one responsibility within a method

- minimize the scope of mutable data by removing variables and replacing them with their calculations/derivations

- Having objects that are pass by copy/value can be confusing if the data is mutable because updates reflecting the mutations will need to be made for each of the client copies


# simplify_conditional_logic_ch10
- Decompose conditional logic and its actions into separate function calls

- For conditional branches that are equally likely:
```python 
if:
  #branch 1
elif:
  #branch 2
else:
  #branch 3
```

- For conditional logic that is unusual/unhappy path, use a guard clause:
```python 
if (_invalid_input):
  return("error - wrong datatype ")

#proceed with happy path logic

```


- use a factory function that initializes an object using polymorphism based on the arguement input/object type passed

- assertions for expected code paths are a dry violation of a public interfaces design by contract

- extract reused conditional checks into a dict/record into a function that is returned using deepcopy


# refactoring_apis_ch11
- separate functions that query with no side effects from those that modify with side effects


- replace any function that uses flag arguements with explicit function calls


- Balance the responsibility of providing the needed input for a function between the caller (via a function arguement) and the function body(obtain value via query) with the objective of having as many pure functions as possible (functions that idempotently give the same output for a given input)


- To get around constructor limitations (like python ```__init__``` having to return ```None```), wrap the class instantiation into a factory function that instantiates/returns the object while applying any custom business logic

# inheritance_ch13
- if you can change and understand the base class without breaking/understanding the sub class, then inheritance might be a good fit

> favor object composition over class inheritance

- create a new object that provides the needed functionality that the base class calls instead of creating subclasses 

- Do not use inheritance if every method on the supertype does not apply to the subtype

- Do not use inheritance if the subclass can be easily broken/is tightly coupled to the superclass

- The impression that the function based refactorings averaged 3-5 pages while the inheritance based refactorings were 5-15 pages on average demonstrates while I bias towards function based solutions