from src.stock import Stock


class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __repr__(self):
        return f"Name: {self.name}\nQuantity: {self.quantity}\nPrice: {self.price}"

    def __str__(self):
        return f"Name: {self.name}\nQuantity: {self.quantity}\nPrice: {self.price}"

    def to_dict(self):
        return {
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price
        }

    def add_quantity(self, quantity):
        """
        Добавить количество товара
        """
        self.quantity += quantity

    def remove_quantity(self, quantity):
        """
        Удалить количество товара
        """
        self.quantity -= quantity


class Meat(Product):
    """
    Класс "Мясо"
    """

    def __init__(self, name, quantity, price):
        super().__init__(name, quantity, price)


class Fish(Product):
    """
    Класс "Рыба"
    """

    def __init__(self, name, quantity, price):
        super().__init__(name, quantity, price)


class Vegetables(Product):
    """
    Класс "Овощи"
    """

    def __init__(self, name, quantity, price):
        super().__init__(name, quantity, price)


cow_meat = Meat("Говядина", 10, 100)
golden_fish = Fish("Золотая рыбка", 10, 100)
tomato = Vegetables("Томат", 10, 100)

for product in [cow_meat, golden_fish, tomato]:
    Stock.add_product(product.to_dict())

for product in Stock.products:
    for key, value in product.items():
        print(f"{key}: {value}")
    print()
