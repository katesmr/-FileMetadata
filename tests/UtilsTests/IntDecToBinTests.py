import unittest
from src.utils.utils import int_dec_to_bin


class IntDecToBinTests(unittest.TestCase):
    def setUp(self):
        self.bin_number1 = int_dec_to_bin(8, 5)
        self.bin_number2 = int_dec_to_bin(356, 10)
        self.bin_number3 = int_dec_to_bin(145, 10)
        self.bin_number4 = int_dec_to_bin(68, 8)

    def test_int_dec_to_bin(self):
        self.assertEqual(self.bin_number1, "01000")
        self.assertEqual(self.bin_number2, "0101100100")
        self.assertEqual(self.bin_number3, "0010010001")
        self.assertEqual(self.bin_number4, "01000100")

if __name__ == "__main__":
    unittest.main()
