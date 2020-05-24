# Raises exception if a string is entered, not a number as expected.
# It also can be solved using ValueError.
try:
    num = int(input("Enter a number. Otherwise it will raise exception. : "))
    # Checks if number is instance of integer or not.
    if not isinstance(num, int):
        raise Exception()
except:
    print("Exception raised. You didn't enter number.")
# If no exception arises.
else:
    print("You've entered a number. You're good.")
finally:
    print("Keep practicing python.")
