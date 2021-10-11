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
