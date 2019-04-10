from __future__ import print_function
print()
print("Hello "*3)
print("All the power \n is with in you") #\n is new line character


a,b = 10,20
print(a,b,sep='\n')


name = "John"
marks = 94.5

# This is how we print the value of multiple variables using comma operator inside the print function.
print("Name = ",name,"Marks = " ,marks)

# This is how we print the value of strings and integers using format specifier and format specifier for the numeric data also can shorten or longen the data 
print("Name is %s,Marks is %.3f"%(name,marks))

# This is how we print the value of variables using braces
print("Name is {},Marks is {}".format(name,marks))

# This is how we print the value of variables using braces indexing
print("Name is {0},Marks is {1}".format(name,marks))

