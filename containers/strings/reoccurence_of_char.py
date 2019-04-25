# Write a Python program to get a string from a given string where all
# occurrences of its first char have been changed to '$', except the first
# char itself.

test_string = input()

# Redundant code:
# count_char = {char: list(test_string).count(char) for char in test_string}
# repeated_chars = [keys for keys, values in count_char.items() if values > 1]

# Dictionary of characters in test string whose occurence is more than 1.
repeated_chars_appearence = {keys: 1 for keys in test_string if test_string.count(keys) > 1}

new_string = ''
for char in test_string:

    # If the character has appeared more than once.
    if char in repeated_chars_appearence:

        # If the repeated character has been printed once.
        if repeated_chars_appearence[char] == 1:
            new_string += char
            repeated_chars_appearence[char] += 1
        # If it has been already printed, it should be replaced by '$'.
        else:
            new_string += '$'
    # Else print as usual.
    else:
        new_string += char

print(new_string)
