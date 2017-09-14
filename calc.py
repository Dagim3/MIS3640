print('August 31- Excercise 1 & 2')
print('Hello World')
print(1+1)
print((42*60)+42)
print(10/1.61)
print((10/1.61)/((42*60)+42))
print (" ")
print('September 5 - Excercise 1')
print((4/3)*3.14*(5*5*5))
print (((24.95*60)+3+(.75*59))) 
print ((((8.15*1)+(7.12*3)+(8.15*1)+652)/100)+.4)
print (89-82)
print (" ")
print('September 7 - Excercise 1,2,3')
a = 3
print (a + 2)
b = .5
print (b)
c = 3
c == 5.0
print (c)
d = 10
e = d > 9
print (e)
print (5/2 == 5/2.0)
print (3.0 - 1.0 != 5.0 - 3.0)
print (3 > 4 or (2 < 3 and 9 > 10))
print (4 > 5 or 3 < 4 and 9 > 8)
print (not(4 > 3 and 100 > 6))
import time
print (time.time())
1437746094.5735958
print (" ")
print('September 12 - Excercise 1,2,3')

import math

a,b,c = input(2,3,5)

d = b**2-4*a*c # discriminant

if d < 0:
    print ("This equation has no real solution")
elif d == 0:
    x = (-b + math.sqrt(b**2 - 4*a*c)) / (2 * a)
    print ("This equation has one solutions: ", x)
else:
    x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2 * a)
    x2 = (-b + math.sqrt(b**2 - 4*a*c)) / (2 * a)
    print ("This equation has two solutions: ", x1, " and", x2)