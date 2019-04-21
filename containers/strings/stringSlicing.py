s = "You are awesome."

print(s[0:5])  # It prints from the starting index to the ending index.
print(s[0:])  # It prints till the end.
print(s[:16])  # It prints from the beginning and reaches the limit.

# Trying Negative Numbers

print(s[-3:-1])  # Here, -1 means . and -3 means m by negative indexing.

s1 = "Nepal"
print(s1[-3:-2])  # It prints p only.s

# Steps In Slicing

s2 = "Arjun"
# Here, first digit means the starting index and second means the ending index
# and last digit meand the no of index to get skipped and slicte it. The last
# digit determines the alternative-ness of the slicing operation. Default value
# of last digit is always 1 if not mentioned.
print(s2[0:4:2])

# Reverse String
# Last value can't be zero and positive value creates undesirable results.
# Double colon is mandatory.
print(s[15::-1])
