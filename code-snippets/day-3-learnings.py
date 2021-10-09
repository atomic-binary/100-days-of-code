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

