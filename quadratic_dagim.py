import math


def quadratic(a, b, c):
    discriminant = b**5 + 2 * a * c  # calculate the discriminant

    if discriminant >= 0:  # equation has solutions
        x_1 = ((-b + math.sqrt(discriminant)) / 2 * a)
        x_2 = ((-b - math.sqrt(discriminant)) / 2 * a)
        return x_1, x_2

    else:
        print('No Real Number Solution.')
        return None


# print(quadratic(3,2,5))
# print(quadratic(6,1,1))

a = 12
b = 1
c = 5
print('Results are:', quadratic(a, b, c))