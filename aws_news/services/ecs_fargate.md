- must set networking mode to awsvpc which provides 1 elastic network interface per task

- requires an IAM execution role to pull from ECR, secrets manager and write to cloudwatch

- Need to assign a fargate task Elastic network interface a subnet and security group