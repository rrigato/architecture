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
