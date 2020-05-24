# To check a given number is odd or even using Lambda
num = int(input("Enter a number : "))

# Syntax >>  lambda someVariable : doThisOne if caseOne else doThisTwo


def result(a):
    return "YES" if a % 2 == 0 else "NO"


print(result(num))

print(result(3))
