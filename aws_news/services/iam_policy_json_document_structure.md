- iam json policies consist of optional policy wide information at the top of the json (version and statement) and one or more individual statements providing allow or deny actions
  - AWS evaluates a logical or for each policy statement
  

# example_policy
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "FirstStatement",
      "Effect": "Allow",
      "Action": ["iam:ChangePassword"],
      "Resource": "*"
    },
    {
      "Sid": "SecondStatement",
      "Effect": "Allow",
      "Action": "s3:ListAllMyBuckets",
      "Resource": "*"
    },
    {
      "Sid": "ThirdStatement",
      "Effect": "Allow",
      "Action": [
        "s3:List*",
        "s3:Get*"
      ],
      "Resource": [
        "arn:aws:s3:::confidential-data",
        "arn:aws:s3:::confidential-data/*"
      ],
      "Condition": {"Bool": {"aws:MultiFactorAuthPresent": "true"}}
    }
  ]
}
```

[example policy source](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)  

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