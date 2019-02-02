# Calculates sum of two numbers using lambdas

numberOne = int(input("Enter a number : "))
numberTwo = int(input("Enter another number : "))

# Lambda expression for sum of two numbers
addition = lambda x, y: x+y
# Printing the result
print("Sum = ",addition(numberOne,numberTwo))
