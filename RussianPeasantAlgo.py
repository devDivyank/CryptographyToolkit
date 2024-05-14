def russianPeasant(a: hex, b: hex):
    column = []
    while True:
        if b % 2 != 0:
            column.append(a)
        if b == 1:
            break

        if a > 0x7f:
            a = a << 1
            a = a ^ 0x11b
        else:
            a = a << 1
        b = b >> 1
    result = column[0]
    for val in column[1:]:
        result ^= val

    return hex(result)

if __name__ == '__main__':
    # print(russianPeasant(0x0e, 0xed))
    print(hex(0x4e ^ 0x94 ^ 0x99 ^ 0X05))

