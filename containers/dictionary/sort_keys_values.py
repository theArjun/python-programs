#  Write a Python script to sort (ascending and descending) a dictionary by
# value.

import random
import operator

country_name = ['Nepal', 'India', 'Bangladesh', 'Pakistan', 'China']
my_dict = {name: random.randint(1, 100) for name in country_name}

print(my_dict)
# Returns list of tuples
sorted_list_by_value = sorted(my_dict.items(), key=operator.itemgetter(1))
# Sort by values
my_dict_sorted_by_value = dict(sorted_list_by_value)
print(my_dict_sorted_by_value)

sorted_list_by_key = sorted(my_dict.items(), key=operator.itemgetter(0))
my_dict_sorted_by_key = dict(sorted_list_by_key)
print(my_dict_sorted_by_key)