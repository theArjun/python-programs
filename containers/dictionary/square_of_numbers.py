# Write a Python script to generate and print a dictionary that contains a
# number (between 1 and n) in the form (x, x*x).

num = int(input)
my_dict = {num: num * num for num in range(1, num + 1)}
print(my_dict)
