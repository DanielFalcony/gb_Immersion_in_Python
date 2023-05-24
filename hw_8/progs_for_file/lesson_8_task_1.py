import random
import string
import json

"""
Задание №1
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее
файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.

"""


def make_file(flag: str):
    with open('data.txt', flag, encoding='utf-8') as f:
        lenght = random.randint(4, 7)
        s = ""
        for i in range(lenght):
            s += random.choice(string.ascii_lowercase)
        f.write(f'{s}: {random.randint(1, 100)}\n')


make_file('w')
for _ in range(10):
    make_file('a')

with (open("data.txt", 'r', encoding='utf-8') as f,
      open('data.json', 'w', encoding='utf-8') as f_1):
    my_dict = {}
    for line in f.readlines():
        key, val = line.split(':')
        my_dict[key.title()] = int(val)

    json.dumps(my_dict, f, f_1, separators=(',\n', ':'))
