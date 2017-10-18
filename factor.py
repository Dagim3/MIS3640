your_number = int(input("Pick a number:")) #Enter value

for factor in range( 1, your_number+1): #Range is from 1 to the entered number, +1 is used as the range function stops right before the last value
    factors = your_number % factor == 0 #This runs to check that the entered number doesn't have a remainder
    if factors == True: 
        print (factor) #Prints the number 
