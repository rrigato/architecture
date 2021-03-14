[article link](
https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/)

# recommendation
Read, great info on making systems safe for client retries

# notes

- Many network I/O issues, server errors and rate limit errors can be avoided with a simple retry logic

- Allowing for a retry simplifies client code since you do not need to write a bunch of handler code for fault scenarios

- The mandatory assumption needed for a retry is that an api call can make the same call multiple times without any side effect (idempotency)

- The contract is that a client can make the assumption that any error that isn’t a validation error can be overcome by retrying the request until it succeeds 

- The aws approach is to create a unique ‘session’ for the request by combining the client and the client provided unique identifier

- the process involving  recording the idempotent token and any mutations on your backend must be atomic, consistent, isolated and durable (acid)

- this prevents the scenario where you could record the token, but your backend operation fails, or your backend operation fails but you don’t record the token

- The responses must be semantically equilvalent (same structure and response code, so the client does not need to handle error conditions that might never happen)

- Input validation to store both the client ID and request parameters
- return an input validation error if the client calls with the same token but different request parameters

- idempotency is key to reliability, because it enables the safe retry of logic