import socket

print("========================================")
print("               RECON SCOUT              ")
print("========================================")

hostname = input("Enter the hostname: ").strip()

try:
    ip_addr = socket.gethostbyname(hostname)
    print("\nResult")
    print("------------------------------")
    print(f"Hostname : {hostname}")
    print(f"IP Address: {ip_addr}")
except socket.gaierror:
    print(f"Unable to resolve hostname: {hostname}")

