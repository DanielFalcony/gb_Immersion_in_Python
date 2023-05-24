from random import randint, choices, randbytes
from string import ascii_letters

'''
Задание №4
✔ Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона.
'''


def create_file(extension: str, min_rand_name_len: int = 6, max_rand_name_len: int = 30,
                min_size_bit: int = 256, max_size_bit: int = 4096, file_count: int = 2) -> None:
    for i in range(file_count):
        len_name = randint(min_rand_name_len, max_rand_name_len)
        file_name = ''.join(choices(ascii_letters, k=len_name)) + f'.{extension}'
        random_size = randint(min_size_bit, max_size_bit)
        with open(file_name, 'bw') as f:
            f.write(randbytes(random_size))


if __name__ == '__main__':
    create_file('txt')
