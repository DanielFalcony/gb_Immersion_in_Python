import os
from pathlib import Path

'''
Доделать дома задания которые не сделали на семинаре:

Задание №7
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
'''


def sort_files(way: Path) -> None:
    video = ['avi', 'mp4', 'avi']
    image = ['bmp', 'gif', 'jpg', 'jpeg', 'png', 'webp']
    text = ['txt', 'doc', 'pdf', 'csv']
    audio = ['mp3', 'wav']
    for dir_path, dir_names, file_names in os.walk(way):
        for file_name in file_names:
            file_path = Path(dir_path) / file_name
            file_extension = file_path.suffix[1:]  # Извлекаем расширение файла без точки

            if file_extension in video:
                target_directory = way / 'video'
            elif file_extension in image:
                target_directory = way / 'image'
            elif file_extension in text:
                target_directory = way / 'text'
            elif file_extension in audio:
                target_directory = way / 'audio'
            else:
                continue

            target_directory.mkdir(exist_ok=True)
            new_file_path = target_directory / file_path.name
            file_path.replace(new_file_path)


if __name__ == '__main__':
    way_to_sort = Path.cwd() / '..' / 'lessons' / 'other'  # мой путь до папки с файлами
    sort_files(way_to_sort)
