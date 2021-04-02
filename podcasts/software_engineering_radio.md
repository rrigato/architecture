
# [Vladimir Khorikov](https://www.se-radio.net/2020/07/episode-418-functional-programming-in-enterprise-applications/)
- functional programming occurs when you have no hidden inputs or hidden outputs
  - All mutations are defined within the function body

- Push business logic into your entities and usecase(domain model) while persisting output/state in the repo layer
- Keep your usecase and entities as functional pure as possible and only validate I/O when an object is created