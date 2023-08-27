
- main point of architecture **what is where and why**
- inversion of control = component maintains an interface that is contstant while the continously changing out the implementation
- the exact lines of where you draw the architecture are irrelevant, the important thing is that you have clearly specified separation of concerns between layers
- Having clearly defined interfaces with black box implementation reduces developer overhead for having to understand how an application is structured when making enhancements
- ```lower``` and ```higher``` layers refer to the level of abstraction away from implementation details
- Entities knows nothing of any of the details of the outer layers, usecase only knows of entities
- pass data to higher level layers using more abstract data types (entities)
- higher layers contain representations of the business concepts, lower level layers handle the details of the real life implementation