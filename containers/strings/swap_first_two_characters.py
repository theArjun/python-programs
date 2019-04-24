# Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string.

string_one, string_two = input().split()

temp = string_one[:2]
string_one = string_two[:2] + string_one[2:]
string_two = temp + string_two[2:]
print(string_one, string_two)
