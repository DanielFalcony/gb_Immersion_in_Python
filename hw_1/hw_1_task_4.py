"""
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
числа используйте код:
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)
"""

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000

num = randint(LOWER_LIMIT, UPPER_LIMIT)
print(f'Правильный ответ: {num}\n'
      f'Подсказывай компьютеру больше или меньше!')
try_count = 1

while try_count <= 10:
    val = int((LOWER_LIMIT + UPPER_LIMIT) / 2)
    if val == num:
        print(f'Значение {val}')
        print('Поздравляю я Выиграл!')
    else:
        choice = str(input(f'Значение {val} больше или меньше нужного? "введи < или >": '))
        if choice == '>':
            UPPER_LIMIT = val
        else:
            LOWER_LIMIT = val
    try_count += 1
if try_count == 10:
    print('Я проиграл :( ')
