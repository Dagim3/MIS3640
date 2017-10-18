import turtle
import random

alex = turtle.Turtle()


def test(d,t):
    import random
    x = 0
    y = 0
    for i in range(t):
            directions = ['North','East','South','West']  
            a = random.choice(directions) 
            if a == 'North':
                d.fd(10)
                print ('North 10')
                y += 10
            elif a == 'South':
                d.fd(-10)
                print ('South 10')
                y -= 10
            elif a == 'East':
                d.rt(10)
                print ('East 10')
                x += 10
            else:
                d.lt(10)
                print ('West 10')
                x += 10
            distance = (x + y)
            print ("Drunkard walked", abs(distance), "steps away from his original spot")

n = input('How many steps? ')
test (alex,int(n))
