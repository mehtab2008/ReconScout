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
security_headers = [
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

print()
print("HTTP check")
print("------------------------------")
response = check_status("http", hostname)

print()
print("HTTPS check")
print("------------------------------")
response = check_status("https", hostname)

print()
print("Headers check")
print("------------------------------")
for header in headers:
    if response and header in response.headers:
        print(f"{header:<20}: {response.headers[header]}")
    else:
        print(f"{header:<20}: Not found")

print()
print("Security Headers check")
print("------------------------------")
for header in security_headers:
    if response and header in response.headers:
        print(f"{header:<30}: Present")
    else:
        print(f"{header:<30}: Missing")


print()
print("robots.txt check")
print("------------------------------")
robots_response = check_status("http", f"{hostname}/robots.txt")
if robots_response and robots_response.status_code == 200:
    print("\nrobots.txt content (first 10 lines):")
    print("------------------------------")
    lines = robots_response.text.splitlines()
    for line in lines[:10]:
        print(line)
else:
    print("robots.txt not found or inaccessible.")

print()
print("sitemap.xml check")
print("------------------------------")
sitemap_response = check_status("http", f"{hostname}/sitemap.xml")
if sitemap_response and sitemap_response.status_code == 200:
    print("\nsitemap.xml content (first 10 lines):")
    print("------------------------------")
    lines = sitemap_response.text.splitlines()
    for line in lines[:10]:
        print(line)
else:
    print("sitemap.xml not found or inaccessible.")


