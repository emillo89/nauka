from coffee import MENU, resources, profit


def report():
    """Returns f-string report"""
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    global profit
    return f"Water : {water} ml\nMilk : {milk} ml\nCoffee : {coffee} ml\nMoney : ${profit}"


def is_resource_sufficient(drink_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient. """
    for i in resources:
        if resources[i] >= drink_ingredients[i]:
            return True
        else:
            print(f"Sorry,there is not enough {i}")
            return False


def process_coins():
    """Return the total calulated from coins inserted. """
    print('Please insert coins')
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))

    result = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return result


def check_transaction(payment, drink_cost):
    """Return True when the payment is accepted, or False if money is inufficient. """
    if payment >= drink_cost:
        change = round(payment - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_coffee, drink_ingedients ):
    """Deduct the required ingredients from the resources"""
    for i in drink_ingedients:
        resources[i] -= drink_ingedients[i]
    print(f"Here is your {drink_coffee} ☕")


def coffee_machine():
    """Final definition to make a coffee"""
    while True:
        question = input("What would you like? (espresso/latte/cappucino):")
        if question == 'off':
            return False
        elif question == 'report':
            print(report())
        else:
            drink = MENU[question]
            if is_resource_sufficient(drink['ingredients']) == True:
                payment = process_coins()
                if check_transaction(payment, drink['cost']):
                    make_coffee(question,drink['ingredients'])


coffee_machine()


