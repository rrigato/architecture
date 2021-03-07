# introduction
Discussion on the pros/cons of writing the tests first

https://www.youtube.com/watch?v=z9quxZsLcfo

# speakers
- David Heinemeier Hansson (DHH)
- Kent Beck
- Martin Fowler

## discussion_notes
- All panelists agree that automated testing is absolutely necessary
- DHH argues that tests should talk across layers (entities/domain model and even database)
- DHH only mocks external api calls
- Kent argues that you can develop a component that can be represented/tested independently

- DHH = getting reliability from 80% to 99% to 99.999% is an exponent effort 

- There are tradeoffs between the work to mock out different architecture layers to create isolation

- There needs to be feedback loops from the user to the engineer (engineers on call)
 