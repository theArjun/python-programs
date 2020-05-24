#  Demonstrates order of exceptions

try:
    print("Error is bound to happen here.")

    # This shouldn't be the order of exceptions.
    try:
        print("Excepted : SyntaxError: default except: must be last.")
    except:
        pass
    except EnvironmentError:
        pass
except SyntaxError:
    print("You encountered syntax error.")
finally:
    print("Do not worry. You are learning.")
