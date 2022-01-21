1) client directs resource owner user-agent to authorization server with client_id, request_type, scope and state
2) authorization server authenticates resource owner and gets authorization from the resource owner for the scope requested by client
3) authorization server returns an authorization code to the callback uri of the client along with state parameter
4) client exchanges authorization code for access and refresh token
