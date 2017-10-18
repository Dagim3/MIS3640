import random #Randomly picks values in a range

def drunkard_walk(steps): #The variable is the range length
    x = 0  
    y = 0 #Starting position
    print("The drunkard started at (%d,%d)." % (x, y))
    directions = ['North', 'East', 'South', 'West']  #List of different directions
    for i in range(int(steps)): #For loop for all values in the range of steps
        a = random.choice(directions)  #Will randomly select directions in the list above
        if a == 'North': #If North was selected, 1 step will be added to the y value
            y += 1
            print("The drunkard is now at (%d,%d)." % (x, y))
            distance = abs(x) + (y) #Distance is calculated by adding x and y, as the starting location was 0
            print("After", i+1, "intersections, he's", abs(distance), "blocks from where he started.")
        elif a == 'South': #If South was selected, 1 step will be subtracted from the y value
            y -= 1
            print("The drunkard is now at (%d,%d)." % (x, y))
            distance = abs(x) + (y) #Distance is calculated by adding x and y, as the starting location was 0
            print("After", i+1, "intersections, he's", abs(distance), "blocks from where he started.")
        elif a == 'East': #If East was selected, 1 step will be added to the x value
            x += 1
            print("The drunkard is now at (%d,%d)." % (x, y))
            distance = abs(x) + (y) #Distance is calculated by adding x and y, as the starting location was 0
            print("After", i+1, "intersections, he's", abs(distance), "blocks from where he started.")
        else: #If West was selected, 1 step will be subtracted from the x value
            x -= 1
            print("The drunkard is now at (%d,%d)." % (x, y))
            distance = abs(x) + (y) #Distance is calculated by adding x and y, as the starting location was 0
            print("After", i+1, "intersections, he's", abs(distance), "blocks from where he started.")
  
drunkard_walk (input('How many steps? ')) #Input the number of steps
