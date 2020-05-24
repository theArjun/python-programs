# Write a Python program to get a dictionary from an object's fields.


class Student:
    def __init__(self, name, roll, grade):

        self.name = name
        self.roll = roll
        self.grade = grade

    def convert_to_dict(self):

        return {"name": self.name, "roll": self.roll, "grade": self.grade}


s_one = Student("Arjun", 5, "Bachelors")
print(s_one.convert_to_dict())
