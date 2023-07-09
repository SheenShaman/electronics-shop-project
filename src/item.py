import csv
import os
from src.csv_error import InstantiateCSVError


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """

        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.name}"

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        raise Exception

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.quantity * self.price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate

    @property
    def name(self):
        """ Геттер для атрибута name """
        return self.__name

    @name.setter
    def name(self, name):
        """
        Сеттер name проверяет, что длина наименования товара не больше 10 симвовов.
        В противном случае, обрезает строку
        """
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name

    @classmethod
    def instantiate_from_csv(cls):
        """
        Класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv
        """
        items_csv = os.path.join(os.path.dirname(__file__), '../src/items.csv')

        try:
            Item.all = []
            with open(items_csv, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if "name" and "price" and "quantity" in row:
                        cls(row['name'], row['price'], row['quantity'])
                    else:
                        raise InstantiateCSVError
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')

    @staticmethod
    def string_to_number(string):
        """
        Статический метод, возвращающий число из числа-строки
        """
        return int(float(string))
