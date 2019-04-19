# Raising an exception

try:
    num_one = int(input('Enter a number : '))
    num_two = int(input('Enter another number : '))
    if num_two == 0:
        raise ZeroDivisionError()
    print("Quotient : {}".format(num_one / num_two))
except ZeroDivisionError:
    print("Dividing any number by zero. That leads to complications.")
finally:
    print("Exceptions are necessary, though.")
