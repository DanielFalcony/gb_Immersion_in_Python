import os
from pathlib import Path

"""
1. Напишите функцию группового переименования файлов. Она должна:
2. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
3. принимать параметр количество цифр в порядковом номере.
4. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
5. принимать параметр расширение конечного файла.
6. принимать диапазон сохраняемого оригинального имени.
7. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
"""


def group_rename(count_nums_name: int, old_file_ext: str, new_file_ext: str, name_range: list,
                 new_file_name: str = False) -> None:
    """
    :param count_nums_name: Number of digits in serial number
    :param old_file_ext: old file extension
    :param new_file_ext: new file extension
    :param name_range: name range [3, 4]
    :param new_file_name: new filename is optional
    :return: None
    """

    for dir_path, dir_names, file_names in os.walk(Path.cwd() / 'files_to_rename'):
        count_file_id = 1
        for file_name in file_names:
            file_name_no_ext = Path(file_name).stem
            start = 0
            end = 0
            if name_range:
                if len(file_name_no_ext) >= name_range[1]:
                    start = name_range[0]
                    end = name_range[1]
                else:
                    start = name_range[0]
                    end = len(file_name_no_ext)
            file_id = str(count_file_id).zfill(count_nums_name)  # формируем порядковый номер для файла
            file_path = Path(dir_path) / file_name
            file_extension = file_path.suffix[1:]
            if file_extension == old_file_ext:
                if new_file_ext:
                    if new_file_name:
                        name_to_change = f'{new_file_name}{file_id}.{new_file_ext}'
                    elif name_range:
                        name_to_change = f'{file_name_no_ext[start:end]}{file_id}.{new_file_ext}'
                    else:
                        name_to_change = f'{file_name_no_ext}{file_id}.{new_file_ext}'
                else:
                    name_to_change = f'{file_name_no_ext}{file_id}.{file_extension}'
            else:
                name_to_change = f'{file_name_no_ext}{file_id}.{file_extension}'
            file_path.rename(file_path.with_name(name_to_change))
            count_file_id += 1


group_rename(5, 'bmp', 'new_ext', [1, 3], 'new_file_name')
