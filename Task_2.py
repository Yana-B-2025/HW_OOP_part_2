# Нужно написать функцию, которая на вход принимает список блюд из cook_book и количество персон 
# для кого мы будем готовить

# get_shop_list_by_dishes(dishes, person_count)

# На выходе мы должны получить словарь с названием ингредиентов и его количества 
# для блюда. Например, для такого вызова

# get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

# Должен быть следующий результат:
# {
#   'Картофель': {'measure': 'кг', 'quantity': 2},
#   'Молоко': {'measure': 'мл', 'quantity': 200},
#   'Помидор': {'measure': 'шт', 'quantity': 4},
#   'Сыр гауда': {'measure': 'г', 'quantity': 200},
#   'Яйцо': {'measure': 'шт', 'quantity': 4},
#   'Чеснок': {'measure': 'зубч', 'quantity': 6}
# }



import os
import pprint

def get_cook_book():
    cook_book = {}
    with open('recipes.txt', 'r', encoding='utf-8') as file:
        for line in file:
            dish_name = line.strip()
            ingredient_count = int(file.readline().strip())
            ingredients = []
            for _ in range(ingredient_count):
                ing_line = file.readline().strip()
                name, quantity, measure = ing_line.split(' | ')
                
                ingredient_dict = {
                    'ingredient_name': name,
                    'measure': measure,
                    'quantity': int(quantity)
                }
                ingredients.append(ingredient_dict)
            cook_book[dish_name] = ingredients
            file.readline()
    return cook_book

    print(cook_book)

def get_shop_list_by_dishes(dishes, person_count): 
    shop_list = {}  
    cook_book = get_cook_book()
    for dish_ in dishes:   
        for ingredients in cook_book[dish_]:
            prod_name = ingredients['ingredient_name']
            quantity = ingredients['quantity'] * person_count
            if prod_name in shop_list:
                shop_list[prod_name]['quantity'] += quantity
            else:
                shop_list[prod_name] = {
                    'measure': ingredients['measure'],
                    'quantity': quantity        
                }         
                    
    return shop_list    
pprint.pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))


                         


         

# Вызываем функцию и печатаем результат
# cook_book = get_cook_book()
# for dish_name, ingredients in cook_book.items():
#     print(f"{dish_name}:") 
#     for ing in ingredients:
#         print(f" ingredient_name: {ing['ingredient_name']} , quantity: {ing['quantity']} , measure: {ing['measure']}")
#     print() 