# This program calculates the product of only two command line arguments; else array will be out of index and error message will be delivered.
import sys
lst = sys.argv
product = 1
# The default data type of the list element is string. We need to type-cast into integer inorder to carry out arithmetic operation.
product=int(lst[1])*int(lst[2]) # Index one contains the name of the script by-default.
print("Product is %d . "%(product))