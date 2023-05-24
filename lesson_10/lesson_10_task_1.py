from cmath import pi

'''
Задание №1
Создайте класс окружность.
Класс должен принимать радиус окружности при создании
экземпляра.
У класса должно быть два метода, возвращающие длину
окружности и её площадь.
'''


class Circles:

    def __init__(self, radius_circle: int):
        self.radius_circle = radius_circle

    def long_circle(self):
        return 2 * pi * self.radius_circle

    def area_of_circle(self):
        return pi * self.radius_circle ** 2


circle1 = Circles(3)
print(f'{circle1.long_circle()=:.2f}, {circle1.area_of_circle()=:.2f}')
