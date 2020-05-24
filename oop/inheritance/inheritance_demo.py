# Inheritance in Python - Shows Single Inheritance


# Super Class
class A:
    def feature_one(self):
        print("Feature 1 working.")

    def feature_two(self):
        print("Feature 2 working.")


# This is how inheritance is done in Python.
# Sub Class
class B(A):
    def feature_three(self):
        print("Feature 3 working.")

    def feature_four(self):
        print("Feature 4 working.")


a_one = A()
a_one.feature_one()

b_one = B()
b_one.feature_one()
b_one.feature_four()

# Multiple Inheritance : class C(P,Q)
