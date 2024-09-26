
import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()

def main():
    print("Welcome to the Ham Sandwich Maker!")
    for size in recipes:
        print(f"{size.capitalize()} Sandwich: ${recipes[size]['cost']}")

    choice = input("Which size sandwich would you like (small, medium, large)?: ").lower()

    if choice in recipes:
        if sandwich_maker_instance.check_resources(recipes[choice]['ingredients']):

            cost = recipes[choice]['cost']
            payment = cashier_instance.process_coins()

            if cashier_instance.transaction_result(payment, cost):

                sandwich_maker_instance.make_sandwich(choice, recipes[choice]['ingredients'])
        else:
            print("Sorry, we can't make that sandwich.")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()

