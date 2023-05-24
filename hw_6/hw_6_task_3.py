from modules import *

"""
Напишите функцию в шахматный модуль.
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
"""

#  Размер доски
board_size = 6  # Пример на доске 6х6, на доске 8х8 ищет очень долго (заменить 6 на 8).
count = 0

#  Исполнительный код
good_list = []
while len(good_list) != 4:
    positions = random_queens_positions(board_size)
    if check_horizontal_and_vertical(positions):
        print(check_horizontal_and_vertical(positions))
        good_list.append(positions)
for i in good_list:
    count += 1
    print(f'Расстановка №{count} = {i}')
print_the_desk(good_list, board_size)
