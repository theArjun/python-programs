
# Tuple
# It is a list which can not be modified. We cant use methods like append(),
# extend(), insert(), delete(), remove(), clear()

# Declaring a tuple
tpl = ()
print(tpl)
print(type(tpl))

tpl = (1)  # Considers a single integer value
print(type(tpl))

tpl = (1,)  # But now it considers it as a tuple
print(type(tpl))

# print(tpl[3]) # Returns error message tuple index out of range though it
# supports indexing.

tpl = (1, 2, 3, 4, 5)

# Length
print(len(tpl))

# Repeatition
print(tpl*3)

tpl1 = tpl*3
print(tpl1)

print(tpl1.count(4))  # Counts how many times 4 is repeated in tuple.

# Indexing
print(tpl1[5])
