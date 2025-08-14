print("Welcome to the leap year calculator!")
year = int(input("What year do you want to check for? "))
new = year % 4 
newhundred = year % 100
newfour = year % 400
if new != 0:
    print("This is not a leap year.")
else:
    if newhundred != 0:
        print("This is a leap year.")
    else:
        if newfour != 0:
            print("This is not a leap year.")
        else:
            print("This is a leap year.")

