""" Write a Python program to combine two dictionary adding values for common
keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})"""

# Python: how to convert a dictionary into a subscriptable array?
# https://stackoverflow.com/questions/33674033/python-how-to-convert-a-dictionary-into-a-subscriptable-array

d1 = {"a": 100, "b": 200, "c": 300}
d2 = {"a": 300, "b": 200, "d": 400}

# I think I misused dictionary comprehension here.
# new_dict = {key: value_one + value_two for key, value_one in d1.items()
#             for value_two in d2.values()}

# Merging two dictionaries.
# print({**d1, **d2})

new_dict = {}

# Convert the items into list first and then access by index.
for i in range(min(len(d1), len(d2))):
    new_dict[list(d1)[i]] = list(d1.values())[i] + list(d2.values())[i]

print(new_dict)
