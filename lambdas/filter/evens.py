# Filter takes two arguments.
# Function and itearble


# Filter are used to filter the iterables based on specific condition.

# We can use defined function or lambda both.
nums = [1, 2, 3, 4, 5, 6, 7]


def is_even(n):
    return n % 2 == 0


# First it return the filter object, so we need to convert it into list.
# We can also convert it in set, tuple etc.
evens = list(filter(is_even, nums))

# By using lamdba.
evens = list(filter(lambda x: x % 2 == 0, nums))

print(evens)
