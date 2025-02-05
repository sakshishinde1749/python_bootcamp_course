# tip calculator

print("Welcome to the tip calculator!")

bill = float(input("What was the total bill?\n"))
tip = int(input("What percent of tip would you like to give? 10, 12 or 15\n"))
people = int(input("how many people to split the bill?\n"))

bill_per_person = ((tip/100) * bill + bill)/people
final_bill = round(bill_per_person, 2)

print(f"The final bill per person is: {final_bill}")