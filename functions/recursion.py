# Factorial of a given number

# Caution : Give a condition so that the recursion stops, here is num equal to zero.

# Function takes a number as parameter
def factorial (num):
    # If number is equal to 0 return 1
    if num == 0:
        return 1
    # If number isn't equal to 1, return that number * factorial of number -1 i.e. recursively calling the function until it's 0
    else:
        return num * factorial(num - 1)

# Prompting user to input a number
number = int(input("Enter a number : "))
# Calling the function with the prompted number as argument
fact = factorial(number)
print(fact)
