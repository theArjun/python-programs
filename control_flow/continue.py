# This programs prints the number from 1 to 20 and skips the number if it is
# multiple of 3.

for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)
