"""
Task 2
Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента.
Если ключ не хешируем, используйте его строковое представление. .
"""


def key_word_only(**kwargs):
    result_dict = {}
    for key, value in kwargs.items():
        result_dict[str(value)] = hash(key) if isinstance(key, (int, str, float)) else str(key)
    return result_dict


print(key_word_only(val=25, txt='test', lst=[1, 2, 3, 4], flt=5.17))
