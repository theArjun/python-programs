def bin_to_dec(num):

    dec = 0
    str_num = list(str(num))[::-1]
    for i in range(len(str_num)):
        dec += int(str_num[i]) * (2 ** i)

    return dec
