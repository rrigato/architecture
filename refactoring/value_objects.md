# overview
- [value objects](https://martinfowler.com/bliki/ValueObject.html) 
- value objects are equal if the attributes between two instantiated objects are the same
  
- reference objects are equal if there location in memory is the same 
  - example: checking if you have the same reference to an object
  
- value objects should always be immutable

- value objects can be made immutable by not having setters as functions on the class or by returning a deep copy for any getters

- value objects that are created equal should remain equal through immutability 

- value objects are set once on instantiation and have no getters/setters