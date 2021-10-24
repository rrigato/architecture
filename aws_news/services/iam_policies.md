- identity based policies = attach to iam entities (users/groups/roles)
- resource based policies = attach inline permissions to resources that the principal (either your account or a different aws account) specified in the policy is able to use 
- permissions boundaries = maximum permissions the IAM entity (user/group/role) can grant to another entity, does not grant permissions or affect resource based policies 

- access control lists (ACL's) = legacy xml that only allows access for principals in another aws account

- session policies =  limit the maximum permissions that a role or identity based policy can grant to an entity who performed an ```AssumeRole``` api call
  - Limits max permissions to the union of the identity based policy, resource based policies, and session policy but does not grant permissions