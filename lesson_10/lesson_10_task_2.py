"""
Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании
экземпляра.
У класса должно быть два метода, возвращающие периметр
и площадь.
Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат.
"""


class Rectangle:
    def __init__(self, side_a: int, side_b: int | None = None):
        self.side_a = side_a
        self.side_b = side_b if side_b else side_a

    def perimeter(self):
        return 2 * (self.side_a + self.side_b)

    def rec_sqr(self):
        return self.side_a * self.side_b


rec_1 = Rectangle(4, 3)
print(f'{rec_1.perimeter()= }, {rec_1.rec_sqr()= }')
rec_2 = Rectangle(4)
print(f'{rec_2.perimeter()= }, {rec_2.rec_sqr()= }')
