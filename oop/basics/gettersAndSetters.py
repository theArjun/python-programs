class Programmer:
    def setName(self, name):
        self.name = name

    def setSalary(self, salary):
        self.salary = salary

    def setTechnologies(self, technologies):
        self.technologies = technologies

    def getName(self):
        return self.name

    def getSalary(self):
        return self.salary

    def getTechnologies(self):
        return self.technologies


p1 = Programmer()
p1.setName("John")
p1.setSalary("1234")
p1.setTechnologies("Java")

print(p1.getName())
print(p1.getSalary())
print(p1.getTechnologies())
