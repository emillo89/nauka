import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#your choice
your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
#radomly choice computer
computer_choice = random.randint(0, 2)

choice_images = [rock, paper, scissors]

if your_choice >= 3 or your_choice < 0:
    print(f"You typed an invalid number, you lose!")
elif your_choice == 0 and computer_choice == 2:
    print(f"You win. Your choice is: {choice_images[your_choice]} and computer choice is: {choice_images[computer_choice]}")
elif computer_choice == 0 and your_choice == 2:
    print(f"You lose. Your choice is: {choice_images[your_choice]} and computer choice is: {choice_images[computer_choice]}")
elif your_choice == computer_choice:
    print(f"It's a draw. Yours choice is: {choice_images[your_choice]} and computer choice is: {choice_images[computer_choice]}")
elif computer_choice > your_choice:
    print(f"You lose. Your choice is: {choice_images[your_choice]} and computer choice is: {choice_images[computer_choice]}")
elif your_choice > computer_choice:
    print(f"You win. Your choice is: {choice_images[your_choice]} and computer choice is: {choice_images[computer_choice]}")

