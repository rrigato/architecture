# values
- kaizen = take ownership of constantly improving your work
- when you miss a delivery expectation, provide options not excuses
- fix broken windows of bad code design, implementation and roadblocks as soon as they appear
- make quality and scope part of the requirements
- Make a habit of investing in your technical skills by diversifying and managing risk of knowledge gaps in new technologies/programming environments you are not familiar with
- software engineering values help you make quick decisions by consciously re-enforcing self-discipline
- evaluate each design decision in terms of how easily it can be changed in the future

# communication
> the meaning of your communication is in the response you get

- prepare before communicating, prioritize listening to your audience, consider the correct time to present the material, apply MVP to all communication/meetings
- focus non-api commenting on why something is done because the code shows how it is done, keep DRY in mind
- email is permanent so make sure to reflect before sending and maintain the habit of not complaining no matter the recipient

# dry
- every piece of knowledge must have a single, unambiguous, authoritative representation within a system
- whenever a module exposes a data structure it couples your implementation to that data structure
- be cognizant of duplicating business logic in docstrings and the implementation of private functions

# decoupled_systems
- modules should never expose any unnecessary interfaces, never rely on other modules implementations, and have any context passed in as parameters
- implementation changes should be localized to a specific unit test case 


# reversability
> nothing is more dangerous than an idea if it is the only one you have

> there are no final decisions

- delay and hide critical implementation details (3rd party api's, database schemas) behind your own abstraction layer interfaces


# e2e_tracers
- prioritize critical requirements and the biggest technical risks first with each tracer
- build apps with production intent e2e across architectural layers with the smallest functionality that improves the existing customer baseline

![images/e2e_tracer.png](images/e2e_tracer.png)

- prototypes are disposable and focus on testing a specific aspect of a system
- use a UI tool that focuses on appearance/interactions without spending time on the code/markup


# tooling
- the best format for persisting data is plain text because it can be understood without the application logic, parsed in any programming language, and outlives the lifespan of the application that created it