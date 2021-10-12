#!/usr/bin/env python3
import random

#Rock Paper Scissors game exercise.
#Rules:
#1. Rock wins against scissors.
#2. Scissors win against paper.
#3. Paper wins against rock.

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
gesture_list = [rock, paper, scissors]

print("Welcome to the Rock Paper Scissors Game!!")
user_selection = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

#Little bit better logic.
if user_selection >= 3 or user_selection < 0:
    print("You typed an invalid number. You lose!")
else:
    print(f"You chose: {user_selection}.\n{gesture_list[user_selection]}")

    computer_selection = random.randint(0, 2)
    print(f"Computer chose: {computer_selection}.")
    print(gesture_list[computer_selection])
    # print(type(user_selection))
    # print(type(computer_selection))
    if user_selection == 0 and computer_selection == 2:
        print("You Win!")
    elif computer_selection == 0 and user_selection == 2:
        print("You lose.")
    elif computer_selection > user_selection:
        print("You lose.")
    elif user_selection > computer_selection:
        print("You win!")
    elif computer_selection == user_selection:
        print("It's a draw.")


#Simple straight-forward logic.
# if user_selection == 0:
#     if computer_selection == 0:
#         print(f"You chose: \n{gesture_list[user_selection]}\n")
#         print(f"Computer chose: {gesture_list[computer_selection]}\nIt's a Draw.")
#     elif computer_selection == 1:
#         print(f"You chose: \n{gesture_list[user_selection]}")
#         print(f"Computer chose: {gesture_list[computer_selection]}\nComputer wins.")
#     else:
#         print(f"You chose: \n{gesture_list[user_selection]}")
#         print(f"Computer chose: {gesture_list[computer_selection]}\nYou win.")
# if user_selection == 1:
#     if computer_selection == 0:
#         print(f"You chose: \n{gesture_list[user_selection]}\n")
#         print(f"Computer chose: {gesture_list[computer_selection]}\nYou win.")
#     elif computer_selection == 1:
#         print(f"You chose: \n{gesture_list[user_selection]}")
#         print(f"Computer chose: {gesture_list[computer_selection]}\nIt's a Draw.")
#     else:
#         print(f"You chose: \n{gesture_list[user_selection]}")
#         print(f"Computer chose: {gesture_list[computer_selection]}\nComputer wins.")
# if user_selection == 2:
#     if computer_selection == 0:
#         print(f"You chose: \n{gesture_list[user_selection]}\n")
#         print(f"Computer chose: {gesture_list[computer_selection]}\nComputer wins.")
#     elif computer_selection == 1:
#         print(f"You chose: \n{gesture_list[user_selection]}")
#         print(f"Computer chose: {gesture_list[computer_selection]}\nYou win.")
#     else:
#         print(f"You chose: \n{gesture_list[user_selection]}")
#         print(f"Computer chose: {gesture_list[computer_selection]}\nIt's a Draw.")
