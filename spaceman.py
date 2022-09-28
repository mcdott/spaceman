import random
from re import S, T

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True
    
def is_repeat_guess(guess, letters_guessed, letters_not_guessed):
    # Check if the letter has already been guessed
    if guess in letters_guessed:
        return True
    else:
        letters_guessed.append(guess)
        letters_not_guessed.remove(guess)
        return False

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    # Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    guessed_word = ''
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word = guessed_word + letter
        else:
            guessed_word = guessed_word + '_'
    return guessed_word


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    # Check if the letter guessed is in the secret word
    if guess in secret_word:
        return True
    else:
        return False


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    # Initialize game variables
    remaining_incorrect_guesses = 7
    letters_guessed = []
    letters_not_guessed = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    # Show the player information about the game according to the project spec
    print("Welcome to Spaceman!")
    print(f"The secret word contains {len(secret_word)} letters")
    print("You're allowed 7 incorrect guesses.  Please enter one letter per round.")

    while not is_word_guessed(secret_word, letters_guessed):
        #Ask the player to guess one letter per round (and check that it is only one letter)
        guess = input("Enter a letter: ")
        
        # Check if the user has already guessed that letter
        if is_repeat_guess(guess, letters_guessed, letters_not_guessed):
            print('You previously guessed that letter. Guess again!')
            continue

        # Check if the user has guessed all of the correct letters, if so, tell them they have won
        if is_word_guessed(secret_word, letters_guessed):
            print("You won!")
            return

        # Check if the guessed letter is in the secret or not and give the player feedback
        if is_guess_in_word(guess, secret_word):
            print("Your guess appears in the word!")
        else:
            print("Sorry, your guess was not in the word. Try again!")
            remaining_incorrect_guesses -= 1
            # If the user has remaining guesses, tell them how many
            if remaining_incorrect_guesses > 0:
                print(f'You have {remaining_incorrect_guesses} guesses left.')
            # If the user is out of guesses, tell them they have lost and end the game    
            else:
                print("Sorry, you didn't win.  Try again!")
                print(f"The word was: {secret_word}")
                return

        # Show the letters that have been guessed correctly so far 
        print(get_guessed_word(secret_word, letters_guessed))
        # Show the letters that haven't been guessed yet
        letters_not_guessed_str = ''
        for letter in letters_not_guessed:
            letters_not_guessed_str = letters_not_guessed_str + letter
        print(f"These letters haven't been guessed yet: {letters_not_guessed_str}")


# These function calls start the game
secret_word = load_word()
# print(secret_word)
spaceman(secret_word)
