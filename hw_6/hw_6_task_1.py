import sys

from modules import *

if __name__ == '__main__':
    date = sys.argv[1] if len(sys.argv) > 1 else input('Введите дату вручную: ')
    if calendar(date):
        print("Дата верна")
    else:
        print('Дата не верна')
