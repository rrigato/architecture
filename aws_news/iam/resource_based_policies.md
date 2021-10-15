- resource based policies enable a principal to maintain existing permissions in the trusted account while simultaneously being able to use the permissions granted to them in the trusting account which is not allowed in a cross account assume role operation

- iam users, roles, accounts and aws services can be listed as the trusted principal in resource based policies

- roles and resource based polcies only delgate access in a single partition either the standard (aws) partition or china partition (aws-cn) or aws gov cloud (aws-us-gov)

- By default users have no permissions unless they are explicitly granted access, so even if a principal account is listed in the resource policy trust policy, the user must still have a permissions policy in the trusted account enabling permissions in the trusting account