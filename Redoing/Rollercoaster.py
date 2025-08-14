print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You get to ride the rollercoaster! But first, answer the next question to calculate your ticket price.")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Children's ticket is $5.")
        wants = input("Do you want your photo taken? Yes or No? This would include an additional price. ")
        if wants == "Yes":
            bill +=3
            print(f"Your final bill is ${bill}")
        if wants == "No":
            bill +=0
            print(f"Alright. Your bill would be ${bill}. Have fun and come back next time! Bye!")
    elif age <= 18: 
        bill = 7
        print("Teenagers' tickets are $7.")
        wants = input("Do you want your photo taken? Yes or No? This would include an additional price. ")
        if wants == "Yes":
            bill +=3
            print(f"Your final bill is ${bill}")
        if wants == "No":
            bill +=0
            print(f"Alright. Your bill would be ${bill}. Have fun and come back next time! Bye!")
    elif age >= 45 and age<= 55:
        bill = 0
        want2 = input("Do you want your picture taken? ")
        if want2 == "Yes":
            print("Noted! The ride is on us, you don't have to pay anything! We love you! Have a lovely time on the rollercoaster! See you again soon!")
    else:
        bill = 12
        print("Adult tickets are $12.")
        wants = input("Do you want your photo taken? Yes or No? This would include an additional price. ")
        if wants == "Yes":
            bill +=3
            print(f"Your final bill is ${bill}")
        if wants == "No":
            bill +=0
            print(f"Alright. Your bill would be ${bill}. Have fun and come back next time! Bye!")
else:
    print("Sorry, you won't be able to get on. Come back later, okay? See you!")