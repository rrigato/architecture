https://pages.awscloud.com/Enabling-Observability-of-Serverless-Workflows-with-AWS-X-Ray_2021_0306-SRV_OD.html

- Step functions can define exponential backoffs and retry criteria of different tasks based on how they returned (error code, timeout)

- Step functions supports dedicated exception handling tasks, running the same task in parallel with different input items, and direct integrations with other aws services (SNS, Lambda, DynamoDB, SQS, APIGW)

- observability encompasses metrics (ram used, function invocation count, function invocation duration), logging (direct messages from application code with a timestamp), and traces (follows a single users journey across multiple microservices and systems)
