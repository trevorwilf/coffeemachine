

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
    return(float(money_sum))

def get_drinktype(selection):
    if(selection == 1):
        type = "espresso"
    elif(selection == 2):
        type = "latte"
    else:
        type = "cappuccino"
    return(type)

def check_resources(resources, water, coffee, milk):
    ret_str = ""
    if ( resources["water"] < water):
        ret_str = "not enough water"
    if ( resources["water"] < coffee):
        ret_str = ret_str + ", not enough coffee"
    if (resources["water"] < milk):
        ret_str = ret_str + ", not enough milk"
    return(ret_str)

def update_resources(resources, water, coffee, milk):
    resources["water"] = resources["water"] - water
    resources["coffee"] = resources["coffee"] - coffee
    resources["milk"] = resources["milk"] - milk
    return(resources)