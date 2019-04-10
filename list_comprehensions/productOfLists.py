# Prints the product of elements of two different lists 

listOne = [1, 2, 3, 4, 5, 6, 7, 8]
listTwo = [11, 12, 13, 14, 15, 16, 17, 18]

# Conventional Way
result = []
# We are providing length of listOne in loop. 
for i in range(0,len(listOne)):
    result.append(listOne[i]*listTwo[i])
print(result)

# Using list comprehension
result = []
result = [listOne[i]*listTwo[i] for i in range(0,len(listOne))]
print(result)
