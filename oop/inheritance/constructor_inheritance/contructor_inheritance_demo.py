class A:

    def __init__(self):
        print("Class A Init.")

    def feature_one(self):
        print("Feature 1 working.")

    def feature_two(self):
        print("Feature 2 working.")


# Constructor Inheritance
class B(A):

    def __init__(self):
        # To call the init method of superclass, super keyword is used.
        # It will call the init method of immediate super class.
        super().__init__()

        print("class B Init")

    def feature_three(self):
        print("Feature 3 working.")

    def feature_four(self):
        print("Feature 4 working.")

# First, it calls the init method of sub class; if not then calls the init
# method of super class.
b_one = B()
