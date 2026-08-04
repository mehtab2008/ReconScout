import unittest

from modules.headers import summarize_headers


class HeaderSummaryTests(unittest.TestCase):
    def test_summarize_headers_reports_present_and_missing(self):
        class Response:
            headers = {"Server": "nginx"}

        summary = summarize_headers(
            Response(),
            ["Server", "Content-Type"],
            ["Strict-Transport-Security"],
        )

        self.assertEqual(summary["common"]["Server"], "nginx")
        self.assertEqual(summary["common"]["Content-Type"], "Not found")
        self.assertEqual(summary["security"]["Strict-Transport-Security"], "Missing")


if __name__ == "__main__":
    unittest.main()
