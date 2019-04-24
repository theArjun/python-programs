# Use a dictionary comprehension to count the length of each word in a
# sentence.

test_string = input()

# Dictionary Comprehension
my_word = {word: len(word) for word in test_string.split()}

print(my_word)
