# Here, we define a function named display with a parameter 'name'
def display():
    # Then we define another function inside the display() function named 'message'
    def message():
        # The inner function returns the literal "display "
        return "Hello "
    # We are returning the function; no parenthesis here
    return message
# Assigning the function to a variable
fun = display()
# Printing a variable that is assigned to function; put parenthesis here too.
print (fun())