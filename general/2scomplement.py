def dec_to_bin(num):

    ans = []
    while num > 0:
        ans.append(str(num % 2))
        num = num // 2
    return int(''.join(ans)[::-1])

def bin_add(*args): return bin(sum(int(x, 2) for x in args))[2:]


def complement(num):

    bin_num = list(str(dec_to_bin(num)))

    for i in range(len(bin_num)):

        if bin_num[i] == '1':
            bin_num[i] = '0'
        else:
            bin_num[i] = '1'

    return ''.join(bin_num)

print(bin_add(complement(4), '1'))
