import turtle


for i in range (4):
    print (i)



alex = turtle.Turtle()
print (alex)

def square(t, length): 
    for i in range (4):
        t.fd(length)
        t.rt(90)
        
square(alex, 100)

tom = turtle.Turtle()
print (tom)

def polygon(t, length, n): 
    for i in range (n):
        t.fd(length)
        t.lt(360/n)
        
polygon (alex, 12, 15)

import math
def circle(t, r): 
   circumference = 2 * math.pi * r

   n= 50
   length = circumference / n
   polygon (t,length, n)
        
circle(alex, 20)

import math
def circle(t, r): 
   circumference = 2 * math.pi * r

   n= 50
   length = circumference / n
   polygon (t,length, n)
        
def arc (t, r ,angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

# circle (alex, 80)

arc (alex, 100, 180)

def star(t, length, n): 
    for i in range (n):
        t.fd(length)
        t.lt(360/n)
        
star (alex, 30, 50)

def arc1 (t, r ,angle):
    arc1_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc1_length / n
    step_angle = angle / n
    
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

# circle (alex, 80)

arc (alex, 100, 180)

jerry = turtle.Turtle()

print (jerry)
jerry.backward (100)
jerry.lt (90)
jerry.backward (100)
jerry.lt (90)
jerry.backward (100)
jerry.lt (90)
jerry.backward(100)

def polyline  (t, n, length, angle):
    for i in range (n):
        t.fd(length)
        t.lt(angle)

def polygon (t, n, length):
    angle=350/n
    polyline (t, n, length, angle)

# polygon (alex, 4, 100)
polyline (alex, 4, 100,90)

turtle.mainloop()