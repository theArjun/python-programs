# Types of Methods
# - Class Methods
# - Static Methods
# - Instance / Object Methods


class Student:

    school = "Gandaki College of Engineering and Science"

    # These are instance methods.
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def set_m1(self):
        self.m1 = m1

    def set_m2(self):
        self.m2 = m2

    def set_m3(self):
        self.m3 = m3

    def get_m1(self):
        return m1

    def get_m2(self):
        return m2

    def get_m3(self):
        return m3

    def average(self):
        return (self.m1 + self.m2 + self.m3) / 3

    # If we're working with class, not relating to objects, then we use cls
    # instead of self.

    # Decorator 'classmethod' is required.
    @classmethod
    def get_school(self):  # Class Method
        return cls.school

    # Decorator 'staticmethod' is required.
    # Static variables don't interact class variable and instance variables.
    # They are generally used to serve information.
    @staticmethod
    def info():  # Static method.
        print("This is Student class, in oop directory.")


s1 = Student(34, 89, 34)
s2 = Student(34, 80, 64)

print("Average : ", s1.average())
print("Average : ", s2.average())

print(Student.info())
