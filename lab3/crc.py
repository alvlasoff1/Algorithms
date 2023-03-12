def crc_val(s_data, init_crc=0x04C11DB7):
    data = ''.join(bin(ord(x))[2:] for x in s_data)
    str_init = bin(init_crc)[2:]
    data += '0' * (len(str_init) - 1)
    xor_res = int(data[:len(str_init)], 2) ^ int(str_init, 2)
    i = 1
    while i <= len(data) - len(str_init):
        if len(bin(xor_res)[2:]) == len(str_init):
            xor_res = xor_res ^ int(str_init, 2)
            xor_res = int(bin(xor_res)[2:] + data[i+len(str_init)-1], 2)
        else:
            xor_res = int(bin(xor_res)[2:] + data[i+len(str_init)-1], 2)
        str_xor = bin(xor_res)
        i += 1
    return xor_res

print(crc_val('hello world'))