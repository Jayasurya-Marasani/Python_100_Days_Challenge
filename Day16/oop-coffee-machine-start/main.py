from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cm = CoffeeMaker()
menu = Menu()
money = MoneyMachine()
while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        print(f"The Coffee Machine is Shutting Down.....")
        break
    elif choice == "report":
        cm.report()
        money.report()
    elif choice in menu.get_items():
        drink = menu.find_drink(choice)
        if cm.is_resource_sufficient(drink= drink):
            if money.make_payment(cost = drink.cost):
                cm.make_coffee(drink)
    else:
        print(f"Sorry your {choice} is not in the Menu. Try Again!!!")
