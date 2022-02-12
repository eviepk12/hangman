# Simple program on the hangman game on python
# Made by enal

import random
import string
from words_list import words

def get_valid_word(words): # takes in the list of words from the words_list
    word = random.choice(words) # Randomly chooses a word from the list
    while '-' in words or ' ' in words:
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
        print(f"You have {lives}, lives left and you have used these letters: ", " ".join(used_letters))