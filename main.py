import json
import random

 
def load_words():
    with open('five_letter_words.json') as json_file:
        return json.load(json_file)

if __name__ == '__main__':
    english_words = load_words()
    word_to_guess = random.choice(list(english_words))

    for i in range(6):
        guess = input("Enter guess "+str(i+1)+": ")
        
        if guess in english_words:
            print("Correct!")