from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

d = Menu()
machine = CoffeeMaker()
money = MoneyMachine()

is_on = True
while is_on:
    options = input("What would you like? (espresso/latte/cappuccino/): ").lower()

    if options == "off":
        is_on = False
        break

    elif options == "latte":
        options = d.menu[0]
    elif options == "espresso":
        options = d.menu[1]
    elif options == "cappuccino":
        options = d.menu[2]
    elif options == "report":
        machine.report()
        money.report()
        continue

    elif options != "report" or options != "off":
        d.find_drink(options)
        continue

    if machine.is_resource_sufficient(options) and money.make_payment(options.cost):
        machine.make_coffee(options)
    else:
        continue