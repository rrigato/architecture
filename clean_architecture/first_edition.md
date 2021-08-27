- [author](#author)
- [software_guidelines_ch1](#software_guidelines_ch1)
- [functionality_versus_maintainability_ch2](#functionality_versus_maintainability_ch2)
- [programming_paradigms_ch3_ch6](#programming_paradigms_ch3_ch6)
- [solid_ch7_ch11](#solid_ch7_ch11)
- [open_closed_principle_ch8](#open_closed_principle_ch8)
- [liskov_substitution_principle_ch9](#liskov_substitution_principle_ch9)
- [interface_segregation_principle_ch10](#interface_segregation_principle_ch10)
- [dependency_inversion_principle_ch11](#dependency_inversion_principle_ch11)
- [component_grouping](#component_grouping)
- [module_coupling_ch14](#module_coupling_ch14)
- [software_architecture_ch15](#software_architecture_ch15)
- [layer_decoupling_ch16](#layer_decoupling_ch16)
- [architecture_layer_development_approach_ch17](#architecture_layer_development_approach_ch17)
- [boundaries_ch18](#boundaries_ch18)
- [component_abstraction_level_ch19](#component_abstraction_level_ch19)
- [business_rules_ch20](#business_rules_ch20)
- [mapping_code_base_to_architecture_ch21](#mapping_code_base_to_architecture_ch21)
- [architecture_layers_ch22](#architecture_layers_ch22)
- [testable_architecture_ch23](#testable_architecture_ch23)
- [partial_boundaries_ch24](#partial_boundaries_ch24)
- [how_many_layers_ch25](#how_many_layers_ch25)
- [main_ch26](#main_ch26)
- [services_ch27](#services_ch27)
- [testing_ch28](#testing_ch28)
- [firmware_ch29](#firmware_ch29)
# author
Robert C Martin

# software_guidelines_ch1
> architecture is a hypothesis that needs to be proven by the implementation

- software engineering requires a passion for the craft and a desire to be professional
- The goal of software architecture is to minimize the human resources required to build and maintain the desired system

# functionality_versus_maintainability_ch2
- The time it takes to make a change to a software system should be proportional to the size of the feature request, not where the feature request fits in the existing system

- It is easier to maintain a program that is easy to change, but does not meet the current business requirements than maintaining a program that meets the current business requirements but is impossible to change

# programming_paradigms_ch3_ch6

- structured programming taught us that unrestricted direct transfer of control like GOTO statements make it impossible to break down code into small, modular pieces

- We should never use break statements and strongly bias towards if/for loops transfering control to a function call?

- testing shows that a software product is correct enough for our purposes, not that a program is bug free

- Encapsulation and polymorphism are programming techniques that can be implemented just as easily in a functional style as an object oriented class-based style?

- Device independence = strive to make our programs able to complete the same jobs on different devices

- **Dependency Inversion (p.44-46)** = Business Rules(entities/usecase) call the interfaces of of lower level modules (repo/UI/externals)
  - The lower level modules can be developed and deployed independently as long as they implement the design by contract outlined in the interface

- Main entry point calls you usecase as part of the flow of control, but does not depend on anything other than the interface(name of the function) for intializing the program


- There should be a clear separation between immutable and mutable components, where mutable components are encapsulated behind an abstraction/interface and we strongly preference immutable components?


- event sourcing = store all transactions and when state is required, we apply all the transactions from the beginning of time


# solid_ch7_ch11
- The clean architecture is applied at the directory level (repo/entities/usecase), while SOLID is applicable to modules(file name) and components(public interface functions/private implementation functions)?

- Design by contract is validated with test cases for public components?
- For private functions, we are testing to make sure our implementation applies the necessary logic to implement the interface? 
  - These test are independent of interface test cases for complicated applications?
  - Try to test as many components as possible in one test case if there is no external I/O in any of the individual components?

- Don't patch what you don't own, use fakes instead?

- Single responsibility principle guidelines:
  
  - In python, only public functions are allowed to be imported outside a module(file name), while anything that starts with an underscore ```_``` should not be used outside the module?
  
  - In JS, only exported functions/data can be called outside a module(file name)?
    - Should we test complicated implementation, because jest cannot patch non-exported private functions like you can test private functions in python?
    - DHH point that you should only mock external network calls 

# open_closed_principle_ch8
- components should not have circular dependencies, all dependencies should flow in one direction between modules
- if component A needs to be protected from changes in component B, component B should import component A and component A should have no knowledge of component B

- Higher level components should be protected from lower level components by having the lower level components implement interfaces since they are closer to the input/output
  - higher level components use/import these public interfaces, allowing the implementations to be easily modified without affecting higher level structures

# liskov_substitution_principle_ch9
- REST API's should have well defined input/output via an OpenAPI and **consistently** follow these design by contract behaviors reguardless of the implementation

- Having a public functions interface that can easily swap private implementations without affecting the public functions contract is most critical for functions are invoked by other layers


# interface_segregation_principle_ch10
- It is harmful to depend on modules that export more public functions than what you use
  - Where do you set the tradeoff between module initialization overhead versus the decoupling having many modules provides?

- We should preference many small public functions over large functions with lots of parameters that can be reused in different contexts?


# dependency_inversion_principle_ch11
- dependency inversion principle = preference having source code dependencies on interfaces/abstractions, not on concrete implementations

- Statically typed languages enforces the interfaces/abstractions at compile time, where dynamic languages like python are not as strictly enforced, so it is up to the software engineer to design and implement clearly defined interfaces/abstractions

- changes to an interface/abstraction always result in a change in implementation, while an implmentation change can still meet the interface

> Don't derive from volatile concrete classes


- The abstraction/interface components (public functions) contain all the business rules, while the concrete implementation provides the details of how to meet the abstraction/interface



# component_grouping
- For most applications, maintainability is more important than reusability
- Shared libraries must be versioned with an upgrade plan



# module_coupling_ch14
- All module dependencies should be directed acyclic graphs (DAGs) = one way dependencies where it is impossible to follow a modules dependencies back to itself


- Options for breaking cyclical/circular dependencies:



1) Dependency inversion principle = Apply a public interface between two modules you want to reverse the dependency for

![dependency_inversion_principle](breaking_circular_dependencies/dependency_inversion_principle.png)





2) Extract the shared dependency into a new module that has no dependencies

![create_a_third_module](breaking_circular_dependencies/create_a_third_module.png)




- stable dependencies principle = depend on modules that are more stable


- When a component has no dependencies, but is imported in many other components:
  - It is more difficult to change, more stable and independent of other module changes

- When a component depends on many other modules, but nothing imports it:
  - it is easy to change, volatile, and dependent of other module changes

- stable abstractions principle = depend of components that will be extended with the open closed principle instead of modified
  - a functional implementation of this is to never modify public functions but to instead create new ones


- all components (modules/functions/classes) should either be:
1) stable = many other modules import it and closed for modifications
2) unstable = no/few modules import it and able to change out the private implementation frequently.



# software_architecture_ch15

- The tradeoff of microservices is the work needed to configure and connect the different services via service discovery

- Since hardware is cheaper than people, performance efficiency should always be a second tier concern behind ease of development, ease of deployment, minimizing maitenance and minimizing architecture complexity

- Once the high level policy (business rules) is defined (Entities/Usecase), the implementation details can be developed/deployed independently

- Abstract device I/O behind a public interface so the private implementation details can be swapped to make the implementation of your business logic device independent

- Decouple your device dependent storage implementation details from the business rules policy implementation


# layer_decoupling_ch16
- Decouple application specific business rules (input validation, output response) from application independent business rules (calculation logic for costs, custom override critieria, etc.)
- coincidental duplication = two usecases start with the same/similar logic but evolve over time
- Applications should always horizontally decouple across UI/business rules/peristance storage, but when is the tradeoff of creating a new microservice (API, new repo and CI/CD pipeline) worth the extra overhead?


# architecture_layer_development_approach_ch17
- When beginning development, stub your persistance storage I/O so that your usecase layer knows nothing of your storage implementation other than the repo layers public access methods
  - Tradeoff with shape up recommendation to always tackle biggest technical risk first in a cycle iteration if the biggest technical risk is in the application externals (UI framework, new database, etc.)?

- Implementing your core business logic as pure functions makes the business logic more testable and provides a quicker development feedback loop
- The business rules only know about the public contract/function signature of the database layer public interface
  - The repo layer private implementation imports the business rules (entities/usecase), but the business rules only import the repo layer public function interface 

- The UI and database being plugins that are completely dependent on the business rules enables schema changes, database migrations, web framework modifications to be decoupled/irrelevant to the business logic as long as your public contracts are still met


# boundaries_ch18
- The source code of higher level components, processes and services must not contain any specific knowledge of lower level external entry points
  - Example: the usecase layer will never know the URI path for a REST API


- no name of a lower level layer can be known by a higher level layer of abstraction

- The dependency inversion principle is used to ensure the source code dependencies point towards the higher level layers even if the flow of program execution control is dictated by lower level layers.


# component_abstraction_level_ch19
- low level of abstraction is closest to the the I/O, while the highest level of abstraction is furthest from the the I/O 

- source code dependencies should be coupled to how far a module/function is from the I/O, not the order in which data is passed from function to function in the program

- higher level policies change less frequently and for more important reasons from the business usecase perspective

- lower level policies change mroe frequently and for less important reason from a business perspective
  - Example: your end users do not care if the data is stored in a relational database, NoSQL, flat files

- higher level components know nothing of lower level components
- stable abstractions principle = more abstract components should be more stable


# business_rules_ch20
- business rules and business data would exist even if there was no application to automate them


- entities are enterprise-specific business rules that exist in parallel to your application
- usecases are independent of whether the application is delivered on the web, cli, dial up, etc.
- usecases define the application specific business rules that define the interaction between input/output and what entities are used in the process

- usecases depend on Entities from a flow of control perspective, but are defined according to the needs of the usecase by the dependency inversion principle

> we certainly do not want our usecases to know about our HTML or SQL


- usecase should accept and return simple data structures
  - The data structures are not dependent on anything

- Request/Response objects should be independent of entities because they change for different reasons

- business rules should be the most independent/reusable code in the application

- This chapter aligns with the following layer responsibilities:
  - entities = Value objects with just properties
  - usecase = functions that take/return python built ins or entities
  - repo = any external I/O
  - entry = validators to be used across externals, takes ValidRequest objects, returns ResponseSuccess/ResponseFailure objects, calls repo, passes repo results to usecase
   

# mapping_code_base_to_architecture_ch21

- Be aware of the tradeoffs associated with any framework
- The business logic of your application should be testable independent of your database, network connectivity, cloud provider
- architecture of an application should be centered on the business usecases, not whether it is a web app, mobile app, running in the cloud

# architecture_layers_ch22
- all architectures strive for separation of concerns achieved through layered appliction code
- Architecture should consider the high level peristance storage type (NoSQL, distributed, blob, RDBMS)?
- higher level layers should never mention/import lower level layers of abstraction
- adapters (entry and repo layer) = orchestration that converts externals into data structures required by the public contract of usecase/entities


# testable_architecture_ch23
- group modules and components within a layer by whether they are easy or difficult to unit test


# partial_boundaries_ch24
- for a microservice architecture, start with having multiple endpoints deployed from the same repo with separate modules before splitting out into separate repos if needed

# how_many_layers_ch25
- The public contract of an interface should be owned by the user rather than the implementer
- Adding an architectural layer after deployment has begun is incredibly costly, if not impossible without modyfing existing code (breaking OCP)
- public contracts of lower level layers are designed for the needs of higher level layers


# main_ch26
- when running in a lambda function, environment runtime variables, context and event structure are your dependency injection framework for main configuration
- when running code as a process/daemon/service on a server, the os environment variables are your dependency injection framework for main configuration
- software engineers should optimize main to be setup with the minimum configuration/orchestration necessary to invoke higher level layers of abstraction in order to maximize testability


# services_ch27
- architecture should define the layers that separate hgiher level abstractions from lower level implementations
- Service based architectures need to follow the open closed principle when adding functionality
- My criticism of this chapter is the author does not consider teams with polyglot programming language specialities and assumes modification for cross cutting micro services concerns.


# testing_ch28
- tests follow the dependency inversion rule since they are very detailed, concrete, low level implementations
- fragile tests can make a system more rigid if developers are not following the open closed principle
- assertions should not be repeated among different test cases to avoid one change causing cascading test failure


# firmware_ch29
- any software module that needs to change when the underlying hardware changes is firmware
- sql code embedded in your business logic is like firmware since any references to sql would need to be change if the persistance storage layer changes
- a clean architecture is testable indepedent its target hardware
- Do not allow any references to the underlying hardware/platform outside of your repo layer
- A layered architecture is designed around modules depending on well defined and stable public contracts

