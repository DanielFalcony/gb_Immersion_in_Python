"""
Объедините функции из прошлых задач.
Функцию угадайку задекорируйте:
○ декораторами для сохранения параметров,
○ декоратором контроля значений и
○ декоратором для многократного запуска.
Выберите верный порядок декораторов.
"""
import json
import random

def save_param_deco(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        file_name = f'{func.__name__}.json'
        dump_dict = {}
        dump_dict["arguments"] = [*args]
        for key, value in kwargs.items():
            dump_dict[key] = value
        dump_dict["result"] = result
        json.dump(dump_dict, open(file_name, "a", encoding="utf-8"), indent=4, ensure_ascii=False)
        return result
    return wrapper


def param_control_deco(fun):
    def wrapper(guess: int, attempts: int):
        guess = guess if 1 < guess < 100 else random.randint(1, 100)
        attempts = attempts if 1 < attempts < 10 else random.randint(1, 10)
        return fun(guess, attempts)

    return wrapper


def call_counter_deco(num: int):
    def level_one(func):
        cache = []

        def wrapper(*args, **kwargs):
            for _ in range(num):
                cache.append(func(*args, **kwargs))
            return cache

        return wrapper

    return level_one


@call_counter_deco(3)
@param_control_deco
@save_param_deco
def guess_game(guess, attempts):
    while attempts > 0:
        attempts -= 1
        val = int(input('Угадай число: '))
        if val == guess:
            return 'Вы выиграли!'
    return 'Кол-во попыток исчерпано!'


print(guess_game(5, 1))