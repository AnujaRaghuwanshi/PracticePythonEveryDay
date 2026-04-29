# Coffee Machine

import art
import time

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

COIN_VALUES = {
    "quarter": 0.25,
    "dime": 0.1,
    "nickel": 0.05,
    "penny": 0.01,
}
RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "coins": 0,
}
money_in_machine = 0

print(art.logo)
print("Welcome to Python Coffee Maker!")

def coffee_Machine():
    report_option = input("Do you want a report? (y/n): ").lower()
    if report_option == "y":
        generate_report()
    type_of_coffee = input("What do you want to drink? espresso/latte/cappuccino: ").lower()
    print(f"The {type_of_coffee} costs ${MENU[type_of_coffee]['cost']}.")
    if check_resources(type_of_coffee):
        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))
        if calculate_price(quarters, dimes, nickels, pennies, type_of_coffee):

            print("Making your coffee", end="")
            for i in range(5):
                print(".🔄☕", end="", flush=True)
                time.sleep(1)

            print(f"\nEnjoy your {type_of_coffee} ☕!")

    more_coffee = input("Would you like to order another coffee? (y/n): ")
    if more_coffee == "y":
        return True
    else:
        return False



def check_resources(type_of_coffee):
    for ingredient in MENU[type_of_coffee]["ingredients"]:
        if RESOURCES[ingredient] < MENU[type_of_coffee]["ingredients"][ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
        RESOURCES[ingredient] -= MENU[type_of_coffee]["ingredients"][ingredient]

    return True

def calculate_price(quarters, dimes, nickels, pennies, type_of_coffee):
    global money_in_machine
    cash_received_from_customer = COIN_VALUES["quarter"] * quarters +COIN_VALUES["dime"] * dimes +COIN_VALUES["nickel"] * nickels +COIN_VALUES["penny"] * pennies

    if cash_received_from_customer >= MENU[type_of_coffee]["cost"]:
        change = round(cash_received_from_customer - MENU[type_of_coffee]["cost"], 2)
        money_in_machine += MENU[type_of_coffee]["cost"]
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money 💰. Money refunded.")
        return False

def generate_report():
    print(f"Money in the machine: ${money_in_machine}")
    print(f"Resources remaining: {RESOURCES}")

more_coffee = True
while more_coffee:
    more_coffee = coffee_Machine()