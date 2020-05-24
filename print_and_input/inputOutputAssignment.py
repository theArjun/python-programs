num = int(input("Enter a number : "))
r = range(2, num - 1)
for x in r:
    if x % 2 == 0:
        primeFlag = False
    else:
        primeFlag = True

if primeFlag is False:
    print("The given number is not prime.")
else:
    print("The given number is prime.")
