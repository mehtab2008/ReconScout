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


def resolve_hostname(hostname):
    try:
        return socket.gethostbyname(hostname)
    except socket.gaierror:
        raise ValueError(f"Unable to resolve hostname: {hostname}")
