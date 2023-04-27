import random
from words import words
import string

def get_valid_word():
    word=random.choice(words)
    while '-' in words or ' ' in words:
        word=random.choice(words)
    return word.upper()

def hangman():
    word=get_valid_word(words)
    word_letters=set(word)
    alphabet=set(string.ascii_uppercase)
    used_letters=set()
    
    user_input=input("enter your letter ").upper()
    if user_input in alphabet-used_letters:
        used_letters.add(user_input)
        if user_input in word_letters:
            word_letters.remove(user_input)
            
    
      