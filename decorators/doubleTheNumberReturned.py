# Doubles the number returned by another function

def decorate_number(tempFunction):
    def wrap_decorate_number():
        print("The number is :")
        print(tempFunction()*2)
        print("Was it double? Feel free to comment at thearjun.tech")

    return wrap_decorate_number

@decorate_number
def number():
    return 7

number()
