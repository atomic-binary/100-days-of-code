#!/usr/bin/env python3

# if condition:
#     do this
# else:
#     do this

#draw.io is a great website draw flowchart diagrams.

#Rollercoaster ride exercise:
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))
if height >= 120:
    print("You can ride the Rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")

#Comparison operators: <, >, <=, >=, ==, !=

#Odd or Even exercise:
# Write a program that works out whether if a given number is an odd or even number.
number = int(input("Which number do you want to check?\n"))
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

#Nested if/elif/else Rollercoaster exercise.
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))
if height >= 120:
    print("You can ride the Rollercoaster!")
    age = int(input("What is your age?\n"))
    if age < 12:
        print("Please pay $5.")
    elif age < 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")

#BMI calculator 2.0 exercise.
# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
# It should tell them the interpretation of their BMI based on the BMI value.
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.
bmi_height = float(input("Enter your height in meter: "))
bmi_weight = float(input("Enter your weight in kg: "))

bmi = round(bmi_weight / bmi_height ** 2, 2)
# print(bmi)
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are slightly underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")

#Leap year exercise.
#Write a program that works out whether if a given year is a leap year. 
# A normal year has 365 days, leap years have 366, with an extra day in February.
# This is how you work out whether if a particular year is a leap year.
# on every year that is evenly divisible by 4.
#   **except** every year that is evenly divisible by 100.
#       **unless** the year is also evenly divisible by 400.
year = int(input("Which year do you want to check?\n"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# if/elif/else                  Multiple if
# if condition:                 if condition:
#     do A                          do A
# elif condition:               if condition:
#     do B                          do B
# else:                         if condition:
#     do C                          do C

# In above lines, on the left only one condition will be carried out. While on the right side,
# all the conditins are checked regardless of the other and if True, all will be carried out.

# Multiple if conditions Rollercoaster exercises.
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))
bill = 0
if height >= 120:
    print("You can ride the Rollercoaster!")
    age = int(input("What is your age?\n"))
    if age < 12:
        bill = 5
        print("Children tickets are $5.")
    elif age < 18:
        bill = 7
        print("Teen tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")
    want_picture = input("Do you want to take a picture? y or n.\n")
    if want_picture == "y":
        bill += 3
    print(f"Your final bill is {bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")


#Pizza exercise with multiple if conditions.
# Congratulations, you've got a job at Python Pizza. 
# Your first job is to build an automatic pizza order program.
# Based on a user's order, work out their final bill.
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")
bill = 0

if size == "S":
    bill += 15
    print(f"Small Pizza is ${bill}")
elif size == "M":
    bill += 20
    print(f"Medium Pizza is ${bill}")
else:
    bill += 25
    print(f"Large Pizza is ${bill}")
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is ${bill}")
# else:
#     print("Please provide correct input. S, M or L.")
# For simplicity for now, not using else here. commented above 2 lines.

#LOGICAL OPERATORS
#Multiple conditions in a single if statement with Logical Operators.
# AND, OR, NOT
#Multiple conditions Rollercoaster exercises.
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))
bill = 0
if height >= 120:
    print("You can ride the Rollercoaster!")
    age = int(input("What is your age?\n"))
    if age < 12:
        bill = 5
        print("Children tickets are $5.")
    elif age < 18:
        bill = 7
        print("Teen tickets are $7.")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Everything is going to be ok. Have a free ride on us.!")
    else:
        bill = 12
        print("Adult tickets are $12.")
    want_picture = input("Do you want to take a picture too for $3? y or n.\n")
    if want_picture == "y":
        bill += 3
    print(f"Your final bill is ${bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")

#Love Calculator exercise.
# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs. 
# Then combine these numbers to make a 2 digit number.
# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
# "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:
# "Your score is **z**."

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_names = name1.lower() + name2.lower()

true_count = combined_names.count("t") + combined_names.count("r") + combined_names.count("u") + combined_names.count("e")
# print(true_love_count1)
love_count = combined_names.count("l") + combined_names.count("o") + combined_names.count("v") + combined_names.count("e")
# print(true_love_count2)
score = int(str(true_count) + str(love_count))
# print(score)
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
