import sys
from random import randrange


my_num = sys.argv[1]

if __name__ == '__main__':
    while True:
        rand_num = randrange(0, 2)
        if my_num == rand_num:
            print('Great!')
            break
        else:
            print(f'Try again it was {rand_num}')
        my_num = int(input('guess a number.'))

