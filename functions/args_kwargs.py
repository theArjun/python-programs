# *args and **kwargs


# *args is used to send a non-keyworded variable length argument list to
# function.
# args refers to arguments and takes value as tuple.
# Instead of writing long list of positional arguments, passing args magic
# variable is preferred.
# args is just a variable name and a convention. Anyname is valid, though.
def my_maths(*args):
    print(args)
    print(sum(args))

my_maths(1, 2, 3, 4, 4)


# **kwargs allows you to pass keyworded variable length of arguments to a
# function. You should use **kwargs if you want to handle named arguments
# in a function.
# kwargs refers to keyword arguments and takes value as dictionary.
def my_activity(**kwargs):
    print(kwargs)
    print('I will play {} and eat {}.'.format(kwargs['sport'], kwargs['food']))

my_activity(sport='Cricket', subject='Python', name='Arjun', food='Biryani')


# Both args and kwargs can be used in combination. They are seen so in
# external libraries.W
def my_result(*args, **kwargs):
    print(args)
    print(kwargs)
    print('I have scored {} in {}.'.format(args[0], kwargs['subject']))

my_result(100, 'Arjun Adhikari', 'Bachelors', subject='Python')
