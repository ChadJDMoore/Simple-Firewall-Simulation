# Simple Firewall Simulation

## Objective
To simulate the behavior of a basic firewall by creating a Python script that evaluates access permissions based on predefined rules for IP addresses and ports.

### Skills Learned

- Understanding basic firewall concepts (allowed IPs and blocked ports)
- Implementing simple network-based access control in a script

### Tools Used

- Programming Language: Python 3.x
- Text Editor: VS Code


## Steps
*1. Define the Rules:*

- Create a list of allowed IP addresses.
- Define a list of blocked ports to restrict certain services.

*2. Create a Function:*

- Write the *firewall* function, which accepts two parameters: *ip* and *port*.
- Check if the IP is in the allowed list and if the port is not in the blocked list.
