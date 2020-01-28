#!/usr/bin/env python3
import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
colors = ['red','orange','yellow','green','blue','violet','purple']
play_again = ''
best_count = sys.maxsize            # the biggest number

while (play_again != 'n' and play_again != 'no'):
    match_color = random.choice(colors)
    count = 0
    color = ''
    while (color != match_color):
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip() #.lower() is a special code that lowers the cases.
        count += 1 #count is to counting numbers of tries has taken.
        if (color == match_color):
            print('Correct!')
        else:
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count))
    
    print('\nYou guessed it in {} tries!'.format(count)) #Gives appropriate feedback.

    if (count < best_count):
        print('This was your best guess so far!') #Hints for getting closer to the answer.
        best_count = count

    play_again = input("\nWould you like to play again (yes or no)? ").lower().strip() #the player can type the anwer in any cases and with or without whitespaces.

print('Thanks for playing!') #Ending.