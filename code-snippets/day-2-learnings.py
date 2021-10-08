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
bmi = float(weight) / (float(height) ** 2)
print(int(bmi))
