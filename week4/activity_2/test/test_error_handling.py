import unittest
from src.calculator import Calculator


class TestErrorHandling(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator(10, 'j')

    def test_add(self):
        self.assertEqual(self.calc.add(), 15)  # tests addition functionality

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(), 5)  # tests subtraction functionality

    def test_invalid_operation(self):
        with self.assertRaises(ValueError):
            self.calc('multiply')  # failed to call invalid operation


if __name__ == '__main__':
    unittest.main()
