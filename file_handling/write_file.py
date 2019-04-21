# Writing into a file


my_file = open("my_file_one.txt", 'w')

# It returns the no of characters written.
print(my_file.write("My name is Arjun Adhikari."))
my_file.close()
