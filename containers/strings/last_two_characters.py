# Write a Python program to get a string made of the first 2 and the last 2
# chars from a given a string. If the string length is less than 2, return
# instead of the empty string.

test_string = input()

if len(test_string) >= 2:
    print('{}{}'.format(test_string[:2], test_string[-2:]))
else:
    print('Empty string')
