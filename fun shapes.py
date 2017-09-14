import turtle
import math

practice = turtle.Turtle()
print practice

    def polygon(t, length, n): 
    for i in range (n):
        t.fd(length)
        t.lt(360/n)
        
polygon (practice, 12, 15)

import math
def yingyang(t, r): 
   circumference = 2 * math.pi * r

   n= 50
   length = circumference / n
   polygon (t,length, n)
        
yingyang(alex, 20)