# Write a Python program to find the highest 3 values in a dictionary.

my_dict = {'g': 1, 's': 3, 'r': 2, 'u': 4, 'w': 1, 'c': 5, 'e': 8, 'o': 9}

sorted_list = list(my_dict.values())
sorted_list.sort(reverse=True)

for i in range(3):
    print(sorted_list[i])
