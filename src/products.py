from src.stock import Stock
from uuid import uuid4


class Product:
    def __init__(self, name, price):
        self.id = str(uuid4())
        self.name = name
        self.price = price
        self.add_to_stock()

    def __repr__(self):
        return f"Product({self.id}, {self.name}, {self.price})"

    def __str__(self):
        return f"Product({self.id}, {self.name}, {self.price})"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price
        }

    def add_to_stock(self):
        Stock.add_product(self.to_dict())


class Meat(Product):
    """
    Класс "Мясо"
    """

    def __init__(self, name, price):
        super().__init__(name, price)


class Fish(Product):
    """
    Класс "Рыба"
    """

    def __init__(self, name, price):
        super().__init__(name, price)


class Vegetables(Product):
    """
    Класс "Овощи"
    """

    def __init__(self, name, price):
        super().__init__(name, price)
