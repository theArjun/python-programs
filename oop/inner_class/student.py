# Inner Class in Python


class Student:

    # Inner Laptop
    class Laptop:

        # Instance variables of Inner Laptop class.
        def __init__(self, brand, cpu, ram):
            self.brand = brand
            self.cpu = cpu
            self.ram = ram

        # Show function of Inner Laptop class.
        def show(self):
            print(self.brand, self.cpu, '{} GB'.format(self.ram))

    # Instance variable of outer Student Class.
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        # This is important.
        self.lap = self.Laptop('Dell', 'Intel i7 8th Gen', 8)

    # Show function of outer Student class.
    def show(self):
        print(self.name, self.roll_no)
        self.lap.show()

s1 = Student('Arjun', 6)
s2 = Student('Ashish', 7)

s1.show()

# These two objects are different.
lap_one = s1.lap
lap_two = s2.lap
# Shows object are stored on different memory locations; returns False.
print(id(lap_one) == id(lap_two))

# Creating Laptop object outside the Student Class
my_laptop = Student.Laptop('HP', 'i5 8th Gen', 16)
my_laptop.show()       
