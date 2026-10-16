from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True
while is_on:
    option = menu.get_items()
    choice = input(f"What would you like? ({option})")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
# should_continue = True
#
# def coffee_maker():
#     menu = Menu()
#     coffee_maker = CoffeeMaker()
#     cus_order = input(f"What would you like? {menu.get_items()}")
#     if cus_order == "off":
#         global should_continue
#         should_continue = False
#     elif menu.find_drink(cus_order) is not None:
#         if coffee_maker.is_resource_sufficient(cus_order):
#             print("Pleasr enter coins.")
#
#
# while should_continue:
#     print("Welcome to the Coffee Maker!")
#     coffee_maker()
