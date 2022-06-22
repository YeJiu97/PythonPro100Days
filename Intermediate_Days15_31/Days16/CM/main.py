from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# 进行实例化
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

# 机器是否继续运行
is_on = True

# 调用函数
coffee_maker.report()
money_machine.report()

# 写一个循环函数来进行运行
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}):")

    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if print(coffee_maker.is_resource_sufficient(drink)) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)