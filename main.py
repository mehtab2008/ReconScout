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
Security_headers = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "Referrer-Policy",
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

print("")
print("HTTP check")
print("------------------------------")
response = check_status("http", hostname)

print("")
print("HTTPS check")
print("------------------------------")
response = check_status("https", hostname)

print("")
print("Headers check")
print("------------------------------")
for header in headers:
    if response and header in response.headers:
        print(f"{header}: {response.headers[header]}")
    else:
        print(f"{header}: Not found")

print("")
print("Security Headers check")
print("------------------------------")
for header in Security_headers:
    if response and header in response.headers:
        print(f"{header}: Present")
    else:
        print(f"{header}: Missing")
