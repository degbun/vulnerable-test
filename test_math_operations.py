import unittest
from math_operations import addition, multiplication, division

class TestMathOperations(unittest.TestCase):
    def test_addition(self):
        # Tests pour l'addition
        self.assertEqual(addition(5, 10), 15)
        self.assertEqual(addition(0, 0), 0)
        self.assertEqual(addition(-2, 3), 1)

    def test_multiplication(self):
        # Tests pour la multiplication
        self.assertEqual(multiplication(5, 10), 50)
        self.assertEqual(multiplication(0, 10), 0)  # Cas avec zéro
        self.assertEqual(multiplication(-2, 3), -6)

    def test_division(self):
        # Tests pour la division
        self.assertEqual(division(10, 2), 5)
        self.assertIsNone(division(10, 0))  # Cas avec division par zéro
        self.assertEqual(division(-6, 2), -3)

if __name__ == "__main__":  # pragma: no cover
    unittest.main()
