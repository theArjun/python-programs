# In Python, method overloading is tricky to implement. We can't define
# different methods for each parameter but can assign them to None and
# work on it as shown in below.


class Addition:
    def sum(self, num_one=None, num_two=None, num_three=None):

        if num_one is not None and num_two is not None and num_three is not None:
            sum = num_one + num_two + num_three
        elif num_one is not None and num_two is not None:
            sum = num_one + num_two
        else:
            sum = num_one

        return sum


operation = Addition()
print(operation.sum(4, 5, 6))
print(operation.sum(4, 5))
print(operation.sum(4))
