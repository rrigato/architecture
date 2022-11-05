## a01-broken-access-control
- unathenticated user can unintentionally access the application
- API GET method is authenticated but POST/PUT/DELETE are not
- CORS configuration

## a02-cyrptographic-failures
- Use a DNS provider that automatically renews SSL certs so you do not have to keep track yourself

## a03-injection
- Keep amount of input data from external sources to a minimum
- Use well tested parameterized queries
- Trace through user supplied input before release but after a time break in the PR specifically looking for bad input practices
- Validate input type using built-in's before type casting 
- ```str.isnumeric()```, ```str.isalpha()```, etc.

# a04-insecure-design
- An interesting point from this section is that part of the requirements gathering with the user should invole a discussion over the tradeoffs of different levels of security redundancy

- If security validation is not provable via unit and integration tests that are invoked with each pipeline run, then you are performing security theater instead of actual security

# a05-security-misconfiguration
- Plan for how you are going to upgrade the underlying software and negotiate the life expectancy requirements of the application before developing 
- Specifically around dependencies if the underlying infrastructure is managed
- review application flow to ensure stack trace inforamtion is not propagated to user
- ensure that service roles are being used to avoid having to manage credentials with your cloud provider