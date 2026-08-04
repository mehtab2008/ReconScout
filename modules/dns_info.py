import dns.resolver

def get_dns_records(hostname):
    records = {}
    try:
        for record_type in ['A', 'AAAA', 'MX', 'NS', 'CNAME', 'TXT']:
            try:
                answers = dns.resolver.resolve(hostname, record_type)
                records[record_type] = [r.to_text() for r in answers]
            except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
                records[record_type] = []
    except Exception as e:
        print(f"Error retrieving DNS records: {e}")
    return records