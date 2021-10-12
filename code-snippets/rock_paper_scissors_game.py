#!/usr/bin/env python3
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

print("Welcome to the Rock Paper Scissors Game!!")
user_selection = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_selection = random.randint(0, 2)
# print(type(user_selection))
# print(type(computer_selection))
gesture_list = [rock, paper, scissors]

#The most basic and simple logic.
if user_selection == 0:
    if computer_selection == 0:
        print(f"You chose: \n{gesture_list[user_selection]}\n")
        print(f"Computer chose: {gesture_list[computer_selection]}\nIt's a Draw.")
    elif computer_selection == 1:
        print(f"You chose: \n{gesture_list[user_selection]}")
        print(f"Computer chose: {gesture_list[computer_selection]}\nComputer wins.")
    else:
        print(f"You chose: \n{gesture_list[user_selection]}")
        print(f"Computer chose: {gesture_list[computer_selection]}\nYou win.")


if user_selection == 1:
    if computer_selection == 0:
        print(f"You chose: \n{gesture_list[user_selection]}\n")
        print(f"Computer chose: {gesture_list[computer_selection]}\nYou win.")
    elif computer_selection == 1:
        print(f"You chose: \n{gesture_list[user_selection]}")
        print(f"Computer chose: {gesture_list[computer_selection]}\nIt's a Draw.")
    else:
        print(f"You chose: \n{gesture_list[user_selection]}")
        print(f"Computer chose: {gesture_list[computer_selection]}\nComputer wins.")


if user_selection == 2:
    if computer_selection == 0:
        print(f"You chose: \n{gesture_list[user_selection]}\n")
        print(f"Computer chose: {gesture_list[computer_selection]}\nComputer wins.")
    elif computer_selection == 1:
        print(f"You chose: \n{gesture_list[user_selection]}")
        print(f"Computer chose: {gesture_list[computer_selection]}\nYou win.")
    else:
        print(f"You chose: \n{gesture_list[user_selection]}")
        print(f"Computer chose: {gesture_list[computer_selection]}\nIt's a Draw.")
