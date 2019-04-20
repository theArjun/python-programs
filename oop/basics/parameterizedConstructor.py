# Parameterized Constructor

class Course:
    # Parameterized Constructor (self, parameters)
    def __init__(self, name, ratings):
        self.name = name
        self.ratings = ratings

# Parameters can be list, tuple or any objects
c1 = Course("Python Course",[1,2,3,4,5])
print(c1.name)
print(c1.ratings)

c2 = Course("Python Course", [1,2,3,4])
print(c2.name)
print(c2.ratings)
