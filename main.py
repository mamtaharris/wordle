import json
import random

 
def load_words():
    with open('five_letter_words.json') as json_file:
        return json.load(json_file)

if __name__ == '__main__':
    english_words = load_words()
    word_to_guess = random.choice(list(english_words))
    count = 0 


    while (count<6):
        guess = input("Enter guess "+str(count+1)+": ")
        guess = guess.strip()
        if len(guess) != 5:
            print("Please enter a 5 letter word.\n")
            continue
        if guess not in english_words:
            print("Sorry, that's not a word.\n")
            continue
        
        count += 1

        if guess == word_to_guess:
                print("Congratulations, you guessed correctly!\n")
                break
        for letter in range(0, len(guess)):
            if guess[letter] == word_to_guess[letter]:
                print(guess[letter].capitalize(), ": * ")
            elif guess[letter] in word_to_guess:
                print(guess[letter].capitalize(), ": + ")
            else:
                print(guess[letter].capitalize(), ": - ")
        print("")
    
    print("The word was: " + word_to_guess)