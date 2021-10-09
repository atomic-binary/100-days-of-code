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
