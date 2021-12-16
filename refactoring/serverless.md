- a trade off of serverless is that there is no longer a centralized app server in charge of authentication, orchestration and database logic 


- serverless provides a more loosely coupled architecture that can be modified more cheaply and easily, but requires better monitoring and is more difficult for an individual to have a complete mental model of


- function as a service is about running application code in an ephemeral container, not managing your server systems hardware


- the major difference between faas and paas is scaling and startup latency


- 12 factor processes are stateless and share nothing, any state that needs to be shared must be persisted in a backend database


- the safe source environment for running integration tests for serverless should be the cloud for your CI/CD pipeline, not your local environment 


- bias towards minimizing app logic in your api gateway as it is difficult to test, version control, and define as code
