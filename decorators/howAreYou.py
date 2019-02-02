# Adds how are you to the function that prints Hello and passed parameter using decorator

def how_are_you(tempFunction):
    def wrap_hello(name):
        print(tempFunction(name))
        print("How are you ?")
    # Returning the wrapper inner function
    return wrap_hello

# Don't forget the @ before the name of decorator function
@how_are_you
def hello(name):
    return "Hello "+name

hello("Arjun")