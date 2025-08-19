MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0

def question():
    global profit
    is_on = True
    #or can use (before the coffee_type), "while True" and indent every other thing under it. Helps eliminate the constant use of the question function
    #after each block of code.
    while is_on:
        coffee_type = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if coffee_type == "off":
            is_on = False
            break
        elif coffee_type in MENU and (resources["water"] < MENU[coffee_type]["ingredients"]["water"] or resources["milk"] < MENU[coffee_type]["ingredients"]["milk"] or resources["coffee"] < MENU[coffee_type]["ingredients"]["coffee"]):
            print(f"Not enough resources for {coffee_type}! Try again later or ask an operator to fill me up!")
        else:
            if coffee_type in MENU:  # only valid coffee types
                profit += MENU[coffee_type]["cost"]
                print("please insert coins.")
                quarters = float(input("How many quarters do you have? "))
                pennies = float(input("How many pennies do you have? "))
                nickels = float(input("How many nickels do you have? "))
                dimes = float(input("How many dimes do you have? "))
                quarter_total = quarters * 0.25
                nickel_total = nickels * 0.05
                dime_total = dimes * 0.1
                pennies_total = pennies * 0.01
                given_money = [quarter_total, nickel_total, dime_total, pennies_total]
                total_given_money = sum(given_money)

            #print(total_given_money)
                if total_given_money < MENU[coffee_type]["cost"]:
                    print("Sorry, your money is not complete. Money refunded. Try again with the correct amount. Thank you!")
                    question()
                elif total_given_money == MENU[coffee_type]["cost"]:
                    print(f"Here's your {coffee_type} ☕! Enjoy!")

                elif total_given_money > MENU[coffee_type]["cost"]:
                    change = round(total_given_money - MENU[coffee_type]["cost"],2)
                    #print(change)
                    print(f"Here is ${change} in change!")
                    print(f"Enjoy your {coffee_type} ☕!")
                    #print(profit)
                    resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
                    resources["milk"] -= MENU[coffee_type]["ingredients"]["milk"]
                    resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]

            if coffee_type == "report":
                print(f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${profit}')

            if coffee_type not in MENU and (coffee_type != "report"):
                print("Oh, sorry. We do not have what you selected.\nKindly choice between our options (espresso, latte and cappuccino) to get something that refreshes your day!")

question()
