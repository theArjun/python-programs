# Find all of the numbers from 1-1000 that have a 3 in them.

my_list = [num for num in range(1001) for splitted_digit in str(
    num) if splitted_digit == '3']
print(my_list)

# Or it can be done like this :

my_list = [num for num in range(1001) if '3' in str(num)]
print(my_list)
