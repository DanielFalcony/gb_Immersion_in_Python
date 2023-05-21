import os
import json
import csv

'''
Напишите функцию, которая получает на вход директорию и рекурсивно
обходит её и все вложенные директории. Результаты обхода сохраните в
файлы json, csv.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер
файлов в ней с учётом всех вложенных файлов и директорий.
Соберите из созданных на уроке и в рамках домашнего задания функций
пакет для работы с файлами разных форматов.

'''


def traverse_directory(directory):
    result = []

    # Рекурсивная функция для обхода директории
    def traverse_helper(path):
        # Получаем список всех файлов и директорий в текущей директории
        items = os.listdir(path)

        # Перебираем все элементы в текущей директории
        for item in items:
            item_path = os.path.join(path, item)
            item_type = 'Файл' if os.path.isfile(item_path) else 'Директория'
            item_size = os.path.getsize(item_path) if os.path.isfile(item_path) else get_directory_size(item_path)

            # Создаем словарь с информацией об элементе
            item_info = {
                'Имя': item,
                'Тип': item_type,
                'Размер (в байтах)': item_size,
                'Родительская директория': path
            }

            result.append(item_info)

            # Рекурсивно вызываем функцию traverse_helper для вложенных директорий
            if os.path.isdir(item_path):
                traverse_helper(item_path)

    # Вспомогательная функция для подсчета размера директории с учетом всех вложенных файлов и директорий
    def get_directory_size(dir_path):
        total_size = 0
        for path, dirs, files in os.walk(dir_path):
            for file in files:
                file_path = os.path.join(path, file)
                total_size += os.path.getsize(file_path)
        return total_size

    # Вызываем вспомогательную функцию traverse_helper для обхода директории
    traverse_helper(directory)

    # Сохраняем результаты в файлы JSON и CSV
    json_path = 'result.json'
    csv_path = 'result.csv'

    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(result, json_file, ensure_ascii=False, indent=4)

    with open(csv_path, 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=result[0].keys())
        writer.writeheader()
        writer.writerows(result)

    print(f'Обход директории завершен. Результаты сохранены в файлы {json_path} и {csv_path}.')


if __name__ == '__main__':
    directory_path = 'A:\PythonPyCharm\PyCharmProjects\gb_Immersion_in_Python\hw_7'  # Заменить на свой путь к директории
    traverse_directory(directory_path)
