- iam json policies consist of optional policy wide information at the top of the json (version and statement) and one or more individual statements providing allow or deny actions
  - AWS evaluates a logical or for each policy statement
  
```json

```

# statement_elements
- Sid (optional) = statement id to differentiate between statements
- Effect = allow or deny
- Action = aws api calls
- Resource = aws resource arns the actions can be applied to
  - required for permissions policy
  - if you do not include, the resource to which the action applied is the resource to which the policy is attached
- Principal = IAM user/group/role/account to allow access for resource based policies 
  - Cannot be included in IAM permissions policy as the principal is implied by whichever entity is attached
- Condition = boolean selection logic