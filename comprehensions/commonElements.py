# Prints common elements in two different lists

# Conventional Way
listOne = [1, 2, 3, 4, 5, 6, 7, 8, 9]
listTwo = [1, 3, 5, 7, 9, 11, 13, 15, 17]

result = []
for i in range(0, len(listOne)):
    for j in range(0, len(listTwo)):
        if listOne[i] == listTwo[j]:
            result.append(listOne[i])
print(result)

# Another Method
result = []
for i in listOne:
    if i in listTwo:
        result.append(i)
print(result)

# Using list comprehensions
result = []
result = [i for i in listOne if i in listTwo]
print(result)
