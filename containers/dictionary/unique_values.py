# Write a Python program to print all unique values in a dictionary.


my_dict = {'g': 1, 's': 3, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
# Set doesn't contain duplicate values.
unique_values = set(my_dict.values())
print(unique_values)
