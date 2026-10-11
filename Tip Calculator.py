print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? Rs."))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
each_pay = tip / 100 * bill / people
print("Each person should pay a tip of" + str(round(each_pay , 2 )))
total_tip = each_pay * people
print("The total tip is " + str(round(total_tip , 2)))
each_total = each_pay + bill / people
print(f"Each person should pay a total of {each_total}")
