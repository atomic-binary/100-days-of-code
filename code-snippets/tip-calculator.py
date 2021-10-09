
#!/usr/bin/env python3
print("Welcome to the tip calculator.\n")

total_bill = float(input("What was the total bill?\n$"))
# print(total_bill)
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
no_of_people = int(input("How many people to split the bill?\n"))
tip_calculated = total_bill * tip / 100
split_bill = (total_bill + tip_calculated) / no_of_people
# print(split_bill)

print(f"Each person should pay: ${round(split_bill, 2)}")
