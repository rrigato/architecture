# routing_policies
- simple = return a single IP Address for one resource
 
- multi value = return multiple IP addresses of endpoints passing health checks


- geolocation = Different IP Address per country client IP address or a default IP address if no location info is found on the client IP address 
  
- geoproximity = IP address closet to client ip requestor location, you can add a bias to expand shrink the size of a geographic region

- weighted = set percentages for which IP address to return
  
- failover (active passive) = return different IP addresses based on resource health status

- latency based = return the IP address with the lowest latency
