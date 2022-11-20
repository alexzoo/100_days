from data import MENU, resources

profit = 0
is_on = True


def is_enough_resources(drink_ingredients: dict):
    """Check if resources of ingredients is enough
    """
    for item in drink_ingredients:
        if drink_ingredients[item] >= resources[item]:
            print(f'Sorry there is not enough {item}')
            return False
        else:
            return True


def process_coins():
    """Return total caclulated coins
    """
    print('Insert coins: ')
    total = int(input('how many 0.25?: ')) * 0.25
    total += int(input('how many 0.1?: ')) * 0.1
    total += int(input('how many 0.05?: ')) * 0.05
    total += int(input('how many 0.01?: ')) * 0.01
    return total


def is_transaction_successful(money, drink_price):
    """Return True if money is enough or False if insufficient"""
    if money >= drink_price:
        change = round(money - drink_price, 2)
        print(f'Here is ${change} in change')
        global profit
        profit += drink_price
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return True


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f'Here is your {drink_name} ☕️')


while is_on:
    choice = input(
        'What would you like? (espresso/latte/cappuccino/report/off): ')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Money: ${profit}')
    else:
        drink = MENU[choice]
        print(drink)
        if is_enough_resources(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])
