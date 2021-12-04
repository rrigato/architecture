1) launch constraint = IAM role service catalog assumes when deploying a product on the users behalf
2) template constraint = restrictions on what the user can pass to the underlying cloudformation template as parameters
3) stackset constraint = multi-region/multi-accounts
4) notification constraint = sns topic to provide updates about a selected products deployment status
5) Tag update constraint = allow/disallow tags 