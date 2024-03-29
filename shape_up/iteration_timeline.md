- [introduction](#introduction)
  - [agile_iteration_prequisites](#agile_iteration_prequisites)
  - [week_1](#week_1)
    - [circuit_breakers](#circuit_breakers)
      - [day_1](#day_1)
      - [day_2](#day_2)
      - [day_3](#day_3)
      - [day_4](#day_4)
      - [day_5](#day_5)
  - [week_2](#week_2)
    - [circuit_breakers](#circuit_breakers-1)
      - [day_1](#day_1-1)
      - [day_3](#day_3-1)
      - [day_5](#day_5-1)
  - [week_3](#week_3)
    - [circuit_breakers](#circuit_breakers-2)
      - [day_1](#day_1-2)
      - [day_2](#day_2-1)
      - [day_3](#day_3-2)
      - [day_4](#day_4-1)
      - [day_5](#day_5-2)
  - [week_4](#week_4)
  - [how_to_communicate_progress](#how_to_communicate_progress)
  - [engineer_expectations](#engineer_expectations)


# introduction
Software design phases of a 4 week agile iteration. 

The culmination of every iteration is a shipped product.

Circuit breakers provide hard deadlines where the milestone must be completed or the project is abandonded in order to force tradeoffs.

![iteration_cycle](img/iteration_cycle.png)

## agile_iteration_prequisites
- Engineers have uninterrupted allocation for the full iteration 

- disagree and commit

- Engineers empowered to take feedback as feedback and not as a directive

- Engineers empowered to say no to non-essiential bugs/suggestions/feature requests

## week_1
Conceptual design of public interfaces and modules defined as code

### circuit_breakers

#### day_1
- entities and usecase layer 

#### day_2
- openapi spec for api endpoints

#### day_3
- react UI components

#### day_4
- CI/CD pipeline working
- AWS resources

#### day_5
- independent project scopes/features identified
- repo layer


## week_2
Implementation phase where you prioritize the project scopes with the biggest technical unknowns

### circuit_breakers

#### day_1 
- Demoable project link

#### day_3
- E2E tracer of 1 project scope/feature

#### day_5
- No remaining technical unknowns
- All risks resolved


## week_3
Completion of all remaining project scopes and downhill integration tasks 

### circuit_breakers

#### day_1
- UI style matches shipped product

#### day_2
- All essiential project scopes are complete as E2E tracers

#### day_3
- Integration Testing complete

#### day_4
- E2E automated UI testing complete

#### day_5
- product is shipped and considered done
  
- **No technical debt for future iterations**

## week_4
Cooldown:

- technical skill development/POC's

- Review team best practices, retrospective items, continual process improvement suggestions

- short adhoc requests/technical debt
  
- Shape next iterations bet:
  - Scope hammering to smallest number of features that still improves the current baseline for the customer
  - Time appetite 
  - Fat marker sketch


## how_to_communicate_progress
- hill graph 
- Demoable link 


## engineer_expectations
Software engineers are trusted to do the following:
- Meet the core business requirements
- Unit test code coverage
- Docstrings
- Documentation (README's, user guide, 1 page high level diagram of solution, etc.)