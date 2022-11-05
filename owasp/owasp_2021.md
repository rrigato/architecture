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
