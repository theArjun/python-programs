# Write a Python program to print a dictionary in table format.

sample_dict = {'a': 3, 's': 3, 'd': 3, 'j': 2, 'f': 2, 'n': 1, 'l': 1, 'i': 1,
               'b': 1}

# center(width, fillchar)
print('Keys'.center(10, ' '), '|', 'Values'.center(10, ' '))
print(''.center(21, '-'))
for key, value in sample_dict.items():
    print('{}'.format(key).center(10, ' '), '|',
          '{}'.format(value).center(10, ' '))
