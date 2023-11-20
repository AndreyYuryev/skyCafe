class Product:
    __last_product_number = 0
    __catalog = {}

    def __init__(self, name, product_id=0):
        if product_id == 0:
            self.__product_id = Product.__new_number()
        else:
            self.__product_id = product_id
            if Product.__last_product_number < product_id:
                Product.__last_product_number = product_id
        self.__name = name

    @property
    def product_id(self):
        """ Идентификатор """
        return self.__product_id

    @property
    def name(self):
        """ Наименование """
        return self.__name

    def __repr__(self):
        return f"Product({self.product_id}, {self.name})"

    def __str__(self):
        return f"Наименование: {self.name} Идентификатор: {self.product_id}"

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
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
        """ Очистка счетчика номера продуктов """
        cls.__last_product_number = 0

    @classmethod
    def add_product(cls, name, product_id=0):
        """ Добавить продукт в каталог """
        product = Product(name=name, product_id=product_id)
        product_value = {'object': product, }
        cls.__catalog[product.product_id] = product_value

    @classmethod
    def add_product_by_obj(cls, product):
        """ Добавить продукт в каталог по ссылке """
        product_value = {'object': product, }
        cls.__catalog[product.product_id] = product_value

    @classmethod
    def get_by_id(cls, product_id):
        """ Получить ссылку на продукт """
        product = cls.__catalog.get(product_id, None)
        if product is not None:
            return product['object']
        return None

    @classmethod
    def get_by_name(cls, name):
        product_list = []
        obj = None
        for item in cls.__catalog.values():
            obj = item['object']
            if name in obj.name:
                product_list.append(obj)
        return product_list

    @classmethod
    def upload_products(cls, product_list={}):
        """ Добавить продукты в каталог """
        for item in product_list:
            name = item.get('name', 'Без наименования')
            product_id = item.get('product_id', 0)
            cls.add_product(name=name, product_id=product_id)


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
