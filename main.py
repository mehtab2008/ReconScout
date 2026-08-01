import socket
import requests

def check_status(protocol, hostname):
    try:
        response = requests.get(f"{protocol}://{hostname}", timeout=10)
        if response.status_code == 200:
            print(f"Status Code: {response.status_code} - Reason : OK")
        elif response.status_code == 301:
            print(f"Status Code: {response.status_code} - Reason : Moved Permanently")
        elif response.status_code == 403:
            print(f"Status Code: {response.status_code} - Reason : Forbidden")
        elif response.status_code == 404:
            print(f"Status Code: {response.status_code} - Reason : Not Found")
        return 0
    except requests.RequestException:
        return False

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
check_status("http", hostname)

print("HTTPS check")
print("------------------------------")
check_status("https", hostname)