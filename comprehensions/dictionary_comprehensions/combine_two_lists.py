# Dictionary Comprehension using zip function

names = ['arjun', 'hari', 'shyam', 'krishna']
salary = [10000, 20000, 30000, 40000]

my_dict = {name: salary_ for name, salary_ in zip(names, salary)}

print(my_dict)
