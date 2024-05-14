def squareMultiply(x, ex, n):
    r = x
    ex = bin(ex)[2:]
    for i in range(0, len(ex)-1):
        r = (r**2) % n
        if ex[i+1] == "1":
            r = (r*x) % n
    return r

if __name__ == '__main__':
    x = 1234567
    ex = 23456789
    n = 3333337
    print(squareMultiply(x, ex, n))   # ANS = 1138812
