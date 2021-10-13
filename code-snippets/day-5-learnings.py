#!/usr/bin/env python3

#For Loop
# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#   print(fruit)
#   print(f"I love {fruit} juice.")
# print(fruits) 

#Average Height exercise
# You are going to write a program that calculates the average student height from a List of heights.
# e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
# The average height can be calculated by adding all the heights together and dividing by the total number of heights.
#The challenge here is to not use len() and sum().
student_heights = input("Input a list of student heights ").split()   #takes input and creates a list with type strings by default as usual.
no_of_students = 0
sum = 0

# It's a good idea to use singular variable names in for loop in relation to the list.
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])    
  #this line of code takes each element and converts each element into integer.
  no_of_students += 1
  sum = sum + student_heights[n]
average_height = sum / no_of_students
print(round(average_height))

#using sum() and len() function.
# total_height = sum(student_heights)
# number_of_students = len(student_heights)
# average_height = round(total_height / number_of_students)
# print(average_height)


