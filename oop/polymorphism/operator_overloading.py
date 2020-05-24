# Operator Overloading in Python

num_one = 5
num_two = 6

print(num_one + num_two)
# Basically, + operator calls the magic method __add__() behind the scenes.
print(int.__add__(num_one, num_two))
# Both outputs the same.

# Let's overload various operators for Student class.


class Student:
    def __init__(self, mark_one, mark_two):

        self.mark_one = mark_one
        self.mark_two = mark_two

    # Overloading + operator
    def __add__(self, other):

        mark_one_total = self.mark_one + other.mark_one
        mark_two_total = self.mark_two + other.mark_two
        total = Student(mark_one_total, mark_two_total)

        return total

    # Overloading print method
    def __str__(self):

        return "{} {}".format(self.mark_one, self.mark_two)

    # Overloading greater than operator
    def __gt__(self, other):

        if self.mark_one + self.mark_two > other.mark_one + other.mark_two:
            return True
        else:
            return False


student_one = Student(40, 80)
student_two = Student(67, 90)

# Unless we overload the print method, it prints memory address of object.
print(student_one)
print(student_two)
print(student_one + student_two)

if student_one > student_two:
    print("Student one wins.")
else:
    print("Student two wins.")
