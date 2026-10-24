import unittest
from canteen import calculate_total


class TestCanteen(unittest.TestCase):

    def test_no_discount(self):
        self.assertEqual(calculate_total(200), 210)

    def test_price_at_300(self):
        self.assertEqual(calculate_total(300), 315)

    def test_discount_applied(self):
        self.assertEqual(calculate_total(400), 378)


if __name__ == "__main__":
    unittest.main()
