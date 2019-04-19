def addition(num_one, num_two):
# Till number two is equal to zero, the loop runs, else number one is sum itself.
    while num_two > 0:
        # Carryover is the logical AND operation.
        carry = num_one & num_two
        # Adding without carryover is simply the logical XOR operation.
        num_one = num_one ^ num_two
        # The carry is shifted to left, so that it can be added to the number ahead of it.
        num_two = carry << 1
        # As we are assigning, sum to number one, it is returned from the function.
    return num_one

print(addition(5, 6))
