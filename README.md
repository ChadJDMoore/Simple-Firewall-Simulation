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
#### *1. Define the firewall Function:*

- Write a Python function named **firewall** that takes two inputs: an **ip** (IP address) and a **port** (port number).
- Inside the function, define the following rules:
  - **allowed_ips:** A list of permitted IP addresses
  - **blocked_ports:** A list of restricted ports
  - Use an **if-else** statement to check whether the provided **ip** is in **allowed_ips** and the **port** is not in **blocked_ports**
  - Print **"Allowed"** if both conditions are met; otherwise, print **"Blocked"**
<div>
  <img width="322" alt="image" src="https://github.com/user-attachments/assets/49dabaa5-0d95-49b9-8d65-8b07eca21426">
</div>

#### *2. Test the Function:*

- Call the firewall function with test cases to verify its behavior





