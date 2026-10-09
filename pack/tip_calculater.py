print("Welcome to tip calculater")
bill= (float(input("What was total bill ? $")))
tip = (int(input("What percentage would you like to give ? 10 12 15 ")))
people =(int(input("Split bill into how many people ")))
tip_as_pwercentage= tip/100
total_bill= bill + tip
bill_per_person = total_bill/people
final_bill= round(bill_per_person,2)
print(f"Each person bill is ${ final_bill} ")