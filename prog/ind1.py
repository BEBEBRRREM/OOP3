#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Pair:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def set_values(self, a, b):
        self.a = a
        self.b = b

    def product(self):
        return self.a * self.b


class Rectangle(Pair):
    def __init__(self, width=0, height=0):
        super().__init__(width, height)

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b


if __name__ == '__main__':
    # Создание экземпляра класса Pair
    pair = Pair(3, 4)
    print(f"Произведение чисел в паре: {pair.product()}")

    # Изменение значений
    pair.set_values(5, 6)
    print(f"Новое произведение чисел в паре: {pair.product()}")

    # Создание экземпляра класса Rectangle
    rectangle = Rectangle(5, 10)
    print(f"Периметр прямоугольника: {rectangle.perimeter()}")
    print(f"Площадь прямоугольника: {rectangle.area()}")

    # Изменение размеров прямоугольника
    rectangle.set_values(7, 3)
    print(f"Новый периметр прямоугольника: {rectangle.perimeter()}")
    print(f"Новая площадь прямоугольника: {rectangle.area()}")
