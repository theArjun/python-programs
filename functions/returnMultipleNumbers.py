def calc(a, b):
    w = a + b
    x = a - b
    y = a * b
    z = a / b
    # We can return the variables separated by comma
    return w, x, y, z


# The returned results will be assigned as a tuple which means it can't be
# modified , but can be indexed,repeated and length-measurable.
result = calc(10, 5)
print(result)
# We can cross-check the type of result by type() method
print(type(result))
for i in result:
    print(i)
