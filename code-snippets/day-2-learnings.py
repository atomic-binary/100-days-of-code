# Underscores can be used in integers as we use commas in larger numbers for easier readability.
# Ex. 1_22_342    this will be interpreted as 122342, and python will just remove the underscores.

# Write a program that adds the digits in a 2 digit number.
# e.g. if the input was 35, then the output should be 3 + 5 = 8.
two_digit_number = input("Type a two digit number: ")

#Write your code below this line 👇
print(type(two_digit_number))
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
addition = int(first_digit) + int(second_digit)
print(addition)

#Mathematical 
# order is PEMDAS [paranthesis, exponent, multiply/division, additin/substract] from left to right.
print(3 * 3 + 3 / 3 - 3)

#Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
#Write your code below this line 👇
bmi = int(weight) / (float(height) ** 2)
print(int(bmi))
#When we use type conversin on float number to int, it will just get rid of all decimal places.
#Alternatively, we can round them off like this 👇
print(round(bmi))
#And if we want to print few decimal places, then simply make these changes:
print(round(bmi, 2))
#There is another way to get the whole number with flow division which requires no type conversion.
print(8 // 3) # this can be verified by using type() method. print(type(8 // 3))
#Shorthand --> number += 2, etc.

#f-String
#Say if we want to print different data types in a single statement without any need of type conversion.
score = 2
height = 1.8
winning = True
print(f"Your score is {score}, your height is {height}, you are winning is {winning}")

#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left 
# if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# You have x days, y weeks, and z months left.
age = input("What is your current age?\n")
#Write your code below this line 👇
age_int = int(age)
years_left = 90 - age_int
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12

message = f"You have {days_left} days, {weeks_left} weeks, {months_left} months left if you live to the age of 90."
print(message)
