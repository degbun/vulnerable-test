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


class ClassC:
    def greet(self):
        print("Hello from ClassC!")  # Code dupliqué

    def unique_method_c(self):
        print("This is a unique method in ClassC.")


class ClassD:
    def unique_method_d(self):
        print("This is a unique method in ClassD.")


class ClassE:
    def unique_method_e(self):
        print("This is a unique method in ClassE.")


# Exemple d'utilisation
if __name__ == "__main__":
    obj_a = ClassA()
    obj_b = ClassB()
    obj_c = ClassC()
    obj_d = ClassD()
    obj_e = ClassE()

    # Appel des méthodes `greet` dupliquées
    obj_a.greet()
    obj_b.greet()
    obj_c.greet()

    # Appel des méthodes uniques
    obj_a.unique_method_a()
    obj_b.unique_method_b()
    obj_c.unique_method_c()
    obj_d.unique_method_d()
    obj_e.unique_method_e()
