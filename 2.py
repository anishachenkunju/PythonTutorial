import time, os
while True:
    if os.path.exists('file/vegetables.txt'):
        with open('file/vegetables.txt') as file:
            print(file.readlines())
            
    else:
        print('file does not exist')
    time.sleep(10)