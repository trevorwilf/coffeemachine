

# print resource report
def print_report(resources):
    for key in resources:
        print(f'{key} remaining: {resources[key]}')
    #print(f'Water remaining: {resources["water"]}')
    #print(f'Milk remaining: {resources["milk"]}')
    #print(f'Coffee remaining: {resources["coffee"]}')

def print_coffee_menu(MENU):
    for key in MENU:
        print(f'{key}: ${MENU[key]["cost"]}')
    print("")

def total_input_money(quarters, dimes, nickels, pennies):
    money_sum = quarters * .25 + dimes * .1 + nickels * .05 + pennies * .01
    return(money_sum)

def enough_money(total_money, price):
