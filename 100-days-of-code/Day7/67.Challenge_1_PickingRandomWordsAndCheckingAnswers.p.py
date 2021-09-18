"""#Step 1
word_list = ["aardvark", "baboon", "camel"]
1. TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
2. TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
3. TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
"""
#ad1
import random

word_list = ["aardvark", "baboon", "camel"]

choosen_word = random.choice(word_list).lower()
print(choosen_word)


#ad2

guess = input("Guess a letter: ").lower()

#ad3
for letter in choosen_word:
    if letter == guess:
        print('Right')
    else:
        print('Wrong')
