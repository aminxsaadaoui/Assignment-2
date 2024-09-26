# cashier.py

class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))
        total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
        return total

    def transaction_result(self, coins, cost):
        if coins >= cost:
            change = round(coins - cost, 2)
            print(f"Transaction successful! Here is your ${change} in change.")
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False
