- software design is the process of alternating between decomposing a large system into small pieces that can be developed/understood independently and continually modifying those independent interfaces to reduce complexity
- complexity is anything related to a software system that increases the difficulty of understanding and modifying the system 

- most of the code in any complex system is written by extending existing interfaces
- a top tier design concern is minimizing the resource hours required for extending an interface 

# iceberg_interfaces_ch4

- function signature = interface of a function comprising everything you need to know as the invoking client
  - names/types of parameters, names/types of return values, exceptions thrown

- interfaces should be designed to make the common case as simple as possible

# information_hiding_ch5
- temporal idempotency = a function/module/usecase produces the same output reguardless of the order it is run in


# general_modules
- A module's functionality should meet today's current needs but it's interface can be designed with future business usecases in mind
- it is more important for a function to have a simple interface than a simple implementation
- configuration parameters provide an example of a module delegating behavior of a solution instead of solving it themselves internally

# interface_splitting
- avoid using the extract function refactor when the extracted function has a complex interface
- two interfaces should be combinded in the client always needs the output of the first interface in order to invoke the second interface
- blocks within ```if/else/while``` should be one line long, preferably with function calls

# exception_handling
- secondary exception handling during recovery from primary exceptions are often more subtle and complex
- exceptions thrown by a function are part of its interface

# design_it_twice_ch11
- design multiple interface/implementation options with a time break in between on a piece of paper before selecting the optimal solution
- the most important consideration of an interface is the ease of use for higher level software
- when smart people are growing up, they often discover their first idea solves the problem, resulting in bad work habits that stifle their development

# comments
- if a client needs to read the function implementation in order to use an interface, no abstracton of complexity is being provided by the interface
- strive to have interface docstrings that abstract complexity/compress cognitive load and implementations that are straight forward enough to not need comments

- developers should be able to understand the abstraction provided by an interface without reading any code outside of its docstring and public contract
- function implementations should assume all function contract/docstring prequisites are met
- docstrings should capture all side effects(exceptions raised, data structures modified, changes to persistant storage)

- comment types:
1) interface comments = defines the abstraction by telling the client what they need to know to invoke the interface
2) implementation comments = describes the details of the abstraction implementation

- keep implementation details out of interface comments
- Have a safe source getting started readme that leverages stable urls for external documentation and is linked to by all git repositories readmes