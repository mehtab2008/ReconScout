
import socket


def scan_ports(hostname):
    common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3389]
    open_ports = []

    print("\nPort Scan Results")
    print("------------------------------")
    for port in common_ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((hostname, port))
            if result == 0:
                open_ports.append(port)
                print(f"Port {port} is open.")
            else:
                print(f"Port {port} is closed.")

    if not open_ports:
        print("No common ports are open.")