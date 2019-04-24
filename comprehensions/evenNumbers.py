# Prints even number from 1 to 20

# Using condition
result = [x for x in range(1, 21) if x % 2 == 0]
print(result)

# Using the range function too
result = [x for x in range(2, 21, 2)]  # Initial is 2 and then jumps 2 forward
print(result)
