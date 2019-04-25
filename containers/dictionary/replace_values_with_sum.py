# Write a Python program to replace dictionary values with their sum.
from functools import reduce

sample_dict = {'a': 3, 's': 3, 'd': 3, 'j': 2, 'f': 2, 'n': 1, 'l': 1, 'i': 1,
               'b': 1}

values_sum = reduce(lambda a, b: a+b, sample_dict.values())

for key in sample_dict.keys():
    sample_dict[key] = values_sum

print(sample_dict)
