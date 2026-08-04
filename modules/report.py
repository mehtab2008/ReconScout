def save_report(hostname, report):
    filename = f"{hostname}_report.txt"
    with open(filename, "w") as file:
        file.write(report)