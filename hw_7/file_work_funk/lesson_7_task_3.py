'''
Задание №3
✔ Напишите функцию, которая открывает на чтение созданные
в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните
имя и произведение:
✔ если результат умножения отрицательный, сохраните имя
записанное строчными буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя
прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк,
сколько в более длинном файле.
✔ При достижении конца более короткого файла,
возвращайтесь в его начало.
'''


def whatever():
    with (open('lesson_7_task_1_new_random_file', 'r', encoding='utf-8') as random_file,
          open('lesson_7_task_2_names_file', 'r', encoding='utf-8') as names_file):
        numbers = random_file.readlines()
        names = names_file.readlines()

    lines_to_write = []
    lenght_of_longest = max(len(numbers), len(names))
    for i in range(lenght_of_longest):
        two_numbers = numbers[i % len(numbers)]
        a, b = map(float, two_numbers.split('|'))
        mult = a * b

        name = names[i % len(names)]
        if mult >= 0:
            lines_to_write.append(f'{name.upper().rstrip()}; {round(mult)}\n')
        else:
            lines_to_write.append(f'{name.lower().rstrip()}; {abs(mult)}\n')

    with open('lesson_7_task_3_two_files_from_1_and_2', 'w', encoding='utf=8') as f:
        f.writelines(lines_to_write)


if __name__ == '__main__':
    whatever()
