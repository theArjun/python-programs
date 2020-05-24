# Method Overriding


class Animal:
    def makesound(self):

        print("Sound of Animal")


class Cat(Animal):

    # Overrided Method
    def makesound(self):

        print("Meow")


cat = Cat()
cat.makesound()
