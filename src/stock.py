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
    def add_product(cls, product):
        """
        Добавить продукт:
        """
        cls.products.append(product)

    def remove_product(self, product):
        """
        Удалить продукт:
        """
        self.products.remove(product)
