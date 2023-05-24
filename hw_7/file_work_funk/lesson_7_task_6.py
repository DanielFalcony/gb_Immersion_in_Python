from pathlib import Path
import os
from lesson_7_task_5 import some_ext_files

'''
Задание №6
✔ Дорабатываем функции из предыдущих задач.
✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
(добавьте проверки).
✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
'''


def create_dir(name_dir: str):
    name = Path(Path.cwd() / '..' / name_dir)
    if not name.exists():
        name.mkdir()
    os.chdir(name)
    some_ext_files(my_dict)


if __name__ == '__main__':
    my_dict = {
        'txt': 2,
        'csv': 3,
        'doc': 4,
        'bin': 5,
        'pdf': 1,
        'mp4': 3,
        'jpeg': 2,
        'mp3': 4,
        'wav': 1,
        'avi': 2,
        'bmp': 3,
    }

    create_dir('files_to_rename')
