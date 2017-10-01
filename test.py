def example():
    print('this code will run')
    z = 3 + 9
    print(z)

example()

def basic_window(width,height,font='TNR'):
    # let us just print out everything
    print(width,height,font)
basic_window(350,500)


import math


def newtons(n):
    n = float(n)  # convert input to float so printout() doesn't have to
    x = n / 2  # rough estimate
    i = 0
    while i < 10:
        y = (x + n / x) / 2  # newtons method
        x = y
        i += 1
    return y


def libmath(n):
    n = float(n)
    return math.sqrt(n)


def printout():
    print ('{:<12}\t{:<12}\t{}'.format('newtons', 'libmath', 'delta'))
    for i in range(1, 10):
        n = round (newtons(i),3)
        l = round (libmath(i),3)
        ab = abs(n - l)
        print ('{:<12}\t{:<12}\t{}'.format(n, l, ab))

printout()