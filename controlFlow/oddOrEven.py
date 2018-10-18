num = int(input("Enter a number : "))
if num%2==0:
    evenFlag = True;
else:
    evenFlag = False;

if evenFlag==True:
    print('%d is even number.'%(num))
else:
    print('%d is odd number.'%(num))
