lst = [1,2,3,4,5]
product=1

# for i in lst:
#     product*=i

for i in range(0,len(lst)):
    product*=lst[i]

print("Product is %d."%(product))
