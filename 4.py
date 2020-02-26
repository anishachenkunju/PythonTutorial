import json
from difflib import get_close_matches
file = open('file/data.json')
data = json.load(file)


def translate(word):
    w = word.lower()
    if w in data:
        return data[w]
    elif get_close_matches(w,data)[0]:
        yn = input('Did you mean {}: '.format(get_close_matches(w,data)[0]))
        if yn == 'Y':
            return data[get_close_matches(w,data)[0]]
        else:
            print('word does not exist')
            
    else:
        print('word does not exist')

word  = input('enter a word:')
output = translate(word)
for item in output:
    print(item)

