# [fault injection simulator](https://aws.amazon.com/podcasts/417-introducing-aws-fault-injection-simulator-fis/)

- [Fault injection simulator](https://aws.amazon.com/fis/) = managed chaos engineering aws offering
- gamedays are important because they let you test monitoring/response protocols that are not typically tested

- fault injection simulator let’s you inject latency to apis, provide metrics to monitor for rolling back

- start in a non prod environment for chaos engineering

- [aws Aurora can invoke a lambda function](https://aws.amazon.com/about-aws/whats-new/2020/12/amazon-aurora-postgresql-integrates-with-aws-lambda/)



# [machine learning service lens](https://aws.amazon.com/podcasts/421-aws-well-architected-machine-learning-lens/)

- machine learning production workloads have different ops considerations than traditional applications:
  - making sure your deployed model has not degraded over time
  - differences between the hardware used to train the model versus the hardware needed to deploy the model

- constantly validate your solution is meeting the business requirements


- ML models have security considerations such as often needing production data in dev environments in order to train the models


# update_podcasts

- [aws constructs](https://aws.amazon.com/solutions/constructs)
provides open source common usecases built on top of the cdk 

- [cdk pipelies](https://aws.amazon.com/blogs/developer/cdk-pipelines-continuous-delivery-for-aws-cdk-applications/)
helps you create a ci/cd pipeline when using cdk