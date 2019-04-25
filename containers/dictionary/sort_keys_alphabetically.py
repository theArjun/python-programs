# Write a Python program to sort a list alphabetically in a dictionary.

# Module for sorting dictionary
import operator

sample_dict = {'a': 3, 's': 3, 'd': 3, 'j': 2, 'f': 2, 'n': 1, 'l': 1, 'i': 1,
               'b': 1}

# It sorts the list, not the dictionary itself, so convert to list invoking
# the items() function.
# itemgetter(0) refers to key, itemgetter(1) refers to value.
sorted_dict = sorted(sample_dict.items(), key=operator.itemgetter(0))
print(sorted_dict)
