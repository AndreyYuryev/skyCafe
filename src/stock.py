class Stock:
    """
    Класс для хранения склада
    """
    __stock = {}

    def __init__(self, name='Склад 1'):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def add_product(self, product, quantity=0):
        """
        Добавить продукт на склад
        """
        product_id = product.product_id
        product_value = {'object': product, 'quantity': quantity}
        self.__stock[product_id] = product_value

    def get_quantity_by_id(self, product_id):
        """ Получить количество продукта по ID """
        stock_value = self.__stock.get(product_id, None)
        if stock_value is not None:
            return stock_value['quantity']
        return 0

    def get_quantity_by_product(self, product):
        """ Получить количество по продукту """
        product_id = product.product_id
        return self.get_quantity_by_id(product_id)

    def add_quantity_by_product(self, product, quantity):
        """ Добавить количество по продукту"""
        product_id = product.product_id
        stock_value = self.__stock.get(product_id, None)
        if stock_value is None:
            self.add_product(product=stock_value['object'], quantity=quantity)
        else:
            stock_value['quantity'] += quantity

    # def __str__(self):
    #     return "Здесь хранятся все наши продукты"
    #
    # def __repr__(self):
    #     pass
    #
    # def is_product_in_stock(self, product):
    #     """
    #     Проверить наличие продукта в наличии:
    #     """
    #     for item in self.products:
    #         if item.product_id == product.product_id:
    #             return True
    #     return False
    #
    # def add_product(self, product, quantity=0):
    #     """
    #     Добавить продукт:
    #     """
    #     self.products.append(StockItem(product_id=product.product_id, name=product.name, quantity=quantity))
    #
    # def remove_product(self, product):
    #     """
    #     Удалить продукт:
    #     """
    #     for item in self.products:
    #         if product.product_id == item.product_id:
    #             del item
    #
    # def get_quantity(self, product):
    #     """ Вернуть количество продукта """
    #     for item in self.products:
    #         if product.product_id == item.product_id:
    #             return item.quantity
    #
    # @classmethod
    # def add_quantity(cls, product, quantity):
    #     """
    #     Увеличить количество продукта:
    #     """
    #     cls.products[product]["quantity"] += quantity
    #
    # @classmethod
    # def remove_quantity(cls, product, quantity):
    #     """
    #     Уменьшить количество продукта:
    #     """
    #     product["quantity"] -= quantity
