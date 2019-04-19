# Namespace
# It is an area where you create and store object / variable.
# - Class namespace
# - Object / Instance namespace


class Car:
    # If some variable values are to be common for class such as no of wheel
    # for car, it is declared as class variable and written outside init
    # method.

    wheels = 4  # Belongs to class namespace.

    # Here, mileage and company are known as instance variables, and they are
    # supposed to be different for every objects.
    def __init__(self):
        self.mileage = 10  # Belongs to object namespace.
        self.company = "BMW"

c1 = Car()
c2 = Car()

# Let's change for c1 object.
c1.mileage = 40
c1.company = "Audi"

print(c1.company, c1.mileage, c1.wheels)
print(c2.company, c2.mileage, c2.wheels)
