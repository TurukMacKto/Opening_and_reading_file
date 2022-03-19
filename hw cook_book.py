from pprint import pprint


def recipes(input_file) -> {}:
    cook_book = {}
    with open(input_file, encoding='utf-8') as file:
        food_list = file.read().splitlines()
        for index, digit in enumerate(food_list):
            if digit.isdigit():
                cook_book[food_list[index - 1]] = []
                for food in food_list[index + 1:index + int(digit) + 1]:
                    cook_book[food_list[index - 1]].append({'ingredient_name': food.split('|')[0],
                                                            'quantity': int(food.split('|')[1]),
                                                            'measure': food.split('|')[2]})
    return cook_book


def get_shop_list_by_dishes(dishes, persons) -> {}:
    cook_book = recipes('recipes.txt')
    shop_list = {}
    for dish in dishes:
        for value in cook_book[dish]:
            value_list = dict(
                [(value['ingredient_name'],
                  {'measure': value['measure'], 'quantity': int(value['quantity']) * persons})])
            if value['ingredient_name'] in shop_list.keys():
                shop_list[value['ingredient_name']]['quantity'] = (
                            int(shop_list[value['ingredient_name']]['quantity']) +
                            int(value_list[value['ingredient_name']]['quantity']))
            else:
                shop_list.update(value_list)
    return shop_list


print()
print('Задача №1:')
pprint(recipes('recipes.txt'), sort_dicts=False)
print('----------------------------------------------------------------------------------------')
print('Задача №2:')
pprint(get_shop_list_by_dishes(['Омлет', 'Омлет'], 2))
print('----------------------------------------------------------------------------------------')
