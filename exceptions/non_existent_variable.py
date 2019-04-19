#  Raises exception if a non-existent variable is operated. This will raises NameErrorException.

try:
    # The following statement will raise exception because num_one is not defined.
    print(num_one * 5)
except NameError:
    print("Try defining variable.")
finally:
    print("Keep practicing Python.")