beginNumber = int(input("Enter the starting number : "))
endNumber = int(input("Enter the ending number : "))
while beginNumber <= endNumber:
    if beginNumber % 2 == 1:
        print(beginNumber)
        beginNumber += 2
