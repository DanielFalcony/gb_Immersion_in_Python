from random import randint, uniform

'''
Задание №1
✔ Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции.
'''


def write_random_nums(count_lines: int, filename: str) -> None:
    with open(filename, 'a', encoding='utf-8') as f:
        for i in range(count_lines):
            int_num = randint(-1000, 1000)
            float_num = uniform(-1000, 1000)
            f.write(f'{int_num:>5} | {float_num:.3f}\n')


if __name__ == '__main__':
    write_random_nums(10, 'lesson_7_task_1_new_random_file')
