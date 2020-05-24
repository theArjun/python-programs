# Remove all of the vowels in a string

vowels = ["a", "b", "c", "d", "e"]

test_string = input()
my_str = [char for char in test_string if char.lower() not in vowels]

# To print the string, rather than list.
print("".join(my_str))
