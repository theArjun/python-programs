class Product:
    # self points to the current object
    # __init__ is constructor in python
    def __init__(self):
        self.name = "Iphone"
        self.description = "Awesome"
        self.price = 700

p1 = Product()
print(p1.name)
print(p1.description)
print(p1.price)

p2 = Product()
print(p2.name)
print(p2.description)
print(p2.price)
