def dec_to_bin(num):

    ans = []
    while num > 0:
        ans.append(str(num % 2))
        num = num // 2
    return int("".join(ans)[::-1])
