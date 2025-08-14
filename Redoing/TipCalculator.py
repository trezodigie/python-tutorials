print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
percentage = input("What percentage tip would you like to give? 10, 20 or 25? ")
people = input("How many people will split the bill? ")
b = float(bill)
p = float(percentage)
peo = float(people)
first_result = b * ((p/100) + 1)
second_result = first_result / peo
round = round(second_result,2)
message = f"Each person should pay: ${round}"
print(message)