#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


class Currency(ABC):
    @abstractmethod
    def to_rubles(self):
        """Переводит сумму в рубли."""
        pass

    @abstractmethod
    def display(self):
        """Выводит сумму на экран."""
        pass


class Dollar(Currency):
    def __init__(self, amount):
        self.amount = amount

    def to_rubles(self):
        """Конвертирует доллары в рубли (курс 1 доллар = 80 рублей)."""
        return self.amount * 80

    def display(self):
        """Выводит сумму в долларах."""
        print(f"{self.amount} USD")


class Euro(Currency):
    def __init__(self, amount):
        self.amount = amount

    def to_rubles(self):
        """Конвертирует евро в рубли (курс 1 евро = 90 рублей)."""
        return self.amount * 90

    def display(self):
        """Выводит сумму в евро."""
        print(f"{self.amount} EUR")


def show_currency_info(currency):
    """Функция, принимающая объект Currency и демонстрирующая виртуальный вызов."""
    currency.display()
    print(f"Сумма в рублях: {currency.to_rubles()} RUB\n")


if __name__ == '__main__':
    # Создание экземпляров классов Dollar и Euro
    dollar_amount = Dollar(100)
    euro_amount = Euro(50)

    # Демонстрация работы с долларами
    show_currency_info(dollar_amount)  # Вывод информации о долларах

    # Демонстрация работы с евро
    show_currency_info(euro_amount)     # Вывод информации о евро
