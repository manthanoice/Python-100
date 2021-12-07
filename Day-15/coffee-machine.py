from the_menu import MENU, resources

the_money ={
    'quarters': 0.25,
    'dimes': 0.10,
    'nickles': 0.05,
    'pennies': 0.01
}

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print("Sorry there is not enough {}.".format(item))
            return False
    return True


def process_coins():
    print("Insert coins, please!")
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickles = int(input("How many nickles: "))
    pennies = int(input("How many pennies: "))
    the_total = quarters*the_money["quarters"] + dimes*the_money["dimes"] + nickles*the_money["nickles"] + pennies*the_money["pennies"]
    return the_total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print("Here is ${} in change.".format(change))
        profit = 0
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print("Here is your {} ☕️. Enjoy!".format(drink_name))


def coffee():
    is_on = True
    while is_on:
        choice = input("What would you like to have? (espresso/latte/cappuccino): ").lower()
        if choice == "off":
            is_on = False
        elif choice == "report":
            print("Water: {}ml".format(resources['water']))
            print("Milk: {}ml".format(resources['milk']))
            print("Coffee: {}g".format(resources['coffee']))
        else:
            drink = MENU[choice]
            if is_resource_sufficient(drink["ingredients"]):
                payment = process_coins()
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])

coffee()