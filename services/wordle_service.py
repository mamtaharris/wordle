import json
import random
from flask import Flask
from models.wordle_request import *
from models.wordle_response import *
from models.error_response import *

def load_words():
    with open('services/five_letter_words.json') as json_file:
        return json.load(json_file)

def wordle_logic(reqBody):
    english_words = load_words()
    word_to_guess = random.choice(list(english_words))
    response = [] 

    guess = WordleReqBody(reqBody).word
    guess = str(guess).strip()
    if len(guess) != 5:
        return ErrorRespBody("Please enter a 5 letter word.", 400)
    if guess not in english_words:
        return ErrorRespBody("Sorry, that's not a word.", 400)
    
    for letter in range(0, len(guess)):
        if guess[letter] == word_to_guess[letter]:
            list.append(response, WordleRespBody(guess[letter], 2))
        elif guess[letter] in word_to_guess:
            list.append(response, WordleRespBody(guess[letter], 1))
        else:
            list.append(response, WordleRespBody(guess[letter], 0))
    
    return(list)
     