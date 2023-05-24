from typing import Callable

'''
Задание №4
Создайте декоратор с параметром.
Параметр - целое число, количество запусков декорируемой
функции.
'''


def counter(num: int):
    def level_one(func: Callable):
        cache = []

        def wrapper(*args, **kwargs):
            for _ in range(num):
                cache.append(func(*args, **kwargs))
            return cache

        return wrapper

    return level_one


@counter(5)
def func(text: str):
    return text.upper()


print(func('Все кончено'))
