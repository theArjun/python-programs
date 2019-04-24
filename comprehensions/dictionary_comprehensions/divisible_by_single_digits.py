# Use a nested list comprehension to find all of the numbers from 1-1000 that
# are divisible by any single digit besides 1 (2-9)

# My first approach: Returned a lot of duplicate numbers.
my_list = [num for num in range(1001) for i in range(2, 10) if num % i == 0]

# Using Boolean values
# Uses nested list comprehensions
my_list = [num for num in range(1000) if True in [
    True for i in range(2, 10) if num % i == 0]]

# It's a nice little python trick that an empty list returns false in a
# conditional, so if nothing is generated in the sub-comprehension.

my_list = [num for num in range(
    1001) if [i for i in range(2, 10) if num % i == 0]]

print(my_list)
