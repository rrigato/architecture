- provides openid connect for facebook, google accounts, login with amazon, apple

- provides saml based login for active directory

- user pools = authentication that creates usernames/passwords
  - cognito acts as an identity broker between IdP and AWS

- identity pools = authorization that specifies what aws resources an authenticated (or unauthenticated user) can access via short term credentials via STS

