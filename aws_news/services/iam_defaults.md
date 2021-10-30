- users have no permissions by default
- all permissions are implicitly denied by default in an IAM policy


- iam role trust policy is an example of a resource based policy, whereas an iam roles permissions policy is an example of an identity based policy

- role based access control (rbac) = assign privileges based on groups of users

- attribute based access control (abac) = assign permissions based on tags



- resource based and identity based policies are a logical OR unless there is an explicit deny


- identity based policy is a logical AND when used with Organizations SCP/permissions policy

- permissions boundary and session policy does not apply to resource based policies
