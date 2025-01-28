# Calcul de la somme de deux nombres
def add(a, b):
    return a + b

# Calcul de la somme de deux nombres
def add_again(a, b):
    return a + b

# Calcul de la différence entre deux nombres
def subtract(a, b):
    return a - b

# Calcul de la différence entre deux nombres
def subtract_again(a, b):
    return a - b

# Multiplication de deux nombres
def multiply(a, b):
    return a * b

# Multiplication de deux nombres
def multiply_again(a, b):
    return a * b

# Division de deux nombres
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

# Division de deux nombres
def divide_again(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

# Fonction pour utiliser les opérations
def main():
    print(add(10, 5))       # 15
    print(add_again(10, 5)) # 15

    print(subtract(10, 5))       # 5
    print(subtract_again(10, 5)) # 5

    print(multiply(10, 5))       # 50
    print(multiply_again(10, 5)) # 50

    print(divide(10, 5))         # 2.0
    print(divide_again(10, 5))   # 2.0

if __name__ == "__main__":
    main()
