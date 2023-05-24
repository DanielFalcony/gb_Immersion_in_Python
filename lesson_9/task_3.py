import json

'''
Задание №3
Напишите декоратор, который сохраняет в json файл
параметры декорируемой функции и результат, который она
возвращает. При повторном вызове файл должен
расширяться, а не перезаписываться.
Каждый ключевой параметр сохраните как отдельный ключ
json словаря.
Для декорирования напишите функцию, которая может
принимать как позиционные, так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой
функции.
'''


def deco(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        file_name = f'{func.__name__}.json'
        dump_dict = {}
        dump_dict['arguments'] = [*args]
        for key, val in kwargs.items():
            dump_dict[key] = val
        dump_dict['result'] = result
        json.dump(dump_dict, open(file_name, 'a', encoding='utf-8'), indent=4)
        return result
    return wrapper


@deco
def func_sum(x, y):
    return x + y


print(func_sum(x=3, y=5))
