
import random
import hangman_words
import hangman_art
#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(hangman_words.word_list).lower()
print(chosen_word)

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


#lives
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it
print(hangman_art.logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for letter in chosen_word:
    display += '-'

won = False
while won == False:
    guess = input("Guess a letter: ").lower()

    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")
    #check guessed letter
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess
            if '-' in display:
                continue
            else:

                print(f'You win, the chosen_word is: {chosen_word}')
                won = True

    if guess not in chosen_word:
        # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's you lost a lives")
        lives -= 1
        print(f'You have {lives} lives')
        if lives == 0:
            print(f'You lose: {lives} lives')
            won = True

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(hangman_art.stages[lives])