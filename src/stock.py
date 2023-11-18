class StockItem:
    def __init__(self, product_id, name, quantity=0):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f'Наименование {self.name} количество: {self.quantity}'


class Stock:
    """
    Класс для хранения склада
    """
    products = []

    def __init__(self):
        pass

    def __str__(self):
        return "Здесь хранятся все наши продукты"

    def __repr__(self):
        pass

    def is_product_in_stock(self, product):
        """
        Проверить наличие продукта в наличии:
        """
        for item in self.products:
            if item.product_id == product.product_id:
                return True
        return False

    def add_product(self, product, quantity=0):
        """
        Добавить продукт:
        """
        self.products.append(StockItem(product_id=product.product_id, name=product.name, quantity=quantity))

    def remove_product(self, product):
        """
        Удалить продукт:
        """
        for item in self.products:
            if product.product_id == item.product_id:
                del item

    def get_quantity(self, product):
        """ Вернуть количество продукта """
        for item in self.products:
            if product.product_id == item.product_id:
                return item.quantity

    @classmethod
    def add_quantity(cls, product, quantity):
        """
        Увеличить количество продукта:
        """
        cls.products[product]["quantity"] += quantity

    @classmethod
    def remove_quantity(cls, product, quantity):
        """
        Уменьшить количество продукта:
        """
        product["quantity"] -= quantity
