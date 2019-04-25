# Credit : Abiral Bhattarai
# Title : Delete a element of order x from List in Python

# a = int(input("How many number you want to enter?"))
# numlist = list()  # Entered array
# latelist = list()
# for i in range(a):
#     x = int(input("Enter the number="))
#     numlist.append(int(x))
# print("Entered numbers array")
# print(numlist)
# b = int(input("Which order array you want to delete?"))
# for i in range(a):
#     if b != i:
#         latelist.append(int(numlist[i]))
# print(latelist)

# Author : Arjun Adhikari
a = int(input("How many number you want to enter ?"))
lst = input().split()[:a]
# Also can be done like this.
# lst = list(map(lambda x: int(x), input().split()[:a]))
lst = list(map(lambda x: int(x), lst))
print(lst)

b = int(input("Which order array you want to delete ?"))
del(lst[b-1])
print(lst)
