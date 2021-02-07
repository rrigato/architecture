- [introduction](#introduction)
- [database](#database)
- [serverless](#serverless)
- [storage](#storage)
# introduction
The theme of reinvent 2020 was new integrations between AWS services, in addition to integrations between aws services and third party SAAS from the AWS marketplace

# database
- [aws redshift federated query](https://docs.aws.amazon.com/redshift/latest/dg/federated-overview.html) = allows you to query across S3, RDS
- [aws redshift naitively supports json](https://aws.amazon.com/about-aws/whats-new/2020/12/amazon-redshift-announces-support-native-json-semi-structured-data-processing/)

- [partiql](https://partiql.org/faqs.html) is a sql language that allows you to use the same syntax across Amazon S3 Select, Amazon Glacier Select, Amazon Redshift Spectrum, Amazon Quantum Ledger Database, dynamodb
  - Doesn't change how the data is stored, but might help with the cloud transition since more developers are familiar with SQL


# serverless
- [aws lambda now supports up to 10 gb ram and 6 vcpus](https://aws.amazon.com/about-aws/whats-new/2020/12/aws-lambda-supports-10gb-memory-6-vcpu-cores-lambda-functions/)
- [you can bring your own container image to run a lambda function](https://aws.amazon.com/blogs/aws/new-for-aws-lambda-container-image-support/)
- [lambda billing duration is at the millisecond level](https://aws.amazon.com/about-aws/whats-new/2020/12/aws-lambda-changes-duration-billing-granularity-from-100ms-to-1ms/)


- [aws proton](https://aws.amazon.com/proton/) = is a managed deployment service that can help platform teams build pipelines for developers

# storage
