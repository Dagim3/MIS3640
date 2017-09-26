import turtle
from turtle_shape import arc, circle, move, polygon

alex = turtle.Turtle()
alex.speed(0)

circle(alex, 100)

def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        t.lt(180 - angle)


def flower(t, n, r, angle):
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0 / n)


bob = turtle.Turtle()

move(bob, 0, 100)
flower(bob, 7, 100.0, 60.0)

bob.hideturtle()
turtle.mainloop()