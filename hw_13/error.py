class RectangleException(Exception):
    pass


class RectangleTypeError(RectangleException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Передаваемые стороны, должны быть int!\n ' \
               f'У вас тип {type(self.value)}, значение: {self.value}'


class RectangleValueError(RectangleException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Передаваемые стороны должны быть больше нуля! ' \
               f'У вас тип: {type(self.value)}, значение: {self.value}'
