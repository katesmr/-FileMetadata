import unittest
from src.utils.utils import split_on_bit


class SplitOnBitTests(unittest.TestCase):
    def setUp(self):
        self.splitted_number1 = split_on_bit("777", 3)
        self.splitted_number2 = split_on_bit("446", 6)
        self.splitted_number3 = split_on_bit("190", 4)
        self.splitted_number4 = split_on_bit("222", 2)

    def test_split_on_bit(self):
        self.assertEqual(self.splitted_number1, ["111", "111", "111"])
        self.assertEqual(self.splitted_number2, ["000100", "000100", "000110"])
        self.assertEqual(self.splitted_number3, ["0001", "1001", "0000"])
        self.assertEqual(self.splitted_number4, ["10", "10", "10"])

if __name__ == "__main__":
    unittest.main()
