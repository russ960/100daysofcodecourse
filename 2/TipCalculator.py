print("Welcome to the tip calculator.")
bill_amount = float(input("What is the total bill?"))
tip_precentage = float(input("What tip would you like to give? 12, 15, 20 precent?"))/100 + 1
party_count = int(input("How many people in your party?"))
total_per_person = round((bill_amount * tip_precentage) / party_count, 3)
print("Each person in the party should pay: {:.2f}".format(total_per_person))