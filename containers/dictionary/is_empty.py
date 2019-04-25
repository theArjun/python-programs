#  Write a Python program to check a dictionary is empty or not.


def is_dict_empty(d):
    return len(d) == 0


my_dict = {'name': 'Arjun', 'roll': 5, 'grade': 'Bachelors'}
empty_dict = {}

print(is_dict_empty(my_dict))
print(is_dict_empty(empty_dict))
