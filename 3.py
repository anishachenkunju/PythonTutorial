import json

def translate(word):
    file = open('file/data.json')
    data = json.load(file)
    if word in data:
        return data[word]
    else:
        print('word does\'nt exist')


print(translate(input('enter word:')))