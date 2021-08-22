https://aws.amazon.com/elasticloadbalancing/gateway-load-balancer/

- aws gateway load balancer allows you to route network traffic to third party vendors for analysis

- aws app config can deploy, monitor and automatically roll back application configuration 

- [amazon certificate manager]( https://aws.amazon.com/about-aws/whats-new/2021/03/aws-certificate-manager-provides-certificate-expiry-monitoring-through-amazon-cloudwatch/) can publish TLS certificate expiration metrics to cloudwatch and events to EventBridge


- [aws secrets manager]( https://aws.amazon.com/about-aws/whats-new/2021/03/aws-secrets-manager-provides-support-to-replicate-secrets-in-aws-secrets-manager-to-multiple-aws-regions/) can automatically replicate secrets from a primary region to other aws regions and keep them in sync on an ongoing basis

- [fault injection simulator]( https://aws.amazon.com/fis/) currently supports chaos engineering for EC2, RDS, ECS

- efs scales automatically and can be used for cloud and on premise applications

- [rds proxy]( https://aws.amazon.com/about-aws/whats-new/2021/03/amazon-rds-proxy-adds-read-only-endpoints-for-amazon-aurora-replicas/) pools database connections and can connect to read only replicas as well

- [s3 object lambda]( https://aws.amazon.com/s3/features/object-lambda/) allows you to run lambda functions to modify an S3 GET object request



- ec2 supports legacy bios boot and [uefi]( https://aws.amazon.com/about-aws/whats-new/2021/03/amazon-ec2-now-supports-uefi-boot-when-migrating-virtual-machines-to-ec2/)

- [aws cloud map]( https://aws.amazon.com/about-aws/whats-new/2021/03/aws-cloud-map-now-supports-api-only-services-in-namespaces-configured-with-dns-resolution/) allows you to give a custom name for ECS, EC2, S3, Dynamodb that you can reference in your applications while changing out the backend IP address or DNS name of those resources

- [kinesis data analytics]( https://aws.amazon.com/about-aws/whats-new/2021/03/amazon-kinesis-data-analytics-now-supports-python-with-apache-flink-v1-11/) instance of Apache flink supports Python 


- [sagemaker supports hugging face transformers]( https://aws.amazon.com/about-aws/whats-new/2021/03/leverage-state-of-the-art-natural-language-processing-with-hugging-face-and-amazon-sagemaker/) which is an open source NLP library