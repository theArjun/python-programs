# We are assigning the numbers in a list

lst = [x for x in raw_input("Enter three numbers separated by space : \n").split()]
print(type(lst))
print(lst)

lst = [x for x in raw_input("Enter the numbers separated by comma : \n").split(",")]
print(lst)
