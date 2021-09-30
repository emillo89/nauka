import random

from art import logo

easy_level_turns = 10
hard_level_turns = 5

def set_difficulty():
    answer = input("""Choose a difficulty. type 'easy' or 'hard' : """)
    if answer == 'easy':
        return easy_level_turns
    else:
        return hard_level_turns

def check_answer(quess,answer,attempts):
    if quess > answer:
        print(print('Too high.'))
        return attempts - 1
    elif quess < answer:
        print(print('Too low.'))
        return attempts - 1
    else:
        print(f"You got it. The number is {answer}")


def game():
    print(logo)

    print("""Welcome to the Number Guessing Game!\n
        I'm thinking of a number between 1 and 100\n""")

    attempts = set_difficulty()

    answer = random.randint(1, 100)
    quess = 0
    while quess != answer:
        print(f"You have {attempts} attempts remaining to guess the number.")
        quess = int(input("Make a guess: "))

        attempts = check_answer(quess,answer,attempts)

        if attempts == 0:
            print("You've run out of guesses, You lose")
        elif quess != answer:
            print("Guess again")



game()



# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
