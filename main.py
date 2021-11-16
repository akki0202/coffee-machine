#first import the needed dictionary
import menu

# creating variables
loop=0
while loop == 0:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    amount = 0
    # report
    if order == 'report':
        print(f"water: {menu.resources['water']}")
        print(f"milk: {menu.resources['milk']}")
        print(f"coffee: {menu.resources['coffee']}")

    # checkin if we have enough
    else:
        # calculations
        quarter = int(input("How many quarters?: "))
        dime = int(input("How many dimes?: "))
        nickel = int(input("How many nickels?: "))
        penny = int(input("How many pennies?: "))
        amount = round((quarter * 0.25) + (dime * 0.10) + (nickel * 0.05) + (penny * 0.01), 2)

        # judging if there's enough cash
        if menu.resources["water"] < menu.MENU[order]['ingredients']["water"]:
            print("Sorry not enough Ingredients. Here's your refund.1")
        elif menu.resources["milk"] < menu.MENU[order]['ingredients']["milk"]:
            print("Sorry not enough Ingredients. Here's your refund.2")
        elif menu.resources["coffee"] < menu.MENU[order]['ingredients']["coffee"]:
            print("Sorry not enough Ingredients. Here's your refund.3")
        elif amount >= menu.MENU[order]['cost']:
            change = round(amount - (menu.MENU[order]['cost']), 2)
            print(f"$ {amount}")
            print(f"$ {menu.MENU[order]['cost']}")
            print(f"Here's your change. ${change}")
            print(f"Enjoy your {order}☕. Enjoy!")
            # altering resources
            for a in ('water', 'milk', 'coffee'):
                menu.resources[a] = menu.resources[a] - menu.MENU[order]['ingredients'][a]
        elif amount < menu.MENU[order]['cost']:
            print(f"Sorry that's not enough money. Money refunded. ${amount}")

