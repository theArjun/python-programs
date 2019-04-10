import mymath

print(mymath.sum(20, 10))
print(mymath.diff(20, 10))
print(mymath.mult(20, 10))
print(mymath.divi(20, 10))

# Creating a alias name to import so that no need to always type mymath while envoke mymath.function_name everytime.
import mymath as ma
print(ma.sum(20, 10))

# If we ever feel to exclude the module name, and just envoke the function by its name, then :
from mymath import *
print(sum(10,20))


