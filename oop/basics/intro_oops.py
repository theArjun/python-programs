# Introduction to OOPS
# - Attributes are declared as variables.
# - Behaviour are written as methods (functions).


class Computer:
    def config(self):
        print("i7 8th Gen", "16 GB", "1 TB")


com1 = Computer()
print(type(com1))

# ID prints the address in memory.
print(id(com1))

# Computer.config() TypeError: config() missing 1 required positional argument: 'self'
Computer.config(com1)

#  Commonly used method of calling objects function is :
com1.config()
# com1 is passed as parameter behind the scenes in places of self.
