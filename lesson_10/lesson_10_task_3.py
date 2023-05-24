"""
Задание №3
Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст.
"""


class People:
    def __init__(self, name: str, last_name: str, age: int):
        self.__name = name
        self.__last_name = last_name
        self.__age = age

    def birthday_up(self):
        self.__age += 1

    def age_getter(self):
        return self.__age

    def full_name_getter(self):
        return f'{self.__name} {self.__last_name}'


man_1 = People('Федор', 'Пупкин', 25)
man_1.birthday_up()
man_1.birthday_up()
print(f'{man_1.age_getter()= }, {man_1.full_name_getter()= }')

man_2 = People('Иван', 'Жопкин', 20)
man_2.birthday_up()
man_2.birthday_up()
print(f'{man_2.age_getter()= }, {man_2.full_name_getter()= }')
