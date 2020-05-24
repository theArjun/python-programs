# Count the number of spaces in a string

test_string = input()

no_of_spaces = len([character for character in test_string if character == " "])
print(no_of_spaces)
