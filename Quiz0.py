def pos_neg(a, b, negative):
    if a<0 and b>0:
        return ('true')
    elif a>0 and b<0:
        return ('true')
    elif negative==True:
        return ('true')
    else:
        return('False')

# Expected outputs:

print(pos_neg(1, -1, False))
# True
print(pos_neg(-1, 1, False))
# True
print(pos_neg(-4, -5, True))
# True
print(pos_neg(-2, -5, False))
# False
print(pos_neg(1, 2, False))
# False


# 2. Given two int values, return their sum. Unless the two values
# are the same, then return double their sum.


def sum_double(a, b):
    if a==b:
        return (2*(a+b))
    else:
        return (a+b)


# Expected outputs:

print(sum_double(1, 2))
# 3
print(sum_double(2, 2))
# 8


# 3. Given an int n, return the absolute difference between n and 21,
# except return double the absolute difference if n is over 21.

def diff21(n):
    if n>21:
        return abs(21-n)
    else:
        return abs(2*(n-21))


# Expected outputs:

print(diff21(19))
# 2
print(diff21(21))
# 0
print(diff21(25))
# 8