import json
import random
from flask import jsonify, make_response

def load_words():
    with open('services/five_letter_words.json') as json_file:
        return json.load(json_file)

def wordle_logic(reqBody):
    english_words = load_words()
    word_to_guess = random.choice(list(english_words))
    response = {}

    guess = reqBody['word']
    guess = str(guess).strip()
    if len(guess) != 5:
        return make_response(jsonify({'error': 'guess must be 5 letters long'}), 400)
    if guess not in english_words:
        return make_response(jsonify({'error': "sorry, that's not a word"}), 400)
    
    for letter in range(0, len(guess)):
        alphabet_numbered = 'alphabet_' + str(letter)
        if guess[letter] == word_to_guess[letter]:
            response[alphabet_numbered] = 2
        elif guess[letter] in word_to_guess:
            response[alphabet_numbered] = 1
        else:
            response[alphabet_numbered] = 0
    
    return make_response(response, 200)
     