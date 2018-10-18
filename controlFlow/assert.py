# This program requests user to enter a number greater than 10.

num=int(input("Enter a number greater than 10 : "))
assert num>10 , "Invalid number"
print("You entered %d"%(num))