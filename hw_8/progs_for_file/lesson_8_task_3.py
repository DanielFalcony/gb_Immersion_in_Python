import csv
import json

"""
Задание №2
Напишите функцию, которая в бесконечном цикле
запрашивает имя, личный идентификатор и уровень
доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в
JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо
от уровня доступа.
При перезапуске функции уже записанные в файл данные
должны сохраняться.
"""


def save_users_as_csv():
    try:
        with open('users.json', 'r') as file:
            users = json.load(file)
    except FileNotFoundError:
        print("Файл users.json не найден.")
        return

    fieldnames = ['Name', 'User ID', 'Access Level']

    try:
        with open('users.csv', 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for user_list in users.values():
                for user in user_list:
                    writer.writerow(
                        {'Name': user['name'], 'User ID': user['user_id'], 'Access Level': user['access_level']})

        print("Данные пользователей успешно сохранены в файл users.csv.")
    except IOError:
        print("Ошибка при сохранении данных в файл users.csv.")


if __name__ == '__main__':

    save_users_as_csv()
