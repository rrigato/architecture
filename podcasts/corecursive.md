
# legacy_code
[podcast link](https://corecursive.com/loving-legacy-code-with-jonathan-boccara/)
- accept that you will always have to work with legacy code

- Document the specific reasons why the legacy code is bad
  - Criticise only for learning purposes for improving the code 
  - Take ownership of the legacy code
  - Have empathy for the original developer 

- Do not do a refactoring project for legacy code if it does not drive business value

- Don't do documentation just to do it, but because it helps the business
  - Document things because you will need it when you look at this code in the future




# [Chris Krycho ](https://corecursive.com/034-chris-krycho-typescript/)

- so much of our sense of fatigue comes out of a deep obligation to show that our productivity is continuing to improve



# [Jimmy Koppel](https://corecursive.com/036-jimmy-koppel-advanced-software-design/)

- focus on interfaces in a PR 

- the input/output is more important than the method body

- Just getting more experience will not make you a better software engineer, you need to deliberately focus on trying new techniques to continually improve over time


# [david heinemeier hansson](https://corecursive.com/045-david-heinemeier-hansson-software-contrarian/)

**their is some profane language in this podcast**

- architecture astronaut = you can get so up in the weeds of designing a system but never build it, so high in the clouds you run out of oxygen 

- programming ideology is good, but you need to understand that ideology is a personal truth not a universal for everyone

- chat has done cognitive harm because it is a lower level of reflection than full fledged asynchronous responses via email

- The idea that you need to respond to messages immediately at any time is just totally disruptive to your workflow

- made a really interesting argument that if people are not able to just ping immediately, they might actually think through and solve the problem themselves

   - this really opened my eyes, but it is funny that he also has over 50k tweets



-made an argument for monolithic architectures that function calls are easier than network calls

   -in the abstract they are, but maintaining function changes as a library is much more difficult than maintaining changes of an api network call

-Disagrees with TDD, loves automated testing, but does not like the inner workings of his functions/classes

   -I understand his point of view that it is nice to explore functionality first so you are not writing tests that will not be used

   -the problem with this is you want to have the public interfaces defined via the clean architecture before you begin development

   -I think the good compromise here is that you always write the test case for the happy path first (what you want your function to take as input and return as output), then use your manual exploration to further flesh out the details

   -TDD is not that you write all your tests before you write any code just that you start with your test in an iterative process

   -do the same thing with the unhappy path by setting up the test to make sure an exception is thrown/etc.

    - then do manual component testing to flesh out your unhappy path





