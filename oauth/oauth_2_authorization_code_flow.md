1) client directs resource owner user-agent to authorization server with client_id, request_type, scope and state
2) authorization server authenticates resource owner and gets authorization from the resource owner for the scope requested by client

3) authorization server returns an authorization code to the callback uri of the client along with state parameter
```HTTP 
HTTP/1.1 302 Found
Location: https://client.example.com/callback_url?code=<authorization_code>
```

4) client exchanges authorization code for access and refresh token using http post by providing their
client secret to the token server:
```HTTP
POST /token HTTP/1.1
Host: server.example.com
Content-Type: application/x-www-form-urlencoded

grant_type=authorization_code&code=<authorization_code>&redirect_uri=https://client.example.com
```

- note that the client contacts the token server directly not through the user-agent