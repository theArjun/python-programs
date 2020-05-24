# Reading text from a file.


# One way of opening file
with open("my_file.txt", "r") as f:
    f.seek(0)
    content = f.read()
    print(content)

# Another way of opening file
my_file = open("my_file.txt", "r")
print(my_file.mode)

# This leads the file cursor to the end of the file.
print(my_file.read())

# To set the cursor position to the beginning of the file, we should invoke
# seek() method. It takes parameter as the position of file cursor.
my_file.seek(0)

# Passing parameter in read() method will read upto the passed parameter only.
print(my_file.read(12))

my_file.seek(0)

# To know the position of the cursor, we can invoke tell() method.
my_file.tell()

# Inspite of reading character by character, we can read line too.
# For that, we should invoke readline() method.
# It accepts parameter as size of characters.
my_file.seek(0)
print(my_file.readline())

my_file.seek(0)

# We can also read lines of a file using readlines() method.
# It prints a space between them because newline is auto-added by
# print() method.
for line in my_file.readlines():
    print(line)

my_file.seek(0)

# Prints lines which starts from 'W'
for line in my_file.readlines():
    if line.startswith("W"):
        print(line)
