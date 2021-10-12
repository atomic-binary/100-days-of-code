#!/usr/bin/env python3

import random

# random_integer = random.randint(1, 20)
# print(random_integer)
# random_float = random.random()
# print(random_float)

#Heads/Tails exercise.
random_number = random.randint(0, 1)
if random_number == 1:
    print("Heads")
else:
    print("Tails")

#LISTS
#We can store mixed data types in a list as well.
fruits = ["Cherry", "Apple", "Grape"]

states_of_india = ["Maharashtra", "Karnataka", "Madhyapradesh", "Uttarakhand"]
print(states_of_india)
print(states_of_india[0])
print(states_of_india[-1])

states_of_india[2] = "Himachal Pradesh" #alter any existing item in the list and it will be replaced.
states_of_india.append("Kerala")    #append() will add items to the list at the end as the word suggests.
print(states_of_india)

states_of_india.extend(["Goa", "West Bengal", "Punjab"])
#another list can be added with extend(), this will be added to the end of the list.
print(states_of_india)


#Exrcise: Who's paying the bill.
#You are going to write a program which will select a random name from a list of names. 
# The person selected will have to pay for everybody's food bill.
# important: You are not allowed to use the choice() function.
all_names = input("Give me everybody's name, separated by a comma and a space.\n")
names = all_names.split(", ")
random_name = random.randint(0, len(names) - 1)
print(f"{names[random_name]} is going to buy the meal today!")

#same thing above but with the choice() function.
list_length = len(names) - 1
print(f"{random.choice(names)} is going to buy the meal tomorrow.")


#Index errors.
# print(states_of_india[8])  #most errors you will get are likely to be "off by one error" due to indexing.

#Nested Lists.
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# print(fruits)
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
# print(vegetables)
# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen)

#Treasure Map exercise.
#You are going to write a program which will mark a spot with an X.
#Your job is to write a program that allows you to mark a square on the map using a two-digit system.
# The first digit is the vertical column number and the second digit is the horizontal row number.
#First your program must take the user input and convert it to a usable format.
#Next, you need to use it to update your nested list with an "x".
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
column = int(position[0])
row = int(position[1])
# selected_row = map[row - 1]
# selected_row[column - 1] = "X"
#Another simplified way to do this in a single line.
map[row - 1][column - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")
