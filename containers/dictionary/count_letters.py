# Write a Python program to create a dictionary from a string.

test_string = input()

my_dict = {key: test_string.count(key) for key in test_string}
print(my_dict)
