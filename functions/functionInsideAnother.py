# Here, we define a function named display with a parameter 'name'
def display(name):
    # Then we define another function inside the display() function named
    # 'message'
    def message():
        # The inner function returns the literal "Hello "
        return "Hello "

    # In the outer function assigns the value returned by the message function
    # and the parameter passed to it into a variable and returns it
    result = message() + name
    return result


# Now, we can pass a name and can get the value
print(display("Arjun"))
# But, we can't directly invoke function named message, because it doesn't
# have global scope and it has it's limited scope inside the display()
# function only.
print(message())
