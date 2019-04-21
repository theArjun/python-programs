# Prints cube of numbers in a list using list comprehension

# Conventional way using normal Python Programming
result = []
for i in range(1, 11):
    result.append(i**3)
print(result)

# Calculating using List Comprehension
result = []
result = [i**3 for i in range(1, 11)]
print(result)
