# Global variable
num = 123


def display():
    # Without a variable of same name inside the local scope, we can access
    # the global variable
    y = 678
    num = 789
    print(num)


# If we want to print the value of y in global scope, which was defined in
# local scope, the compiler will throw a error "Name 'y' is not defined"
print(y)

# But we can access the num variable
print(num)
display()
