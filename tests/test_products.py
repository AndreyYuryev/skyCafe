from src.products import *


def test_product():
    product = Product("test", 100)
    assert product.name == "test"
    assert product.price == 100

    product.price = 200
    assert product.price == 200
