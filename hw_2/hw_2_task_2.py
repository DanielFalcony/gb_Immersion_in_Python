"""
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""

number = input('Введите число: ')

hex_changer = '0123456789abcdefg'
result = ''

while True:
    if number.isdigit():
        edit_number = int(number)
        break
    else:
        number = input('Необходимо ввести число: ')

while edit_number:
    result += str(hex_changer[(edit_number % 16)])
    edit_number = edit_number // 16

print(f'Число "{number}" в 16-ричной системе равно: "0x{result[::-1]}"')
print('Проверка через метод hex():', hex(int(number)))
