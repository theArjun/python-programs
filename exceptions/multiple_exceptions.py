# Multiple exceptions

try:
    my_list = [1, 2, "Arjun", 6.0, True]
    print(my_list[10] / 0)
# Note that parenthesis are necessary for multiple exceptions.
except (IndexError, ZeroDivisionError):
    print("Exception occured.")
finally:
    print("Wow ! That is new taste of exception.")
