import random
from random import randint

'''
Задание №2
✔ Напишите функцию, которая генерирует
псевдоимена.
✔ Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
✔ Полученные имена сохраните в файл.
'''

VOWELS = 'аеиоуяюёэы'
CONSONANTS = ''.join([chr(ch) for ch in range(ord('а'), ord('я') + 1) if chr(ch) not in VOWELS])


def make_random_name(amount_of_names: int) -> None:
    count = 0
    while count != amount_of_names:
        word_len = randint(4, 8)
        word = ''.join(random.choices(VOWELS + CONSONANTS, k=word_len)).title()
        if any(ch in VOWELS for ch in word):
            with open('lesson_7_task_2_names_file', 'a', encoding='utf-8') as f:
                f.write(f'{word}\n')
                count += 1
        else:
            make_random_name(amount_of_names)


if __name__ == '__main__':
    make_random_name(10)
