num = int(input("Enter a number : "))
if num == 0:
    print("It is zero, considered as even.")
elif num % 2 == 0:
    print("%d is even number." % (num))
else:
    print("%d is odd number." % (num))
