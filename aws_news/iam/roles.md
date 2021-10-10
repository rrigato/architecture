- iam roles can be assumed by iam users in the same/different accounts, aws services, or third party iDP providers such as SAML/openID

- aws service role = role that you setup for an aws service to assume

- aws service linked role = subset of service roles that is created/tied by a specific aws service

- role chaining = assume role A and then use that to assume role B, time limited to 1 hour
    - regular IAM assumeRole without chaining has a 12 hour max


- delegation of resource you own requires the following:
    - permissions policy = json that specifies what the IAM entity/principal (user/group/role) is allowed to do with the role
    - trust policy = json that defines what IAM entities/principal are allowed to assume the role


- federation = creation of trust between AWS and a third party identity provider such as  Login with Amazon, Facebook, Google(openID connect) or Security Assertion Markup Language (SAML) 2.0, such as Microsoft Active Directory Federation Services


- cross account role = role that grants permissions policy in the trusting account to a principal/entity in a trusted account listed in the trust policy defined by the trusting account