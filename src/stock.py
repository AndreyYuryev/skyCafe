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

    @classmethod
    def is_product_in_stock(cls, product):
        """
        Проверить наличие продукта в наличии:
        """
        return product in cls.products

    @classmethod
    def add_product(cls, product, quantity=0):
        """
        Добавить продукт:
        """
        product["quantity"] = quantity
        cls.products.append(product)

    @classmethod
    def remove_product(cls, product):
        """
        Удалить продукт:
        """
        cls.products.remove(product)

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
