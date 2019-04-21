# This is how we create a dictionary in Python.
dict1 = {1: "Mercury", 2: "Venus", 3: "Earth"}
print(dict1)

# We can add any numbers or string as key or a value.

# This is how we access the items with keys and values.
print(dict1.items())


# This is how we access the keys from a dictionary.
k = dict1.keys()
for i in k:
    print(i)

# This is how we access the values from a dictionary.
v = dict1.values()
for i in v:
    print(i)

# This is how we print the particular element from a dictionary with
# key-indexing.
print("\n"+dict1[3])

# This is how we delete the element of a dictionary with key-indexing.
del dict1[2]

print(dict1)
