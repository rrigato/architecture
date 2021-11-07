- encrypted end-to-end connection using IPsec where the client connects using a VPN client (openVPN) on port 443 (SSL/TLS)
- Client VPN endpoint is fully managed and creates a network interface in each subnet

- Client VPN endpoint spans an Availability Zone, you can only associate with one subnet in each AZ
  
- Authentication options: 
  - Active Directory Services
  - setup client certificates for mutual authentication 
  - SAML single sign on