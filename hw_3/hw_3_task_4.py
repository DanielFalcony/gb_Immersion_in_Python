import random
"""
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака.
"""

items = {
    'Отвертка': 2,
    'Фонарик': 3,
    'Термобелье': 6,
    'Дождевик': 3,
    'Личная аптечка': 3,
    'Средства личной гигиены': 4,
    'Нитки с иголкой': 1,
    'Спальный мешок': 10,
    'Термос': 3,
    'Палатка': 10,
    'Трекинговые палки': 7,
    'Посуда': 5,
    'Коврик': 2,

}

# version 1 (пошаговая комплектация рюкзака)
backpack = int(input('version 1 Введите размер рюкзака (Например: 30): '))
items_in_backpack = {}

while True:
    for i in items:
        if backpack > 0 and (backpack - items[i]) >= 0:
            items_in_backpack[i] = items[i]
            print(f'Вы положили в рюкзак {i}')
            backpack -= items[i]
            print(f'Осталось место в рюкзаке {backpack}')
    break

for i in items_in_backpack.items():
    print(f'В ваш рюкзак влезет: {i}')


# version 2 (Рандомная комплектация рюкзака)
backpack = int(input('version 2 Введите размер рюкзака (Например: 30): '))
items_in_backpack = {}


while True:
    for i in range(1, 40):
        random_item = random.sample(list(items.items()), 1)[0]
        if backpack > 0 and (backpack - random_item[1]) >= 0 and random_item[0] not in items_in_backpack:
            items_in_backpack[random_item[0]] = [random_item[1]]
            print(f'Вы положили в рюкзак "{random_item[0]}" Весом "{random_item[1]}" кг')
            backpack -= random_item[1]
            print(f'В рюкзаке осталось "{backpack}" кг свободного места')
    break

for i in items_in_backpack.items():
    print(f'В вашем рюкзаке лежит: {i}')


# version 3 (Все комбинации рюкзака)
backpack = int(input('version 3 Введите размер рюкзака (Например: 30): '))

combinations = [[]]
for item, weight in items.items():
    new_combinations = []
    for c in combinations:
        if sum([items[i] for i in c]) + weight <= backpack:
            new_combinations.append(c + [item])
    combinations.extend(new_combinations)

valid_combinations = [c for c in combinations if sum([items[i] for i in c]) <= backpack]

for c in valid_combinations:
    print(c)
