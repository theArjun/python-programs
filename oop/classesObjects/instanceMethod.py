# Instance Methods

class Course:
    def __init__(self, name, ratings):
        self.name = name
        self.ratings = ratings

    # To pass the objects variables constructed earlier, pass self.
    def average(self):
        # To pass the parameter of member variables pass self.variable_name
        numberOfRatings = len(self.ratings)
        average = sum(self.ratings)/numberOfRatings
        return average

# Parameters can be list, tuple or any objects
c1 = Course("Python Course", [1, 2, 3, 4, 5])
print(c1.name)
print(c1.ratings)
print(c1.average())

c2 = Course("Python Course", [1, 2, 3, 4])
print(c2.name)
print(c2.ratings)
print(c2.average())
