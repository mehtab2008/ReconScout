from pathlib import Path


def save_report(hostname, content):
    reports_dir = Path(__file__).resolve().parent.parent / "reports"
    reports_dir.mkdir(exist_ok=True)
    report_path = reports_dir / f"{hostname.replace('.', '_')}.txt"
    report_path.write_text(content, encoding="utf-8")
    return report_path
