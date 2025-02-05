from main import MENU, resources, cup_logo

print(cup_logo)

def prepare_coffee(order, menu, resources):

    required_ingredients = menu[order]["ingredients"]

    for ingredient, amount in required_ingredients.items():
        if resources[ingredient] < amount:
            print(f"Sorry, there isn't enough {ingredient}.")
            return False
        
    print("Please insert coins.")
    quarters = int(input("\nHow many quarters?: "))
    dimes = int(input("\nHow many dimes?: "))
    nickles = int(input("\nHow many nickles?: "))
    pennies = int(input("\nHow many pennies?: "))

    user_cost = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    coffee_cost = menu[order]["cost"]
    if user_cost == coffee_cost:
        print(f"Here is your {order} ☕, Enjoy!")
    elif user_cost > coffee_cost:
        print(f"Here is ${round(user_cost - coffee_cost, 2)} in change.")
        print(f"Here is your {order} ☕, Enjoy!")
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    
    for ingredient, amount in required_ingredients.items():
        resources[ingredient] -= amount
    
    return True

while True:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if not order:  # Check for empty input
        print("Please enter a valid option.")
        continue

    if order == 'off':
        print("Turning off the coffee machine. Goodbye!")
        break
    
    elif order == 'report':
        print(f"Resources: {resources}")
    
    elif order in MENU:
        success = prepare_coffee(order, MENU, resources)
        if not success:
            print("Unable to prepare your coffee. Please try a different option.")
    
    else:
        print("Invalid choice. Please try again.")


