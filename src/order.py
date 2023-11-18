""" Заказ """


class Order:
    """
    Класс заказ
    """
    __last_order_number = 0

    def __init__(self):
        self.__number = Order.__new_number()
        self.title = f'Заказ {self.__number} с описанием'
        self.__items = {}

    @classmethod
    def __new_number(cls):
        """
        Получить следующий номер заказа.
        Если будет история заказов считать последний номер
        заказа и присвоить last_order_number
        :return:
        """
        cls.__last_order_number += 1
        return cls.__last_order_number

    def add_item(self, product_id, quantity):
        """
        Добавить позицию в заказ
        :param product_id:
        :param quantity:
        :return:
        """
        if self.__items.get(product_id, None) is not None:
            self.__items[product_id] = quantity
        else:
            item_quantity = self.__items.get(product_id, 0)
            self.__items[product_id] = item_quantity + quantity

    @property
    def items(self):
        """
        Получить позиции заказа
        :return:
        """
        return self.__items

    @property
    def number(self):
        """ Вернуть номер заказа """
        return self.__number

    def __str__(self):
        """ Текстовое представление """
        return f'Заказ {self.__number}'

