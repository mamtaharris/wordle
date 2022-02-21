import json
import random
from flask import Flask
from models.wordle_request import *

def load_words():
    with open('services/five_letter_words.json') as json_file:
        return json.load(json_file)

def wordle_logic(reqBody):
    english_words = load_words()
    word_to_guess = random.choice(list(english_words))
    tempStringReturn = ""

    guess = WordleReqBody(reqBody).word
    guess = guess.strip()
    if len(guess) != 5:
        return("Please enter a 5 letter word.\n")
    if guess not in english_words:
        return("Sorry, that's not a word.\n")
    
    if guess == word_to_guess:
        return("Congratulations, you guessed correctly!\n")
        
    for letter in range(0, len(guess)):
        if guess[letter] == word_to_guess[letter]:
            tempStringReturn = tempStringReturn + (guess[letter].capitalize(), ": * ")
        elif guess[letter] in word_to_guess:
            tempStringReturn = tempStringReturn + (guess[letter].capitalize(), ": + ")
        else:
            tempStringReturn = tempStringReturn + (guess[letter].capitalize(), ": - ")
    tempStringReturn = tempStringReturn + "\n"
    
    return(tempStringReturn)
     