from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_cash_drawer = MoneyMachine()

machine_on = True
while machine_on:
    my_drink_order = (input(f"​What would you like? ({my_menu.get_items()}): ")).lower()
    if my_drink_order == 'report':
        # TODO: Report
        my_coffee_maker.report()
        my_cash_drawer.report()
    elif my_drink_order == 'off':
        machine_on = False
    else: 
        my_menu_item = my_menu.find_drink(my_drink_order)

        if my_coffee_maker.is_resource_sufficient(my_menu_item):
            if my_cash_drawer.make_payment(my_menu_item.cost):
                my_coffee_maker.make_coffee(my_menu_item)
            else:
                print("Sorry that's not enough money. Money refunded." )
        else:
            print("Sorry not enough resources. Money refunded.")