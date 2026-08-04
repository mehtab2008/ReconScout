from modules.headers import print_header_summary, summarize_headers
from modules.network import check_status, resolve_hostname
from modules.utils import print_banner, print_section
from modules.webfiles import print_webfile_checks
from modules.ssl_info import collect_ssl_info


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

if __name__ == "__main__":
    main()

