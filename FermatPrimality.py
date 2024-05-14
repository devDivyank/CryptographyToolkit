import random
from SquareAndMultiply import *

def primalityCheck(n):
    for i in range(20):
        a = random.randint(2, n-1)
        if squareMultiply(a, n - 1, n) == 1:
            print("Possible prime.")
        else:
            print("Not prime.")
            break
