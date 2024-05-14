import math

def EEA(a, b):
    if a == 0:
        return b, 0 , 1
    else:
        gcd, _x, _y = EEA(b%a, a)
        x = _y - (int(b / a) * _x)
        y = _x
        return gcd, x, y

if __name__ == '__main__':

    a = int(input("First number: "))
    b = int(input("Second number: "))
    gcd, x, y = EEA(a, b)

    if x < 0:
        num = x
        while num < 0:
            num += b
        x = num

    if y < 0:
        num = y
        while num < 0:
            num += a
        y = num

    print("gcd = " + str(gcd))
    print("x = " + str(x))
    print("y = " + str(y))
