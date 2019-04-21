stringOne = str(input("Enter string one : "))
stringTwo = str(input("Enter string two : "))

print("\nBefore Swapping\n")
print("String One : %s" % (stringOne))
print("String Two : %s" % (stringTwo))

# Pre-Defined Method
# stringOne,stringTwo = stringTwo,stringOne

# First, we concatenate the string in form of list.
stringOne = list(stringOne)+list(stringTwo)
# Then we extract the first string from the concatenated list and assign it to
# string two.
stringTwo = stringOne[0:len(stringTwo)]
# Then, we assign the extracted second string to string one.
stringOne = stringOne[len(stringTwo):len(stringOne)]
# The string one and string two still contains the list. Below statements
# convert the list into string.
stringOne = ''.join(stringOne)
stringTwo = ''.join(stringTwo)

# Appending the list will create a nested-array which is unwanted result this
# time.
# stringOne.append(stringTwo)

print("\nAfter Swapping\n")
print('String One : %s' % (stringOne))
print("String Two : %s" % (stringTwo))
