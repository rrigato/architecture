- engineers should be empowered to use any solution architecture they think works best, along with the responsibilities that come with the design decisions they make
- teams should be **highly aligned, loosely coupled** with the same goal but freedom to implement how they see fit

- complex systems = any system where one person is unable is incapable of having a complete understanding 
- It is crucial to understand the HTTP level (4xx/5xx) codes a system will return in a fault scenario to handle errors gracefully
- client induced retry storm = user clicking refresh 50 times causes 50 api calls flooding the downstream service