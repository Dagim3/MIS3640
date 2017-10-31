import random

WORDLIST_FILENAME = "words.txt"
wordlist = open('words.txt').readlines() 

def loadWords():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    line = inFile.readline()
    wordlist = string.split(line)
    print ("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    return random.choice(wordlist)


def isWordGuessed(secretWord, lettersGuessed):
    count = 0
    wordcount = len(secretWord) #counts the letter in the word
    for let in lettersGuessed:   
        if let in secretWord:
            count += 1
        else:
            count += 0
    if count == int(wordcount): #if the number of letters found equals the letters in the word, it will return True as the whole word was found. If the values don't equal, the whole word was not found
        return True
    else: 
        return False

secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(isWordGuessed(secretWord, lettersGuessed))

# Expected output:
# False


def getGuessedWord(secretWord, lettersGuessed):
    guessed=''
    for e in secretWord:
        if e in lettersGuessed:#Walks through the letters in the secretWord, in order
            guessed=guessed+e #If found, it will add the letter to the empty string
        else:
            guessed=guessed+'_' #If not, it will add a space to the empty string
    return guessed 

secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getGuessedWord(secretWord, lettersGuessed))

# Expected output:
# '_ pp_ e'


def getAvailableLetters(lettersGuessed):
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for value in lettersGuessed: #Walks through the letters in lettersguessed
        alpha.remove(value) #It will remove the letter from the alphabet list, if found in lettersguessed
    return ' '.join(alpha)

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))

# Expected output:
# abcdfghjlmnoqtuvwxyz


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many 
      letters the secretWord contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.
    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.
    Follows the other limitations detailed in the problem write-up.
    '''
    guessesLeft = 8
    lettersGuessed =[]

    print('-----------')
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.' ) #Calculates the length of the word
    print('-----------')

    while guessesLeft > 0: #While loop until the guesses left reaches 0
        if isWordGuessed(secretWord, lettersGuessed): #If the isWordGuessed functions returns a True, you win
            return print('Congratulations, you won!')
        print('You have ' + str(guessesLeft) + ' guesses left.') #Prints the number of guesses left
        print('Available Letters: ' + getAvailableLetters(lettersGuessed)) #Prints available letters
        user_input = input('Please guess a letter: ') #User input for a letter
        user_input = str(user_input)
        user_input = user_input.lower() #Makes sure that all inputted value are lowercase

        if user_input not in lettersGuessed: #If the letter is still available for use, it will add it to the lettersGuessed list
            lettersGuessed.append(user_input)

            if user_input in secretWord: #If the lettter was in the secret word, it will show the status of your hangman game with the Good Guess statement
                print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
                print('-----------')
            else:
                print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed)) #If the lettter was in the secret word, it will show the status of your hangman game with the not in my word statement
                print('-----------')
                guessesLeft -= 1 #Decreases guesses left by 1
        else:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)) #If the letter is not available for use, it will print the already guessed statement with the status of the hangman game
            print('-----------')

    return print("Sorry, you ran out of guesses. The word was " + str(secretWord)) #Loss statement with the full word

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)