class A:

    def __init__(self):
        print("Class A init")

    def feature(self):
        print("Feature A")


class B:

    def __init__(self):
        print("Class B init")

    def feature(self):
        print("Feature B")


# Due to method order resolution in multiple inheritance, method of left-class
# is given priority, which also prevents ambiguity.
class C(A, B):

    pass


c_one = C()
c_one.feature()


class D(B, A):

    pass


d_one = D()
d_one.feature()
