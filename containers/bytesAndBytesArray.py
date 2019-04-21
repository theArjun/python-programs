# First create a list

lst = [1, 2, 3, 4]
print(type(lst))

# Converting from list to Bytes
b = bytes(lst)
print(type(b))

# Bytes are those data types which can't perform or add element in bytes.
# Update (X)
# Indexing (X)

# b[3] = 32 # This is error. 'str' object does not support item assignment

b1 = bytearray(lst)

print(type(b1))

"""Notes:
We can add or modify element in bytearray.
No slicing or indexing is allowed on either bytes or byte array."""
