import random


class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    # Using the property decorator, we can assign class methods as properties /
    #  attributes.
    @property
    def full_name(self):
        return '{} {}'.format(
            self.first_name,
            self.last_name
        )

    @property
    def email(self):
        return '{}.{}{}@email.com'.format(
            self.first_name.lower(),
            self.last_name.lower(),
            random.randrange(11, 99)
        )

    # Setting the attributes which are created using property decorator.
    @full_name.setter
    def full_name(self, name):
        self.first_name, self.last_name = name.rstrip().split()

    # Deletes the attributes set by using property decorator.
    # Property value are to be cleared when del() method is invoked.
    @full_name.deleter
    def full_name(self):
        print("Deletion going on ...")
        self.first_name = None
        self.last_name = None

    def __str__(self):
        return 'First Name : {} \nLast Name : {}'.format(
            self.first_name, self.last_name)


if __name__ == "__main__":

    p1 = Person('Arjun', 'Adhikari')
    print(p1.full_name)
    print(p1.email)
    # Deletion
    del(p1.full_name)
    # Check what are the calues after deletion
    print(p1)
    # Setting another values using the full_name attribute
    p1.full_name = 'Hari Sharma'
    print(p1)
    print(p1.full_name)
    print(p1.email)