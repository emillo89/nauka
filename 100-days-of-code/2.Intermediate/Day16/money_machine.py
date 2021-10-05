class MoneyMachine():

    CUREENCY = "$"

    COIN_VALUES = {
        "quarters" : 0.25,
        "dimes" : 0.10,
        "nickles" : 0.05,
        "pennies" : 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Print the current profit"""
        print(f"Money: {self.CUREENCY}{self.profit}")

    def process_coins(self):
        """Return the total calulated from coins inserted. """
        print('Please insert coins')
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}? ")) * self.COIN_VALUES[coin]
        return self.money_received

    def check_transaction(self,payment, drink_cost):
        """Return True when the payment is accepted, or False if money is inufficient. """
        if payment >= drink_cost:
            change = round(payment - drink_cost, 2)
            print(f"Here is ${change} in change.")
            self.profit += drink_cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False