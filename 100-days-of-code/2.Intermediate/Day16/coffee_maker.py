class CoffeeMaker():
    """Models the amchine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Returns f-string report"""
        water = self.resources["water"]
        milk = self.resources["milk"]
        coffee = self.resources["coffee"]
        return f"Water : {water} ml\nMilk : {milk} ml\nCoffee : {coffee} ml"

    def is_resource_sufficient(self,drink_ingredients):
        """Returns True when order can be made, False if ingredients are insufficient. """
        for i in self.resources:
            if self.resources[i] >= drink_ingredients[i]:
                return True
            else:
                print(f"Sorry,there is not enough {i}")
                return False

    def make_coffee(self,drink_coffee, drink_ingedients):
        """Deduct the required ingredients from the resources"""
        for i in drink_ingedients:
            self.resources[i] -= drink_ingedients[i]
        print(f"Here is your {drink_coffee} ☕")