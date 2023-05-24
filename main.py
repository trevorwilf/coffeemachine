# this is meant to mimick a basic coin operated coffee machine

import Functions as func


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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO 1. Print report of all coffee resources
# TODO 2. Check resources of all coffee machines resources
#func.print_report(resources)
#func.print_coffee_menu(MENU)

want_coffee = True

while want_coffee:
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0

    first_menu_selection = int(input(print("Menu - 1) Print resource report - 2) Print coffee Menu - 3) exit")))

    if (first_menu_selection == 1):
        func.print_report(resources)
    elif (first_menu_selection == 2):
        func.print_coffee_menu(MENU)

        order = int(input("What would you like? (1 - espresso, 2 - latte, 3 - cappuccino, 4 - exit"))

        quarters = int(input("How many quarters: "))
        dimes = int(input("Hom many dimes: "))
        nickels = int(input("How many nickels: "))
        pennies = int(input("How many pennies? "))

        total inserted = fun.total_input_money(quarters, dimes, nickels, pennies)

        if

    elif (first_menu_selection == 3):
        want_coffee = False


