from src.stock import Stock
from uuid import uuid4


class Product:
    __last_product_number = 0

    def __init__(self, name, price, product_id=0):
        if product_id == 0:
            self.product_id = Product.__new_number()
        else:
            self.product_id = product_id
            if Product.__last_product_number < product_id:
                Product.__last_product_number = product_id
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product({self.product_id}, {self.name}, {self.price})"

    def __str__(self):
        return f"Наименование: {self.name} Идентификатор: {self.product_id}"

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price
        }

    @classmethod
    def __new_number(cls):
        """
        Получить следующий номер продукта.
        Если будет история продуктов считать последний номер
        заказа и присвоить last_product_number
        :return:
        """
        cls.__last_product_number += 1
        return cls.__last_product_number

    @classmethod
    def clear_numbers(cls):
        cls.__last_product_number = 0


class ProductFactory:
    def __init__(self):
        """ Хранилище информации о продуктах """
        self.products = []
        Product.clear_numbers()

    def add_product(self, product: Product):
        """ Добавить продукт в хранилище """
        self.products.append(product)

    def upload_products(self, product_list=[]):
        """ Добавить продукты из словаря в хранилище """
        for item in product_list:
            product = Product(name=item['name'], price=item['price'], product_id=item['product_id'])
            self.add_product(product)

    def get_product_by_id(self, product_id):
        """ Вернуть продукт по ID """
        for item in self.products:
            if item.product_id == product_id:
                return item


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
