def decorate_add_number(tempFunction):
    def wrap_add_number(numOne, numTwo):
        print("The sum is : ")
        # Call the pre-defined function with temporary function.
        result = tempFunction(numOne, numTwo)
        print(result)
        print("Keep enjoying mathematical journey")
    return wrap_add_number


@decorate_add_number
def add_number(numOne, numTwo):
    return numOne+numTwo


add_number(5, 6)
