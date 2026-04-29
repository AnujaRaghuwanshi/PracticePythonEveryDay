# OOP Coffee Machine
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import art
print (art.logo)
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


is_on= True
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")

    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink is None:
            print(f"We are sorry, {choice} is not available.")
            continue
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
