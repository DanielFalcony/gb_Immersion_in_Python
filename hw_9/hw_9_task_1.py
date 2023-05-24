import json
import csv
import math
from random import randint
from typing import Callable

'''
Напишите следующие функции:
○ Нахождение корней квадратного уравнения
○ Генерация csv файла с тремя случайными числами в каждой строке.
100-1000 строк.
○ Декоратор, запускающий функцию нахождения корней квадратного
уравнения с каждой тройкой чисел из csv файла.
○ Декоратор, сохраняющий переданные параметры и результаты работы
функции в json файл.
'''


def quadratic_equation(a: int, b: int, c: int) -> (float, float):
    discr = b ** 2 - 4 * a * c
    print(f'Дискриминант = {discr:.2f}')

    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        return f'{x1:.2f}, {x2:.2f}'
    elif discr == 0:
        x = -b / (2 * a)
        return f'{x:.2f}'
    else:
        return 'Корней нет'


def num_csv_gen(file_name):
    with open(file_name, 'w', newline='') as csv_f:
        writer = csv.writer(csv_f)
        for _ in range(randint(100, 1000)):
            row = [randint(1, 20) for _ in range(3)]
            writer.writerow(row)


def deco_roots(func: Callable):
    def wrapper(csv_file):
        results = []
        with open(csv_file, 'r', newline='') as csv_f:
            reader = csv.reader(csv_f)
            for row in reader:
                a, b, c = map(int, row)
                roots = func(a, b, c)
                results.append((a, b, c, roots))
                print(f"Корни уравнения {a}x^2 + {b}x + {c} = 0: {roots}")
            return results

    return wrapper


def save_to_json_deco(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        data = {
            'function_name': func.__name__,
            'arguments': {
                'args': args,
                'kwargs': kwargs
            },
            'result': result
        }
        file_name = f'{func.__name__}_results.json'
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f'Результаты сохранены в файл {file_name}')
        return result

    return wrapper


@save_to_json_deco
@deco_roots
def find_roots(a, b, c):
    return quadratic_equation(a, b, c)


csv_file = 'random_numbers.csv'
num_csv_gen(csv_file)

find_roots(csv_file)
