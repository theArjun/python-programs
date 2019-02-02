# Retrives even number from the list of random numbers using filter function
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 23, 45]

# Syntax for filter function : filter(lambda expression,data to be filtered). Don't forget to assign it to a variable.
result = filter(lambda x: x % 2 == 0, lst)

# The result is of filter data type.
print(type(result))

# To display, convert it into list.
result = list(result)
print(result)

# Do it in set too.
result = set(result)
print(result)

# Do it in tuple too.
result = tuple(result)
print(result)
