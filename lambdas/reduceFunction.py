# Calculates sum of numbers in list

# Reduce function is not available by default, so need to import it from
# functools module.
from functools import reduce

# Assigning a list for operation
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 23, 45]

# Syntax for reduce function : reduce(lambda expression,data to be operated).
# Don't forget to assign it to a variable.
result = reduce(lambda x, y: x + y, lst)

# The data type is int
print(type(result))
print(result)
