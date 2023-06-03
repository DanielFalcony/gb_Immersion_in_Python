"""
📌Создайте класс Моя Строка, где:
📌будут доступны все возможности str
📌дополнительно хранятся имя автора строки и время создания (time.time)
"""
import datetime


class MyStr(str):
    """
    My Class
    """
    # def __init__(self, data):
    #     super().__init__(self, str, data)
    def __new__(cls, value, author_name, create_time=''):
        """
        Some text
        :param value: str
        :param author_name: str
        :param create_time: is datetime.now()
        """
        instance = super().__new__(cls, value)
        instance.author_name = author_name
        instance.create_time = datetime.datetime.now()

        return instance


if __name__ == '__main__':
    s = MyStr('Stroka', 'ilyusha')
    print(s, s.author_name, s.create_time)

    print(help(MyStr))
