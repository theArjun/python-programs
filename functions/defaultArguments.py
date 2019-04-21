# Default Arguments

# Declaring default arguments; this will come to use when no or incomplete
# argument is passed while calling function i.e. unpassed arguments takes
# value from the default arguments and function will execute smoothly.


def average(a=10, b=20):
    print(a)
    print(b)
    print((a+b)/2)


# Doing this, first parameter is assigned to 10 and second parameter is
# assigned to 20 according to their position.
average()

# Doing this, first parameter is assigned as 40; its being passed and second
# parameter is assigned to 20 from default arguments.
average(a=40)
