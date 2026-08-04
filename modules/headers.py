headers = [
    "Server",
    "Content-Type",
    "Content-Length",
    "Location",
]

security_headers = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "Referrer-Policy",
]


def summarize_headers(response, header_names=None, security_header_names=None):
    header_names = header_names or headers
    security_header_names = security_header_names or security_headers

    common_summary = {}
    security_summary = {}

    for header in header_names:
        if response and header in response.headers:
            common_summary[header] = response.headers[header]
        else:
            common_summary[header] = "Not found"

    for header in security_header_names:
        if response and header in response.headers:
            security_summary[header] = "Present"
        else:
            security_summary[header] = "Missing"

    return {"common": common_summary, "security": security_summary}


def print_header_summary(summary):
    for header, value in summary["common"].items():
        print(f"{header:<20}: {value}")

    print()
    print("Security Headers check")
    print("------------------------------")
    for header, value in summary["security"].items():
        print(f"{header:<30}: {value}")
