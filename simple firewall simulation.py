def firewall(ip, port):
    allowed_ips = ["192.168.1.10", "192.168.1.11"]
    blocked_ports = [23, 3389]

    # Check if IP address is allowed and port is allowed
    if ip in allowed_ips and port not in blocked_ports:
        print("Allowed")
    else:
        print("Blocked")

firewall("192.168.1.10",80)
firewall("192.168.1.15", 23)