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


def add_user():
    while True:
        name = input("Введите имя пользователя (или 'q' для выхода): ")
        if name == 'q':
            break

        user_id = input("Введите личный идентификатор пользователя: ")

        while True:
            access_level = input("Введите уровень доступа (от 1 до 7): ")
            if access_level.isdigit() and 1 <= int(access_level) <= 7:
                break
            else:
                print("Некорректный уровень доступа. Попробуйте снова.")

        # Загрузка существующих данных из файла
        try:
            with open('users.json', 'r') as file:
                data = json.load(file)
                if isinstance(data, list):
                    users = {}
                else:
                    users = data
        except FileNotFoundError:
            users = {}

        # Создание нового пользователя
        user = {
            'name': name,
            'user_id': user_id,
            'access_level': int(access_level)
        }

        # Проверка уникальности идентификатора пользователя
        for existing_user in users.get(access_level, []):
            if existing_user['user_id'] == user_id:
                print("Пользователь с таким идентификатором уже существует.")
                break
        else:
            # Добавление нового пользователя в словарь пользователей
            if access_level in users:
                users[access_level].append(user)
            else:
                users[access_level] = [user]

            # Сохранение обновленных данных в файл
            with open('users.json', 'w', encoding='utf-8') as file:
                json.dump(users, file, indent=4)

            print("Информация о пользователе успешно добавлена.")


if __name__ == '__main__':

    add_user()
