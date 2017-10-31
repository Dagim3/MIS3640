import random 

print ('Loading word list from file...')
with open('words.txt') as f:
        wordss = [word for line in f for word in line.split()]
        wordss = len(wordss)
print (wordss,' words loaded.')
print ('Welcome to the game, Hangman!')

words = open('words.txt').readlines() 
word = random.choice(words)
check = word    
print ('I am thinking of a word that is', len(word)-1, 'letters long.')
print ('--------------------------------')

guesses = []
turns = 8
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

guessed_letters = (len(word)-1) * ['_']
while turns > 0:         
    print ('--------------------------------')
    print ('You have', turns,'guesses left')
    letters2 = letters[:]

    guess = str(input("Please guess a letter: "))
    guesses.append(guess)
    win = 0
    for ch in guesses:
        string=(([s.replace(ch, '') for s in letters2]))
    print (' '.join(string))
    
    if guess in guesses:
        print ("Oops! You've already guessed that letter:",' '.join(guessed_letters))
            

    if guess in word:
        for position, letter in enumerate(word):
            if letter == guess:
                guessed_letters[position] = letter
        print('Good Guess: ',' '.join(guessed_letters))
        win += 1
        if guessed_letters == word:
            print('Good Guess: ',' '.join(guessed_letters))
            print ('--------------------------------')
            print ('Congratulation, you won!')
            break
    if guess not in word:  
        turns -= 1       
        for position, letter in enumerate(word):
            if letter == guess:
                guessed_letters[position] = letter
        print('Oops! That letter is not in my word: ',' '.join(guessed_letters))
        if turns == 0:
            print ('Sorry, you ran of guesses. The word was ', word)
