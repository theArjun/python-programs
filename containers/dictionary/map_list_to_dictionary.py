# Write a Python program to map two lists into a dictionary.

list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_two = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Zip function is required.
zipped_list = zip(list_one, list_two)
# Zip object
print(type(zipped_list))
# Convert into dictionary then.
print(dict(zipped_list))
