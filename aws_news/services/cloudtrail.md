- cloudtrail trails = enables cloudtrail logs to be written to s3, CW logs, or EventBridge 
  - all regions by default
  - Can trigger SNS of delivery
  - Can be centralized in 1 bucket for an entire AWS Organization
- Default retion is for 90 days
  
- cloudtrail has log file audit integrity validation

- management events = api actions to change aws resources
- data events = change data such as s3 objects/dynamodb items
- 