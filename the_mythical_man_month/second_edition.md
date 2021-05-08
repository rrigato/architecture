- [ch1](#ch1)
- [ch2_estimation_myths](#ch2_estimation_myths)
- [ch3_team_structure](#ch3_team_structure)
- [ch4_architecture_versus_implementation](#ch4_architecture_versus_implementation)
- [ch6_team_structure](#ch6_team_structure)
- [ch8_project_time_estimation](#ch8_project_time_estimation)
- [performance_optimization_ch9](#performance_optimization_ch9)
- [documentation_ch10](#documentation_ch10)
- [throw_away_design_ch11](#throw_away_design_ch11)
- [developer_tooling_ch12](#developer_tooling_ch12)
- [debugging_ch13](#debugging_ch13)
- [project_estimation_ch14](#project_estimation_ch14)

# ch1

- The difference between a program that runs and a program that is a product offering is that the latter is generalized, well documented/tested with defined interfaces
- As soon as one freezes the design it becomes obsolete, but implementation of real products demands versioning
- The obsolesence of an implementation can only be measured when compared against other existing implementations, not unrealized concepts

# ch2_estimation_myths
- The number of software engineers does not always result in a decrease in development time because software construction is a systems effort with complex interdependencies
  - If task can be partioned without communication, men and months are interchangeable
  - For complex systems, communication and strategy onboarding takes up more time than is saved by dividing up tasks among more software engineers

- The author argues that 50% of the time estimate should be devoted to system integration testing
  - Misallocating the integration estimate can be costly because it has to be done at the end of the development life cycle right before the product is ready to ship

- The number of months depends on how sequential the components of the software product are
- The number of man-hours depends on how independent the sub tasks are
  - Adding men will not reduce the number of months because of the increased training, communication, and integration testing time between indepedently developed components

# ch3_team_structure
- The author argues that the architecture ultimately comes down to the team lead and copilot.
  - copilot provides feedback, but the ultimate decision authority comes down to the team lead

- Everyone else on the team is a specialist (devops/platform engineer, language specialist, component/integration tester, documentation reviewer)

- Increasing the number of developers with architectural input results in increased communication costs and increased miscommunication costs (system debugging)

# ch4_architecture_versus_implementation

- Architecture is the complete detailed specification of what the interface is while implementation is how the interface is delivered

- Architecture specification should be created by the team lead and copilot to ensure the unity of a system
- 
- The goal of having a few architects design the specification is because it allows for conceptual integrity across the system implementations

- Good design is measured by the ratio of functionality to ease of use


# ch6_team_structure

- The lead architect and copilot must define every detail of the public interfaces, but leave the private implementation details to the developer

- Having your code be your documentation can lead to ambigouity for whether a side effect is intended for the interface or just a bug
- Have a written proposal for bugs/problems/discussion points sent out before the meeting
  - If a consensus is formed in the meeting, go with that, otherwise the lead architect has the final say

- Questions that arise during the implementation should be immediately documented in the readme
  
# ch8_project_time_estimation
- programming effort is exponentially related to program size
  - "Linear extrapolation of the 100 yard dash shows that humans can run a mile in under 3 minutes"
  - 
- Author posits that developers only spend 50% of their allocated man hours doing technical work, with the rest of the day filled with meetings, short term firedrills, support, etc.

# performance_optimization_ch9
- System architects must maintain vigilance throughout an implementation that all interfaces match their required specifications

# documentation_ch10
- Creating a design documentation before beginning implementation enables clear and exact interfaces

# throw_away_design_ch11
- Plan with the assumption that the first version of a large scale system will barely be usabe and will almost always require a version 2 redesign

- The user need and the perception of that solution will change as the program is built, tested and used

- Attributes that encourage code to be open for extension but closed for modification:
  - Careful modularization
  - extensive subroutining
  - complete specification of inter-module interfaces

- Every product should have its own numered version and release date

- The reluctance to document design is not that the developer is lazy, just that once the designs are documented the developer opens himself up to criticism on every design decision made

- The author posits that software maitenance is roughly 40% of the time it takes to develop the software originally

- Maitenance/support work is lineraly related to the number of users, because more users find more bugs

- The problem with maitenance work is that often fixing one bug introduces another if you do not have a strong test suite for regression testing

- The total number of modules increases linearly with each new feature realease, while the number of modules impacted/changed by each feature release increases exponentially over time

# developer_tooling_ch12
- sustained concentration reduces thinking time, one 4 hour block is more effective than 6 1 hour blocks spread throughout a day
- it is important to have your local dev computer be able to consistently emulate your target prod environment across a team
  - Does not need to perfectly emulate prod, but the local testing must be dependable/repeatable

- Use a PR from the implementer to the architect to gate integration of components and the CI/CD pipeline merging from a dev branch to a master branch as marking the progression from feature branch to integration to release

- The IBM OS/360 documentation was 6 feet tall to demonstrate that the key to good docs is that they are modular
- The user should have the option treat docs as a library, not trying to read everything, but able to easily find what they are looking for


# debugging_ch13
- Architect a system starting from the top-down design of modules/interfaces, while stubbing lower level functions, through a series of refinement steps without getting into implementation concerns
  
- The use of clean, debugged components saves time in system, integration and E2E tests
- Invest heavily in test fixture sacffolding that can be reused
- There should be a clear distinction between quick patches and well thought through, tested, and documented bug fixes

- Assume your system has many bugs, snake them out by only adding one component/changing at a time


# project_estimation_ch14
- Have concrete, sharp edged milestones that are atomic instead of vague phases of planning, coding and debugging
  - Is the business usecase complete or not?

- When discussing a project with your boss, it is important to differentiate between status updates that ar meant to keep your boss in the know versus escalation updates where you are requiring action from your boss


# documentation_ch15
- highly recommend
- Focus on having a one page high level overview flow chart of the application

- multi page flow charts are a dry violation because they can be generated from the code

- minimize documentation burden by having function docstrings as the safe source of information in your program

- Bias towards block comments that explain why you are doing something over line comments that explain what a program does syntactically

# no_silver_bullet_ch16
- highly recommend, a precsient and seminal chapter written in 1986
- abstract data type = object type is defined by a name, set of attributes, and a set of functions rather than how the object is persisted in storage

- the time consuming part of software engineering is the specification/design/testing of how data structures/interfaces/algorithms interact, not the implementation of these representations as code


- multipage flow charts are often done after the software was designed and constantly out of date with the implementation


> the hardest part of a software task is arriving at a complete and consistent specification, and much of the effort of building a program is the dubugging of the specification


- It is impossible to completely specify the exact requirements of a software system without having the users trying some built version of the software and providing feedback

- the point of a prototype is to provide a tangible/real demo of the conceptual requirements so that the user can iterate/validate the requirements without the software engineer taking the development time to go from POC to prod
- Design software top down by first making it run, even if all sub modules are stubbed out


# no_silver_bullet_1995
- Because the architecting of interfaces, data structures, and algorithms will always be the most time consuming portions of software engineering, upgrades to tooling or runtime environments will never produce the 2x YoY improvements seen in the hardware space

- Fight the problem of software complexity heiarchially (layered modules and objects) and incrementally (adding new features one at a time so the system is always in a working state)
- Focus on building abstract data types that align with the business domain terminology

# key_takeaways
- programming projects converge more slowly as they near completion due to system component/integration testing
- Adding more engineers to a project increases communication and training effort
- Teams should be organized around a team lead and a copilot, final architectural decisions come down to the team lead
- Conceptual integrity is the most important consideration in system design

- Separate the definition of architectural interfaces from the implementation
- when delegating tasks, each developer does not know/care about the private implementation details of the interface they are using


- Maitenance costs is linearly related to the number of users you have, as more users find more bugs
- Most projects fail to provide a digestable high level architectural overview in the readme
- Focus on block comments describing why a block of code is doing something non-standard


- The architect is the user's agent representing their requirements as interface specifications
- Having a system architect who is responsible for the entire e2e conceptual integrity is central to product quality
- Prefence simple applications that do one thing well
- Have tangible, explicit and measurable user requirements 
