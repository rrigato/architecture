
# [andy hunt](https://corecursive.com/029-learn-to-think-andy-hunt/)

- In a production down situation train yourself to take a deep breath, relax and understand the situation logically not in a panic state

- Engineering is not about right and wrong it's about trade-offs and consequences

- Don't try to make your software maintainable or extensible, try to make it replaceable because it is difficult to predict what will need to be maintained or replaced

- The majority of the solutions to your problems will come to you when you are away from a computer so always be willing to step away from your computer and take a break

- Don't document just to document



# [Chris Krycho](https://corecursive.com/034-chris-krycho-typescript/)

- so much of our sense of fatigue comes out of a deep obligation to show that our productivity is continuing to improve



# [Jimmy Koppel](https://corecursive.com/036-jimmy-koppel-advanced-software-design/)

- focus on interfaces in a PR review, not implementations

- the input/output of a function is more important than the method body implementation

- Just getting more experience will not make you a better software engineer, you need to deliberately focus on trying new techniques to continually improve over time



# [jonathan-boccara](https://corecursive.com/loving-legacy-code-with-jonathan-boccara/)
- accept that you will always have to work with legacy code

- Document the specific reasons why the legacy code is bad
  - Criticise only for learning purposes for improving the code 
  - Take ownership of the legacy code
  - Have empathy for the original developer 

- Do not do a refactoring project for legacy code if it does not drive business value

- Don't do documentation just to do it, but because it helps the business
  - Document things because you will need it when you look at this code in the future



# [david heinemeier hansson](https://corecursive.com/045-david-heinemeier-hansson-software-contrarian/)

**their is some profane language in this podcast**


- programming ideology is good, but you need to understand your ideology is a personal truth not a universal for everyone

- Work chat has done cognitive harm because it enables a lower level of reflection than asynchronous responses via email where you actually contemplate your response before typing it

  - The idea that you need to respond to messages immediately at any time is totally disruptive to your workflow

  - Guest makes a convincing argument that if people are not able to just ping immediately, they might actually think through and solve the problem themselves

  - this really opened my eyes, but it is funny that he also has over 50k tweets, when that is such an ephemeral medium



- Guest made an argument for monolithic architectures over microservices because function calls are easier than network calls

   - In abstract they are, but maintaining function changes as a library is much more difficult than maintaining changes of an api network call

- Disagrees with TDD, loves automated testing, but does not like the inner workings of his functions/classes being determined by tests

   - I understand his point of view that it is nice to explore functionality first so you are not writing tests that will not be used

   - The problem is you should have public interfaces defined via the clean architecture before you begin development

   - I think the good compromise here is that you always write the test case for the happy path first (what you want your function to take as input and return as output), then use your manual exploration to further flesh out the implementation details of the test

   - TDD is not that you write all your tests before you write any code just that you start with your test in an iterative process

  - do the same thing with the unhappy path by setting up the test to make sure an exception is thrown/etc.

  - then do manual component testing to flesh out your unhappy path





# [pat helland](https://www.stitcher.com/show/corecursive-with-adam-bell/episode/data-and-scale-with-pat-helland-the-long-view-on-distributed-databases-59756734)

- Think about distributed systems as a series of immutable transactions that whenever you need the current state you calculate all of the historical transactions from the last save point up to the current point time
- 
- Separate the portions of your software workloads that can be replayed without side effects from those that replaying causes side effects 