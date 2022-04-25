def get_recipes_from_file(file_name: str, mode: str='r', encoding: str='utf-8'):
    count = 0
    cook_book = {}
    with open(file_name, mode, encoding = encoding) as file:
        for line in file:
            line = line.rstrip('\n')
            count += 1
            if count == 1:
                name = line
                reciple = []
            elif count == 2:
                qty = int(line)
            elif count < qty + 3:
                ingredient = line.split(' | ')
                additional = {
                    'ingredient_name': ingredient[0],
                    'quantity': int(ingredient[1]),
                    'measure': ingredient[2]
                }
                reciple.append(additional)
            else:
                count = 0
                cook_book[name] = reciple
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = get_recipes_from_file('recipes.txt')
    ingredients = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            name = ingredient['ingredient_name']
            if(name in ingredients):
                ingredient['quantity'] = ingredients[name]['quantity'] + ingredient['quantity']

            ingredients[ingredient['ingredient_name']] = {
                'measure': ingredient['measure'],
                'quantity': ingredient['quantity']
            }
    print(ingredients)

get_recipes_from_file('recipes.txt')
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)