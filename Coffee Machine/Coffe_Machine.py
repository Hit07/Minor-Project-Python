from Coffe_Maachine_menu import MENU, resources


def cost_of_coffee():
    print("Please insert coins.")
    total = float(input("How many quaters?")) * 0.25
    total += float(input("how many dimes?")) * 0.10
    total += float(input("How many nickels?")) * .05
    total += float(input("How many pennies?")) * 0.01
    return total


def resources_required(drink):
    for item in drink:
        if drink[item] > resources[item]:
            print(f"Sorry there is not enough {item}😓")
            return False
    return True


def make_coffe(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️!!")


def transaction_successful(coin_inserted, cost):
    if coin_inserted > cost:
        change = round(coin_inserted - cost, 2)
        print(f"Here is your change:{change}$")
        global profit
        profit += cost
        return True
    else:
        print("Sorry that's not enough money,Money Refunded!😅")
        return False


profit = 0
while True:
    your_choice = input("What would you like?(espresso/latte/cappuccino):")
    if your_choice == "report":
        print(f"Water:{resources['water']}ml")
        print(f"Milk:{resources['milk']}ml")
        print(f"Coffee:{resources['coffee']}g")
        print(f"Money:{profit}$")
    elif your_choice == "restart":
        print("Have a nice day!\nEnjoy your coffee!!")
        break
    else:
        drink = MENU[your_choice]
        print(drink)
        if resources_required(drink["ingredients"]):
            payment = cost_of_coffee()
            if transaction_successful(coin_inserted=payment, cost=drink["cost"]):
                make_coffe(your_choice, drink["ingredients"])
