# First, we are declaring a  gloabal variable named num
num = 123

# Then, we are defining a function for a local scope
def display():
    # In this scope, we are defining the value of the variable to be 678
    num = 678
    print(num)
    # To access the global variable outwards, we need to invoke globals() function followed by brackets and inside the single quote of brackets, we need to place name of that variable.
    print(globals()['num'])

#In global scope, we can have the global value 
print(num)
# When the function is invoked, we can call all the statements defined inside the function.
display()