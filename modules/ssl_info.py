import ssl
import socket



def collect_ssl_info(hostname):
    ssl_info = {}
    try:
        # Create a socket and wrap it with SSL
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()

                # Extract relevant information from the certificate
                ssl_info['Issuer'] = dict(x[0] for x in cert['issuer'])
                ssl_info['Subject'] = dict(x[0] for x in cert['subject'])
                ssl_info['Valid From'] = cert['notBefore']
                ssl_info['Expires'] = cert['notAfter']

    except Exception as e:
        print(f"Error collecting SSL info: {e}")
        ssl_info['Error'] = str(e)

    return ssl_info