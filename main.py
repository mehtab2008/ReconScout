import socket
import requests

def check_status(protocol, hostname):
    try:
        response = requests.get(f"{protocol}://{hostname}", timeout=10)
        print("Status Code:", response.status_code)
        print(f"Reason : {response.reason}")
        return response
        
    except requests.RequestException:
        print(f"Unable to connect to {protocol}://{hostname}")
        return None

headers = [
    "Server",
    "Content-Type",
    "Content-Length",
    "Location"
]

print("========================================")
print("               RECON SCOUT              ")
print("========================================")

hostname = input("Enter the hostname: ").strip()

try:
    ip_addr = socket.gethostbyname(hostname)
    print("\nTarget Information")
    print("------------------------------")
    print(f"Hostname : {hostname}")
    print(f"IP Address: {ip_addr}")
except socket.gaierror:
    print(f"Unable to resolve hostname: {hostname}")
    exit(1)

print("HTTP check")
print("------------------------------")
response = check_status("http", hostname)

print("HTTPS check")
print("------------------------------")
response = check_status("https", hostname)

print("Headers check")
print("------------------------------")
#print(dir(response))
for header in headers:
    if response and header in response.headers:
        print(f"{header}: {response.headers[header]}")
    else:
        print(f"{header}: Not found")
