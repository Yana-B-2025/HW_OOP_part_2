# Данные в файле .txt:

# Омлет
# 3
# Яйцо | 2 | шт
# Молоко | 100 | мл
# Помидор | 2 | шт

# Утка по-пекински
# 4
# Утка | 1 | шт
# Вода | 2 | л
# Мед | 3 | ст.л
# Соевый соус | 60 | мл

# Запеченный картофель
# 3
# Картофель | 1 | кг
# Чеснок | 3 | зубч
# Сыр гауда | 100 | г

# Фахитос
# 5
# Говядина | 500 | г
# Перец сладкий | 1 | шт
# Лаваш | 2 | шт
# Винный уксус | 1 | ст.л
# Помидор | 2 | шт

# Должен получится следующий словарь

# cook_book = {
#   'Омлет': [
#     {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#     {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#     {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ],
#   'Утка по-пекински': [
#     {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
#     {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
#     {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
#     {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
#     ],
#   'Запеченный картофель': [
#     {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
#     {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
#     {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
#     ]
#   }

# Что нужно сделать:
# 1. В одном файле может быть произвольное количество блюд.
# 2. Читать список рецептов из этого файла.
# 3. Соблюдайте кодстайл, разбивайте новую логику на функции 
# и не используйте глобальных переменных.

import os
# import pprint

def get_cook_book():
    # Создаем пустой словарь, куда будем складывать рецепты
    cook_book = {}

    # Открываем файл для чтения ('r') с нужной кодировкой
    with open('recipes.txt', 'r', encoding='utf-8') as file:
        for line in file:
            # 1. Читаем название блюда (убираем лишние пробелы по краям)
            dish_name = line.strip()
            
            # 2. Читаем следующую строку — это количество ингредиентов
            ingredient_count = int(file.readline().strip())
            
            # 3. Создаем список для хранения ингредиентов этого блюда
            ingredients = []
            
            # 4. Циклом проходим столько раз, сколько у нас ингредиентов
            for _ in range(ingredient_count):
                # Читаем строку с ингредиентом и режем её по символу "|"
                ing_line = file.readline().strip()
                name, quantity, measure = ing_line.split(' | ')
                
                # Собираем словарик одного ингредиента
                ingredient_dict = {
                    'ingredient_name': name,
                    'measure': measure,
                    'quantity': int(quantity)
                }
                # Добавляем его в общий список для этого блюда
                ingredients.append(ingredient_dict)
            
            # 5. Кладем список ингредиентов в основной словарь cook_book
            cook_book[dish_name] = ingredients
            
            # 6. Читаем пустую строку между рецептами, чтобы перейти к следующему названию
            file.readline()

    return cook_book

# Вызываем функцию и печатаем результат
cook_book = get_cook_book()
# pprint.pprint(result, width=500, indent=2, sort_dicts=False)

# Перебираем словарь: название (key) и список ингредиентов (value)
for dish_name, ingredients in cook_book.items():
    print(f"{dish_name}:") # Печатаем название блюда и переходим на новую строку
    
    for ing in ingredients:
        # Печатаем каждый ингредиент в одну строку с небольшим отступом
        print(f" ingredient_name: {ing['ingredient_name']} , quantity: {ing['quantity']} , measure: {ing['measure']}")
    
    print() # Добавляем пустую строку между разными блюдами для красоты

print (cook_book)