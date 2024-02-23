from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
'''Coffee Machine code using OOP concept rather than crude method of coding '''
choice = Menu()
report = CoffeeMaker()
money = MoneyMachine()
is_on = True
while is_on:
    input_1 = input(f"Which item you wanna order?{choice.get_items()}:").lower()
    if input_1 == "report":
        report.report()
        money.report()
    elif choice == 'off':
        is_on = False
    else:
        order = choice.find_drink(input_1)
        if order is not None:
            if report.is_resource_sufficient(order):
                if money.make_payment(order.cost):
                    report.make_coffee(order)
                else:
                    break
            else:
                break
        else:
            break
