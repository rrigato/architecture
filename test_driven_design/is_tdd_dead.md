# introduction
6 part discussion on the pros/cons of writing the tests first

https://www.youtube.com/watch?v=z9quxZsLcfo

# speakers
- David Heinemeier Hansson (DHH)
- Kent Beck
- Martin Fowler

## discussion_notes
- All panelists agree that automated testing is absolutely necessary
- DHH argues that tests should talk across layers (entities/domain model and even database repo)
- DHH only mocks external api calls


- Kent argues that you can develop an abstraction layer for a feature that can be represented/tested/mocked independently
  - DHH argues that the mocking is not worth the effort

- DHH = getting reliability from 80% to 99% to 99.999% is an exponential effort 

- There are tradeoffs between the work to mock out different architecture layers to create isolation

- There needs to be feedback loops from the user to the engineer (engineers on call)

- If you are spending more time changing tests, then you are over testing

- If you are not confident that changing the behavior of a program will break a test, you are under testing

- TDD provides confidence and helps you break down large problems into small steps

- TDD works best with well defined small interfaces, not as well with complicated user interface browser

- DHH argues that the benefit is from the test suite and self testing code, not the immediate feedback and isolation from TDD


- TDD goes really well with the clean architecture and cloud computing since all the layers are independent?
    - DHH's testing style works really well for monolithic architectures where you control everything on the server

 