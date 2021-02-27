- [introduction](#introduction)
- [chapter_1](#chapter_1)
- [chapter_2](#chapter_2)
# introduction

# chapter_1

> Any Fool can write code that a computer can understand, good programmers write code that humans can understand

- refactoring does not change a systems external structure, but focuses on incremental improvements to the system design during the development process
  
- first refactor the code to make adding the feature easy, then add the new feature

- local temporary variables make refactoring more difficult as they encourage large functions, replace them with a function lookup call if possible
- Bias towards immutable data
  - mutable state makes it difficult to determine what client made the change to the data

- Always leave the code base healthier than you found it
- The key to refactoring is to take small enough steps to where your unit tests are never failing
  
# chapter_2

- refactoring is a series of small steps that reduce the total debugging time because each step is followed by running your test suite
- Choose one of adding functionality or restructuring current code at a time
  - iterate between adding new capabilities and refactoring existing code to make addding new features easier

- Make sure your code has everything the developer needs to remember so you do not have to remember it manually

> I am not a good programmer, I am just an average guy with a methodological approach

- Good modularity results in you only having to understand a small subset of the code base to make a change
- Refactoring is a continual part of the development process, not something you set time for

- Refactor to add new features faster, fix bugs faster, and understand code faster, not to have "good engineering practices"
- Integrate with the mainline branch at least once a day and do not have any long lived feature branches
- Refactoring makes your code more modular for performance tuning
  - do not assume you know the bottleneck of your performance issues, use a profiler