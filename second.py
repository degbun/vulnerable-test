class ClassA:
    def greet(self):
        print("Hello from ClassA!")

    def unique_method_a(self):
        print("This is a unique method in ClassA.")


class ClassB:
    def greet(self):
        print("Hello from ClassB!")  # Code dupliqué

    def unique_method_b(self):
        print("This is a unique method in ClassB.")





class ClassE:
    def unique_method_e(self):
        print("This is a unique method in ClassE.")


# Exemple d'utilisation
if __name__ == "__main__":
    obj_a = ClassA()
    obj_b = ClassB()
    obj_e = ClassE()

    # Appel des méthodes `greet` dupliquées
    obj_a.greet()
    obj_b.greet()


    # Appel des méthodes uniques
    obj_a.unique_method_a()
    obj_b.unique_method_b()

    obj_e.unique_method_e()
