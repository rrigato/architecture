- AWS Orgranizations service control policies (SCP's) = maximum permissions for an account or organizational unit (OU) 
  - Sets limit of max identity based policies permissions for IAM entities but does not grant permissons
  - Account admins still need to grant permissions by attaching identity based policies to principals
  - service control policies do not apply to users in the management account 
  - by default all permissions are allowed in an scp for newly created accounts, explicit deny overrides allow
  - scps flow down all levels of the heiarchy no matter how nested your org chart is
  

- consolidated billing = aws organizations feature to get one bill and combined usage tiered pricing across aws accounts

- by default any user with assumeRole in the management account (top of heiarchy) can assume a role with admin privileges in child accounts in the organization hierarchy 

- tag policies can be used to standardize tagging across accounts

