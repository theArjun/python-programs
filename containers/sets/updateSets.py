s = {1,2,3,4,5}

# Update Operation

s.update([88,99]) # Elements to be updated should be kept inside the brackets.

print(s)

# Set doesn't guarantee any order.So, slicing, indexing and repeatition can't be performed.

# PVM throws error like: 'set' doesn't suppport indexing.

#Remove Operation

s.remove(88)
print(s)