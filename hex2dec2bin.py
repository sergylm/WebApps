def hex2bin(num):
    return bin(int(num, 16))[2:].zfill(len(num)*4)


def dec2bin(num):
    relleno = len(bin(int(num, 10))[2:])
    while not relleno % 4 == 0:
        relleno = relleno + 1
    return bin(int(num, 10))[2:].zfill(relleno)


def bin2dec(num):
    return int(num, 2)


def bin2hex(num):
    return hex(int(num, 2))[2:].zfill(int((len(num)/4)))

