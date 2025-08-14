print("Welcome to the rollercoaster!")
height = int(input("What is your age in cm? "))
if height == 120:
    print("Congrats! You can ride the rollercoaster!")
    age = input("Before I print your ticket, can you tell me what your age is? ")
    age = 18
    if age < 12:
        print("Your bill is $5.")
    elif age <=18:
        print("Your bill is $7.")
    else:
        print("Your bill is $12.")
else:
    print("Aww! You can't ride it right now. Come back later ans check again, okay?")