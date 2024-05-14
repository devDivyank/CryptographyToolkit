def gcd(num1: int, num2: int):
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1 % num2)

if __name__ == '__main__':
    print(gcd(102, 351))