import random
from replit import clear

import art
from game_data import data



def generate_person():
    """Generate first person"""
    person = random.choice(data)
    return person

def search(compare, against):
    """Search if compare and against name is the same"""
    if (compare['name'] == against['name']) :
        return True
    else:
        return False

def generate_second(compare):
    """Generate second person"""
    a = True
    while a:
        against = generate_person()

        answer = search(compare, against)
        if answer == False:
            a = False
        else:
            continue
    return against



def higher_lower(compare, against,guess):
    """Take the user guess and follower counts and returns if they got it right."""
    if compare['follower_count'] > against['follower_count']:
        return guess == 'a'
    else:
        return guess == 'b'

def format_data(account):
    """Takes the account data and return the printabl e format"""
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_descr}. from {account_country}"



def game():
    """Play in higher or lover game"""
    compare = generate_person()

    total_point = 0
    while True:

        print(art.logo)
        print(f"Compare A: {format_data(compare)}")

        print(art.vs)
        against = generate_person()
        print(f"Against B: {format_data(against)}")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        correct = higher_lower(compare, against, guess)

        if correct:
            total_point += 1
            compare = against
            print(f'Your score is: {total_point}')
            clear()


        else:
            print(f"Sorry, that's wrong. Final score is {total_point}")
            break


game()
