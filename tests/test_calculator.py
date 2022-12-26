import unittest
from lsh23_calculator import calculator


class AddTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(1, 2), 3)

    def test_sub(self):
        self.assertEqual(calculator.sub(2,1), 1)


if __name__== '__main__':
    unittest.main()