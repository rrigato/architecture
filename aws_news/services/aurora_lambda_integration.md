- [aurora mysql](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.Lambda.html#AuroraMySQL.Integrating.NativeLambda) can invoke a lambda function syncronously or asyncronously

```
lambda_sync('<lambda_arn>', '{"json": "payload"}')
lambda_async('<lambda_arn>', '{"json": "payload"}')
```


- [aurora postgresql](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/PostgreSQL-Lambda.html#PostgreSQL-Lambda-invoke) can also invoke an aws lambda function
```SQL
SELECT * from 
aws_lambda.invoke(aws_commons.create_lambda_function_arn('arn:aws:lambda:aws-region:<account_id>:function:<function_name>', 'us-west-1'), '{"example": "json_body"}'::json )
;
```