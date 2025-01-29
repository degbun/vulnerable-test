def addition(a, b):
    """
    Ajoute deux nombres et retourne le résultat.
    """
    return a + b


def multiplication(a, b):
    """
    Multiplie deux nombres et retourne le résultat.
    """
    if a == 0 or b == 0:  # Vérifie si un des nombres est 0
        return 0
    return a * b


def division(a, b):
    """
    Divise `a` par `b` et retourne le résultat.
    Si `b` est 0, retourne None pour éviter une division par zéro.
    """
    if b == 0:
        return None
    return a / b


if __name__ == "__main__":  # pragma: no cover
    print("Addition:", addition(10, 5))
    print("Multiplication:", multiplication(10, 0))
    print("Division:", division(10, 2))
