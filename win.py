if guess in word:
        for position, letter in enumerate(word):
            if letter == guess:
                guessed_letters[position] = letter
        print('Good Guess: ',' '.join(guessed_letters))
        win += 1
        if win == (lens(word)-1):
            print('Good Guess: ',' '.join(guessed_letters))
            print ('--------------------------------')
            print ('Congratulation, you won!')
            break