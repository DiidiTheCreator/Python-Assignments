# TIP CALCULATOR!
# Tasks below:
# Total of bill, percentage of tip desired, and number of people splitting the bill desired!
# Utilizes inputs, conversions, f-strings, concatenations, and subscripting

print("Welcome to the TIP CALCULATOR!")

raw_bill_total = input("What is the total of your bill?\n$")
conv_bill_total = float(raw_bill_total)
raw_percentage = int(input("How much would you like to tip for the service?\n 10 12 15\n"))
decimal_percentage = float(raw_percentage/100)
raw_persons = input("How many people are splitting the bill?\n")
conv_persons = int(raw_persons)

semi_totals = ((conv_bill_total + (conv_bill_total*decimal_percentage)) / conv_persons)
totals = round(semi_totals, 2)

print(f"Since your bill was {conv_bill_total} dollars, the {conv_persons} of you must pay {totals}!")
