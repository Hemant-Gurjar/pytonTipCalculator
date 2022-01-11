#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Code....!         ⇩

print("Welcome to the tip calculator.")

total_bill = int(input("What was the total bill? $"))

tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

no_of_people = int(input("How many people to split the bill? "))

final_tip = (tip / 100) + 1

bill_split = (total_bill / (no_of_people) * final_tip)

final_bill_split = round(bill_split, 2)

print(f"Each person should pay: {final_bill_split}")
