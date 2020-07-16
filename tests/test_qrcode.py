import unittest
from promptpay import qrcode


class TestSum(unittest.TestCase):

    def test_e(self):
        self.assertEqual(qrcode.generate_payload(3), "eee", "Should be generate payload")


if __name__ == "__main__":
    unittest.main()
