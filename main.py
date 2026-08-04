from modules.headers import print_header_summary, summarize_headers
from modules.network import check_status, resolve_hostname
from modules.utils import print_banner, print_section
from modules.webfiles import print_webfile_checks
from modules.ssl_info import collect_ssl_info
from modules.dns_info import get_dns_records
from modules.portscan import scan_ports
from modules.report import save_report


def main():
    print_banner()

    hostname = input("Enter the hostname: ").strip()

    try:
        ip_addr = resolve_hostname(hostname)
    except ValueError as error:
        print(error)
        return

    print_section("Target Information")
    print(f"Hostname : {hostname}")
    print(f"IP Address: {ip_addr}")

    print_section("HTTP check")
    response = check_status("http", hostname)

    print_section("HTTPS check")
    response = check_status("https", hostname)

    print_section("Headers check")
    summary = summarize_headers(response)
    print_header_summary(summary)

    print_webfile_checks(hostname)

    print_section("SSL/TLS Information")
    ssl_info = collect_ssl_info(hostname)
    for key, value in ssl_info.items():
        print(f"{key}: {value}")

    print_section("DNS Information")
    dns_info = get_dns_records(hostname)
    for record_type, records in dns_info.items():
        print(f"{record_type} Records: {', '.join(records) if records else 'None'}")

    open_ports = scan_ports(hostname)
    if open_ports:
        print(f"Open Ports: {', '.join(map(str, open_ports))}")

    save_report(hostname, f"Report for {hostname}\n\nIP Address: {ip_addr}\n\nOpen Ports: {', '.join(map(str, open_ports)) if open_ports else 'None'}\n\nDNS Records: {dns_info}\n\nSSL/TLS Info: {ssl_info}\n\nHeaders Summary: {summary}")

   


if __name__ == "__main__":
    main()

