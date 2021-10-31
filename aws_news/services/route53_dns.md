- authoritative name server = knows all the name servers for a top level domain (tld) ex .com


- name server = knows how to route traffic for your domain and sub domain based on the records found in your hosted zone


- dns query = provides an IP address for a client to use to request a resource from a domain name


- dns resolver = 3rd party such as internet service provider that takes the client request and finds the appropriate name server that can return the IP address back to the client


- Domain name system = worldwide connected computers to return IP addresses from human readable domain names


- hosted zones = container of records with the same name as your domain that collects how you want traffic routed to your domain


- time to live (tll) how long you want a dns resolver (recursive name server/ISP) to cache a record before checking with the authoritative name server to get the updated values for that record
