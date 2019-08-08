def dec_to_bin(num):

    ans = []
    while num > 0:

        rem = num % 2
        num = num // 2
        ans.append(rem)

    return ''.join(list(map(str, ans))[::-1])

print(dec_to_bin(int(input())))
