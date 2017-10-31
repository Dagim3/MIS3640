Print ('Loading word list from file...')
Print ('113809 words loaded.')
Print ('Welcome to the game, Hangman!')

import random 
words = open('words.txt').readlines() 
word = random.choice(words)
check = word
Print ('I am thinking of a word that is', len(word), 'letters long.')

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
guesses = ''
turns = 10

while turns > 0:         
    print ('You have', turns,'guesses left')	
	print ('Available letters: ', letters)  
	guess = input("Please guess a letter: ") 
    guesses += guess  
	failed = 0             
	for char in check:
		if char in guesses:
			print ('hi')
		else:
            print ("_"*len(word))     
            failed += 1    
    if failed == 0:        
        print ("Congratulations, you won!")
        break              
    if guess not in word:  
        turns -= 1        
        letter.remove(guess)
		print ('Oops! That letter is not in my word: _ a_ _')    
 		if turns == 0:           
            print ('Sorry, you ran out of guesses. The word was ', word)