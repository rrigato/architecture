- [introduction](#introduction)
- [analytics](#analytics)
- [compute](#compute)
- [containers](#containers)
- [database](#database)
- [infrastructure_as_code](#infrastructure_as_code)
- [machine_learning](#machine_learning)
- [miscellaneous](#miscellaneous)
- [networking](#networking)
- [serverless](#serverless)
- [storage](#storage)
# introduction
The theme of reinvent 2020 was new integrations between AWS services, in addition to integrations between aws services and third party SAAS from the AWS marketplace

# analytics
- Connect provides real time sentiment analysis of calls, voice identitification for customer authentication based on the voice of the caller

# compute
- [Ec2 has a MacOs instance type](https://aws.amazon.com/ec2/instance-types/mac/)

# containers
- [ECR Public](https://aws.amazon.com/about-aws/whats-new/2020/12/announcing-amazon-ecr-public-and-amazon-ecr-public-gallery/) = basically docker hub but on aws


- [aws proton](https://aws.amazon.com/proton/) = is a managed deployment service that can help platform teams build pipelines for developers
- 

# database
- [aws redshift federated query](https://docs.aws.amazon.com/redshift/latest/dg/federated-overview.html) = allows you to query across S3, RDS
- [aws redshift naitively supports json](https://aws.amazon.com/about-aws/whats-new/2020/12/amazon-redshift-announces-support-native-json-semi-structured-data-processing/)

- [babelfish](https://aws.amazon.com/rds/aurora/babelfish/) allows you to mnigrate SQL Server clients to Amazon Aurora Postgresql without changing drivers or T-SQL code

- [partiql](https://partiql.org/faqs.html) is a sql language that allows you to use the same syntax across Amazon S3 Select, Amazon Glacier Select, Amazon Redshift Spectrum, Amazon Quantum Ledger Database, dynamodb
  - Doesn't change how the data is stored, but might help with the cloud transition since more developers are familiar with SQL

- AWS Glue supports materialized views


# infrastructure_as_code
- service catalog can group multiple cloudformation templates and metadata into a centrailized product offering

# machine_learning
- [AWS neuron](https://github.com/aws/aws-neuron-sdk) sdk for using aws custom inference and training optimized cpu/gpus

- [aws data wrangler](https://aws.amazon.com/sagemaker/data-wrangler/) visual ui for etl into sagemaker 
- [sagemaker pipelines](https://aws.amazon.com/sagemaker/pipelines/) CI/CD for machine learning
- [sagemaker model monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) detect drift in your prod machine learning model


- Sagemaker supports[ distributed training ](https://docs.aws.amazon.com/sagemaker/latest/dg/distributed-training.html ) across multiple gpus
- Sagemaker supports [edge device](https://aws.amazon.com/sagemaker/neo/) monitoring and deployment
# miscellaneous
- monitron = hardware gateway/monitoring system for e2e equipment monitoring of temperature/machine vibrations/etc.

# networking
- transit gateway support IP multicast for one-to-many notifications

# serverless
- [aws lambda now supports up to 10 gb ram and 6 vcpus](https://aws.amazon.com/about-aws/whats-new/2020/12/aws-lambda-supports-10gb-memory-6-vcpu-cores-lambda-functions/)
- [you can bring your own container image to run a lambda function](https://aws.amazon.com/blogs/aws/new-for-aws-lambda-container-image-support/)
- [lambda billing duration is at the millisecond level](https://aws.amazon.com/about-aws/whats-new/2020/12/aws-lambda-changes-duration-billing-granularity-from-100ms-to-1ms/)

- [lambdci/lambda](https://hub.docker.com/r/lambci/lambda/) = docker image runtime environment for python3.7/python3.8/node/etc.that closely mimics the lambda runtime environment
  - use for running your python source code locally before archiving and uploading to lambda
  - use for building aws layers that contain your application dependencies (pip/npm install) as an archive
  
- [lambda runtime interface emulator](https://github.com/aws/aws-lambda-runtime-interface-emulator) = used to locally test container images you plan to invoke from lambda


# storage
- [EBS gp3](https://aws.amazon.com/ebs/general-purpose/) = improved through and higher I/O that can be changed independently of EBS volume storage size
- [s3 intelligent tiering](https://aws.amazon.com/s3/storage-classes/#Unknown_or_changing_access) = automatically moves objects to lower priced storage tiers based on access patterns

- [s3 replication](https://aws.amazon.com/about-aws/whats-new/2020/12/amazon-s3-replication-adds-support-for-multiple-destinations-in-the-same-or-different-aws-regions/) can have multiple targets in the same or different regions

- [aws s3 ](https://aws.amazon.com/about-aws/whats-new/2020/12/amazon-s3-now-delivers-strong-read-after-write-consistency-automatically-for-all-applications/) has strong read after write consistentcy!!

- [aws s3 supports 2 way replication](https://aws.amazon.com/about-aws/whats-new/2020/12/amazon-s3-replication-adds-support-two-way-replication/)