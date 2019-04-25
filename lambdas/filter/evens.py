# Filter takes two arguments.
# Function and itearble


# We can use defined function or lambda both.
nums = [1, 2, 3, 4, 5, 6, 7]


def is_even(n):
    return n % 2 == 0


evens = list(filter(is_even, nums))

# By using lamdba.
evens = list(filter(lambda x: x % 2 == 0, nums))

print(evens)
