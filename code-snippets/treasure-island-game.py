#!/usr/bin/env python3

print("Welcome to the Treasure Island.")
print("Your mission is to find the lost treasure.") 

user_input = input("You are at the crossroads, please choose if you want to go left or right.\n").lower()
if user_input == "left":
    print("You have reached bank of the river.")
    swim_boat = input("Would you like to swim to cross across the river or wait for a boat? Enter swim or wait.\n").lower()
    if swim_boat == "wait":
        print("You just saved yourself from crocodiles in the river by choosing to wait for the boat.")
        print("You have now crossed the river and there are three doors. Red, Blue and Yellow.")
        door = input("Please choose any one of the door.\n").lower()
        if door == "yellow":
            print("Congratulations!!! You have found the treasure no one else could. You are filthy rich now.")
        elif door == "blue":
            print("You entered the wrong door. \nThere was a hungry lion waiting for you across this door. You died. Game Over!")
        elif door == "red":
            print("You entered the wrong door. \nIt's an empty room with no windows and the only door that you came through is locked now. Have a fun stay. Game Over!")
        else:
            print("You could only choose between those 3 doors. \nYou chose something else. You were shot dead by a pirate before you could enter the door. Game Over!")
    elif swim_boat == "swim":
        print("Before you could even reach half the distance, crocodiles in the river started attacking you. You died. Game Over!")
    else:
        print("You could only choose Swim or Wait. \nYou chose something else, someone killed you before you could make a decision and took your map. \nGame Over!")
elif user_input == "right":
    print("You were looking at treasure map while walking and fell into a hole. \nGame Over!")
else:
    print("You could only choose Left or Right. \nYou chose something else, while you were waiting someone killed you and took your treasure map. Game Over!")
