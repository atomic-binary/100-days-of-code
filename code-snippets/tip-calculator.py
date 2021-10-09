#!/usr/bin/env python3
print("Welcome to the tip calculator.\n")

total_bill = float(input("What was the total bill?\n$"))
# print(total_bill)
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
no_of_people = int(input("How many people to split the bill?\n"))

tip_calculated = total_bill * tip / 100
split_bill = (total_bill + tip_calculated) / no_of_people
#Another way to replace above 2 lines.
# split_bill = (total_bill * (1 + tip / 100)) / no_of_people

# final_bill = round(split_bill, 2)
#If we use round(), for some calculations, where the result itself is say 33.6 then it will display
# 33.6 even though we have used round() to display 2 decimal places.
#To print 2 decimal places even if the result was 33.6, we have to use format() like below.
final_bill = "{:.2f}".format(split_bill)

print(f"Each person should pay: ${final_bill}")
