# Day 02
# Date: 16 Nov 2021
# Tip Calculator 


'''
Tip Calculator
Instructions
If the bill was $150.00, split between 5 people, with 12% tip.

Each person should pay (150.00 / 5) * 1.12 = 33.6

Format the result to 2 decimal places = 33.60

Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.

Example Input:
Welcome to the tip calculator!
What was the total bill? $124.56
How much tip would you like to give? 10, 12, or 15? 12
How many people to split the bill? 

Example Output:
Each person should pay: $19.93
'''

print("Welcome to the TIP CALCULATOR")
total_bill = float(input("Enter the total bill:"))
tip = int(input("How much tip would ypu like to give? 10, 12, or 15?"))
spilt = int(input("How many people to spilt the bill?"))

final = round((total_bill/spilt)*((100+tip)/100),2)
print(f"Each person should pay: ${final}")
