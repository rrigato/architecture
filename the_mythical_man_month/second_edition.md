- [ch1](#ch1)
- [ch2_estimation_myths](#ch2_estimation_myths)
- [ch3_team_structure](#ch3_team_structure)
- [ch4_architecture_versus_implementation](#ch4_architecture_versus_implementation)
- [ch6_team_structure](#ch6_team_structure)
- [ch8_project_time_estimation](#ch8_project_time_estimation)

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