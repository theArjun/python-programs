def square_number(lst):
    for i in lst:
        yield i**2


lst = [1, 2, 3, 4, 5, 6]

result = square_number(lst)
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))

# Only six elements are passed, so another calling of generator function will
# throw StopIteration Exception.
print(next(result))
