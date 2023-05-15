import csv
import json

"""
Задание №4
Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка
csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы
функции.
"""


def read_csv_convert_save(csv_file, json_file):
    try:
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            headers = next(reader)
            rows = list(reader)
    except FileNotFoundError:
        print(f"Файл {csv_file} не найден.")
        return

    converted_data = []
    for row in rows:
        # Преобразование данных и добавление хеша
        name = row[0].capitalize()
        user_id = row[1].zfill(10)
        access_level = int(row[2])
        hash_value = hash(name + user_id)

        converted_data.append({
            'Name': name,
            'User ID': user_id,
            'Access Level': access_level,
            'Hash': hash_value
        })

    try:
        with open(json_file, 'w', encoding='utf-8') as file:
            json.dump(converted_data, file, indent=4)
        print(f"Данные из {csv_file} успешно прочитаны, преобразованы и сохранены в {json_file}.")
    except IOError:
        print(f"Ошибка при сохранении данных в файл {json_file}.")


if __name__ == '__main__':
    csv_file = 'users.csv'
    json_file = 'converted_users.json'
    read_csv_convert_save(csv_file, json_file)
