- route 53 health checks = you provide the IP address or domain name, protocol(https/tcp), frequency of the check and how many consecutive response failures are required to consider the endpoint unhealthy 

- route 53 health checks can publish to cloudwatch alarms triggering an SNS alert if the health check criteria failed


