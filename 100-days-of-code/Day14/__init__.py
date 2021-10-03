import random
import clear

import art
from game_data import data



def generate_person():
    person = random.choice(data)
    return person

def search(compare, against):
    if (compare['name'] == against['name']) :
        print(compare['name'])
        print(against['name'])
        return True
    else:
        return False

def generate_second(compare):
    a = True
    while a:
        against = generate_person()

        answer = search(compare, against)
        if answer == False:
            a = False
        else:
            continue
    return against

def higher_lower(compare, against,guess,total_point):
    """Take the user guess and follower counts and returns if they got it right."""
    if compare['follower_count'] > against['follower_count'] and guess == 'a':
        return total_point + 1
    elif compare['follower_count'] < against['follower_count'] and guess == 'b':
        return total_point + 1
    else:
        return total_point - 100000000


def format_data(account):
    """Takes the account data and return the printabl e format"""
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_descr}. from {account_country}"



def game():
    compare = generate_person()

    total_point = 0
    while total_point >= 0:
        print(art.logo)
        print(f"Compare A: {format_data(compare)}")

        print(art.vs)
        against = generate_person()
        print(f"Against B: {format_data(against)}")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        total_point = higher_lower(compare, against, guess, total_point)

        if total_point > 0:
            compare = against
            print(f'Your score is: {total_point}')

        else:
            print(f'You loose. Your score is {total_point}')
            break


game()
