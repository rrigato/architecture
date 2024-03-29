# feb_2021_service_announcements
- [x ray insights](https://aws.amazon.com/about-aws/whats-new/2021/02/insights-is-now-generally-available-for-aws-x-ray/) = anamoly detection for applications run through x ray
  
- [cloudwatch synthetics](https://aws.amazon.com/about-aws/whats-new/2021/02/amazon-cloudwatch-synthetics-supports-amazon-api-gateway-api-blueprint/) Has a low code integration for monitoring api gateway resources/query parameters and headers in the same region
  
- [aws copilot](https://aws.amazon.com/containers/copilot/) = cli tool for deploying containers to Aws


- [cloudfront savings bundle](https://aws.amazon.com/about-aws/whats-new/2021/02/introducing-amazon-cloudfront-security-savings-bundle/) = enables you to commit to a certain amount of cloudfront spend and get a 30% discount with WAF included

- [dynamodb local](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html) = docker image that you can run locally instead of testing on dynamodb directly

- [aws ecs service discovery](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html) = refer to a service by name and the dns is looked up by the service dynamically at runtime

- [alb](https://aws.amazon.com/about-aws/whats-new/2021/02/application-load-balancer-supports-application-cookie-stickiness/) supports using a custom cookie for making sure a user stays on the same load balancer
- [aws glue has a feature](https://aws.amazon.com/about-aws/whats-new/2021/02/aws-glue-provides-column-importance-metrics-findmatches-machine-learning-transform/) that can identify duplicate records without the dataset having a primary key
- [aurora global tables](https://aws.amazon.com/about-aws/whats-new/2021/02/amazon-aurora-global-database-supports-managed-planned-failover/) have a primary region for writing and additional regions for reading that can be automatically failed over to
OpenId Connect sits on top of oauth 2.0 and enables you to pull login and profile information about users
- [flutter](https://aws.amazon.com/about-aws/whats-new/2021/02/announcing-general-availability-amplify-flutter-data-authentication-support/) a google sdk for iOS and Android development is supported by amplify
Amplify data store enables development for a user syncing data across multiple devices and online/offline syncing
- 10DLC [ten digit long codes](https://aws.amazon.com/about-aws/whats-new/2021/02/amazon-sns-now-supports-sending-sms-messages-to-us-destinations-using-ten-digit-long-codes-and-toll-free-numbers/)a new standard for application to human text messaging enforced by phone carrier and supported by aws pinpoint and SNS
- [Redshift query editor](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor.html) = run sql queries in the Aws console without jdbc or odbc drivers
- Aws waf can parse and [inspect json](https://aws.amazon.com/about-aws/whats-new/2021/02/aws-waf-support-json-body-inspection/)


- [config conformance pack](https://docs.aws.amazon.com/config/latest/developerguide/conformance-packs.html) = yaml collection of customer rules/remediation actions for AWS Config