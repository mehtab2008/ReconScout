from modules.network import check_status


def print_webfile_checks(hostname):
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
