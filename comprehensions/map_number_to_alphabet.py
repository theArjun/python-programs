# Map alphabet to number

# It could also be like this, but keys can't be duplicate, so every keys gets
# mapped to 4(last value).
# my_dict = {char: digit} for char in 'abcd' for digit in '1234'}

my_dict = [{char: digit} for char in "abcd" for digit in "1234"]
print(my_dict)
