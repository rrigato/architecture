- [introduction](#introduction)
- [chapter_1](#chapter_1)
- [chapter_2](#chapter_2)
# introduction

# chapter_1

- "Any Fool can write code that a computer can understand, good programmers write code that humans can understand"
- refactoring does not change a systems external structure, but focuses on incremental improvements to the system design during the development process
  
- first refactor the code to make adding the feature easy, then add the new feature

- local temporary variables make refactoring more difficult as they encourage large functions, replace them with a function lookup call if possible
- Bias towards immutable data
  - mutable state makes it difficult to determine what client made the change to the data

- Always leave the code base healthier than you found it
- The key to refactoring is to take small enough steps to where your unit tests are never failing
  
# chapter_2