# Find all of the words in a string that are less than 4 letters

test_string = input()

my_str = [word for word in test_string.split() if len(word) < 4]
print(my_str)
