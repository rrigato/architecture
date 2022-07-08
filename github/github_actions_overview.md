- workflows = Automated tasks triggered by yaml file events located in ```.github/workflows``` 
- event types = source control repo events, external api call, or triggered on a schedule
- jobs can be run in parallel, steps within a job are ordinal and can share dependencies
- ```actions``` = reuse repetive complex tasks:
  -  checkout code/setup build environment
  -  pull action from docker hub
  ```yaml
  - uses: actions/checkout@v3
  ```

- ```actions syntax``` = ```<github_user_owner>/<repo>@<version_reference>```