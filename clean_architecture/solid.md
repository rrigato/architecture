# solid_overview
solid principles created by Robert Martin

Notes from the following sources:
- Clean Architecture by Robert Martin
- Becoming a better developer by using the SOLID design principles by Katerina Trajchevska

# single_responsibility_principle
- A function/class should accomplish only one task.
- Create lots of small functions/components that are accurately named

# open_closed_principle
- Code should be open for extension but closed for modifiction
- Get to the point where you never break the core functionality of your system
- need modular/well defined code
- use polymorphism to enable the same interface to be used for many different implementations

# liskov_substitution_principle
- any derived class should be able to substitute its parent class without clients knowing

# interface_segregation_principle
- a client should not depend on functions it does not use
- Replace large interfaces with small dedicated ones

# dependency_inversion_principle
- High level modules (furthest from I/O where your business logic is stored) should not depend on modules closest to the I/O, they should depend on abstractions
- Only depend on abstractions, so the implementation can be easily switched
  - This is especially important because the closer you get to the I/O, the more likely you are to need to change your implementation


- solid is a tool not an end goal, only use it in cases it makes sense
