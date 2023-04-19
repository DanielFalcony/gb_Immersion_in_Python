import os

"""
Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла.
"""

my_path = (os.path.abspath('hw_5_task_2.py'))


# my_path = 'A:\PythonPyCharm\PyCharmProjects\gb_Immersion_in_Python\hw_5\hw_5_task_2.py' - путь к файлу, у меня в ПК

# С помощью Лямбда-функции, режем правым поиском, индексы нужных разделителей и сохраняем обрезки в эл. Картежа.
def get_file_info(path):
    return (lambda s: (s[:s.rfind('\\')], s[s.rfind('\\') + 1:s.rfind('.')], s[s.rfind('.') + 1:]))(path)


print(get_file_info(my_path))
