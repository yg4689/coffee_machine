from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


m=Menu()
coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()
is_on=True
while is_on:
    options=m.get_items()
    i=input(f"enter the item({options}): ")
    if i=="off":
        is_on=False
    elif i=="report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink=m.find_drink(i)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)





