# guessing game using sys and random modules

from random import randint

import sys

answer = randint(int(sys.argv[1]), int(sys.argv[2]))

while True:
    try:
        guess = int(input(f'guess a number {sys.argv[1]}~{sys.argv[2]}: '))
        if 0 < guess < 11:
            if guess == answer:
                print('you are a genius')
                break
        else:
            print('hey, I said from 1~10')
    except ValueError:
        print('enter a number')
        continue

#python package index, pretty much any libraries you need can be foung here and installed

import pyjokes

joke = pyjokes.get_joke('en','neutral')
print(joke)