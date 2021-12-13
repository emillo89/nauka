import requests
from data_users import DataUsers

def your_data():
    print(f"""Welcome to Angela's Flight Club.\nWe find the best Flight deals and email you.""")
    first_name = input("What is your first name? ")
    print(f"{first_name}")
    last_name = input("What is your last name? ")
    print(f"{last_name}")
    email = input("What is your email? ")
    print(f"{email}")
    email_again = input("Type your email again")
    print(f"{email_again}")
    if email == email_again:
        data_users = DataUsers()
        data_users.update_users(first_name, last_name, email)
        print("You're in the club!")

    else:
        return False

your_data()

