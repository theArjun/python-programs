# Raises exception if a non-existent file is opened for reading purpose with
# FileNotFoundError.

try:
    with open('my_file.txt', 'r') as my_file:
        data = my_file.read()
except FileNotFoundError:
    print("The file doesn't exist.")
finally:
    print("You're going really good in Python.")

