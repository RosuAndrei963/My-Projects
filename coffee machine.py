import sys

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
    "money": 0,
}



def check_availability(user_order):
    """Checks the availability of each item in the recipe"""
    for key, value in MENU[user_order]["ingredients"].items():
        if value <= resources[key]:
            resources[key] -= value
            print(resources[key])
        else:
            print(f"Sorry, there is not enough {key}.")
            sys.exit()


repeat = True
while repeat:
    order = input("What would you like? (espresso, latte, cappuccino): ")
    if order == 'off':
        repeat = False
    elif order == "report":
        for key, value in resources.items():
            if key == "water" or key == "milk":
                print(f"{key.capitalize()}: {value}ml")
            elif key == "coffee":
                print(f"{key.capitalize()}: {value}g")
            elif key == "money":
                print(f"{key.capitalize()}: ${value:.2f}")
    else:
        check_availability(order)

        price = MENU[order]["cost"]
        print(f"That would be ${price}")
        print("Please insert the coins.")
        # given_amount = 0
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickels = int(input("how many nickels?: "))
        pennies = int(input("how many pennies?: "))
        given_amount = 0.25 * quarters + 0.1 * dimes + 0.05 * nickels + 0.01 * pennies
        if price <= given_amount:
            given_amount -=  price
            resources["money"] += price
            print(f"Here is ${given_amount:.2f} in change.")
            print(f"Here is your {order}: ☕️ Enjoy!")
        else:
            print("Sorry, you provided not enough money. Here is your refund: 💵")