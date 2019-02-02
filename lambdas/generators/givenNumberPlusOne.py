# Defining a generator function that returns given number plus one
def my_generator(num):
    # Yield keyword makes this lfunction generator like return in normal functions
    yield num+1

# Testing function
g = my_generator(5)
# Generator type object 
print(g)
# Printing the elements of generator
print(next(g))
# Since, only one result is expected, calling the next function again will throw StopIteration Exception
print(next(g))
