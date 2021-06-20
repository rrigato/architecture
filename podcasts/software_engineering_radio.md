# [shipping software with bugs](https://www.se-radio.net/2021/01/episode-441-shipping-software-with-bugs/)

- after ensuring you are following best practices, ci/cd/tdd/etc. you aren’t going to catch all bugs so just ship

- microservices force you to conform to your design by contract and document your public interfaces

- evaluate 3rd party libraries carefully before integrating into your app

- unit/integration tests are run in a clean environment, the reason bugs only appear when your users get their hands on the product is because prod code has all different types of state that is difficult to anticipate
 
- the software engineer that writes the code should own it
 

# [Vladimir Khorikov](https://www.se-radio.net/2020/07/episode-418-functional-programming-in-enterprise-applications/)
- functional programming occurs when you have no hidden inputs or hidden outputs
  - All mutations are defined within the function body

- Push business logic into your entities and usecase(domain model) while persisting output/state in the repo layer
- Keep your usecase and entities as functional pure as possible and only validate I/O when an object is created

- only throw an exception when something unexpected happens, otherwise perform routine validation

- Perform API validation outside of your entities/usecase layer, because this allows your request object to be backwards compatible to the client's provided input while enabling you to continually refactor your internal business logic

- keep external api calls away from your usecase


# [Alexis Richardson](https://www.se-radio.net/2020/12/episode-440-alexis-richardson-on-gitops/)

- the key to infrastructure as code is git represents the safe source of your system configuration and representation 
- completion of PRs or manual reviews steps should trigger automated deployment

- the next evolution of IaC is orchestration frameworks that can automatically converge to remove drift differences between your definition in git and your current system implementation 

- gitops = you declaratively define your infrastructure as code and push code to your pipeline to deploy containers



# [Adam Barr](https://www.se-radio.net/2019/02/se-radio-episode-357-adam-barr-on-code-quality/)


- the problem with how everyone learns to code is that they are single developers in one code base when production systems rely on many contributors, with many of the original engineers no longer working on the project

- in almost any language, you can make a program do what you want it to do, the problem is when you want to modify it in the future and the original authors are no longer around

- the most important part of working in a production system is the documentation/development of easy to use APIs

- you must understand that code reviews are not a personal attack, but simply a way to improve code quality

- you need to be humble and realize code reviews are not criticisms

- Everything about maintainable large scale systems revolves around developing stable and well defined interfaces

- you need to read a lot of code that is not your own to understand different styles that are accomplishing the same thing

- when you are working in industry you will be spending most of your time fitting into existing systems with large code bases


- just because you made a program do what you need it to do does not make it production quality in the same way that just because you put a bandaid on your elbow does not mean you do not need to go to medical school to be a doctor

- their are few situations where the performance of a program is more important than code readability and maintainability 
