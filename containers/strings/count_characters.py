# Write a Python program to count the number of characters (character
# frequency) in a string.

test_string = input()

# Converts into list of characters.
lst = str(test_string)

my_dict = {item: test_string.count(item) for item in lst}
print(my_dict)
