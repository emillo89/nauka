class Money():
    CUREENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_receive = 0

    def report(self):
        """Print the current profit"""
        print(f"Money: {self.CUREENCY}{self.profit}")

    def process_coins(self):
        """Return the total calulated from coins inserted. """
        print("Please insert coin")
        for coin in self.COIN_VALUES:
            self.money_receive += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]

        return self.money_receive

    def make_transaction(self, drink_cost):
        """Return True when the payment is accepted, or False if money is inufficient. """
        self.process_coins()
        if self.money_receive >= drink_cost:
            change = round(self.money_receive - drink_cost, 2)
            print(f"Here is ${change} in change.")
            self.profit += drink_cost
            self.money_receive = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_receive = 0
            return False

