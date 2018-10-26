stringOne = str(input("Enter string one : "))
stringTwo = str(input("Enter string two : "))

print("\nBefore Swapping\n")
print("String One : %s"%(stringOne))
print("String Two : %s"%(stringTwo))

# Pre-Defined Method
# stringOne,stringTwo = stringTwo,stringOne

stringOne=list(stringOne)+list(stringTwo)
stringTwo=stringOne[0:len(stringTwo)]
stringOne=stringOne[len(stringTwo):len(stringOne)]
stringOne=''.join(stringOne)
stringTwo=''.join(stringTwo)

# Appending the list will create a nested-array which is unwanted result this time
# stringOne.append(stringTwo)

print("\nAfter Swapping\n")
print('String One : %s'%(stringOne))
print("String Two : %s"%(stringTwo))