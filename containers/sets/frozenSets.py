# Frozen Sets

# Frozen Set doesn't allow to Update and remove operations.
# It is immutable set.


s = {1, 2, 3, 4, 5}  # This is a set.

# This is a expression which is supposed not to work. Let's see PVM throws
# what sort of error message ?
f = frozenset(s)
f.update([20])

# Only Navigate and access the values of frozen set are allowed.
