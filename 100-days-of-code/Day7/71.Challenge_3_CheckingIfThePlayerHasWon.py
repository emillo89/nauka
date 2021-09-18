
import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list).lower()
print(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for letter in chosen_word:
    display += '-'

#TODO-1: - Use a while loop to let the user guess again.
# The loop should only stop once the user has guessed all the letters in the chosen_word
# and 'display' has no more blanks ("_"). Then you can tell the user they've won.

won = False
while won == False:
    guess = input("Guess a letter: ").lower()

    #check guessed letter
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess
            if '-' in display:
                continue
            else:

                print(f'You win, the chosen_word is: {chosen_word}')
                won = True
    print(display)

