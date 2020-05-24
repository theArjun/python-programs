# Retrives double of numbers from the list using map function
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 23, 45]

# Syntax for map function : map(lambda expression,data to be mapped). Don't
# forget to assign it to a variable.
result = map(lambda a: a * 2, lst)

# The result is of map data type.
print(type(result))

# To display, convert it into list.
result = list(result)
print(result)
