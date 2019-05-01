# Python uses C-Style formatting to create new formatted strings.

# The "%" operator is used to format a set of variables enclosed in a "tuple"(a fixed sized list).

# %s - String(or any string like representation like numbers or sequences.)
# %d - Integer
# %f - Float
# .<number of decimal precision> - Floating digits with a fixed amount of
# digits to the right of the dot.

# %x / %X - Integers in hexadecimal representation (uppercase or lowercase).


# For single object, no need og parenthesis.
name = "Arjun"
print("Hello %s" % name)

age = 20
print("%s is %d year old." % (name, age))

# To print the precise decimal number.
bank_balance = 3435884.90
print("%s have %.1f bank balance." % (name, bank_balance))

# Objects like lists, tuples, set also can be formatted like string.
my_score = [1, 2, 3, 4, 5]
print("%s loves the position %s." % (name, my_score))

my_hobbies = ('cycling', 'swimming', 'designing')
print("%s doing %s" % (name, my_hobbies))

sample_num = 243
print("%d in Hexadecimal : %x (lowercase)" % (sample_num, sample_num))
print("%d in Hexadecimal : %X (uppercase)" % (sample_num, sample_num))
