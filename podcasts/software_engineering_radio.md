
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