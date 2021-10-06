from menu import MenuItem, Menu
from maker import Maker
from money import Money

money = Money()
maker = Maker()
menu = Menu()


is_on = True

while is_on:
    options = menu.get_items()
    question = input(f"What would you like? ({options}): ")
    if question == 'off':
        is_on = False
    elif question == 'report':
        maker.report()
        money.report()
    else:
        drink = menu.find_drink(question)
        if maker.is_resource_sufficient(drink):
            if money.make_transaction(drink.cost):
                maker.make_coffee(drink)