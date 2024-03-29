- aws transcribe call analytics = developers provide audio files and transcribe can provide customer and agent sentiment, call drivers, and conversation characteristics such as non-talk time, interruptions, loudness, and talk speed

- sagemaker pipelines supports invoking lambda functions

- ebs supports idempotent device creation by providing a unique client token

- aws appsync supports openid connect, cognito user pools and custom authorization via aws lambda 

- redshift enables central storage of json configuration files that clients need in order to connect via JDBC/ODBC



- third party saas offerings can create custom cloudformation resource types that you can import into your stacks



- cloud watch supports cross account alarms


- rekognition supports identifying video segments such as opening/closing scenes, company logos, content segments, etc.


- aws waf supports managed rule versioning and sns notifications of when a new version is available 





Python 3.6 - 3.9 is now supported for aws lambda

Python 2.7 was deprecated on 2022-09-30

https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html


Glue DataBrew - UI to perform ETL on datasets

CodeBuild supports build result public badges


Cdk assertions library enables unit testing with CDK pipelines


https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.assertions/README.html


Amazon MemoryDB = multi AZ managed version of redis, database recovery


Data lifecycle manager supports ebs snapshots, ami creation and deprecation