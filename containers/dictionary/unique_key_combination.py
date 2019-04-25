# Write a Python program to create and display all combinations of letters,
# selecting each letter from a different key in a dictionary.


my_dict = {'g': 1, 's': 3, 'r': 2}

# Avoiding duplicates by mapping to set
combinations = set([key_one + key_two + key_three for key_one in my_dict.keys()
                    for key_two in my_dict.keys()
                    for key_three in my_dict.keys()])

for item in combinations:
    print(item)
