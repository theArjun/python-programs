# SchoolMember - Super Class
# Teacher - Sub Class
# Student - Sub Class


class SchoolMember:
    def __init__(self, name, date_joined):

        self.name = name
        self.date_joined = date_joined


class Student(SchoolMember):
    def __init__(self, name, date_joined, grade, rank):

        super().__init__(name, date_joined)
        self.grade = grade
        self.rank = rank

    def info(self):
        return "Name : {} \nDate Joined : {} \nGrade : {} \nRank : {}".format(
            self.name, self.date_joined, self.grade, self.rank
        )


class Teacher(SchoolMember):
    def __init__(self, name, date_joined, salary, subject):

        super().__init__(name, date_joined)
        self.salary = salary
        self.subject = subject

    def info(self):
        return "Name : {} \nDate Joined : {} \nSalary : {} \nSubject : {}".format(
            self.name, self.date_joined, self.salary, self.subject
        )


student_one = Student("Arjun", 2017, "Bachelors", "Rank does not matter")
print(student_one.info())

teacher_one = Teacher("Ram Bahadur KC", 2009, 100000, "Programming in Java")
print(teacher_one.info())
