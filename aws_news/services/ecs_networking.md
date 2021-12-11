1) awsvpc = task gets an Elastic Network Interface and private ipv4
   - only option for fargate launch type
2) bridge = utilizes docker built in virtual network
3) host = bypasses docker virtual network and maps container ports to the ENI of the ec2 instance hosting the task
4) none = no external network connectivity