try:
    first_name = input("Enter your first name : ")
    # We need to provide a condition, if the condition is true, code runs smoothly, if false it throws AssertionError.
    assert len(first_name) < 10, "You entered first name of length greater than 10."
    print("Welcome {}".format(first_name))
except AssertionError:
    print("Something went wrong while entering name.")
    print("Please try again.")
else:
    print("Thanks for filling your name.")