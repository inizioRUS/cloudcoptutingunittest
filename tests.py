import unittest
import requests


class TestSum(unittest.TestCase):
    def test_health(self):
        self.assertEqual(requests.get("http://localhost:5000/health").status_code, 200, "Should be True")

    def test_42(self):
        self.assertEqual(requests.get("http://localhost:5000/give42").text, '42', "Should be 42")


if __name__ == '__main__':
    unittest.main()
