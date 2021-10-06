class Maker():
    def __init__(self):
        self.resources = {
            'water' : 300,
            'milk' : 200,
            'coffee' : 100
        }

    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self,drink):
        """Returns True when order can be made, False if ingredients are insufficient. """
        for i in self.resources:
            if self.resources[i] >= drink.ingredients[i]:
                return True
            else:
                print(f"Sorry,there is not enough {i}")
                return False

    def make_coffee(self, drink):
        """Deduct the required ingredients from the resources"""
        for i in drink.ingredients:
            self.resources[i] -= drink.ingredients[i]
        print(f"Here is your {drink.name} ☕")

