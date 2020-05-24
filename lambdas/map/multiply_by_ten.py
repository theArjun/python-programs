# If we want to change whole chunk of data based on specific operation, we use
# map.

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# It returns the map object, so converting it into iterable is necessary.
result = map(lambda n: n * 10, lst)
print(list(result))
