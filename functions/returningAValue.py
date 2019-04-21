# A function is defined which takes two inputs a and b as formal parameters
def average(a, b):
    # It returns the average of those numbers by return keyword after
    # arithmetic operation.
    return (a+b)/2


# It will prompts user for inputs and stores it in a list named num
num = [int(x)
       for x in input("Enter two numbers separated by space : ").split()]
# Then it will print the average by invoking the function inside the print
# statement.
print("Average of given numbers : ", average(num[0], num[1]))
