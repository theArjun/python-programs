""" Write a Python program to count the values associated with key in a
dictionary.
Sample data: = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2,
'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
Expected result: Count of how many dictionaries have success as True """

sample_dict_list = [{'id': 1, 'success': True, 'name': 'Lary'}, {
                    'id': 2, 'success': False, 'name': 'Rabi'}, {
                        'id': 3, 'success': True, 'name': 'Alex'}]

count_True = 0

for dict_item in sample_dict_list:

    if True in dict_item.values():
        count_True += 1

print(count_True)
