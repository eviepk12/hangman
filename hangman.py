# Simple program on the hangman game on python
# Made by enal

import random
import string
from words_list import words
from hangman_visuals import lives_visual_dict

def get_valid_word(words): # takes in the list of words from the words_list
    word = random.choice(words) # Randomly chooses a word from the list
    while '-' in words or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # Letters in the word list
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7 

    # User input
    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print = (lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                lives = lives - 1
                print(f"\nYour letter, {user_letter}, is not in the word.")

        elif user_letter in used_letters:
            print("\nYou have already used that letter. Guess another letter.")
        else:
            print("\nThat is not a valid letter")
        
        # Only gets here when len(word_letters) == 0 OR when lives == 0, you lost basically
        if lives == 0:
            print(lives_visual_dict[lives])
            print(f"You lost!!, try again, the word was {word}")
        else:
            print(f"YAY!!! You guessed the word! {word}!!!")
        
if __name__ == '__main__':
    hangman()