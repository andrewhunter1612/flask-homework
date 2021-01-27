from application.models.calculator import Calculator
import unittest

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator(6, 3)

    def test_add(self):
        self.assertEqual(9, self.calculator.add(self.calculator.number_1, self.calculator.number_2))

    def test_subtract(self):
        self.assertEqual(3, self.calculator.subtract(self.calculator.number_1, self.calculator.number_2))

    def test_multiply(self):
        self.assertEqual(18, self.calculator.multiply(self.calculator.number_1, self.calculator.number_2))

    def test_divide(self):
        self.assertEqual(2, self.calculator.divide(self.calculator.number_1, self.calculator.number_2))
