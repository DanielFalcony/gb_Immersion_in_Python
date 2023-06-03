"""
Задание №2
Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
При нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списковархивов
list-архивы также являются свойствами экземпляра

Задание №3
Добавьте к задачам 1 и 2 строки документации для классов.

Задание №4
Доработаем класс Архив из задачи 2.
Добавьте методы представления экземпляра для программиста
и для пользователя.


"""


# class Archive:
#     all_previous_numbers = []
#     all_previous_string = []
#     previous_numbers = None
#     previous_string = None
#
#     def __init__(self, number, some_str):
#         self.number = number
#         self.some_str = some_str
#         if Archive.previous_numbers is not None:
#             Archive.all_previous_numbers.append(Archive.previous_numbers)
#             Archive.all_previous_string.append(Archive.previous_string)
#
#         Archive.previous_numbers = self.number
#         Archive.previous_string = self.some_str
#
#     def __str__(self):
#         return f'Number: {self.number}, string: {self.some_str}, ' \
#                f'archive: {list(zip(Archive.all_previous_numbers, Archive.all_previous_string))}'


class Archive:
    """
    Архив, который хранит пару свойств.
    Например, число и строку.
    При нового экземпляра класса, старые данные из ранее
    созданных экземпляров сохраняются в пару списковархивов
    list-архивы также являются свойствами экземпляра
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        Actually a Singleton
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.all_previous_numbers = []
            cls._instance.all_previous_string = []
        else:
            cls._instance.all_previous_numbers.append(cls._instance.number)
            cls._instance.all_previous_string.append(cls._instance.some_str)
        return cls._instance

    def __init__(self, number, some_str):
        """
        Initiation of cls
        :param number: number
        :param some_str: string
        """
        self.number = number
        self.some_str = some_str

    def __str__(self):
        """
        Human-read text
        :return:
        """
        return f'Number: {self.number}, string: {self.some_str}, ' \
               f'archive: {list(zip(self.all_previous_numbers, self.all_previous_string))}'

    def __repr__(self):
        return f'Archive({self.number}, {self.some_str})'


if __name__ == '__main__':
    arc = Archive(1, 'Ark1')
    print(arc)
    arc1 = Archive(2, 'Ark2')
    print(arc1)
    arc2 = Archive(3, 'Ark3')
    print(arc2)
    print(help(Archive))
    arc3 = Archive(4, 'Ark4')
    print(arc3.__repr__())
