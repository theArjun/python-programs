# Raises exception if we tried to access an item by a non-existent index with
# IndexError.

try:
    my_list = [1, 2, 3, False, "Arjun"]
    print("Possible maximum indexing of list : {}".format(len(my_list) - 1))

    # Let's try to access with non - existent index.
    print(my_list[7])
except IndexError:
    print("You tried to access with non - existent index.")
finally:
    print("You're being good with Python exceptions. Go on.")
