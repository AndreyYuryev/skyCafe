from src.stock import Stock
from src.products import *


def test_stock():
    correct_stock = [{'id': 'e7ac57cb-abb2-44f0-8c5b-9af96d0f1b5d', 'name': 'Морковь', 'price': 100, 'quantity': 1},
                     {'id': 'd93b5d1a-dd0e-4a6f-86a8-8c0e2a6e0725', 'name': 'Мясо', 'price': 200, 'quantity': 1},
                     {'id': '9cf14c28-53a0-4a19-b524-967f6e12b748', 'name': 'Рыба', 'price': 300, 'quantity': 1}]

    carrot = Vegetables("Морковь", 100)
    cow_meat = Meat("Мясо", 200)
    fish = Fish("Рыба", 300)

    assert Stock.products == correct_stock  # будет ошибка из-за генерации id

    for product in Stock.products:
        if product['name'] == 'Яблоко':
            product['quantity'] += 1
            assert product['quantity'] == 1
        elif product['name'] == 'Мясо':
            product['quantity'] += 2
            assert product['quantity'] == 2
        elif product['name'] == 'Рыба':
            product['quantity'] += 3
            assert product['quantity'] == 3


def test_is_in_stock():
    carrot = Vegetables("Морковь", 100)

    assert Stock.is_product_in_stock(carrot)


def test_add_quantity():
    carrot = Vegetables("Морковь", 100)

    Stock.add_quantity(carrot, 2)

    assert Stock.products[0]['quantity'] == 2
