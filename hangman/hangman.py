import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) # randomly choses a word from words.py  
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # keeping track on what letter has been guessed in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed

    lives = 6

    while len(word_letters) > 0 and lives > 0:

        print('You have', lives, 'lives, You have used the letters:', ' '.join(used_letters)) # letters used

        word_list = [letter if letter in used_letters else '-' for letter in word] # location of the current word
        print('Current word: ', ' '.join(word_list))


        user_letter = input('Guess a letter: ').upper() # getting user input
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            
            else:
                lives = lives - 1
                print('You just lost a life')
        
        elif user_letter in used_letters:
            print('You have already selected this letter')
        
        else:
            print('Invalid character')

    if lives == 0:
        print('Your lives are up, the word was', word)
    else:
        print('You guessed the', word, '!!!')

hangman()