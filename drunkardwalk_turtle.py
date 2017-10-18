import turtle
import random

walk = turtle.Turtle()


def drunkard_walk(d,t): #The two variables are turtle function and the range length
    import random #Randomly picks values in a range
    x = 0
    y = 0 #Starting position
    for i in range(t): #For loop for all values in the range of t
            directions = ['North','East','South','West']  #List of different directions
            a = random.choice(directions) #Will randomly select directions in the list above
            if a == 'North': #If north was selected, the turtle will move forward 10, print "North 1 step" and add 1 to the current y of the drunkard
                d.fd(10)
                print ('North 1 step')
                y += 1
            elif a == 'South': #If south was selected, the turtle will move back 10, print "South 1 step" and subtract 1 from the current y of the drunkard
                d.fd(-10)
                print ('South 1 step')
                y -= 1
            elif a == 'East': #If north was selected, the turtle will move to the right 10, print "East 1 step" and add 1 to the current x of the drunkard
                d.rt(10)
                print ('East 1 step')
                x += 1
            else: #If west was selected, the turtle will move to the left 10, print "West 1 step" and subtract 1 from the current x of the drunkard
                d.lt(10)
                print ('West 1 step')
                x += 1
            distance = abs(x) + abs(y) #Calculates the number of steps away from the original location, which was a base 0
            print ("Drunkard walked", abs(distance), "steps away from his original spot")

n = input('How many steps? ') #Input number of steps
drunkard_walk (walk,int(n)) #Run the function


