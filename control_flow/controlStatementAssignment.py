# This programs prints the number till the entered number, skips the
# of number and doesn't exceed 100.
num = int(input("Enter a number : "))
i = 0
while i <= num:
    i += 1
    if i % 10 == 0:
        continue
    if i > 100:
        break
    print(i)
    i += 1
