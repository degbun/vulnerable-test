import unittest
from second import addition, multiplication  # Remplace `your_module_name` par le nom du fichier contenant ton code.

class TestMathFunctions(unittest.TestCase):
    def test_addition(self):
        # Test de l'addition
        self.assertEqual(addition(5, 10), 15)
        self.assertEqual(addition(-2, 3), 1)
        self.assertEqual(addition(0, 0), 0)
        self.assertEqual(addition(-5, -5), -10)

    def test_multiplication(self):
        # Test de la multiplication
        self.assertEqual(multiplication(5, 10), 50)
        self.assertEqual(multiplication(-2, 3), -6)
        self.assertEqual(multiplication(0, 5), 0)
        self.assertEqual(multiplication(-5, -5), 25)

if __name__ == "__main__":
    unittest.main()
