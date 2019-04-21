# A set sequence doesnt allow to make duplicates of element(unique) and
# elements are immutable. (which cant be changed).

# But the set itself is mutable. We can add or remove items fro it.
# Sets are used to perform mathematical operations like unions, intersection,
# symmetric difference etc.
print("")

s = {}

print(type(s))  # It returns type dictionary.

s = {1, 2, 3, 4, "Arjun", 1}
print(len(s))  # Last element 1 is discarded and the length is returned 5.
print(type(s))
