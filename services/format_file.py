import json
from os import write

 
def load_words():
    with open('services/words.json') as json_file:
        return json.load(json_file)

if __name__ == '__main__':
    english_words = load_words()
    five_letter_words = {}
    for word in english_words:
        if len(word) == 5:
            five_letter_words[word] = 1
  
    json_object = json.dumps(five_letter_words)
    with open("services/five_letter_words.json", "w") as outfile:
        outfile.write(json_object)
