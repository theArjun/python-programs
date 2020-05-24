# Max split in Python

my_intro = "My name is Arjun Adhikari."

# It's default splitting method.
print(my_intro.split())
# same as
print(my_intro.split(" "))

print("When splitted by 0 : ", end=" : ")
print(my_intro.split(" ", 0))

print("When splitted by 1 : ", end=" : ")
print(my_intro.split(" ", 1))

print("When splitted by 2 : ", end=" : ")
print(my_intro.split(" ", 2))

print("When splitted by 3 : ", end=" : ")
print(my_intro.split(" ", 3))

print("When splitted by 4 : ", end=" : ")
print(my_intro.split(" ", 4))

# When parameter in split() method reaches length of words in string,
# it's shows it behaviour like default splitting method.

print(my_intro.split(" "))
