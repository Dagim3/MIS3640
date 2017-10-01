import math


def mysqrt(a):
    a = float(a)  
    x = a / 2  
    i = 0
    while i < 10:
        y = (x + a / x) / 2
        x = y
        i += 1
    return y


def mathsqrt(a):
    a = float(a)
    return math.sqrt(a)


def test_square_root():
    print ("{:<12}\t{:<12}\t{}".format('mysqrt(a)', 'math.sqrt(a)', 'diff'))
    for i in range(1, 10):
        n = round (mysqrt(i),4)
        l = round (mathsqrt(i),4)
        ab = abs(n - l)
        print ("{:<12}\t{:<12}\t{}".format(n, l, ab))

test_square_root()