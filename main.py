MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk" : 0,
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

have_water = resources["water"]
have_milk = resources["milk"]
have_coffee = resources["coffee"]

ask = True
all_money = 0


def make_drink(order):
    global have_water
    global have_milk
    global have_coffee
    use_water = MENU[order]["ingredients"]["water"]
    use_milk = MENU[order]["ingredients"]["milk"]
    use_coffee = MENU[order]["ingredients"]["coffee"]

    if have_water >= use_water:
        if have_milk >= use_milk:
            if have_coffee >= use_coffee:
                ask_money(order, use_water, use_milk, use_coffee)
            else:
                print("Sorry there is not enough coffee.")
        else:
            print("Sorry there is not enough milk.")
    else:
        print("Sorry there is not enough water.")


def ask_money(order, use_water, use_milk, use_coffee):
    global have_water
    global have_milk
    global have_coffee
    global all_money
    cost = MENU[order]["cost"]

    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    user_money = ((quarters*25) + (dimes*10) + (nickles*5) + (pennies*1)) / 100
    if user_money - cost >= 0 :
        print(f"Here is ${user_money - cost} in change.")
        print(f"Here is your {order} ☕️. Enjoy!")
        have_water -= use_water
        have_milk -= use_milk
        have_coffee -= use_coffee
        all_money += cost
    else :
        print("Sorry that's not enough money. Money refunded.")

    ask_user()

def ask_user():
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "report":
        print(f"Water: {have_water} ml")
        print(f"Milk: {have_milk} ml")
        print(f"Coffee: {have_coffee} g")
        print(f"Money: ${all_money}")
        ask_user()
    elif order == "off":
        print("The machine is turned off.")
    elif order == "espresso" or order == "latte" or order == "cappuccino":
        make_drink(order)

ask_user()






